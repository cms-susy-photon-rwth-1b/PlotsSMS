
python python/makeSMSplots.py config/PhotonMET/GGM_PhotonMET.cfg GGM
python python/makeSMSplots.py config/PhotonMET/T5gg_PhotonMET.cfg T5gg
python python/makeSMSplots.py config/PhotonMET/T5Wg_PhotonMET.cfg T5Wg

./python/limit_post_proc.py
