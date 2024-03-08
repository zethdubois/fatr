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

**DV**
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
12 operators, 12 students

## Results

The analysis aimed to identify any significant main effects of **Scenario** and **Fault Condition** on the self-assessed performance  (e.g., **Diagnosis Time**), as well as to examine the influence of the expertise factor. **Expertise**, categorized by participant group assignment into levels such as operator or student, is considered to potentially modulate these effects. This analytical approach is designed to elucidate not only whether variations in **Scenario** and **Fault Condition** are associated with changes in the dependent variables but also to explore how these associations might vary as a function of the participant’s level of expertise.

### Effects on Decision
- [ ] short blurb
```
yada
```
{*See anova tables x, y*}
#### Expertise Between-Subjects
For the between-subjects effect, the analysis revealed a significant effect of **Expertise** on **Decision**, $F(1, 22) = 11.355, p = 0.003$.This significant effect suggests that the level of expertise (operator vs. student) has a substantial influence on the decision-making process, explaining approximately 12.9% of the variance in Decision outcomes, as indicated by the partial eta squared value of 0.129. The observed power of this test is 0.662, indicating a relatively strong ability to detect an effect of this size given the sample size and effect size.

Estimated Marginal Means for Expertise

| Expertise | Mean  | Std. Error | 95% Lower Bound | 95% Upper Bound |
|-----------|-------|------------|-----------------|-----------------|
| Operator  | 0.979 | 0.021      | 0.938           | 1.020           |
| Student   | 0.812 | 0.057      | 0.701           | 0.924           |

#### Within-Subject 
Both **Scenario** and **Fault Condition** had a significant effect on participants making the proper decision in the simulators, regardless of **Expertise**.

- Scenario: $F(1, 22) = 15.304, p < 0.001, η² = 0.129$
- Fault Condition: $F(1, 22) = 17.742, p < 0.001, η² = 0.188$
- Scenario * Fault Condition: $F(1, 22) = 15.304, p < 0.001, η² = 0.129$

The analysis showed a significant main effect of **Fault Condition** condition on **Decision**, $F(1, 22) = 17.742, p < 0.001$. This result signifies that **Fault Condition** exerts a significant effect on the decisions made by participants. With an effect size (partial η²) of 0.188, this effect accounts for roughly 18.8% of the variance in Decision scores, indicating that the nature of the fault condition presented is a critical determinant of decision-making outcomes, with a strong influence relative to other variables in the study.

We measure a significant main effect of **Scenario** on **Decision**, $F(1, 22) = 15.304, p < 0.001$. This finding indicates that the Scenario significantly influences Decision outcomes among participants. The effect size, represented by a partial eta squared (η²) of 0.129, suggests that approximately 12.9% of the variance in Decision can be attributed to the Scenario. This demonstrates a considerable impact, highlighting the importance of the specific scenario context in affecting decision-making processes.

A significant interaction effect was found between **Scenario** and **Fault Condition** on **Decision**, $F(1, 22) = 15.304, p < 0.001, η² = 0.129$ suggesting that the combined effect of these variables significantly influences decision outcomes, accounting for approximately 12.9% of the variance.

Our analysis of the estimated marginal means reveals significant variations in decision outcomes across different scenarios and fault conditions. Specifically, the SGTR scenario and the Spoof fault condition were identified as having a more substantial impact on error rates in outcomes for participants. The SGTR scenario, with a mean decision score of 0.812, and the Spoof fault condition, with a mean of 0.792, both resulted in lower performance compared to their counterparts. These findings suggest that participants encountered more difficulties or made more errors when faced with the SGTR scenario and when subjected to Spoof faults, highlighting these conditions as particularly challenging or prone to inducing errors in decision-making processes. The observed differences underline the importance of scenario and fault condition in influencing decision outcomes and point to the need for tailored strategies or interventions to mitigate the adverse effects associated with these specific conditions.

 *Estimated Marginal Means for Scenario*

| Scenario | Mean  | Std. Error | 95% Lower Bound | 95% Upper Bound |
|----------|-------|------------|-----------------|-----------------|
| LOFW     | 0.979 | 0.021      | 0.938           | 1.020           |
| SGTR     | 0.812 | 0.057      | 0.701           | 0.924           |

*Estimated Marginal Means for Fault Condition*

| Fault Condition | Mean | Std. Error | 95% Lower Bound | 95% Upper Bound |
|-----------------|------|------------|-----------------|-----------------|
| True Fault           | 1    | 0          | 1               | 1               |
| Spoof           | 0.792| 0.059      | 0.676           | 0.908           |


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

There were no significant effects between subjects.

#### Within-subject
For the within-subject effects on **Diagnosis Time**, our analysis indicates significant main effects related to **Scenario**, the interaction between **Scenario** and **Expertise**, and a notable effect of **Fault Condition**.

* ***Scenario**: $F(1, 22) = 20.369, p < 0.001$
* **Fault Condition**: $F(1, 22) = 6.550, p = 0.018$
* **Scenario * Expertise Interaction**: $F(1, 22) = 17.902, p < 0.001$

**Scenario**: The effect of Scenario on Diagnosis Time was significant, with an F-value of 20.369 and a p-value less than 0.001, indicating a strong influence of the scenario type on the time taken to diagnose. The effect size, $\eta^2_G$, is 0.208, suggesting that about 20.8% of the variance in Diagnosis Time can be attributed to differences in Scenarios. The observation of a significant effect here aligns with our expectation that the context or nature of a scenario would impact diagnostic efficiency.

**Fault Condition:** The analysis also revealed a significant effect of **Fault Condition** on Diagnosis Time, with an F-value of 6.550 and a p-value of 0.018. This effect, with an effect size of 0.058, accounts for approximately 5.8% of the variance in Diagnosis Time. This result suggests that the type of fault presented influences how quickly participants can diagnose the issue, though its impact is less pronounced compared to the Scenario effect.

**Scenario * Expertise**: There was a significant interaction between Scenario and Expertise on Diagnosis Time, as indicated by an F-value of 17.902 and a p-value less than 0.001. The effect size for this interaction is 0.188, indicating that this interaction explains about 18.8% of the variance in Diagnosis Time. This finding suggests that the impact of the scenario on diagnosis time varies depending on the expertise of the participant, implying that certain scenarios may be more challenging for students compared to operators.

*Estimated Marginal Means Analysis:*

The Estimated Marginal Means for **Scenario** reveal that the LOFW scenario resulted in a higher mean diagnosis time (259.646 seconds) compared to the SGTR scenario (150.979 seconds), suggesting that the LOFW scenario is more complex or challenging, requiring more time for diagnosis.
    
Participants took longer to diagnose Spoof faults (mean = 231.500 seconds) compared to True Fault conditions (mean = 179.125 seconds), indicating that Spoof faults are more difficult to diagnose.
    
The analysis of **Expertise** shows that Operators (mean = 222.062 seconds) had a somewhat higher diagnosis time on average compared to Students (mean = 188.562 seconds), though this difference may be influenced by the scenarios and fault conditions they encountered.
    
The **Scenario * Fault Condition** and **Scenario * Expertise** interactions suggest that the diagnostic challenges vary significantly with different combinations of scenarios, fault conditions, and participant expertise. For instance, the SGTR scenario with a True Fault condition had the lowest mean diagnosis time (130.792 seconds), indicating certain conditions are diagnosed more efficiently than others.

*Estimated Marginal Means for Scenario*

| Scenario | Mean    | Std. Error | 95% Lower Bound | 95% Upper Bound |
| -------- | ------- | ---------- | --------------- | --------------- |
| LOFW     | 259.646 | 18.536     | 223.315         | 295.976         |
| SGTR     | 150.979 | 17.131     | 117.403         | 184.556         |

*Estimated Marginal Means for Fault Condition*

| Fault Condition | Mean    | Std. Error | 95% Lower Bound | 95% Upper Bound |
| --------------- | ------- | ---------- | --------------- | --------------- |
| Fault           | 179.125 | 17.257     | 145.301         | 212.949         |
| Spoof           | 231.500 | 20.873     | 190.589         | 272.411         |

*Estimated Marginal Means for Expertise*

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

# Conclusions and Discussion

