---
date: 2026-11-08
section: AI
importance: Low
kind: paper
source: "Google Research blog"
url: https://research.google/blog/detecting-signs-of-hypertension-using-wearable-sensors/
status: unread
id: 2026-11-08-google-smartwatch-hypertension
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# Google Research a smartwatch model flags hypertension without a cuff, at 90% specificity i

Google's AI-PPG-ACC-HTN reads a consumer smartwatch's optical pulse and motion signals over several days and outputs a hypertension probability, with no cuff calibration. Against 24-hour ambulatory blood pressure, it reached 65.8% sensitivity and 90.0% specificity for first screening (office cuff: 55.3% sensitivity), and 96.7% positive predictive value in confirmatory testing. Tested on: 196 participants at five US sites (48 in the confirmatory subset), one watch, pre-trained on 492,347 hours from 2,109 people.

## Details

**Caveats**
Small sample with wide uncertainty in the 48-person subset; screening sensitivity is moderate, so many cases are missed; early feasibility research, not a product or a diagnosis.

**For your work**
A clean example of self-supervised pre-training on cheap unlabelled sensor data plus a simple classifier on top, relevant for health and insurance clients exploring wearables.

**Method**
- A 1-D convolutional network was pre-trained with self-supervised contrastive learning on 492,347 hours of unlabelled watch data from 2,109 people, producing 15-second waveform embeddings.
- Embeddings are averaged over several days and combined with height, then fed to a regularised logistic regression.
- Prospective five-site US study of 196 people without known heart disease or blood pressure medication, with 24-hour ambulatory monitoring as the reference.

**Problem**
More than half of adults with hypertension don't know they have it, and cuffless wearables usually need regular cuff calibration and only track relative changes.

**Results**
- First screening: sensitivity 65.8%, specificity 90.0%, PPV 80.6%, vs office cuff sensitivity 55.3%, PPV 77.8%.
- Confirmatory testing (48 people with high office readings): sensitivity 78.4%, specificity 90.9%, PPV 96.7%, vs repeat office cuff 67.6% / 63.6% / 86.2%.
- Multi-day home cuff monitoring still had higher sensitivity (89.2%) but lower specificity (81.8%).

**Concepts:** [[AI for science and math]]
**From:** [[2026-11-08]]

# My notes


---
# References
[Google Research blog](https://research.google/blog/detecting-signs-of-hypertension-using-wearable-sensors/)
