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

```
Take this anova output and summarize the output into the following latex template example. The template demonstrates how I summarize a similar anova output for a different measure; replace the irrelevant parts with the new material.

Things to adjust while formatting:

1) change the variable term "Fault Condition" to "Fault". 
- change the Fault value of "Fault" to "True Fault"
- result: Fault with two conditions: True Fault, Spoof

2) Order the output to follow this priority 
Main effects
- Expertise
- Scenario
- Fault
Interactions 2
Interactions 3

Here is the anova:
Running ANOVA for: Diagnosis Time
('Scenario', 'Fault Condition')
('Expertise',)
('Fault Condition', 'Expertise')
('Scenario', 'Fault Condition', 'Expertise')
{('Scenario',): {'y2': array([232.47916667, 178.14583333]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 283402.6666666667, 'mss': 283402.6666666667, 'dfe': 22.0, 'sse': 306098.95833333326, 'mse': 13913.589015151512, 'F': 20.36876799782206, 'p': 0.0001722391992978486, 'eta': 0.2081094358456441, 'obs': 48.0, 'critT': 2.073873067904015, 'se': 18.01461840526471, 'ci': 35.30865207431883, 'lambda': 44.440948358884484, 'power': 0.9999944775423111, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 283402.6666666667, 'mse_gg': 13913.589015151512, 'F_gg': 20.36876799782206, 'p_gg': 0.0001722391992978486, 'obs_gg': 48.0, 'critT_gg': 2.073873067904015, 'se_gg': 18.01461840526471, 'ci_gg': 35.30865207431883, 'lambda_gg': 44.440948358884484, 'power_gg': 0.9999944775423111, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 283402.6666666667, 'mse_hf': 13913.589015151512, 'F_hf': 20.36876799782206, 'p_hf': 0.0001722391992978486, 'obs_hf': 48.0, 'critT_hf': 2.073873067904015, 'se_hf': 18.01461840526471, 'ci_hf': 35.30865207431883, 'lambda_hf': 44.440948358884484, 'power_hf': 0.9999944775423111, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 283402.6666666667, 'mse_lb': 13913.589015151512, 'F_lb': 20.36876799782206, 'p_lb': 0.0001722391992978486, 'obs_lb': 48.0, 'critT_lb': 2.073873067904015, 'se_lb': 18.01461840526471, 'ci_lb': 35.30865207431883, 'lambda_lb': 44.440948358884484, 'power_lb': 0.9999944775423111}, ('Fault Condition',): {'y2': array([192.21875, 218.40625]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 65835.375, 'mss': 65835.375, 'dfe': 22.0, 'sse': 221121.125, 'mse': 10050.960227272728, 'F': 6.550157747252777, 'p': 0.017882051291299928, 'eta': 0.05753688518874263, 'obs': 48.0, 'critT': 2.073873067904015, 'se': 15.311201039168534, 'ci': 30.009954036770324, 'lambda': 14.291253266733335, 'power': 0.9506104769458832, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 65835.375, 'mse_gg': 10050.960227272728, 'F_gg': 6.550157747252777, 'p_gg': 0.017882051291299928, 'obs_gg': 48.0, 'critT_gg': 2.073873067904015, 'se_gg': 15.311201039168534, 'ci_gg': 30.009954036770324, 'lambda_gg': 14.291253266733335, 'power_gg': 0.9506104769458832, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 65835.375, 'mse_hf': 10050.960227272728, 'F_hf': 6.550157747252777, 'p_hf': 0.017882051291299928, 'obs_hf': 48.0, 'critT_hf': 2.073873067904015, 'se_hf': 15.311201039168534, 'ci_hf': 30.009954036770324, 'lambda_hf': 14.291253266733335, 'power_hf': 0.9506104769458832, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 65835.375, 'mse_lb': 10050.960227272728, 'F_lb': 6.550157747252777, 'p_lb': 0.017882051291299928, 'obs_lb': 48.0, 'critT_lb': 2.073873067904015, 'se_lb': 15.311201039168534, 'ci_lb': 30.009954036770324, 'lambda_lb': 14.291253266733335, 'power_lb': 0.9506104769458832}, ('Scenario', 'Expertise'): {'y2': array([215.38541667, 249.57291667, 211.98958333, 144.30208333]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 249084.375, 'mss': 249084.375, 'dfe': 22.0, 'sse': 306098.95833333326, 'mse': 13913.589015151512, 'F': 17.902237498085793, 'p': 0.00034311137530081343, 'eta': 0.1876372845213102, 'obs': 24.0, 'critT': 2.073873067904015, 'se': 25.476517669701323, 'ci': 49.93397463261459, 'lambda': 19.52971363427541, 'power': 0.9880667689795171, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 249084.375, 'mse_gg': 13913.589015151512, 'F_gg': 17.902237498085793, 'p_gg': 0.00034311137530081343, 'obs_gg': 24.0, 'critT_gg': 2.073873067904015, 'se_gg': 25.476517669701323, 'ci_gg': 49.93397463261459, 'lambda_gg': 19.52971363427541, 'power_gg': 0.9880667689795171, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 249084.375, 'mse_hf': 13913.589015151512, 'F_hf': 17.902237498085793, 'p_hf': 0.00034311137530081343, 'obs_hf': 24.0, 'critT_hf': 2.073873067904015, 'se_hf': 25.476517669701323, 'ci_hf': 49.93397463261459, 'lambda_hf': 19.52971363427541, 'power_hf': 0.9880667689795171, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 249084.375, 'mse_lb': 13913.589015151512, 'F_lb': 17.902237498085793, 'p_lb': 0.00034311137530081343, 'obs_lb': 24.0, 'critT_lb': 2.073873067904015, 'se_lb': 25.476517669701323, 'ci_lb': 49.93397463261459, 'lambda_lb': 19.52971363427541, 'power_lb': 0.9880667689795171}, ('SUBJECT',): {'ss': 318553.625, 'sse': 291619.625, 'mse': 13255.4375, 'df': 23.0, 'dfe': 22.0}, ('TOTAL',): {'ss': 1720574.625, 'df': 95.0}, ('WITHIN',): {'ss': 1402021.0, 'df': 72.0}, ('Scenario', 'SUBJECT'): {'ss': 306098.95833333326, 'df': 22.0, 'mss': 13913.589015151512}, ('Fault Condition', 'SUBJECT'): {'ss': 221121.125, 'df': 22.0, 'mss': 10050.960227272728}, ('Scenario', 'Fault Condition', 'SUBJECT'): {'ss': 259553.95833333334, 'df': 22.0, 'mss': 11797.907196969698}}

In the latex, follow the model for "\item[Effects of Decision], continuing with the next \item[Effects on Diagnosis Time]

Here is the latex:

\begin{description}
    \item[Effects on Decision] Analysis revealed significant main effects and interactions impacting the correct decision-making in the trials.
        \paragraph{Main effects} 
            \begin{itemize}
                \item Expertise showed a statistically significant effect, $F(1, 22) = 11.355, p = 0.003$. 
                \item Scenario exhibited a significant effect, $F(1, 22) = 15.304, p < 0.001$
                \item Fault significantly influenced decisions, $F(1, 22) = 17.742, p < 0.001$.
            \end{itemize}
        \paragraph{Two-way interactions} 
            \begin{itemize}
                \item The interaction between Scenario and Fault was significant, $F(1, 22) = 15.304, p < 0.001$.
                \item The interaction of Scenario and Expertise also proved significant, $F(1, 22) = 8.609, p < 0.01$.
                \item Similarly, the Fault and Expertise interaction was significant, $F(1, 22) = 11.355, p < 0.01$.
            \end{itemize}
        \paragraph{Three-way interactions} 
            \begin{itemize}
                \item The three-way interaction among Scenario, Fault, and Expertise was significant, $F(1, 22) = 8.609, p < 0.01$.\\
            \end{itemize}
    
            This analysis illustrates the multifaceted influence on decision-making, underscoring the significant roles played by individual factors and their complex interactions.\\
    \item[Effects on Diagnosis Time] 

\end{description}

```

```
Running ANOVA for: Decision
Decision ~ Scenario * Fault Condition * Expertise

TESTS OF BETWEEN-SUBJECTS EFFECTS

Measure: Decision
     Source        Type III   df    MS       F      Sig.    et2_G   Obs.    SE     95% CI   lambda   Obs.  
                      SS                                                                             Power 
==========================================================================================================
Between Subjects      1.958   23                                                                           
Expertise             0.667    1   0.667   11.355   0.003   0.129     12   0.074    0.145    6.194   0.662 
==========================================================================================================
Error                 1.292   22   0.059                                                                   

TESTS OF WITHIN SUBJECTS EFFECTS

Measure: Decision
                Source                                        Type III   eps   df    MS       F        Sig.      et2_G   Obs.    SE     95% CI   lambda   Obs.  
                                                                 SS                                                                                       Power 
===============================================================================================================================================================
Scenario                                 Greenhouse-Geisser      0.667     1    1   0.667   15.304   7.472e-04   0.129     48   0.032    0.062   33.391       1 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Scenario * Expertise                     Greenhouse-Geisser      0.375     1    1   0.375    8.609       0.008   0.077     24   0.045    0.088    9.391   0.834 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Error(Scenario)                          Greenhouse-Geisser      0.958     1   22   0.044                                                                       
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Fault Condition                          Greenhouse-Geisser      1.042     1    1   1.042   17.742   3.594e-04   0.188     48   0.037    0.073   38.710       1 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Fault Condition * Expertise              Greenhouse-Geisser      0.667     1    1   0.667   11.355       0.003   0.129     24   0.052    0.103   12.387   0.920 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Error(Fault Condition)                   Greenhouse-Geisser      1.292     1   22   0.059                                                                       
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Scenario *                               Greenhouse-Geisser      0.667     1    1   0.667   15.304   7.472e-04   0.129     24   0.045    0.088   16.696   0.974 
Fault Condition                                                                                                                                                 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Scenario * Fault Condition * Expertise   Greenhouse-Geisser      0.375     1    1   0.375    8.609       0.008   0.077     12   0.064    0.125    4.696   0.545 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Error(Scenario *                         Greenhouse-Geisser      0.958     1   22   0.044                                                                       
Fault Condition)                                                                                                                                                

TABLES OF ESTIMATED MARGINAL MEANS

Estimated Marginal Means for Scenario
Scenario   Mean    Std. Error   95% Lower Bound   95% Upper Bound 
=================================================================
LOFW       0.979        0.021             0.938             1.020 
SGTR       0.812        0.057             0.701             0.924 

Estimated Marginal Means for Fault Condition
Fault Condition   Mean    Std. Error   95% Lower Bound   95% Upper Bound 
========================================================================
Fault                 1            0                 1                 1 
Spoof             0.792        0.059             0.676             0.908 

Estimated Marginal Means for Expertise
Expertise   Mean    Std. Error   95% Lower Bound   95% Upper Bound 
==================================================================
Operator    0.979        0.021             0.938             1.020 
Student     0.812        0.057             0.701             0.924 

Estimated Marginal Means for Scenario * Fault Condition
Scenario   Fault Condition   Mean    Std. Error   95% Lower Bound   95% Upper Bound 
===================================================================================
LOFW       Fault                 1            0                 1                 1 
LOFW       Spoof             0.958        0.042             0.877             1.040 
SGTR       Fault                 1            0                 1                 1 
SGTR       Spoof             0.625        0.101             0.427             0.823 

Estimated Marginal Means for Scenario * Expertise
Scenario   Expertise   Mean    Std. Error   95% Lower Bound   95% Upper Bound 
=============================================================================
LOFW       Operator        1            0                 1                 1 
LOFW       Student     0.958        0.042             0.877             1.040 
SGTR       Operator    0.958        0.042             0.877             1.040 
SGTR       Student     0.667        0.098             0.474             0.859 

Estimated Marginal Means for Fault Condition * Expertise
Fault Condition   Expertise   Mean    Std. Error   95% Lower Bound   95% Upper Bound 
====================================================================================
Fault             Operator        1            0                 1                 1 
Fault             Student         1            0                 1                 1 
Spoof             Operator    0.958        0.042             0.877             1.040 
Spoof             Student     0.625        0.101             0.427             0.823 

Estimated Marginal Means for Scenario * Fault Condition * Expertise
Scenario   Fault Condition   Expertise   Mean    Std. Error   95% Lower Bound   95% Upper Bound 
===============================================================================================
LOFW       Fault             Operator        1            0                 1                 1 
LOFW       Fault             Student         1            0                 1                 1 
LOFW       Spoof             Operator        1            0                 1                 1 
LOFW       Spoof             Student     0.917        0.083             0.753             1.080 
SGTR       Fault             Operator        1            0                 1                 1 
SGTR       Fault             Student         1            0                 1                 1 
SGTR       Spoof             Operator    0.917        0.083             0.753             1.080 
SGTR       Spoof             Student     0.333        0.142             0.055             0.612 


{('Scenario',): {'y2': array([0.9375    , 0.85416667]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 0.666666666666667, 'mss': 0.666666666666667, 'dfe': 22.0, 'sse': 0.9583333333333329, 'mse': 0.04356060606060604, 'F': 15.30434782608697, 'p': 0.0007471703218912499, 'eta': 0.1290322580645162, 'obs': 48.0, 'critT': 2.073873067904015, 'se': 0.0318751647707117, 'ci': 0.06247532295059493, 'lambda': 33.39130434782612, 'power': 0.9998090202232512, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 0.666666666666667, 'mse_gg': 0.04356060606060604, 'F_gg': 15.30434782608697, 'p_gg': 0.0007471703218912499, 'obs_gg': 48.0, 'critT_gg': 2.073873067904015, 'se_gg': 0.0318751647707117, 'ci_gg': 0.06247532295059493, 'lambda_gg': 33.39130434782612, 'power_gg': 0.9998090202232512, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 0.666666666666667, 'mse_hf': 0.04356060606060604, 'F_hf': 15.30434782608697, 'p_hf': 0.0007471703218912499, 'obs_hf': 48.0, 'critT_hf': 2.073873067904015, 'se_hf': 0.0318751647707117, 'ci_hf': 0.06247532295059493, 'lambda_hf': 33.39130434782612, 'power_hf': 0.9998090202232512, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 0.666666666666667, 'mse_lb': 0.04356060606060604, 'F_lb': 15.30434782608697, 'p_lb': 0.0007471703218912499, 'obs_lb': 48.0, 'critT_lb': 2.073873067904015, 'se_lb': 0.0318751647707117, 'ci_lb': 0.06247532295059493, 'lambda_lb': 33.39130434782612, 'power_lb': 0.9998090202232512}, ('Fault Condition',): {'y2': array([0.94791667, 0.84375   ]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 1.041666666666667, 'mss': 1.041666666666667, 'dfe': 22.0, 'sse': 1.291666666666666, 'mse': 0.05871212121212119, 'F': 17.74193548387098, 'p': 0.0003594014016013766, 'eta': 0.18796992481203015, 'obs': 48.0, 'critT': 2.073873067904015, 'se': 0.0370057633607433, 'ci': 0.07253129618705687, 'lambda': 38.70967741935487, 'power': 0.9999645642306089, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 1.041666666666667, 'mse_gg': 0.05871212121212119, 'F_gg': 17.74193548387098, 'p_gg': 0.0003594014016013766, 'obs_gg': 48.0, 'critT_gg': 2.073873067904015, 'se_gg': 0.0370057633607433, 'ci_gg': 0.07253129618705687, 'lambda_gg': 38.70967741935487, 'power_gg': 0.9999645642306089, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 1.041666666666667, 'mse_hf': 0.05871212121212119, 'F_hf': 17.74193548387098, 'p_hf': 0.0003594014016013766, 'obs_hf': 48.0, 'critT_hf': 2.073873067904015, 'se_hf': 0.0370057633607433, 'ci_hf': 0.07253129618705687, 'lambda_hf': 38.70967741935487, 'power_hf': 0.9999645642306089, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 1.041666666666667, 'mse_lb': 0.05871212121212119, 'F_lb': 17.74193548387098, 'p_lb': 0.0003594014016013766, 'obs_lb': 48.0, 'critT_lb': 2.073873067904015, 'se_lb': 0.0370057633607433, 'ci_lb': 0.07253129618705687, 'lambda_lb': 38.70967741935487, 'power_lb': 0.9999645642306089}, ('Scenario', 'Fault Condition'): {'y2': array([0.94791667, 0.92708333, 0.94791667, 0.76041667]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 0.6666666666666664, 'mss': 0.6666666666666664, 'dfe': 22.0, 'sse': 0.9583333333333326, 'mse': 0.04356060606060603, 'F': 15.304347826086962, 'p': 0.0007471703218912516, 'eta': 0.12903225806451613, 'obs': 24.0, 'critT': 2.073873067904015, 'se': 0.045078290321617566, 'ci': 0.08835344903037043, 'lambda': 16.695652173913047, 'power': 0.9739299448135662, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 0.6666666666666664, 'mse_gg': 0.04356060606060603, 'F_gg': 15.304347826086962, 'p_gg': 0.0007471703218912516, 'obs_gg': 24.0, 'critT_gg': 2.073873067904015, 'se_gg': 0.045078290321617566, 'ci_gg': 0.08835344903037043, 'lambda_gg': 16.695652173913047, 'power_gg': 0.9739299448135662, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 0.6666666666666664, 'mse_hf': 0.04356060606060603, 'F_hf': 15.304347826086962, 'p_hf': 0.0007471703218912516, 'obs_hf': 24.0, 'critT_hf': 2.073873067904015, 'se_hf': 0.045078290321617566, 'ci_hf': 0.08835344903037043, 'lambda_hf': 16.695652173913047, 'power_hf': 0.9739299448135662, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 0.6666666666666664, 'mse_lb': 0.04356060606060603, 'F_lb': 15.304347826086962, 'p_lb': 0.0007471703218912516, 'obs_lb': 24.0, 'critT_lb': 2.073873067904015, 'se_lb': 0.045078290321617566, 'ci_lb': 0.08835344903037043, 'lambda_lb': 16.695652173913047, 'power_lb': 0.9739299448135662}, ('Expertise',): {'y2': array([0.9375    , 0.85416667]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 0.6666666666666663, 'mss': 0.6666666666666663, 'sse': 1.2916666666666672, 'dfe': 22.0, 'mse': 0.058712121212121236, 'F': 11.354838709677407, 'p': 0.0027639991743925924, 'eta': 0.1290322580645161, 'obs': 12.0, 'critT': 2.073873067904015, 'se': 0.07401152672148663, 'ci': 0.14506259237411379, 'lambda': 6.193548387096769, 'power': 0.6624148483529494}, ('Scenario', 'Expertise'): {'y2': array([0.94791667, 0.92708333, 0.92708333, 0.78125   ]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 0.3750000000000001, 'mss': 0.3750000000000001, 'dfe': 22.0, 'sse': 0.9583333333333329, 'mse': 0.04356060606060604, 'F': 8.60869565217392, 'p': 0.007679868437765414, 'eta': 0.07692307692307696, 'obs': 24.0, 'critT': 2.073873067904015, 'se': 0.04507829032161757, 'ci': 0.08835344903037044, 'lambda': 9.391304347826095, 'power': 0.8335822490341004, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 0.3750000000000001, 'mse_gg': 0.04356060606060604, 'F_gg': 8.60869565217392, 'p_gg': 0.007679868437765414, 'obs_gg': 24.0, 'critT_gg': 2.073873067904015, 'se_gg': 0.04507829032161757, 'ci_gg': 0.08835344903037044, 'lambda_gg': 9.391304347826095, 'power_gg': 0.8335822490341004, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 0.3750000000000001, 'mse_hf': 0.04356060606060604, 'F_hf': 8.60869565217392, 'p_hf': 0.007679868437765414, 'obs_hf': 24.0, 'critT_hf': 2.073873067904015, 'se_hf': 0.04507829032161757, 'ci_hf': 0.08835344903037044, 'lambda_hf': 9.391304347826095, 'power_hf': 0.8335822490341004, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 0.3750000000000001, 'mse_lb': 0.04356060606060604, 'F_lb': 8.60869565217392, 'p_lb': 0.007679868437765414, 'obs_lb': 24.0, 'critT_lb': 2.073873067904015, 'se_lb': 0.04507829032161757, 'ci_lb': 0.08835344903037044, 'lambda_lb': 9.391304347826095, 'power_lb': 0.8335822490341004}, ('Fault Condition', 'Expertise'): {'y2': array([0.94791667, 0.94791667, 0.92708333, 0.76041667]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 0.6666666666666666, 'mss': 0.6666666666666666, 'dfe': 22.0, 'sse': 1.291666666666666, 'mse': 0.05871212121212119, 'F': 11.354838709677423, 'p': 0.0027639991743925807, 'eta': 0.12903225806451613, 'obs': 24.0, 'critT': 2.073873067904015, 'se': 0.052334052430732546, 'ci': 0.10257474276423578, 'lambda': 12.387096774193553, 'power': 0.9195757125364227, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 0.6666666666666666, 'mse_gg': 0.05871212121212119, 'F_gg': 11.354838709677423, 'p_gg': 0.0027639991743925807, 'obs_gg': 24.0, 'critT_gg': 2.073873067904015, 'se_gg': 0.052334052430732546, 'ci_gg': 0.10257474276423578, 'lambda_gg': 12.387096774193553, 'power_gg': 0.9195757125364227, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 0.6666666666666666, 'mse_hf': 0.05871212121212119, 'F_hf': 11.354838709677423, 'p_hf': 0.0027639991743925807, 'obs_hf': 24.0, 'critT_hf': 2.073873067904015, 'se_hf': 0.052334052430732546, 'ci_hf': 0.10257474276423578, 'lambda_hf': 12.387096774193553, 'power_hf': 0.9195757125364227, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 0.6666666666666666, 'mse_lb': 0.05871212121212119, 'F_lb': 11.354838709677423, 'p_lb': 0.0027639991743925807, 'obs_lb': 24.0, 'critT_lb': 2.073873067904015, 'se_lb': 0.052334052430732546, 'ci_lb': 0.10257474276423578, 'lambda_lb': 12.387096774193553, 'power_lb': 0.9195757125364227}, ('Scenario', 'Fault Condition', 'Expertise'): {'y2': array([0.94791667, 0.94791667, 0.94791667, 0.90625   , 0.94791667,
       0.94791667, 0.90625   , 0.61458333]), 'df': 1.0, 'eps_gg': 1.0, 'eps_hf': 1.0, 'eps_lb': 1.0, 'ss': 0.375, 'mss': 0.375, 'dfe': 22.0, 'sse': 0.9583333333333326, 'mse': 0.04356060606060603, 'F': 8.60869565217392, 'p': 0.007679868437765414, 'eta': 0.07692307692307694, 'obs': 12.0, 'critT': 2.073873067904015, 'se': 0.06375032954142339, 'ci': 0.12495064590118983, 'lambda': 4.6956521739130475, 'power': 0.5445816890558139, 'df_gg': 1.0, 'dfe_gg': 22.0, 'mss_gg': 0.375, 'mse_gg': 0.04356060606060603, 'F_gg': 8.60869565217392, 'p_gg': 0.007679868437765414, 'obs_gg': 12.0, 'critT_gg': 2.073873067904015, 'se_gg': 0.06375032954142339, 'ci_gg': 0.12495064590118983, 'lambda_gg': 4.6956521739130475, 'power_gg': 0.5445816890558139, 'df_hf': 1.0, 'dfe_hf': 22.0, 'mss_hf': 0.375, 'mse_hf': 0.04356060606060603, 'F_hf': 8.60869565217392, 'p_hf': 0.007679868437765414, 'obs_hf': 12.0, 'critT_hf': 2.073873067904015, 'se_hf': 0.06375032954142339, 'ci_hf': 0.12495064590118983, 'lambda_hf': 4.6956521739130475, 'power_hf': 0.5445816890558139, 'df_lb': 1.0, 'dfe_lb': 22.0, 'mss_lb': 0.375, 'mse_lb': 0.04356060606060603, 'F_lb': 8.60869565217392, 'p_lb': 0.007679868437765414, 'obs_lb': 12.0, 'critT_lb': 2.073873067904015, 'se_lb': 0.06375032954142339, 'ci_lb': 0.12495064590118983, 'lambda_lb': 4.6956521739130475, 'power_lb': 0.5445816890558139}, ('SUBJECT',): {'ss': 1.9583333333333335, 'sse': 1.2916666666666672, 'mse': 0.058712121212121236, 'df': 23.0, 'dfe': 22.0}, ('TOTAL',): {'ss': 8.958333333333332, 'df': 95.0}, ('WITHIN',): {'ss': 6.999999999999998, 'df': 72.0}, ('Scenario', 'SUBJECT'): {'ss': 0.9583333333333329, 'df': 22.0, 'mss': 0.04356060606060604}, ('Fault Condition', 'SUBJECT'): {'ss': 1.291666666666666, 'df': 22.0, 'mss': 0.05871212121212119}, ('Scenario', 'Fault Condition', 'SUBJECT'): {'ss': 0.9583333333333326, 'df': 22.0, 'mss': 0.04356060606060603}}
```