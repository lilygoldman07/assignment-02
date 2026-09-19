# CMPS 2200 Assignment 02
## Answers

**Name:** Lily Goldman


Place all written answers from `assignment-02.md` here for easier grading.

1. **Asymptotic notation**

    a) $T(n)=2T(n/3)+1$
$\log_3 2 \approx 0.63 > 0$, so the leaves dominate (Master Theorem case 1).
$T(n) \in O(n^{\log_3 2})$


    b) $T(n)=5T(n/4)+n$

 $\log_4 5 \approx 1.16 > 1$, so the leaves dominate.
 $T(n) \in O(n^{\log_4 5})$

    c) $T(n)=7T(n/7)+n$
 $\log_7 7 = 1$, so every level costs $n$ and there are $\log_7 n$ levels (balanced).
    $T(n) \in O(n \log n)$


    d) $T(n)=9T(n/3)+n^2$
$\log_3 9 = 2$, so every level costs $n^2$ over $\log_3 n$ levels (balanced).
    $T(n) \in O(n^2 \log n)$
    e) $T(n)=8T(n/2)+n^3$
$\log_2 8 = 3$, so every level costs $n^3$ over $\log_2 n$ levels (balanced).
    $T(n) \in O(n^3 \log n)$ 
    f) $T(n)=49T(n/25)+n^{3/2}\log n$
 $\log_{25} 49 \approx 1.21 < 3/2$, so the root dominates (level costs shrink geometrically).
    $T(n) \in O(n^{3/2} \log n)$
    g) $T(n)=T(n-1)+2$
There are $n$ levels, each costing 2, so $T(n) = 2n$.
    $T(n) \in O(n)$

    h) $T(n)= T(n-1)+n^c$, with $c\geq 1$
$T(n) = \sum_{i=1}^{n} i^c \le n \cdot n^c$.
    $T(n) \in O(n^{c+1})$ 
    i) $T(n)=T(\sqrt{n})+1$
Let $n = 2^{m}$. Each step halves $m$ ($\sqrt{2^m} = 2^{m/2}$), stopping at $m = 1$ ($n=2$), so there are $\log_2 m = \log_2 \log_2 n$ levels, each costing 1.
    $T(n) \in O(\log \log n)$
   
2. **Algorithms Comparison**
    Algorithm $\mathcal{A}$: $T(n) = 5T(n/2) + n$. Since $\log_2 5 \approx 2.32 > 1$, the leaves dominate: $O(n^{\log_2 5}) \approx O(n^{2.32})$.
    Algorithm $\mathcal{B}$: $T(n) = 2T(n-1) + 1$. The number of calls doubles at each of the $n$ levels, so $T(n) = 2^n - 1$: $O(2^n)$.
    Algorithm $\mathcal{C}$: $T(n) = 9T(n/3) + n^2$. Since $\log_3 9 = 2$, it is balanced: $O(n^2 \log n)$.
    I would choose **Algorithm $\mathcal{C}$**, since $n^2 \log n$ grows slower than $n^{2.32}$ and much slower than $2^n$.