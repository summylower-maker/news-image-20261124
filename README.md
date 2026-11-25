# World News — 24 November 2026

Entry for the make.fun bounty **"Sum up 24 November's world news in one image"**
(`news-image-20261124`, $100, ends Thu 26 Nov 2026 00:00 UTC / 08:00 Beijing).
Top 50 entries share $100: 1st $20, 2nd $12, 3rd $6, 4th–10th $2 each,
11th–50th $1.20 each. No prize is claimed or guaranteed here.

## What it is

One 1024×1024 PNG infographic, `entry.png`, with 8 headline blocks
summarising Tuesday 24 November 2026:

1. **Nvidia brings back Huang as CEO** — shares jump over 30% after the
   board reverses course.
2. **Tankers catch fire after mine strikes** — US Treasury sanctions
   Iran's shadow-banking network.
3. **Ukraine sinks Russian warship in Libya** — sea drones hit corvette
   Merkury in Benghazi.
4. **EU unveils 22nd Russia sanctions** — banks, crypto platforms and
   athletes targeted.
5. **CrowdStrike buys Zscaler for $43.9B** — all-stock cybersecurity
   mega-deal, announced Mon.
6. **Solomon Islands to end China security pact** — will sign a security
   treaty with Australia instead.
7. **NATO vows to defend space** — after reports Russia may launch a
   nuclear satellite.
8. **Israeli strike kills at least 3 in Gaza** — attack near a police post
   in Khan Younis.

## How to run

```sh
python3 main.py
# writes /output/entry.png (falls back to ./output/entry.png if /output is not writable)
```

`main.py` (Python 3.13 compatible) does no network access, uses no
randomness and no timestamps: it copies the bundled `entry.png`
byte-for-byte. Running it twice produces byte-identical output.

`draw.py` is the script that rendered `entry.png` with Pillow; it is kept
for transparency and is not needed to run the entry.

## Sources (all reporting 24 Nov 2026, unless noted as announced 23 Nov)

- Nvidia reinstatement / shares +30%: CNN,
  https://www.cnn.com/2026/11/23/markets/us-stocks-rebound-intl?cid=external-feeds_iluminar_meta
- Iran / Hormuz tankers and US Treasury sanctions: Al Jazeera,
  https://www.aljazeera.com/news/liveblog/2026/11/24/iran-war-live-iran-says-three-ships-catch-fire-after-hitting-hormuz-mines?update=5180475
  and Saudi Gazette,
  https://saudigazette.com.sa/article/666499/world/iran-says-four-oil-tankers-caught-fire-after-hitting-mines-in-strait-of-hormuz
- Ukraine / Russian warship Merkury in Benghazi, and EU 22nd sanctions
  package: Korea Herald, https://www.koreaherald.com/article/10947444 ;
  Al Jazeera,
  https://www.aljazeera.com/news/2026/11/24/why-are-russian-warships-off-libya-and-will-ukraines-attack-change-that?traffic_source=rss
- EU sanctions (Reuters summary): Devdiscourse,
  https://www.devdiscourse.com/article/international/4011043-reuters-world-news-summary
- CrowdStrike / Zscaler $43.9B: Intelligent CXO,
  https://www.intelligentcxo.com/2026/11/24/crowdstrike-to-buy-zscaler/
  and the 24 Nov 2026 summary, https://freemapp.com/index.php?title=2026-11-24&diff=5169&oldid=0
- NATO space defence / China official sentenced to death: The Straits Times,
  https://www.straitstimes.com/world/while-you-were-sleeping-5-stories-you-might-have-missed-nov-24-2026?ref=latest-headlines
- Israeli strike in Khan Younis, Gaza: The Straits Times,
  https://www.straitstimes.com/world/middle-east/israeli-airstrike-kills-at-least-three-palestinians-in-southern-gaza-medics-say

## Still needed before submission (not done here)

- A public GitHub repository owned by the entrant's GitHub account,
  created after the competition opened, under an OSI-approved licence
  (MIT included here), with `main.py` in its root.
- A make.fun account / Solana keypair and registration, which needs the
  user's approval (the approval card times out after ~2 minutes).
- The make.fun kit, local grading, transcript bundle, and submission —
  all via the kit's `makefun.mjs` CLI, after the accounts above exist.
