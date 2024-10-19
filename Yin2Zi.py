from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi
import xerox as clip

def Y2Z(observations):
    hmmparams = DefaultHmmParams()
    ## 2个候选
    result = viterbi(hmm_params=hmmparams, observations=observations, path_num = 3)
    #for item in result:
    #    print(item.score, item.path)
    num=0
    for item in result:
        num=num+1
        tc=''
        for z in item.path:
            tc=tc+z
        print(tc)
        if(num==1):
            clip.copy(tc)