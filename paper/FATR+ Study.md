# Intro
- [ ] draft needed
```
Two studies compare how different groups respond to NPP incident response scenarios under either a true fault or a spoofed fault condition. Participants subjectively score themselves in NASA-TLX and Cooper Harper on performance factors. Let's summarize each study's setup

```

## Hypothesis

Things we might find:
- order effects
- FATR helps make correct decision
- How does FATR effect Decision Time?
- How does FATR effect Scenario Time

# Exp1 - Dependency Study

- [ ] blurb needed
```
Palo Verde opeartors and University of Idaho students
```

## Methods


### Study Design

This is a 2x2x2 mixed design with repeated measures. Two simulator scenarios are combined with two different fault conditions, making four trials. The order of trials is arranged by Latin square, in scenario pairs:
	$1A, 1B, 2A, 2B$
	$1B, 1A, 2B, 2A$
	$2A, 2B, 1A, 1B$
	$2B, 2A, 1A, 1B$

**Within Subjects IVs:**
* Scenario: LOFW, SGTR
* Fault Condition: fault, spoof

**Between Subjects IV:** 
* Expertise: operator / student

### Measures

- Spoof faults create more uncertainty in diagnosis; Time score longer, Decision score lower
```
Spoof Fault Conditions lower mean scores in Decision, and higher mean scores in time demonstrates that incongruency in display and control result in error and longer decision outcomes, under these trial conditions (the procedures and simulator).
```
- [ ] Experts take more time, and get better decision scores, but the time was not significant. Any summary?
	- [ ] Duration of diagnosis is inversely proportionate to error in mean scores... (correlation evaluation?)
- [ ] what else?

* NASA-TLX
	- Mental Demand 
	- Temporal Demand 
	- Performance 
	- Effort 
	- Frustration Level 
- Cooper Harper
* Task Performance Measures
	* Decision: correct / error {cod: "Action Logic" : 1/0}
	* Diagnosis Time: (s)
	* Scenario Time: (s) 
		* [ ] not in data yet 


### Participants
- [ ] 
```
12 operators, 12 students
```

## Results

The analysis aimed to identify significant main effects of Scenario and Fault Condition on Decision and Diagnosis Time, and on the participant self-assessed post-test surveys. Expertise is the between-subject variable, operators vs students. 


```tex
\paragraph{Effects on Decision} 
Analysis revealed that each condition provides a significant main effect for making the correct decision in the trials, and some of the conditions show interactions. 

Expertise had a statistically significant effect $F(1, 22) = 11.355, p = 0.003$. Operator means were measured at $M = 0.979, SE = 0.021$, and students $M = 0.812, SE = 0.057$.
```


### Effects on Decision
Analysis revealed that the each condition have a significant main effect on making the correct decision in the trials, and some conditions show interactions. 

Expertise had a statistically significant effect $[F(1, 22) = 11.355, p = 0.003]$. Operator means were measured at $[(M = 0.979), (SE = 0.021)]$, and students $[(M = 0.812), (SE = 0.057)]$

- [ ] main effects within
- [ ] Fault
The analysis showed a significant main effect of Fault, $F(1, 22) = 17.742, p < 0.001, η² = 0.188$. Scenario , $F(1, 22) = 15.304, p < 0.001, η² = 0.129$. Then the means are

- [ ] Scenario

- [ ] Interaction
- [ ] S * F
Scenario and Fault Condition show an interaction effect, suggesting that the combined effect of these variables significantly influences decision outcomes, $F(1, 22) = 15.304, p < 0.001, η² = 0.129$, means with 

- [ ] three way in a table Scenario * Fault Condition * Expertise
Table X shows est marginal means for Scenario * Fault Condition * Expertise on Decision

| Scenario | Fault Condition | Expertise | Mean  | Std. Error |
| -------- | --------------- | --------- | ----- | ---------- |
| LOFW     | Fault           | Operator  | 1.000 | 0.000      |
| LOFW     | Fault           | Student   | 1.000 | 0.000      |
| LOFW     | Spoof           | Operator  | 1.000 | 0.000      |
| LOFW     | Spoof           | Student   | 0.917 | 0.083      |
| SGTR     | Fault           | Operator  | 1.000 | 0.000      |
| SGTR     | Fault           | Student   | 1.000 | 0.000      |
| SGTR     | Spoof           | Operator  | 0.917 | 0.083      |
| SGTR     | Spoof           | Student   | 0.333 | 0.142      |




Analysis of the estimated marginal means reveals numerical impact of different scenarios and fault conditions. The SGTR scenario and the Spoof fault condition were identified as having a more substantial impact on error rates in outcomes for participants. The SGTR scenario, with a mean decision score of 0.812, and the Spoof fault condition, with a mean of 0.792, both resulted in lower performance compared to their counterparts. These findings suggest that participants encountered more difficulties or made more errors when faced with the SGTR scenario and when subjected to Spoof faults, highlighting these conditions as particularly challenging or prone to inducing errors.

 *Estimated Marginal Means main effects vs Decision*
 - [ ] put this table into text only
 
| Category        | Type     | Mean  | Std. Error |
| --------------- | -------- | ----- | ---------- |
| Scenario        | LOFW     | 0.979 | 0.021      |
| Scenario        | SGTR     | 0.812 | 0.057      |
| Fault Condition | Fault    | 1.000 | 0.000      |
| Fault Condition | Spoof    | 0.792 | 0.059      |
| Expertise       | Operator | 0.979 | 0.021      |
| Expertise       | Student  | 0.812 | 0.057      |


*table: Significant between-subjects effects on Decision*

| Measure          | Type III SS | df  | MS    | F      | Sig.  | et2_G | Obs. Power | SE    | 95% CI | lambda | Obs. |
| ---------------- | ----------- | --- | ----- | ------ | ----- | ----- | ---------- | ----- | ------ | ------ | ---- |
| Between Subjects | 1.958       | 23  |       |        |       |       |            |       |        |        |      |
| Expertise        | 0.667       | 1   | 0.667 | 11.355 | 0.003 | 0.129 | 0.662      | 0.074 | 0.145  | 6.194  | 12   |
| Error            | 1.292       | 22  | 0.059 |        |       |       |            |       |        |        |      |

*table: Significant within-subjects effects on Decision*

| Measure                                | Source             | Type III SS | eps | df  | MS    | F      | Sig.      | et2_G | Obs. Power | SE    | 95% CI | lambda | Obs. |
| -------------------------------------- | ------------------ | ----------- | --- | --- | ----- | ------ | --------- | ----- | ---------- | ----- | ------ | ------ | ---- |
| Scenario                               | Greenhouse-Geisser | 0.667       | 1   | 1   | 0.667 | 15.304 | 7.472e-04 | 0.129 | 1          | 0.032 | 0.062  | 33.391 | 48   |
| Scenario * Expertise                   | Greenhouse-Geisser | 0.375       | 1   | 1   | 0.375 | 8.609  | 0.008     | 0.077 | 0.834      | 0.045 | 0.088  | 9.391  | 24   |
| Error(Scenario)                        | Greenhouse-Geisser | 0.958       | 1   | 22  | 0.044 |        |           |       |            |       |        |        |      |
| Fault Condition                        | Greenhouse-Geisser | 1.042       | 1   | 1   | 1.042 | 17.742 | 3.594e-04 | 0.188 | 1          | 0.037 | 0.073  | 38.710 | 48   |
| Fault Condition * Expertise            | Greenhouse-Geisser | 0.667       | 1   | 1   | 0.667 | 11.355 | 0.003     | 0.129 | 0.920      | 0.052 | 0.103  | 12.387 | 24   |
| Error(Fault Condition)                 | Greenhouse-Geisser | 1.292       | 1   | 22  | 0.059 |        |           |       |            |       |        |        |      |
| Scenario * Fault Condition             | Greenhouse-Geisser | 0.667       | 1   | 1   | 0.667 | 15.304 | 7.472e-04 | 0.129 | 0.974      | 0.045 | 0.088  | 16.696 | 24   |
| Scenario * Fault Condition * Expertise | Greenhouse-Geisser | 0.375       | 1   | 1   | 0.375 | 8.609  | 0.008     | 0.077 | 0.545      | 0.064 | 0.125  | 4.696  | 12   |
| Error(Scenario * Fault Condition)      | Greenhouse-Geisser | 0.958       | 1   | 22  | 0.044 |        |           |       |            |       |        |        |      |

### Effects on Diagnosis Time

For the within-subject effects on **Diagnosis Time**, our analysis indicates significant main effects related to **Scenario**, the interaction between **Scenario** and **Expertise**, and a notable effect of **Fault Condition**.

The effect of Scenario was on Diagnostic Time was found to be significant, $F(1, 22) = 20.369, p < 0.001, \eta^2=0.208$, assuming 20.8% of the variance.  Fault Condition measured $F(1, 22) = 6.550, p = 0.018, \eta^2 = 0.058$, accounting for 5.8% of the variance. The observation of a significant effects on the primary manipulation aligns with our expectation that the context of simulator Scenario and associated procedure should impact diagnostic efficiency.

There was also significant interaction between Scenario and the group Expertise assignment on Diagnosis Time, $F(1, 22) = 17.902, p < 0.001, \eta^2 = 0.188$, with effect size estimating 18.8% for this interaction.

| Category        | Type  | Mean    | Std. Error |
| --------------- | ----- | ------- | ---------- |
| Scenario        | LOFW  | 259.646 | 18.536     |
| Scenario        | SGTR  | 150.979 | 17.131     |
| Fault Condition | Fault | 179.125 | 17.257     |
| Fault Condition | Spoof | 231.500 | 20.873     |


*Estimated Marginal Means Analysis:*

The estimated marginal means for Scenario reveal that the LOFW scenario resulted in a higher mean diagnosis time (260 seconds) compared to the SGTR scenario (151 seconds), suggesting that the LOFW scenario is more complex or challenging, requiring more time for diagnosis. We note here that here the increased diagnostic time is not correlated with error in decision. LOFW scored better in the Decision mean scores, despite taking longer to commit.
- [ ] i used 'correlation' casually here; do I need a correlation calculation $\rho$?

Participants took longer to diagnose Spoof faults ($x \approx 232s$) compared to True Fault conditions ($x \approx 179s$), indicating that Spoof faults create more uncertainty in diagnosis.
 
The analysis of **Expertise** shows that Operators (mean = 222.062 seconds) had a somewhat higher diagnosis time on average compared to Students (mean = 188.562 seconds), though this difference may be influenced by the scenarios and fault conditions they encountered.

The **Scenario * Fault Condition** and **Scenario * Expertise** interactions suggest that the diagnostic challenges vary significantly with different combinations of scenarios, fault conditions, and participant expertise. For instance, the SGTR scenario with a True Fault condition had the lowest mean diagnosis time (130.792 seconds), indicating certain conditions are diagnosed more efficiently than others.

*Estimated Marginal Means for Scenario vs Diagnostic Time*

| Scenario | Mean    | Std. Error | 95% Lower Bound | 95% Upper Bound |
| -------- | ------- | ---------- | --------------- | --------------- |
| LOFW     | 259.646 | 18.536     | 223.315         | 295.976         |
| SGTR     | 150.979 | 17.131     | 117.403         | 184.556         |

*Estimated Marginal Means for Fault Condition vs Diagnostic Time*

| Fault Condition | Mean    | Std. Error | 95% Lower Bound | 95% Upper Bound |
| --------------- | ------- | ---------- | --------------- | --------------- |
| Fault           | 179.125 | 17.257     | 145.301         | 212.949         |
| Spoof           | 231.500 | 20.873     | 190.589         | 272.411         |

*Estimated Marginal Means for Expertise vs Diagnostic Time*

| Expertise | Mean    | Std. Error | 95% Lower Bound | 95% Upper Bound |
| --------- | ------- | ---------- | --------------- | --------------- |
| Operator  | 222.062 | 15.723     | 191.245         | 252.880         |
| Student   | 188.562 | 22.439     | 144.582         | 232.543         |

*Estimated Marginal Means for Scenario * Fault Condition*

| Scenario | Fault Condition | Mean    | Std. Error | 95% Lower Bound | 95% Upper Bound |     |
| -------- | --------------- | ------- | ---------- | --------------- | --------------- | --- |
| LOFW     | Fault           | 227.458 | 20.742     | 186.804         | 268.113         |     |
| LOFW     | Spoof           | 291.833 | 29.730     | 233.563         | 350.104         |     |
| SGTR     | Fault           | 130.792 | 24.161     | 83.436          | 178.147         |     |
| SGTR     | Spoof           | 171.167 | 24.087     | 123.956         | 218.377         |     |

*Estimated Marginal Means for Scenario * Expertise*

| Scenario | Expertise | Mean    | Std. Error | 95% Lower Bound | 95% Upper Bound |
| -------- | --------- | ------- | ---------- | --------------- | --------------- |
| LOFW     | Operator  | 225.458 | 24.371     | 177.690         | 273.226         |
| LOFW     | Student   | 293.833 | 26.619     | 241.659         | 346.008         |
| SGTR     | Operator  | 218.667 | 20.381     | 178.719         | 258.614         |
| SGTR     | Student   | 83.292  | 19.636     | 44.805          | 121.778         |

*Estimated Marginal Means for Fault Condition * Expertise*

| Fault Condition | Expertise | Mean    | Std. Error | 95% Lower Bound | 95% Upper Bound |
| --------------- | --------- | ------- | ---------- | --------------- | --------------- |
| Fault           | Operator  | 207.500 | 24.223     | 160.022         | 254.978         |
| Fault           | Student   | 150.750 | 23.672     | 104.353         | 197.147         |
| Spoof           | Operator  | 236.625 | 20.129     | 197.173         | 276.077         |
| Spoof           | Student   | 226.375 | 37.056     | 153.746         | 299.004         |


```
# Need interaction plot: Scenario * Skill 
## Figures only for interactions

## main effects with means
```

![[Pasted image 20240307115820.png]]

### Mental Demand
- [ ] Between Subjects    419.958   23                                                                                 
Expertise           192.667    1   192.667   18.649   2.772e-04   0.320     12   0.982    1.924   10.172   0.862
## Conclusions and Discussion

 This finding suggests that the impact of the scenario on diagnosis time varies depending on the expertise of the participant, implying that certain scenarios may be more challenging for students compared to operators.
suggesting that the level of expertise has a significant influence on the decision-making process, explaining approximately 12.9% of the variance in Decision outcomes.

Variance in Decision can be attributed to the Scenario, indicating that complexities in procedure and simulator conditions can increase error in decision-making.

Students were confused by spoof * sgtr

# Exp2 "FATR Study"

**Between Subjects IV:** 
* **Decision Support:** Control / FATR
- **Additional DV (Specific to FATR Study):** {FATR Outcome}
    - FATR Timeout
    - Manual Activation
    - FATR Execute

## Methods
## Participants
Dep n=12 each, two groups, 24
FATR n=12


## Results

### Diagnostic Time
TESTS OF BETWEEN-SUBJECTS EFFECTS
Measure: Diagnosis Time - No Significant Effects or Interactions

```python
df2.read_tbl('student_data.csv')
dv2_values = ['Diagnosis Time']
for dv in dv2_values:
	aov.run(df2, dv, wfactors=['Scenario', 'Fault Condition'], bfactors=['Study'])
```

Running ANOVA for: Diagnosis Time
('Scenario', 'Fault Condition')
('Study',)
('Scenario', 'Study')
('Fault Condition', 'Study')
('Scenario', 'Fault Condition', 'Study')
Diagnosis Time ~ Scenario * Fault Condition * Study

TESTS OF BETWEEN-SUBJECTS EFFECTS

Measure: Diagnosis Time - No Significant Effects or Interactions

## Conclusions and Discussion

