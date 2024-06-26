from code_generation.quantity import Quantity
from code_generation.quantity import NanoAODQuantity

lumi = Quantity("lumi")
puweight = Quantity("puweight")
prefireweight = Quantity("prefiring_wgt")
lhe_scale_weight = Quantity("lhe_scale_weight")
base_taus_mask = Quantity("base_taus_mask")
good_taus_mask = Quantity("good_taus_mask")
base_muons_mask = Quantity("base_muons_mask")
good_muons_mask = Quantity("good_muons_mask")
veto_muons_mask = Quantity("veto_muons_mask")
veto_muons_mask_2 = Quantity("veto_muons_mask_2")
muon_veto_flag = Quantity("extramuon_veto")
base_electrons_mask = Quantity("base_electrons_mask")
good_electrons_mask = Quantity("good_electrons_mask")
veto_electrons_mask = Quantity("veto_electrons_mask")
veto_electrons_mask_2 = Quantity("veto_electrons_mask_2")
electron_veto_flag = Quantity("extraelec_veto")
jet_id_mask = Quantity("jet_id_mask")
jet_puid_mask = Quantity("jet_puid_mask")
jet_overlap_veto_mask = Quantity("jet_overlap_veto_mask")
good_jets_mask = Quantity("good_jets_mask")
good_bjets_mask = Quantity("good_bjets_mask")
Tau_pt_ele_corrected = Quantity("Tau_pt_ele_corrected")
Tau_pt_ele_mu_corrected = Quantity("Tau_pt_mu_corrected")
Tau_pt_corrected = Quantity("Tau_pt_corrected")
Tau_mass_corrected = Quantity("Tau_mass_corrected")
Jet_pt_corrected = Quantity("Jet_pt_corrected")
Jet_mass_corrected = Quantity("Jet_mass_corrected")
dileptonpair = Quantity("dileptonpair")
gen_dileptonpair = Quantity("gen_dileptonpair")
truegenpair = Quantity("truegenpair")
leptontriple = Quantity("leptontriple")
gen_leptontriple = Quantity("gen_leptontriple")
truegentriple = Quantity("truegentriple")
good_jet_collection = Quantity("good_jet_collection")
good_bjet_collection = Quantity("good_bjet_collection")

electron_is_nonisowp90_3 = Quantity("electron_is_nonisowp90_3")
muon_is_mediumid_3 = Quantity("muon_is_mediumid_3")
electron_is_nonisowp90_2 = Quantity("electron_is_nonisowp90_2")
muon_is_mediumid_2 = Quantity("muon_is_mediumid_2")
electron_is_nonisowp90_1 = Quantity("electron_is_nonisowp90_1")
muon_is_mediumid_1 = Quantity("muon_is_mediumid_1")
muon_is_tracker_3 = Quantity("muon_is_tracker_3")

pt_1_uncorrected = Quantity("pt_1_uncorrected")
pt_2_uncorrected = Quantity("pt_2_uncorrected")
pt_3_uncorrected = Quantity("pt_3_uncorrected")

nelectrons = Quantity("nelectrons")
nmuons = Quantity("nmuons")
ntaus = Quantity("ntaus")
p4_1 = Quantity("p4_1")
p4_1_uncorrected = Quantity("p4_1_uncorrected")
pt_1 = Quantity("pt_1")
eta_1 = Quantity("eta_1")
phi_1 = Quantity("phi_1")
p4_2 = Quantity("p4_2")
p4_2_uncorrected = Quantity("p4_2_uncorrected")
pt_2 = Quantity("pt_2")
eta_2 = Quantity("eta_2")
phi_2 = Quantity("phi_2")
p4_3 = Quantity("p4_3")
p4_3_uncorrected = Quantity("p4_3_uncorrected")
pt_3 = Quantity("pt_3")
eta_3 = Quantity("eta_3")
phi_3 = Quantity("phi_3")
mass_1 = Quantity("mass_1")
mass_2 = Quantity("mass_2")
mass_3 = Quantity("mass_3")
dxy_1 = Quantity("dxy_1")
dxy_2 = Quantity("dxy_2")
dxy_3 = Quantity("dxy_3")
dz_1 = Quantity("dz_1")
dz_2 = Quantity("dz_2")
dz_3 = Quantity("dz_3")
q_1 = Quantity("q_1")
q_2 = Quantity("q_2")
q_3 = Quantity("q_3")
iso_1 = Quantity("iso_1")
iso_2 = Quantity("iso_2")
iso_3 = Quantity("iso_3")
is_global_1 = Quantity("is_global_1")
is_global_2 = Quantity("is_global_2")
is_global_3 = Quantity("is_global_3")
decaymode_1 = Quantity("decaymode_1")
decaymode_2 = Quantity("decaymode_2")
decaymode_3 = Quantity("decaymode_3")
gen_match_1 = Quantity("gen_match_1")
gen_match_2 = Quantity("gen_match_2")
gen_match_3 = Quantity("gen_match_3")
tau_gen_match_1 = Quantity("tau_gen_match_1")
tau_gen_match_2 = Quantity("tau_gen_match_2")
tau_gen_match_3 = Quantity("tau_gen_match_3")
gen_tau_pt_1 = Quantity("gen_tau_pt_1")
gen_tau_pt_2 = Quantity("gen_tau_pt_2")
gen_tau_pt_3 = Quantity("gen_tau_pt_3")
gen_tau_eta_1 = Quantity("gen_tau_eta_1")
gen_tau_eta_2 = Quantity("gen_tau_eta_2")
gen_tau_eta_3 = Quantity("gen_tau_eta_3")
gen_tau_phi_1 = Quantity("gen_tau_phi_1")
gen_tau_phi_2 = Quantity("gen_tau_phi_2")
gen_tau_phi_3 = Quantity("gen_tau_phi_3")
taujet_pt_1 = Quantity("taujet_pt_1")
taujet_pt_2 = Quantity("taujet_pt_2")
taujet_pt_3 = Quantity("taujet_pt_3")
gen_taujet_pt_1 = Quantity("gen_taujet_pt_1")
gen_taujet_pt_2 = Quantity("gen_taujet_pt_2")
gen_taujet_pt_3 = Quantity("gen_taujet_pt_3")

# Combined event quantities
p4_123met = Quantity("p4_123met")
p4_23 = Quantity("p4_23")
p4_H = Quantity("p4_H")
deltaPhi_12 = Quantity("deltaPhi_12")
deltaPhi_13 = Quantity("deltaPhi_13")
deltaPhi_WH = Quantity("deltaPhi_WH")
Lt = Quantity("Lt")
m_vis = Quantity("m_vis")
p4_23_miss = Quantity("p4_23_miss")
m_tt = Quantity("m_tt")
pt_W = Quantity("pt_W")
m_tt = Quantity("m_tt")
pt_W = Quantity("pt_W")
pt_123met = Quantity("pt_123met")
pt_vis = Quantity("pt_vis")
eta_vis = Quantity("eta_vis")
phi_vis = Quantity("phi_vis")
pzetamissvis = Quantity("pzetamissvis")
mTdileptonMET = Quantity("mTdileptonMET")
mt_1 = Quantity("mt_1")
mt_2 = Quantity("mt_2")
mt_3 = Quantity("mt_3")
pt_tt = Quantity("pt_tt")
pt_ttjj = Quantity("pt_ttjj")
mt_tot = Quantity("mt_tot")
deltaR_ditaupair = Quantity("deltaR_ditaupair")
deltaR = Quantity("deltaR")
deltaR_13 = Quantity("deltaR_13")
deltaR_23 = Quantity("deltaR_23")
deltaR_12 = Quantity("deltaR_12")
njets = Quantity("njets")
nbtag = Quantity("nbtag")
jet_p4_1 = Quantity("jet_p4_1")
jpt_1 = Quantity("jpt_1")
jeta_1 = Quantity("jeta_1")
jphi_1 = Quantity("jphi_1")
jtag_value_1 = Quantity("jtag_value_1")
jet_p4_2 = Quantity("jet_p4_2")
jpt_2 = Quantity("jpt_2")
jeta_2 = Quantity("jeta_2")
jphi_2 = Quantity("jphi_2")
jtag_value_2 = Quantity("jtag_value_2")
mjj = Quantity("mjj")
bjet_p4_1 = Quantity("bjet_p4_1")
bpt_1 = Quantity("bpt_1")
beta_1 = Quantity("beta_1")
bphi_1 = Quantity("bphi_1")
btag_value_1 = Quantity("btag_value_1")
bjet_p4_2 = Quantity("bjet_p4_2")
bpt_2 = Quantity("bpt_2")
beta_2 = Quantity("beta_2")
bphi_2 = Quantity("bphi_2")
btag_value_2 = Quantity("btag_value_2")

dielectron_veto = Quantity("dielectron_veto")
dimuon_veto = Quantity("dimuon_veto")
dilepton_veto = Quantity("dilepton_veto")

## Gen Quantities
gen_p4_1 = Quantity("gen_p4_1")
gen_pt_1 = Quantity("gen_pt_1")
gen_eta_1 = Quantity("gen_eta_1")
gen_phi_1 = Quantity("gen_phi_1")
gen_mass_1 = Quantity("gen_mass_1")
gen_pdgid_1 = Quantity("gen_pdgid_1")

gen_p4_2 = Quantity("gen_p4_2")
gen_pt_2 = Quantity("gen_pt_2")
gen_eta_2 = Quantity("gen_eta_2")
gen_phi_2 = Quantity("gen_phi_2")
gen_mass_2 = Quantity("gen_mass_2")
gen_pdgid_2 = Quantity("gen_pdgid_2")

gen_p4_3 = Quantity("gen_p4_3")
gen_pt_3 = Quantity("gen_pt_3")
gen_eta_3 = Quantity("gen_eta_3")
gen_phi_3 = Quantity("gen_phi_3")
gen_mass_3 = Quantity("gen_mass_3")
gen_pdgid_3 = Quantity("gen_pdgid_3")

gen_m_vis = Quantity("gen_m_vis")

hadronic_gen_taus = Quantity("hadronic_gen_taus")

topPtReweightWeight = Quantity("topPtReweightWeight")
ZPtMassReweightWeight = Quantity("ZPtMassReweightWeight")

## HTXS quantities
ggh_NNLO_weight = Quantity("ggh_NNLO_weight")
THU_ggH_Mu = Quantity("THU_ggH_Mu")
THU_ggH_Res = Quantity("THU_ggH_Res")
THU_ggH_Mig01 = Quantity("THU_ggH_Mig01")
THU_ggH_Mig12 = Quantity("THU_ggH_Mig12")
THU_ggH_VBF2j = Quantity("THU_ggH_VBF2j")
THU_ggH_VBF3j = Quantity("THU_ggH_VBF3j")
THU_ggH_PT60 = Quantity("THU_ggH_PT60")
THU_ggH_PT120 = Quantity("THU_ggH_PT120")
THU_ggH_qmtop = Quantity("THU_ggH_qmtop")
THU_qqH_TOT = Quantity("THU_qqH_TOT")
THU_qqH_PTH200 = Quantity("THU_qqH_PTH200")
THU_qqH_Mjj60 = Quantity("THU_qqH_Mjj60")
THU_qqH_Mjj120 = Quantity("THU_qqH_Mjj120")
THU_qqH_Mjj350 = Quantity("THU_qqH_Mjj350")
THU_qqH_Mjj700 = Quantity("THU_qqH_Mjj700")
THU_qqH_Mjj1000 = Quantity("THU_qqH_Mjj1000")
THU_qqH_Mjj1500 = Quantity("THU_qqH_Mjj1500")
THU_qqH_25 = Quantity("THU_qqH_25")
THU_qqH_JET01 = Quantity("THU_qqH_JET01")

## MET quantities
met_p4 = Quantity("met_p4")
recoil_genboson_p4_vec = Quantity("recoil_genboson_p4_vec")
genbosonmass = Quantity("genbosonmass")
npartons = Quantity("npartons")
met_p4_leptoncorrected = Quantity("met_p4_leptoncorrected")
met_p4_jetcorrected = Quantity("met_p4_jetcorrected")
met_p4_recoilcorrected = Quantity("met_p4_recoilcorrected")
met = Quantity("met")
metphi = Quantity("metphi")
metSumEt = Quantity("metSumEt")
metcov00 = Quantity("metcov00")
metcov01 = Quantity("metcov01")
metcov10 = Quantity("metcov10")
metcov11 = Quantity("metcov11")
met_uncorrected = Quantity("met_uncorrected")
metphi_uncorrected = Quantity("metphi_uncorrected")

## PFMET quantities
pfmet = Quantity("pfmet")
pfmet_p4 = Quantity("pfmet_p4")
pfmetphi = Quantity("pfmetphi")
pfmet_uncorrected = Quantity("pfmet_uncorrected")
pfmetphi_uncorrected = Quantity("pfmetphi_uncorrected")
pfmet_p4_leptoncorrected = Quantity("pfmet_p4_leptoncorrected")
pfmet_p4_jetcorrected = Quantity("pfmet_p4_jetcorrected")
pfmet_p4_recoilcorrected = Quantity("pfmet_p4_recoilcorrected")

## embedding quantities
emb_genweight = Quantity("emb_genweight")
emb_initialMETEt = Quantity("emb_initialMETEt")
emb_initialMETphi = Quantity("emb_initialMETphi")
emb_initialPuppiMETEt = Quantity("emb_initialPuppiMETEt")
emb_initialPuppiMETphi = Quantity("emb_initialPuppiMETphi")
emb_isMediumLeadingMuon = Quantity("emb_isMediumLeadingMuon")
emb_isMediumTrailingMuon = Quantity("emb_isMediumTrailingMuon")
emb_isTightLeadingMuon = Quantity("emb_isTightLeadingMuon")
emb_isTightTrailingMuon = Quantity("emb_isTightTrailingMuon")
emb_InitialPairCandidates = Quantity("emb_InitialPairCandidates")
emb_SelectionOldMass = Quantity("emb_SelectionOldMass")
emb_SelectionNewMass = Quantity("emb_SelectionNewMass")
emb_triggersel_wgt = Quantity("emb_triggersel_wgt")
emb_idsel_wgt_1 = Quantity("emb_idsel_wgt_1")
emb_idsel_wgt_2 = Quantity("emb_idsel_wgt_2")


# sample flags
is_data = Quantity("is_data")
is_embedding = Quantity("is_embedding")
is_ttbar = Quantity("is_ttbar")
is_dyjets = Quantity("is_dyjets")
is_wjets = Quantity("is_wjets")
is_ggh_htautau = Quantity("is_ggh_htautau")
is_vbf_htautau = Quantity("is_vbf_htautau")
is_diboson = Quantity("is_diboson")
is_whtautau = Quantity("is_whtautau")
is_rem_ttbar = Quantity("rem_ttbar")
is_triboson = Quantity("triboson")
is_rem_VH = Quantity("rem_VH")
is_ggZZ = Quantity("ggZZ")

# Electron Weights
id_wgt_ele_wp90nonIso_1 = Quantity("id_wgt_ele_wp90nonIso_1")
id_wgt_ele_wp90nonIso_2 = Quantity("id_wgt_ele_wp90nonIso_2")
id_wgt_ele_wp90nonIso_3 = Quantity("id_wgt_ele_wp90nonIso_3")
id_wgt_ele_wp80nonIso_1 = Quantity("id_wgt_ele_wp80nonIso_1")
id_wgt_ele_wp80nonIso_2 = Quantity("id_wgt_ele_wp80nonIso_2")
id_wgt_ele_wp80nonIso_3 = Quantity("id_wgt_ele_wp80nonIso_3")
iso_wgt_ele_1 = Quantity("iso_wgt_ele_1")
iso_wgt_ele_2 = Quantity("iso_wgt_ele_2")
iso_wgt_ele_3 = Quantity("iso_wgt_ele_3")
# Muon weights
id_wgt_mu_1 = Quantity("id_wgt_mu_1")
id_wgt_mu_2 = Quantity("id_wgt_mu_2")
id_wgt_mu_3 = Quantity("id_wgt_mu_3")
iso_wgt_mu_1 = Quantity("iso_wgt_mu_1")
iso_wgt_mu_2 = Quantity("iso_wgt_mu_2")
iso_wgt_mu_3 = Quantity("iso_wgt_mu_3")
# btag weight
btag_weight = Quantity("btag_weight")
era_2016preVFP = Quantity("era_2016preVFP")
era_2016postVFP = Quantity("era_2016postVFP")
era_2017 = Quantity("era_2017")
era_2018 = Quantity("era_2018")
# ML variables
transformed_pt_1 = Quantity("transformed_pt_1")
transformed_pt_2 = Quantity("transformed_pt_2")
transformed_pt_3 = Quantity("transformed_pt_3")
transformed_eta_1 = Quantity("transformed_eta_1")
transformed_eta_2 = Quantity("transformed_eta_2")
transformed_eta_3 = Quantity("transformed_eta_3")
transformed_eta_1 = Quantity("transformed_eta_1")
transformed_eta_2 = Quantity("transformed_eta_2")
transformed_eta_3 = Quantity("transformed_eta_3")
transformed_phi_1 = Quantity("transformed_phi_1")
transformed_phi_2 = Quantity("transformed_phi_2")
transformed_phi_3 = Quantity("transformed_phi_3")
transformed_deltaR_12 = Quantity("transformed_deltaR_12")
transformed_deltaR_13 = Quantity("transformed_deltaR_13")
transformed_deltaR_23 = Quantity("transformed_deltaR_23")
transformed_m_vis = Quantity("transformed_m_vis")
transformed_met = Quantity("transformed_met")
transformed_Lt = Quantity("transformed_Lt")
transformed_decaymode_3 = Quantity("transformed_decaymode_3")
transformed_era_2016preVFP = Quantity("transformed_era_2016preVFP")
transformed_era_2016postVFP = Quantity("transformed_era_2016postVFP")
transformed_era_2017 = Quantity("transformed_era_2017")
transformed_era_2018 = Quantity("transformed_era_2018")
transformed_met = Quantity("transformed_met")
transformed_m_tt = Quantity("transformed_m_tt")
transformed_mt_1 = Quantity("transformed_mt_1")
transformed_mt_2 = Quantity("transformed_mt_2")
transformed_mt_3 = Quantity("transformed_mt_3")
transformed_pt_vis = Quantity("transformed_pt_vis")
transformed_pt_W = Quantity("transformed_pt_W")
transformed_metphi = Quantity("transformed_metphi")
transformed_mjj = Quantity("transformed_mjj")
transformed_pt_123met = Quantity("transformed_pt_123met")
output_vector = Quantity("output_vector")
predicted_class = Quantity("predicted_class")
predicted_max_value = Quantity("predicted_max_value")
