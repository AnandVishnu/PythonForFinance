# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:36:49 2016

@author: anandvishnu
"""

def bsm_call_value(S0, K, T, r, sigma):
    """ Valuation of European Call option in BSM model.
    Analytical Formula.
    
    Parameters
    ---------------------------------------------------
    S0    : <float>, Intial Stock price
    K     : <float>, strike price
    T     : <float>, maturity date (in years fraction)
    r     : <float>, constant risk-free short rate
    sigma : <float>, vol factor in diffusion
    
    Returns
    ---------------------------------------------------
    call_value : <float>, PV of European call option
    """
    from math import log, sqrt, exp
    from scipy import stats
    
    S0 = float(S0)
    d1 = (log(S0/K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0/K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    
    call_value = (S0 * stats.norm.cdf(d1, 0.0, 1.0)
                  - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    
    return call_value


def bsm_vega(S0, K, T, r, sigma):
    """ Vega of European option in BSM model
    
    Parameters
    ---------------------------------------------------
    S0    : <float>, Intial Stock price
    K     : <float>, strike price
    T     : <float>, maturity date (in years fraction)
    r     : <float>, constant risk-free short rate
    sigma : <float>, vol factor in diffusion
    
    Returns
    ---------------------------------------------------
    vega : <float>, Partial derivative of BSM formula with respect to sigma
    """
    from math import log, sqrt
    from scipy import stats
    
    S0 = float(S0)
    d1 = (log(S0/K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * (sqrt(T))
    
    return vega


def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it=100):
    """ IV of European call option
    Parameters
    -----------------------------------------------------------
    S0        : <float>, Intial Stock price
    K         : <float>, strike price
    T         : <float>, maturity date (in years fraction)
    r         : <float>, constant risk-free short rate
    sigma_est : <float>, estimate of vol factor in diffusion
    it        : <integer> number of iteration
    
    Returns
    -----------------------------------------------------------
    sigma_est : <float>, numerically estimated IV
    """
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, r, T, sigma_est) - C0)/
                      bsm_vega(S0, K, r, T, sigma_est))
        
        return sigma_est


    