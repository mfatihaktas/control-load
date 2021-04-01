from rvs import *
from math_utils import *
from debug_utils import *

def EW_MG1(ar, X):
	EX = X.moment(1)
	ro = ar*EX
	if ro >= 1:
		log(WARNING, "ro= {} > 1, returning None".format(ro))
		return None

	EX2 = X.moment(2)
	return ar*EX2/2/(1 - ar*EX)

def EW_MG1_fromRoAndCVX(ro, CVX):
	# CVX = CoeffVar(X)
	return ro/(1 - ro) * (CVX**2 + 1)/2

# s: Link forwarding speed
# S: Job size
def ET_netLink(ar, s, S):
	ES = S.moment(1)
	EV = ES/s
	ro = ar*EV
	if ro >= 1:
		log(WARNING, "ro= {} > 1, returning None".format(ro))
		return None

	ES2 = S.moment(2)
	EV2 = ES2/s**2
	return ar*EV2/2/(1 - ar*EV)

def ET_compressQ(ar, S, compress_level, compress_time):
	ES = S.moment(1)
	EV, abserr = scipy.integrate.quad(lambda s: S.pdf(s) * compress_time(s, compress_level), S.l, S.u)
	ro = ar*EV
	if ro >= 1:
		log(WARNING, "ro= {} > 1, returning None".format(ro))
		return None

	ES2 = S.moment(2)
	EV2 = ES2/s**2
	return ar*EV2/2/(1 - ar*EV)
