import flask_login
from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import LoginManager, login_required, logout_user

from . import auth_dao
from .auth_forms import (
    LoginForm,
    RegisterForm,
    ForgotForm,
    RestoreForm,
    ProfileForm,
    VerifyForm,
    PasswordForm,
)

bp = Blueprint(
    "auth", __name__, url_prefix="/auth", template_folder="templates"
)
login_manager = LoginManager()


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if flask_login.current_user.is_authenticated:
            return redirect(url_for("main", **request.args))
        else:
            share = request.args.get("share")
            if share:
                query_string = "share={share}".format(share=share)
            else:
                query_string = ""
            return render_template(
                "login.html", query_string=query_string, form=LoginForm()
            )
    email = request.form["email"]
    user = auth_dao.get_user(email)
    if user and user.check_password(request.form["password"]):
        flask_login.login_user(user, remember=True)
        return redirect(url_for("main", **request.args))
    flash(
        "Incorrect login or/and password. Please check it and try again",
        "danger",
    )
    return redirect(url_for("auth.login", **request.args))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        if flask_login.current_user.is_authenticated:
            return redirect(url_for("main", **request.args))
        else:
            share = request.args.get("share")
            if share:
                query_string = "share={share}".format(share=share)
            else:
                query_string = ""
            return render_template(
                "register.html", query_string=query_string, form=RegisterForm()
            )
    email = request.form["email"]
    if auth_dao.get_user(email) is None:
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        user = auth_dao.add_user(
            username=email,
            password=request.form["password"],
            first_name=first_name,
            last_name=last_name,
        )
        flask_login.login_user(user, remember=True)
        return redirect(url_for("main", **request.args))
    flash("Such user already exists", "danger")
    return redirect(url_for("auth.register", **request.args))


@bp.route("/forgot", methods=["GET"])
def render_forgot():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for("main", **request.args))
    return render_template("forgot.html", form=ForgotForm())


@bp.route("/forgot", methods=["POST"])
def post_forgot():
    email = request.form["email"]
    auth_dao.password_email(email)
    flash(
        "The email with the restoration link has been sent. Check your inbox.",
        "success",
    )
    return redirect(url_for("auth.login", **request.args))


@bp.route("/restore/<token>", methods=["GET"])
def render_restore(token):
    return render_template("restore.html", token=token, form=RestoreForm())


@bp.route("/restore/<token>", methods=["POST"])
def restore(token):
    new_password = request.form["password"]
    if auth_dao.restore_password(token=token, new_password=new_password):
        return redirect(url_for("main"))
    else:
        return redirect(url_for("auth.render_forgot"))


@bp.route("/verify/<token>", methods=["GET"])
def verify(token):
    auth_dao.confirm_verify_email(token)
    return redirect(url_for("main"))


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@bp.route("/profile")
@login_required
def render_profile():
    return render_template("profile.html", form=ProfileForm())


@bp.route("/render_verify", methods=["GET"])
@login_required
def verify_reminder():
    return render_template("verify_modal.html", form=VerifyForm())


@bp.route("/render_password", methods=["GET"])
@flask_login.login_required
def render_password():
    return render_template("password_modal.html", form=PasswordForm())


@login_manager.user_loader
def user_loader(id):
    return auth_dao.get_user_by_id(id)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for("auth.login", **request.args))


@bp.record_once
def on_load(state):
    login_manager.init_app(state.app)
