#This a experiemntation of  simple AC controller that uses temperature error and rate of change of error to compute cooling power required .
#e----temperature error and g----rate of change of tempeature .These inputs are taken based on set(remote) and present(outside) temperature.
# here e is computed based on set temperature in remote and atomosheric temperature
def fuzzify_input(e,f):
    membership={'Normal':0,'Medium':0,'High':0,'Low':0} # membership functions
    #fuzzy membership for Normal
    if e==0 and f==0:
        membership['Normal']=1
    elif 0<e<2 and f==0:
        membership['Normal']=(2-e)/2
    elif 0>e>-2 and 0>f:
        membership['Normal']=(e+2)/2
    else:
        membership['Normal']=0
    #fuzzy membership for Medium
    if 2<e<=5 and f==0:
        membership['Medium']=1
    elif 0<e<5 and 0<f<=0.25:
        membership['Medium']=min(1,(5-e)/5)
    else:
        membership['Medium']=0
    #fuzzy membership for High
    if e>=5 and f>=0.25:
        membership['High']=1
    elif 2<e<5 and 0<f<=0.25:
        membership['High']=1-((5-e)/5)
    else:
        membership['High']=0
    #fuzzy membership for Low
    if e <= -3 and f <= -0.25:
        membership['Low'] = 1
    elif -2 < e < 0 and f < 0:
        membership['Low'] = max(0, 1 - ((e + 2) / 2))
    else:
        membership['Low'] = 0

    # Add combined fuzzy memberships
    if -1 < e < 2 and -0.2 < f < 0.2:
        membership['Normal'] = 0.5
        membership['Medium'] = 0.3
        membership['Low'] = 0.2
    return membership



def apply_rules(ac_membership):
    Low_p=24
    Normal_p=48
    Medium_p=72
    High_p=96
    #these represent the cooling power required bazed on the inputs 
    #now weighted average here based on centroid approach yield the single crisp output
    numerator=(ac_membership['Low']*Low_p +ac_membership['Normal']*Normal_p + ac_membership['Medium']*Medium_p + ac_membership['High']*High_p)
    denominator=(ac_membership['Low'] +ac_membership['Normal'] +ac_membership['Medium'] +ac_membership['High'])
    if denominator ==0 :
        return 0
    return numerator/denominator

e= 2.7# sample input
f=0.13
ac_membership=fuzzify_input(e,f)
cooling_power=apply_rules(ac_membership)
print(f"temperature error:{e}*C")
print(f"Rate of change in temperature error :{f}*C")
print(f"cooling_Power:{cooling_power:.2f}%")