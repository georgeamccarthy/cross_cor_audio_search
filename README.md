# cross_cor_audio_search
Given a sound signature it will apply the cross-correlation metric at all times to determine which chunk of sound is the most similar.

Recorded short sound signature (of finger click).

<img width="359" alt="Screenshot 2021-10-12 at 17 43 01" src="https://user-images.githubusercontent.com/65653499/136996570-01d4f60b-6139-4ba0-bf0f-8ceb3960825f.png">

Recorded longer sound file including 3 clicks (circled, red) various ambient background noise and 1 cough (labelled, blue).

<img width="892" alt="Screenshot 2021-10-12 at 17 39 40" src="https://user-images.githubusercontent.com/65653499/136996220-8852d45e-d92d-4814-b1fb-c2c2e708708e.png">

The code produces a cross-correlation score against time plot which correctly identifies 2/3 clicks (misses 1 at ~10 seconds) and shows one false positive (cough at ~8.3 s)

<img width="752" alt="Screenshot 2021-10-12 at 17 41 22" src="https://user-images.githubusercontent.com/65653499/136996396-83afaa8a-886f-4a86-85c1-a277681e6456.png">
