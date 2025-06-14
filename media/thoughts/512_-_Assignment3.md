Muhammet Fatih DİNÇ
2023776042
DSAI512 - HW3

Confession: I took considerable help from ChatGPT, but every line of the submitted homework, reviewed , then was put to the document.

### Question 1 ###
There are 100 two-dimensional points on a plane as shown below. The coordinates of points are saved in first two columns in data.xlsx. The class labels of the points are saved in the third column in data.xlsx, where -1 represents blue and 1 represents red. Please implement PLA to find a boundary that can perfectly separate blue points and red points. Write down the equations of the separator and plot the separator together with data.
### Solution 1 ###
Following step-by-step solution method is embraced

0. Load the file
1. Extract features and labels 
2. Add a bias term to the features
3. Initialize weights to zeros
4. Define the Perceptron Learning Algorithm: It works as, if the sum of the input signals exceeds a certain threshold, it either outputs a signal or does not return an output.

![[512_hw1_1.png]]

since learned weights are 1, 2.125, -3.440, equation becomes
$$
x_2 = \frac{2.125}{3.4440}x_1+\frac{1}{3.4440}
$$




### Question 2 ###
In Lecture 10 (slide #16), we applied the pocket algorithm for recognition of handwritten digits “1” versus “5” using intensity and symmetry as features. Try to reproduce the above results (at least try to obtain similar results) by downloading the related data from “data” section of the link below and apply the pocket algorithm.
### Solution 2 ###
Following step-by-step solution is embraced to solve the problem

1. Load the data, select the ones with '1' and '5'
2. Extract features and labels
3. Add a bias term to the features
4. Run the Pocket Algorithm with max_iterations = 1000
5. Plot the desired error and separator graphs

![[512_img1.png]]

Comments: Results are expected (though not the same with the given one in the slide) and can be considered as successful result since error false to around %2.






### Question  3 ###
Estimate the VC dimensions for the following hypothesis sets: a. H = {h_1, h_2, ..., h_m } where each h_i is a different model. b. H is a set of discs in R^2 c. H is a set of triangles in R^2
### Solution 3 ###
##### a. \(H = \{h_1, h_2, ..., h_m\}\) where each \(h_i\) is a different model: m #####

The VC dimension of this hypothesis set is indeed \(m\). If each model \(h_i\) is distinct, then we can shatter any set of \(m\) points by assigning different models to each point. However, we cannot shatter any set of \(m + 1\) points because there are only \(m\) distinct models.


##### b. \(H\) is a set of discs in \(\mathb{R}^2\): 3 #####

The VC dimension of a set of discs in \(\mathbb{R}^2\) is \(3\). Here's a brief explanation:

- **Lower Bound:** The lower bound for the VC dimension of any set of discs in \(\mathbb{R}^d\) is \(d + 1\). In this case, \(d = 2\), so the lower bound is \(3\).

- **Upper Bound:** To establish the upper bound, we can show that there exists a set of 3 points that can be shattered by a set of discs. For example, we can consider three points forming the vertices of an equilateral triangle. Any arrangement of labels (positive or negative) for these three points can be achieved by choosing appropriately sized discs.

Therefore, the VC dimension of a set of discs in \(\mathbb{R}^2\) is **\(3\)** .



##### c. Answer is 6. #####

1. **Lower Bound:** It's known that the VC dimension for any set of convex shapes in ({R}^d) is at least (d + 1\). In this case, since we are dealing with triangles in ({R}^2), the lower bound is (2 + 1 = 3).

2. **Upper Bound:** The upper bound is established by providing a specific set of points that can be shattered by the hypothesis set. For triangles in {R}^2, we can take a set of 6 points arranged in the form of a hexagon. These points can be shattered by different triangles (with vertices chosen from the 6 points). However, it's not possible to shatter any set of 7 points.

Therefore, the correct VC dimension for a set of triangles in {R}^2 is (6).





### Question 4 ###

Suppose that m_H = N + 1, so d_VC = 1. You have 100 training examples. Use the generalization bound to give a bound for E_out with a confidence of 90%. Repeat for N = 10000
### Solution 4 ###

a. The generalization bound provides an upper bound on the out-of-sample error \(E_{\text{out}}\) with a certain confidence level. The bound is given by:

$$
 E_{\text{out}} \leq E_{\text{in}} + \sqrt{\frac{8}{N} \ln\left(\frac{4((2N)^{d_{\text{VC}}} + 1)}{\delta}\right)} 
$$

where:
- \(E_{\text{in}}\) is the in-sample error.
- \(N\) is the number of training examples.
- \(d_{\text{VC}}\) is the VC dimension of the hypothesis set.
- \(\delta\) is the confidence level.

Given \(m_H = N + 1\), we have \(d_{\text{VC}} = 1\).

Let's calculate the bound for \(N = 100\) with a confidence level of 90%, and then repeat for \(N = 10,000\).

### For \(N = 100\):
$$
E_{\text{out}} \leq E_{\text{in}} + \sqrt{\frac{8}{100} \ln\left(\frac{4((2 \times 100)^1 + 1)}{0.1}\right)}
$$

After running in python, result came out as:
Bound for N = 100: 0.8481596247015304





### For \(N = 10,000\):
$$
E_{\text{out}} \leq E_{\text{in}} + \sqrt{\frac{8}{10000} \ln\left(\frac{4((2 \times 10000)^1 + 1)}{0.1}\right)} 
$$

Bound for N = 10000: 0.10427815497178729 

came out after running python code.

These calculations provide the upper bounds on E_out for the given values of \(N\) and confidence levels.






b. for an H with d_VC = 10, what sample size do you need (as prescribed by the generalization bound) to have a 95% confidence that your generalization error is at most 0.05?

452957



The generalization bound for the out-of-sample error is given by:
$$
E_{\text{out}} \leq E_{\text{in}} + \sqrt{\frac{8}{N} \ln\left(\frac{4((2N)^{d_{\text{VC}}} + 1)}{\delta}\right)}
$$


In our case, we want to find the required sample size (\(N\)) such that \(E_{\text{out}} \leq 0.05\) with a confidence level of 95% (\(\delta = 0.05\)) and assuming \(d_{\text{VC}} = 10\). Let's set \(E_{\text{in}} = 0\) for simplicity.

The equation becomes:
$$
0.05 \geq \sqrt{\frac{8}{N} \ln\left(\frac{4((2N)^{10} + 1)}{0.05}\right)}
$$


To find \(N\), we need to solve this inequality. It's a bit involved, and the solution involves iterative methods or numerical optimization. Python libraries like SciPy can be used for this.

Python script is used (which will be provided through Moodle)
Required Sample Size: **452957**


This script uses the `fsolve` function from SciPy to find the root of the equation. The result is the required sample size to achieve the desired bound on the generalization error with a 95% confidence level.





### Question 5 ##

When there is noise in the data, E_out(g^(D)) = E_(x, y)|g^(D)(x) - y(x))^2| where y(x) = f(x) + epsilon. if epsilon is a zero-mean noise random variable with variance sigma^2, show that the bias variance decomposition becomes E_D|E_out(g^(D))| = bias + var + sigma^2


### Solution 5 ###
The bias-variance decomposition for the expected out-of-sample error with noise can be derived as follows:

Given \(y(x) = f(x) + \epsilon\), where \(\epsilon\) is a zero-mean noise random variable with variance \(\sigma^2\), we have:

1.

The bias-variance decomposition for the expected out-of-sample error with noise can be derived as follows:

Given \(y(x) = f(x) + \epsilon\), where \(\epsilon\) is a zero-mean noise random variable with variance \(\sigma^2\), we have:

1. **Expected Out-of-Sample Error (\(E_{\text{out}})\):**
$$
[E_{\text{out}}(g^{(D)}) = E_{(x, y)}[(g^{(D)}(x) - y(x))^2]
$$
2. **Bias-Variance Decomposition:**
$$
[E_D[E_{\text{out}}(g^{(D)})] = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}\
$$
Now, let's compute each term:

- **Bias:** 
$$
  \text{Bias} = E_x[(g(x) - f(x))^2]
$$


- **Variance:**
$$
  \text{Variance} = E_D[(g^{(D)}(x) - E_D[g^{(D)}(x)])^2]
$$


- **Irreducible Error (due to noise):**
$$
  \text{Irreducible Error} = E_{(x, y)}[\epsilon^2] = \sigma^2
$$



Now, plug these into the bias-variance decomposition:
$$
E_D[E_{\text{out}}(g^{(D)})] = E_x[(g(x) - f(x))^2] + E_D[(g^{(D)}(x) - E_D[g^{(D)}(x)])^2] + \sigma^2
$$



This can be written more compactly as:
$$

E_D[E_{\text{out}}(g^{(D)})] = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}
$$



Therefore, the bias-variance decomposition for the expected out-of-sample error with noise is given by:
$$
E_D[E_{\text{out}}(g^{(D)})] = E_x[(g(x) - f(x))^2] + E_D[(g^{(D)}(x) - E_D[g^{(D)}(x)])^2] + \sigma^2
$$


This decomposition helps in understanding the factors contributing to the expected out-of-sample error, including the bias, variance, and irreducible error due to noise.

Therefore, the bias-variance decomposition for the expected out-of-sample error with noise is given by:
$$
E_D[E_{\text{out}}(g^{(D)})] = E_x[(g(x) - f(x))^2] + E_D[(g^{(D)}(x) - E_D[g^{(D)}(x)])^2] + \sigma^2
$$


This decomposition helps in understanding the factors contributing to the expected out-of-sample error, including the bias, variance, and irreducible error due to noise.




