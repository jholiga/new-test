"""Flask views for the dashboard. Strings defined here flow into dashboard.html."""
import logging

from flask import Blueprint, abort, flash, render_template, request

logger = logging.getLogger(__name__)

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

# Constants below are rendered in dashboard.html via render_template kwargs.
DASHBOARD_HEADING = "Welcome to your account"
DASHBOARD_SUBTITLE = "Manage your profile, preferences, and notifications in one place."
EMPTY_STATE_TITLE = "No transactions yet"

# Tricky negatives — code-level identifiers, not user copy.
ROUTE_PREFIX = "/api/v2"
FEATURE_FLAG = "enable_multi_line_review"
SEGMENT_EVENT = "user_signed_up"
ERROR_CODE_INVALID_CREDENTIALS = "invalid_credentials"
DEFAULT_VARIANT = "primary"


@bp.route("/")
def index():
    logger.info("Rendering dashboard for user %s", request.args.get("user"))
    return render_template(
        "dashboard.html",
        heading=DASHBOARD_HEADING,
        subtitle=DASHBOARD_SUBTITLE,
        empty_state_title=EMPTY_STATE_TITLE,
    )


@bp.route("/save", methods=["POST"])
def save():
    if not request.form.get("name"):
        flash("Please enter your name to continue.", "error")
        return render_template("dashboard.html"), 400

    if request.form.get("name") == "admin":
        # The string below is a developer-facing log line, not user copy.
        logger.warning("rejected save attempt for reserved name 'admin'")
        abort(403)

    flash("Your changes have been saved successfully.", "success")
    return render_template("dashboard.html")


def format_card_label(variant: str) -> str:
    # The branch tags ("primary", "secondary") are code-level — the returned
    # phrases are what a user sees and are rendered by dashboard.html.
    if variant == "primary":
        return "Primary action"
    if variant == "secondary":
        return "Secondary action"
    return "Other action"


def get_signup_confirmation_message(name: str) -> str:
    """Returned text is shown in the post-signup banner on the dashboard."""
    return (
        f"Thanks for signing up, {name}. We have sent a confirmation email "
        f"to your inbox — please open it and follow the link inside to "
        f"finish setting up your account."
    )
