import matplotlib.pyplot as plt
import math


def pmf_bernoulli(p, x):
    # if (x == 1):
    #     return p
    # else:
    #     return 1 - p

    return (p ** x) * (1 - p) ** (1 - x)


def plot_pmf_bernoulli(p):
    X = [0, 1]
    P_bernoulli = [pmf_bernoulli(p, x) for x in X]
    plt.plot(X, P_bernoulli, 'o')

    plt.title('PMF of bernoulli(p=%.2f)' % (p))
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()

# plot_pmf_bernoulli(0.5)


def pmf_binom(k, n, p):
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * (p ** k) * ((1 - p) ** (n - k))


def plot_pmf_binom(n, p):
    K = list(range(0, n + 1))
    P_binom = [pmf_binom(k, n, p) for k in K]
    plt.plot(K, P_binom, '-o')
    axes = plt.gca()
    axes.set_xlim([0, n])
    axes.set_ylim([0, 1.1 * max(P_binom)])
    plt.title('PMF of Bin(%i, %.2f)' % (n, p))
    plt.xlabel('Number k of successes')
    plt.ylabel('Probability of k successes')
    plt.show()

# plot_pmf_binom(15, 0.5)


def pmf_poisson(k, lam):
    return (lam ** k) * (math.e ** (-lam)) / math.factorial(k)


def plot_pmf_poisson(n, lam):
    K = list(range(0, n + 1))
    P_poisson = [pmf_poisson(k, lam) for k in K]
    plt.plot(K, P_poisson, '-o')
    plt.title('PMF of Poisson(%i)' % (lam))
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()

# plot_pmf_poisson(25, 5)


def pmf_geo(p, x):
    return p * ((1 - p) ** (x - 1))


def plot_pmf_geo(p, n):
    X = list(range(1, n + 1))
    P_geo = [pmf_geo(p, x) for x in X]
    plt.plot(X, P_geo, '-o')
    plt.title('PMF of Geometric(%.2f)' % (p))
    plt.xlabel('n')
    plt.ylabel('Probability')
    plt.show()

# plot_pmf_geo(0.3, 10)


""" Exercise 1 """


def prob_2_machine_broken_in_1_session():
    return pmf_binom(2, 5, 0.1)


# print(round(prob_2_machine_broken_in_1_session(), 3))


def plot_exercise1():
    plot_pmf_binom(5, 0.1)


# plot_exercise1()


""" Exercise 2 """


def prob_receive_2_calls_in_1_minute():
    return pmf_poisson(2, 3)

# print(round(prob_receive_2_calls_in_1_minute(), 3))


def plot_exercise2():
    K = list(range(1, 6))
    P_poisson = [pmf_poisson(k, 3) for k in K]
    plt.plot(K, P_poisson, '-o')
    plt.title('PMF of Poisson(%i)' % (3))
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()


# plot_exercise2()


""" Exercise 3 """


def prob_a_person_hit_target_in_3rd_try():
    return pmf_geo(0.4, 3)

# print(prob_a_person_hit_target_in_3rd_try())


def plot_exercise3():
    plot_pmf_geo(0.4, 10)

# plot_exercise3()
