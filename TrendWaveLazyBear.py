import pandas_ta
import numpy 


"""
Source: https://tr.tradingview.com/script/2KE8wTuF-Indicator-WaveTrend-Oscillator-WT/

it returns the difference between wt1 and wt2, if it is positive, it means uptrend, if it is negative, it means downtrend.

Thanks to LazyBear for the original indicator. <3 <3 <3 <3 <3 <3 <3 <3 
"""


def Calculate(highestprices , lowestprices , closeprices , Clength , Alength):

 hlc3 = (highestprices + lowestprices + closeprices) / 3
 ema = pandas_ta.ema(hlc3, length=Clength);   
 diff_ema = pandas_ta.ema(numpy.abs(hlc3-ema), length=Clength);
 ci = (hlc3-ema) / (0.015 * diff_ema);
 tci = pandas_ta.ema(ci, length=Alength);

 wt1 = tci;
 wt2 = pandas_ta.sma(wt1 , 4)

 return wt1-wt2;      #it returns the difference between wt1 and wt2. 

 