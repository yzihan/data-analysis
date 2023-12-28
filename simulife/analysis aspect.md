# analysis aspect

## Conversation data


### Conversation Length
 Line 1: Human
 Line 2: AI

| Single Character Chatting | Group Chatting | Sage Agent 
--|----------|----------|----------
With sage agent group|  |  |  
Without sage agent group|  |  |  



### Time Duration



### Sage Agent -- Topic

Which types of guidance they gave

![conversation](./conversation.png)



## Story

### Narration Arc and Cognition Tension

Link: https://www.liwc.app/help/aon

![narrative](./narrative.png)





## Scale

### Tests for Small Samples

1. **Student's t-test (for small, independent samples):**
   - **Usage**: Suitable when you have two independent groups with small sample sizes. It's often used when the sample sizes are less than 30.
   - **Assumptions**: Assumes that the data are normally distributed and the variances in the two groups are equal (homoscedasticity).
   - **Data Type**: Typically used for continuous data, although it can be applied to discrete data if the normality assumption is met.
   - **Conclusion**: Determines if there is a significant difference between the means of the two groups.
   - **Sensitivity**: More sensitive to outliers compared to non-parametric tests.
2. **Mann-Whitney U Test (non-parametric):**
   - **Usage**: Applicable when the data does not meet the normality assumption. It’s a good alternative to the t-test for small samples that are not normally distributed.
   - **Assumptions**: Assumes that the two samples are independent and that the observations are ordinal or continuous.
   - **Data Type**: Suitable for ordinal data (like Likert scales) or continuous data that is not normally distributed.
   - **Conclusion**: Tests whether one sample is stochastically greater than the other, a useful test for median differences.
   - **Sensitivity**: Less sensitive to outliers and more robust for smaller sample sizes or non-normal data.

