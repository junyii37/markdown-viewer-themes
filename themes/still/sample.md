# Still · 留白

A short note that exercises everything the theme styles: math, code, tables, quotes, lists, and footnotes. 中文段落也能正常排版，标点和行距都照顾到了。

## 1. Math

Bayes' rule for a parameter $\theta$ given data $x$:

$$
p(\theta \mid x) = \frac{p(x \mid \theta)\, p(\theta)}{\int p(x \mid \theta')\, p(\theta')\, d\theta'}
$$

For i.i.d. $X_1, X_2, \dots$ with $\mathbb{E}|X_1| < \infty$, the weak law of large numbers gives
$\bar{X}_n \xrightarrow{P} \mu$, and Chebyshev's inequality reads ==the key tool== here:

$$
P\left(|X - \mathbb{E}X| \ge \varepsilon\right) \le \frac{\operatorname{Var}(X)}{\varepsilon^2}.
$$

> **Note.** Escaped braces and spacing such as $\{x : |x| \ge \varepsilon\}$ and $\int f\,d\mu$ render correctly.[^1]

## 2. Code

```python
import numpy as np

def em_step(x, pi, mu, sigma):
    # E-step: responsibilities
    r = pi * np.exp(-(x[:, None] - mu) ** 2 / (2 * sigma ** 2))
    r /= r.sum(axis=1, keepdims=True)
    return r  # shape (n, k)
```

Inline code like `np.linalg.solve` and a [link](https://github.com/simov/markdown-viewer).

## 3. Table

| Method | Convergence | Needs gradient |
| --- | :---: | :---: |
| EM | linear | no |
| Newton | quadratic | yes |
| Gradient descent | linear | yes |

## 4. Lists

- [x] Install Markdown Viewer
- [x] Upload `still.css` as a custom theme
- [ ] Read your notes in comfort

1. First item
2. Second item
   - nested bullet
   - another one

[^1]: Footnotes are styled in a muted color.

## 5. Long lines and nested lists

```text
experiment = {"model": "baseline", "seed": 42, "learning_rate": 0.0001, "evaluation": "held_out_dataset", "description": "This long line should scroll inside the code block without widening the page."}
```

1. 固定输入与随机种子。
   - 记录模型版本与实验参数。
   - 保留原始结果，便于复查。
2. 比较结果并记录下一步。

<details><summary>补充说明</summary>

正文之外的说明可以折叠收起。按 <kbd>⌘</kbd> + <kbd>−</kbd> 调整阅读大小。

</details>
