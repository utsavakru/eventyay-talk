from django.utils.translation import gettext_lazy as _

from pretalx.common.text.phrases import Phrases


class CfPPhrases(Phrases, app="cfp"):
    auth_password_reset = _(
        "If we know a user by this email address (who has not requested a password reset in the last 24 hours), we will send you an e-mail containing further instructions. If you don’t "
        "see the email within the next minutes, check your spam inbox!"
    )
    auth_reset_fail = _(
        "This link was not valid. Make sure you copied the complete URL from the "
        "email and that the email is no more than 24 hours old."
    )
    auth_reset_success = _("Awesome! You can now log in using your new password.")

    locale_change_success = _(
        "Your locale preferences have been saved. We like to think that we have excellent support "
        "for English in pretalx, but if you encounter issues or errors, please contact us!"
    )

    submission_withdrawn = _("Your proposal has been withdrawn.")
    submission_not_withdrawn = _(
        "Your proposal can’t be withdrawn at this time – please contact us if you need to withdraw your proposal!"
    )
    submission_confirmed = _(
        "Your session has been confirmed – we’re looking forward to seeing you!"
    )
    submission_was_confirmed = _(
        "This proposal has already been confirmed – we’re looking forward to seeing you!"
    )
    submission_not_confirmed = _(
        "This proposal cannot be confirmed at this time – please contact us if you think this is an error."
    )
    submission_uneditable = _("This proposal cannot be edited anymore.")

    account_deleted = _("Your account has now been deleted.")
    account_delete_confirm = _("Are you really sure? Please tick the box")

    invite_invalid_email = _("Please provide a valid email address.")
    invite_sent = _("The invitation was sent!")
    invite_accepted = _(
        "You are now part of this proposal! Please fill in your profile below."
    )

    submissions_closed = _("This event currently does not accept new proposals, sorry!")
    submission_success = _("Your session has been submitted successfully!")
    submission_email_fail = _(
        "We are experiencing difficulties when sending mails, but your session was submitted successfully!"
    )
    speaker_email = _("Speaker email")
    invite_subject = _("{speaker} invites you to join their session!")
    invite_text = _(
        """Hi!

I’d like to invite you to be a speaker in the session

  “{title}”

at {event}. Please follow this link to join:

  {url}

I’m looking forward to it!
{speaker}"""
    )
    questions = _("Questions")
