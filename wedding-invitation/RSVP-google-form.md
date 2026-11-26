# RSVP Google Form: setup guide

For the #pyaarkaPR invitation (Ravi & Priyanshi, 23–24 February 2027).

## 1. How many forms

Make **two forms**, one per side, so each family keeps its own guest list and head count:

| Form | Used by these invitation links |
|---|---|
| **RSVP – Groom side (Gupta family)** | `pyaarkapr.github.io/groom/` and `/groom-shaadi/` |
| **RSVP – Bride side (Chaudhary family)** | `pyaarkapr.github.io/bride/` and `/bride-shaadi/` |

Each form gets **two pre-filled links** (step 5), one for "Shaadi + Engagement" guests and one for "Shaadi only" guests. That makes **four RSVP links** in total, one for each invitation link. Shaadi-only guests never see the Haldi or Sangeet questions.

Build the groom form first. Then use ⋮ → **Make a copy** for the bride form and change only the parts marked *(groom only)* or *(bride only)*.

## 2. Form title and description

**Title:** `RSVP · Ravi & Priyanshi · #pyaarkaPR`
(bride form: `RSVP · Priyanshi & Ravi · #pyaarkaPR`)

**Description:**

> We would love to celebrate with you! Please reply by **[RSVP date, e.g. 31 January 2027]**.
>
> Haldi · Tue 23 Feb, 10:00 am – 2:30 pm · Gulmohar Grand Farms & Banquet, Vasundhara, Ghaziabad
> Sangeet & Engagement · Tue 23 Feb, from 6:30 pm · Gulmohar Grand Farms & Banquet
> Wedding · Wed 24 Feb · Jalsa Hall, Sanssara Banquets, Vasundhara, Ghaziabad

## 3. Questions, by section

The form uses four sections, so each guest only sees the questions that apply to them. To add a section, use the **Add section** icon (two stacked bars) in the right-hand toolbar.

### Section 1: About you

| # | Question | Type | Options / settings |
|---|---|---|---|
| 1 | Your name (or family name) | Short answer | Required |
| 2 | Phone number (WhatsApp) | Short answer | Required. ⋮ → Response validation → Regular expression → Matches → `^[+0-9 ]{10,15}$`, error text "Please enter a valid phone number" |
| 3 | Will you be joining us? | Multiple choice | **Joyfully attending** / **Sorry, can't make it**. Required. ⋮ → **Go to section based on answer**: *Joyfully attending → Section 2*, *Sorry, can't make it → Section 4* |

### Section 2: Your invitation

| # | Question | Type | Options / settings |
|---|---|---|---|
| 4 | Your invitation | Multiple choice | **Shaadi + Engagement** / **Shaadi only**. Required. Description: "Already selected for you, please leave as it is." ⋮ → **Go to section based on answer**: *Shaadi + Engagement → Section 3*, *Shaadi only → Section 4* |
| 5 | Number of people coming (including you) | Short answer | Required. ⋮ → Response validation → Number → Between → 1 and 30 |
| 6 | Food preference | Checkboxes | Vegetarian / Jain / No onion, no garlic / Other… (optional) |
| 7 | *(groom only)* Will you join the baraat? (departs 8:00 pm, reaches the venue 9:00 pm) | Multiple choice | Yes / No / Not sure yet. Required |

### Section 3: Functions (only for Shaadi + Engagement guests)

| # | Question | Type | Options / settings |
|---|---|---|---|
| 8 | Which functions will you attend? | Checkboxes | **Haldi (23 Feb, morning)** / **Sangeet & Engagement (23 Feb, evening)** / **Wedding (24 Feb)**. Required |

At the bottom of Section 3, set **After section 3 → Continue to section 4**.

### Section 4: A note for the couple

| # | Question | Type | Options / settings |
|---|---|---|---|
| 9 | Do you need help with a place to stay? | Multiple choice | Yes / No (optional) |
| 10 | Message or blessings for the couple | Paragraph | Optional |

**How guests move through the form:**

- Declines: Section 1 → Section 4 → Submit
- Shaadi only: Section 1 → Section 2 → Section 4 → Submit
- Shaadi + Engagement: Section 1 → Section 2 → Section 3 → Section 4 → Submit

## 4. Settings (⚙ Settings tab)

- **Responses → Collect email addresses:** *Do not collect*. Guests shouldn't need a Google account.
- **Responses → Limit to 1 response:** **Off**. Leaving it on forces guests to sign in to Google.
- **Responses → Allow response editing:** On. Guests can fix a mistake from their confirmation link.
- **Presentation → Confirmation message:**
  > Thank you! Your RSVP has reached us. We can't wait to celebrate with you. #pyaarkaPR
- **Presentation → Show link to submit another response:** On, for families replying for relatives.
- **Defaults → Make questions required by default:** Off. Set "Required" per question as listed above.

**Theme (🎨 icon):** header image = the couple illustration, colour = maroon or gold, font = "Formal".

## 5. Pre-filled links (four in total)

For each form:

1. ⋮ (top right) → **Get pre-filled link**.
2. In Section 1, leave everything empty and click **Next**. Required questions aren't enforced in pre-fill mode.
3. In Section 2, choose **Shaadi + Engagement** for question 4. Leave everything else empty, then click **Next** until you reach the last section.
4. Click **Get link** → **Copy link**.
5. Repeat with **Shaadi only**.

Send me the four links, labelled like this:

| Label | Form | Q4 pre-filled as |
|---|---|---|
| groom-all | Groom form | Shaadi + Engagement |
| groom-shadi | Groom form | Shaadi only |
| bride-all | Bride form | Shaadi + Engagement |
| bride-shadi | Bride form | Shaadi only |

I'll connect each one to its invitation link, and the RSVP button will appear on the site.

## 6. Collecting responses

### Link a Google Sheet

In each form, go to **Responses** tab → **Link to Sheets** → **Create a new spreadsheet**, named e.g. "RSVP – Groom side". Every reply then lands as a row automatically.

Turn on alerts: **Responses** tab → ⋮ → **Get email notifications for new responses**.

### Columns you will see (groom form)

Google adds the columns in question order. Check yours, because the formulas below assume this layout:

| Col | Content |
|---|---|
| A | Timestamp |
| B | Your name |
| C | Phone number |
| D | Will you be joining us? |
| E | Your invitation |
| F | Number of people |
| G | Food preference |
| H | Baraat (groom form only) |
| I | Which functions will you attend? |
| J | Place to stay |
| K | Message |

On the bride form there is no baraat column, so the later columns move one letter left (functions = **H**, place to stay = **I**, message = **J**).

### Head-count tab

Add a new tab called **Summary** in the response sheet and paste these formulas (groom-form column letters). Replace `'Form Responses 1'` with your response tab's name if it differs.

| What | Formula |
|---|---|
| Replies received | `=COUNTA('Form Responses 1'!B2:B)` |
| Families attending | `=COUNTIF('Form Responses 1'!D2:D,"Joyfully attending")` |
| Families declined | `=COUNTIF('Form Responses 1'!D2:D,"Sorry*")` |
| **Haldi: people** | `=SUMIFS('Form Responses 1'!F2:F,'Form Responses 1'!D2:D,"Joyfully attending",'Form Responses 1'!I2:I,"*Haldi*")` |
| **Sangeet & Engagement: people** | `=SUMIFS('Form Responses 1'!F2:F,'Form Responses 1'!D2:D,"Joyfully attending",'Form Responses 1'!I2:I,"*Sangeet*")` |
| **Wedding: people** | `=SUMIFS('Form Responses 1'!F2:F,'Form Responses 1'!D2:D,"Joyfully attending",'Form Responses 1'!I2:I,"*Wedding*")+SUMIFS('Form Responses 1'!F2:F,'Form Responses 1'!D2:D,"Joyfully attending",'Form Responses 1'!E2:E,"Shaadi only")` |
| Baraat: families joining (groom) | `=COUNTIF('Form Responses 1'!H2:H,"Yes")` |
| Baraat: people (groom) | `=SUMIFS('Form Responses 1'!F2:F,'Form Responses 1'!H2:H,"Yes")` |
| Jain meals (people) | `=SUMIFS('Form Responses 1'!F2:F,'Form Responses 1'!G2:G,"*Jain*")` |
| Need a place to stay | `=COUNTIF('Form Responses 1'!J2:J,"Yes")` |

The Wedding formula has two parts. Shaadi-only guests never see the functions question, so they are counted through the "Your invitation" column instead.

### Combined count for both sides (optional)

In either sheet, add a tab called **Both sides** and pull in the other side's summary:

```
=IMPORTRANGE("<link to the other RSVP sheet>", "Summary!A1:B12")
```

Click **Allow access** the first time. Then add the two sides together, e.g. `=B4 + C4` for Haldi.

### Who should see the responses

In the sheet, use **Share** → add the people who plan seating and catering (e.g. both sets of parents) as **Viewer** or **Editor**. The form link itself only lets guests reply. Guests can never see other people's answers.

## 7. Checklist before sending invitations

- [ ] Both forms created, with sections and "Go to section based on answer" set
- [ ] Email collection off, "Limit to 1 response" off
- [ ] RSVP date filled in the description
- [ ] Response sheets linked, Summary tab added
- [ ] Four pre-filled links tested once each from a phone (submit a test reply, then delete that row from the sheet)
- [ ] Four links sent to me to connect to the invitation
