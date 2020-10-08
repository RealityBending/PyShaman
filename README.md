# PyShaman

**PyShaman** is a Python software that implements different procedures to induce altered states of consciousness and cognition.



### Installation

```
pip install https://github.com/RealityBending/PyShaman/zipball/master
```

### Contribution

You have some ideas? Want to improve things, add information, and help us tweak people's brain? Let us know, we would be very happy to have you on board :relaxed:

## Citation

You can cite this package and website as follows:

```
Makowski, D. (2020). PyShaman: A Python Package to Induce Altered States of Consciousness. GitHub.
Retrieved from https://github.com/RealityBending/PyShaman
```


## Features

### Binaural Beats

A binaural beat is an auditory illusion perceived when two different pure-tone waves with less than a 40 Hz difference between them, are presented to a listener dichotically (one through each ear). For example, listening to 520 and 530 Hz (presented respectively in the left and the right ear) will result in the illusory perception of a third tone, called a **binaural beat**, with a pitch correlating to a frequency of 10 Hz (the difference between the two tones). This effect was discovered in 1839 by Heinrich Wilhelm Dove.

```python
import pyshaman

pyshaman.binaural_beat(left=520, right=530, duration=10, filename="binaural_520_530.wav")
```


#### Mechanism

![](https://upload.wikimedia.org/wikipedia/commons/e/eb/WaveInterference.gif)

*The sum (blue) of two red and green sine waves (red, green) is shown as one of the waves increases in frequency, leading to constructive and destructive interference.*

From Colzato (2017):
> Even though direct causal links between neural activity and binaural beats are yet to be demonstrated, there is converging evidence that binaural beats are accompanied by, and systematically related to, neural synchronization Indeed, it has been proposed that binaural beats represent a neural entrainment technique by means of which the brain “takes over” or synchronizes its activity based on external acoustic stimulation (Chaieb et al. 2015). The basic assumption is that listening to binaural beats in a specific frequency band will entrain the same frequency in the brain (Becher et al. 2015).

From Jirakittayakorn (2017):
> In addition to the difference in the 2 tones, the carrier tone, which is the lower tone of the 2 tones, is also involved in the beat perception. One study measured perception of the beat on different frequency carrier tones and suggested that an intermediate frequency carrier tone of ~440 Hz facilitated the widest range of beat perception compared to lower and higher frequency carrier tones, which facilitated a narrower range (Licklider et al., 1950).

From Perez et al. (2020):

> Contrary to marketing claims, **we failed to find evidence for binaural beats being a "special kind of stimuli" that modulates mood and entrains the brain in a specific fashion**. [...] Marketing claims from companies commercializing binaural beats may be based purely on placebo effects. [...] Binaural beats weakly entrain the cortex and elicit connectivity patterns that were not elicited by a "sham" stimulation. Whether these connectivity patterns have a functional meaning (in terms of cognitive enhancement and mood modulation) or not, is still an open question.

#### Protocols

**TODO**: Add more references and studies.

- **340 - 380 Hz** (Δ = 40 Hz)

Hommel et al. (2016) reports that exposing participants to binaural beats in the gamma range (40 Hz), all embedded in white noise to enhance clarity of the beats (Oster, 1973), for 3 min before and during the task, increased cognitive flexibility (as measured by the crosstalk between tasks in a dual-task paradigm) as compared to a control condition in which participants were exposed to a continuous tone of 340 Hz.

- **250 - 253 Hz** (Δ = 3 Hz)

Jirakittayakorn et al. (2018) report that a binaural beat initiated during the N2 sleep stage is related to an enhancement of power of delta activity, a decreased N2 duration in favour of an increased N3 duration without sleep disturbance and sleep fragmentation.

- **240 - 255 Hz** (Δ = 15 Hz)

Beauchene et al., (2016) found that listening to 15Hz (255-240 Hz) binaural beats during a visuospatial working memory task not only increased the response accuracy, but also modified the strengths of the cortical networks during the task.

- **200 - 209.3 Hz** (Δ = 9.3 Hz)

Isik et al. (2017) report that binaural beats (200 Hz for the left ear and 209.3 Hz for the right ear) could reduce preoperative anxiety.

- **200 - 207 Hz** (Δ = 7 Hz)

Ala et al. (2018) showed that 3 min of 7 Hz binaural beats is not enough to entrain the brain, but applying 6 min of stimulation could change the relative power in the temporal and parietal lobes and further exposure to 9 min of stimuli could also alter the brain network.

- **154 - 168 Hz** (Δ = 14 Hz)

Gálvez et al., report that patients suffering from Parkinson's disease, after two sessions of sound stimulation for 10min separated by a minimum of 7 days, had a decrease in theta activity, a general decrease in Functional Connectivity (FC), and an improvement in working memory performance (but no significant changes were identified in the gait performance, heart rate or anxiety level).



#### References

Ala, T. S., Ahmadi-Pajouh, M. A., & Nasrabadi, A. M. (2018). [Cumulative effects of theta binaural beats on brain power and functional connectivity](https://www.sciencedirect.com/science/article/abs/pii/S1746809418300296). Biomedical Signal Processing and Control, 42, 242-252.

Beauchene, C., Abaid, N., Moran, R., Diana, R. A., & Leonessa, A. (2016). [The effect of binaural beats on visuospatial working memory and cortical connectivity](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166630). PLoS One, 11(11), e0166630.

Colzato, L. S., Steenbergen, L., & Sellaro, R. (2017). [The effect of gamma-enhancing binaural beats on the control of feature bindings](https://link.springer.com/article/10.1007/s00221-017-4957-9). Experimental Brain Research, 235(7), 2125-2131.

Gálvez, G., Recuero, M., Canuet, L., & Del-Pozo, F. (2018). [Short-term effects of binaural beats on EEG power, functional connectivity, cognition, gait and anxiety in Parkinson’s disease](https://www.worldscientific.com/doi/abs/10.1142/S0129065717500551). International journal of neural systems, 28(05), 1750055.

Hommel, B., Sellaro, R., Fischer, R., Borg, S., & Colzato, L. S. (2016). [High-frequency binaural beats increase cognitive flexibility: evidence from dual-task crosstalk](https://doi.org/10.3389/fpsyg.2016.01287). Frontiers in psychology, 7, 1287.

Isik, B. K., Esen, A., Büyükerkmen, B., Kilinc, A., & Menziletoglu, D. (2017). [Effectiveness of binaural beats in reducing preoperative dental anxiety](https://www.sciencedirect.com/science/article/abs/pii/S0266435617300657). British Journal of Oral and Maxillofacial Surgery, 55(6), 571-574.

Jirakittayakorn, N., & Wongsawat, Y. (2017). [Brain responses to a 6-Hz binaural beat: effects on general theta rhythm and frontal midline theta activity](https://www.frontiersin.org/articles/10.3389/fnins.2017.00365/full). Frontiers in neuroscience, 11, 365.

Jirakittayakorn, N., & Wongsawat, Y. (2018). [A novel insight of effects of a 3-Hz binaural beat on sleep stages during sleep](). Frontiers in human neuroscience, 12, 387.

Perez, H. D. O., Dumas, G., & Lehmann, A. (2020). [Binaural Beats through the auditory pathway: from brainstem to connectivity patterns](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7082494/). Eneuro, 7(2).