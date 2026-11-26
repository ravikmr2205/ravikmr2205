# RSVP Google Forms: setup guide

For the #pyaarkaPR invitation (Ravi & Priyanshi, 23–24 February 2027).

## 1. Four forms, one per invitation link

Each invitation link opens its own form, so the replies already tell you which invitation the guest received. The form does not need to ask about functions.

| Invitation link | Form in Google Drive |
|---|---|
| `pyaarkapr.github.io/groom/` | RSVP – Groom – Shaadi + Engagement |
| `pyaarkapr.github.io/groom-shaadi/` | RSVP – Groom – Shaadi only |
| `pyaarkapr.github.io/bride/` | RSVP – Bride – Shaadi + Engagement |
| `pyaarkapr.github.io/bride-shaadi/` | RSVP – Bride – Shaadi only |

## 2. Questions (same in all four forms)

| # | Question | Type | Settings |
|---|---|---|---|
| 1 | Your name (or family name) | Short answer | Required |
| 2 | Phone number (WhatsApp) | Short answer | Required |
| 3 | Will you be joining us? | Multiple choice | Joyfully attending / Sorry, can't make it. Required |
| 4 | Number of people coming (including you) | Short answer | ⋮ → Response validation → Number → Between 1 and 30 |
| 5 | *(groom forms only)* Will you join the baraat? (departs 8:00 pm, reaches the venue 9:00 pm) | Multiple choice | Yes / No / Not sure yet |
| 6 | Message or blessings for the couple | Paragraph | Optional |

**Delete from every form:**
- the food preference question
- "Which functions will you attend?"
- the "Your invitation" question and its section, if you added them

With no sections left, the form is a single page.

## 3. Settings (⚙ Settings tab, in each form)

- **Responses → Collect email addresses:** Do not collect
- **Responses → Limit to 1 response:** Off. If it is on, guests have to sign in to Google.
- **Responses → Allow response editing:** On
- **Presentation → Confirmation message:** "Thank you! Your RSVP has reached us. We can't wait to celebrate with you. #pyaarkaPR"

**Copied forms:** open each copy and click **Publish** (top right) if it shows as unpublished. Copies sometimes start out closed for responses.

## 4. Collecting responses

In each form, go to **Responses** tab → **Link to Sheets** → **Create a new spreadsheet**. Name the sheets to match the forms, e.g. "RSVP – Groom – Shaadi only".

Turn on alerts: **Responses** tab → ⋮ → **Get email notifications for new responses**.

### Head count in each sheet

The columns are: A Timestamp, B Name, C Phone, D Joining?, E Number of people, F Baraat (groom forms), then Message.

Add a tab called **Summary** and paste:

| What | Formula |
|---|---|
| Replies | `=COUNTA('Form Responses 1'!B2:B)` |
| Families attending | `=COUNTIF('Form Responses 1'!D2:D,"Joyfully attending")` |
| Families declined | `=COUNTIF('Form Responses 1'!D2:D,"Sorry*")` |
| People attending | `=SUMIFS('Form Responses 1'!E2:E,'Form Responses 1'!D2:D,"Joyfully attending")` |
| Baraat: people (groom forms) | `=SUMIFS('Form Responses 1'!E2:E,'Form Responses 1'!F2:F,"Yes")` |

### Totals per function

| Function | Who to count |
|---|---|
| Haldi, Sangeet & Engagement | "People attending" from the two **Shaadi + Engagement** sheets |
| Wedding | "People attending" from **all four** sheets |

To see everything in one place, add a tab in any one sheet and pull the other sheets' Summary tabs in:

```
=IMPORTRANGE("<link to another RSVP sheet>", "Summary!A1:B5")
```

Click **Allow access** the first time.

## 5. Checklist

- [ ] Food and "Which functions" questions deleted from all four forms
- [ ] Both copies published and accepting responses
- [ ] Email collection off, "Limit to 1 response" off, in all four
- [ ] Each form linked to its own sheet, with a Summary tab
- [ ] Each of the four invitation links tested once: open the RSVP form, submit a test reply, then delete that row
