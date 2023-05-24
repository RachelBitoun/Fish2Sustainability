import pandas as pd

# Load exported from Kobotoolbox as an xlsx - add file direction and sheet name
df = pd.read_excel(r'filedirection.xlsx',
                     sheet_name='sheet name')

# Drop odd columns generated automatically by kobo that include Bool and NaN values.
falses = (df == False) & (df.astype(str) != '0')
trues = (df == True) & (df.astype(str) != '0')
nans = (df.isna()) & (df.applymap(type) != type(None))
bool_nans_head = falses | nans | trues # The vertical bar corresponds to 'AND'
df = df.drop(bool_nans_head.all()[bool_nans_head.all()].index.to_list(), axis=1) # Drop these columns and header columns
df = df.drop(df.columns[df.columns.str.contains("_head")], axis=1)

# rename columns and define type with first letter: s for score, d for descriptors (stats),
# t for text (to process later), j for justification. To get column names use fct list(df)
df.rename(index=str, columns={"ssf_characteristic/Name": "d_SSF_name",
                                "ssf_characteristic/country": "d_country",
                                "ssf_characteristic/Region": "t_region",
                                "ssf_characteristic/participants": "d_participants",
                                "ssf_characteristic/typecatch": "d_SSF_type",
                                "ssf_characteristic/n_fisher": "d_n_fisher",
                                "ssf_characteristic/geographical_scale": "d_scale",
                                "ssf_characteristic/harvest_area": "d_harvest_area",
                                "ssf_characteristic/ecosystem": "t_ecosystem",
                                "ssf_characteristic/ecosystem_other": "t_ecosystem_other",
                                "ssf_characteristic/specie": "t_species",
                                "ssf_characteristic/gear_type": "t_gear_type",
                                "ssf_characteristic/dscrpt_fishing_practice": "j_fishing_practice",
                                "ssf_characteristic/govern_mode": "d_govern_mode",
                                "ssf_characteristic/rule": "d_rule",
                                "ssf_characteristic/dscrpt_govern": "j_govern",
                                "ssf_characteristic/dscrpt_event": "j_events",
                                "ssf_characteristic/group_threat/threat1": "d_threat1",
                                "ssf_characteristic/group_threat/threat2": "d_threat2",
                                "ssf_characteristic/group_threat/threat3": "d_threat3",
                                "ssf_characteristic/dscrpt_stewardship": "d_stewardship",
                                "ssf_characteristic/dscrpt_steward_other": "d_steward_other",
                                "scores/group_env_cond/ecosystem_health": "s_ecosystem_health",
                                "scores/group_env_cond/ecosystem_health_j": "j_ecosystem_health",
                                "scores/group_env_cond/fish_stock_health": "s_stock_health",
                                "scores/group_env_cond/fish_stock_health_j": "j_stock_health",
                                "scores/group_practice/stewardship": "s_stewardship",
                                "scores/group_practice/stewardship_j": "j_stewardship",
                                "scores/group_practice/mngmnt_effect": "s_mngmnt_effect",
                                "scores/group_practice/mngemt_effect_j": "j_mngmnt_effect",
                                "scores/group_practice/compliance/compliance_formal": "s_comp_formal",
                                "scores/group_practice/compliance/compliance_informal": "s_comp_informal",
                                "scores/group_practice/compliance_j": "j_comp",
                                "scores/group_practice/fishing_effort": "s_fish_effort",
                                "scores/group_practice/fishing_effort_j": "j_fish_effort",
                                "scores/group_practice/compliance_001/gear_ecosystem": "s_gear_ecosystem",
                                "scores/group_practice/compliance_001/gear_bycatch": "s_gear_bycatch",
                                "scores/group_practice/compliance_001/gear_debris": "s_gear_debris",
                                "scores/group_practice/gear_j": "j_gear",
                                "scores/group_practice/innovation_tech": "s_innovation",
                                "scores/group_practice/innovation_tech_j": "j_innovation",
                                "scores/group_access/involve/involve_women": "s_inv_women",
                                "scores/group_access/involve/involve_men": "s_inv_men",
                                "scores/group_access/involve_j": "j_inv",
                                "scores/group_access/involve_children": "s_inv_child",
                                "scores/group_access/involve_child_j": "j_inv_child",
                                "scores/group_access/involve_001/access_resource_women": "s_res_women",
                                "scores/group_access/involve_001/access_resource_men": "s_res_men",
                                "scores/group_access/access_resources_j": "j_res",
                                "scores/group_access/access_market": "s_market",
                                "scores/group_access/access_market_j": "j_market",
                                "scores/group_food/food_depend": "s_food_depend",
                                "scores/group_food/food_depend_j": "j_food_depend",
                                "scores/group_food/food_security": "s_food_security",
                                "scores/group_food/food_security_j": "j_food_security",
                                "scores/group_food/food_waste/food_waste_share": "s_waste_share",
                                "scores/group_food/food_waste/food_waste_growth": "s_waste_growth",
                                "scores/group_food/food_waste_j": "j_waste",
                                "scores/group_food/fuel": "s_fuel",
                                "scores/group_food/fuel_j": "j_fuel",
                                "scores/group_income/income_share_fish": "s_inc_fish",
                                "scores/group_income/income_local": "s_inc_local",
                                "scores/group_income/income_internation_pov": "s_inc_international",
                                "scores/group_income/income_growth": "s_inc_growth",
                                "scores/group_income/income_j": "j_income",
                                "scores/group_wellbeing/well_being_house": "s_house",
                                "scores/group_wellbeing/well_being_house_j": "j_house",
                                "scores/group_wellbeing/well_being_epidemics": "s_epidemics",
                                "scores/group_wellbeing/well_being_health": "s_health",
                                "scores/group_wellbeing/well_being_health_j": "j_health",
                                "scores/group_wellbeing/well_being_cohesion": "d_cohesion",
                                "scores/group_wellbeing/well_being_cohesion_j": "j_cohesion",
                                "scores/group_wellbeing/participation/participation_women": "s_particip_women",
                                "scores/group_wellbeing/participation/participation_men": "s_particip_men",
                                "scores/group_wellbeing/participation_j": "j_particip",
                                "scores/group_wellbeing/well_being_education": "s_educ",
                                "scores/group_wellbeing/well_being_education_j": "j_educ",
                                "scores/group_wellbeing/fisher_mobility": "s_mobility",
                                "scores/group_wellbeing/fisher_mobility_j": "j_mobility",
                                "scores/group_wellbeing/work_condition/work_condition_women": "s_work_cond_women",
                                "scores/group_wellbeing/work_condition/work_condition_men": "s_work_cond_men",
                                "scores/group_wellbeing/work_condition_j": "j_work_cond",
                                "scores/group_wellbeing/cult_h": "s_cult_h",
                                "scores/group_wellbeing/cult_h_j": "j_cult_h",
                                "scores/group_economy/economic_growth": "s_econ_growth",
                                "scores/group_economy/economic_growth_j": "j_econ_growth",
                                "scores/group_economy/tourism": "s_tourism",
                                "scores/group_economy/tourism_j": "j_tourism",
                                "scores/group_economy/cooperation": "s_coop",
                                "scores/group_economy/cooperation_j": "j_coop",
                                "scores/group_global/subsidies": "s_subsidies",
                                "scores/group_global/global_resource": "s_global_resource",
                                "scores/group_global/global_export/export_share": "s_export_share",
                                "scores/group_global/global_export/export_growth": "s_export_growth",
                                "scores/group_global/global_j": "j_global"
                                }, inplace=True)

# extract scores
scores = df.loc[:, df.columns.str.startswith('s_')].copy()
for column in scores:
    scores[column].replace('NA', None, inplace=True)
    scores[column].replace('ND', None, inplace=True)
    scores[column] = scores[column].astype('float64')

#Test if nan>8
scores["count_none"] = scores.isna().sum(axis = 1)
scores["validity"] = scores["count_none"] <= 8
invalid_form = scores[scores['count_none'] > 8]
scores = scores[scores['count_none'] <= 8]

# Function to determine whether you can calculate to mean or skip calculation based on NA.sum
def cond_na(var_list):
    test = scores.loc[:, var_list].where((len(var_list) - scores.loc[:, var_list].isna().sum(axis=1)) >= 2)
    return test.loc[:, var_list].mean(axis=1)

def min_na(var_list):
    test2 = scores.loc[:, var_list].where((len(var_list) - scores.loc[:, var_list].isna().sum(axis=1)) >= 2)
    return test2.loc[:, var_list].min(axis=1)

# Target indicators calculations
scores['T.1.1'] = cond_na(['s_inc_fish', 's_inc_international'])
scores['T.1.2'] = cond_na(['s_inc_local',  's_food_security', 's_house', 's_health',  's_educ'])
scores['T.1.4'] = cond_na(['s_res_women', 's_res_men'])
scores['T.2.1'] = scores['s_food_security']
scores['T.2.3'] = cond_na(['s_inc_fish', 's_inc_growth', 's_food_depend', 's_export_share'])
scores['T.3.3'] = scores['s_epidemics']
scores['T.3.4'] = cond_na(['s_health', 's_food_depend'])
scores['T.5.5'] = cond_na(['s_particip_women', 's_inv_women'])
scores['T.5.A'] = cond_na(['s_res_women', 's_inv_women'])
scores['T.8.2'] = cond_na([ 's_econ_growth', 's_inv_women', 's_inv_men', 's_innovation'])
scores['T.8.4'] = cond_na(['s_fish_effort', 's_gear_bycatch', 's_gear_debris', 's_econ_growth'])
scores['T.8.5'] = cond_na(['s_inc_local', 's_inv_women', 's_inv_men', 's_inc_fish'])
scores['T.8.7'] = scores['s_inv_child']
scores['T.8.8'] = cond_na([ 's_work_cond_women', 's_work_cond_men'])
scores['T.8.9'] = scores['s_tourism']
scores['T.9.4'] = cond_na(['s_fuel', 's_econ_growth'])
scores['T.10.1'] = cond_na(['s_inc_international', 's_inc_growth'])
scores['T.11.1'] = scores['s_house']
scores['T.11.4'] = cond_na(['s_stewardship','s_cult_h'])
scores['T.12.2'] = cond_na(['s_fish_effort', 's_gear_bycatch', 's_gear_debris', 's_econ_growth'])
scores['T.12.3'] = cond_na(['s_waste_share', 's_waste_growth'])
scores['T.12.C'] = cond_na(['s_fuel', 's_subsidies'])
scores['T.14.1'] = cond_na(['s_gear_debris', 's_ecosystem_health'])
scores['T.14.2'] = cond_na([ 's_mngmnt_effect', 's_stewardship', 's_fish_effort', 's_gear_ecosystem', 's_gear_bycatch',
                                   's_res_women', 's_res_men', 's_particip_women', 's_particip_men', 's_mobility'])
scores['T.14.4'] = cond_na(['s_stock_health', 's_fish_effort', 's_gear_bycatch'])
scores['T.14.5'] = cond_na(['s_stewardship', 's_comp_formal', 's_comp_informal', 's_mngmnt_effect'])
scores['T.14.6'] = cond_na([ 's_comp_formal', 's_comp_informal', 's_subsidies'])
scores['T.14.7'] = cond_na(['s_stock_health', 's_fish_effort', 's_gear_bycatch', 's_econ_growth'])
scores['T.14.B'] = cond_na(['s_res_women', 's_res_men', 's_market', 's_mngmnt_effect', 's_work_cond_women',
                                  's_work_cond_men', 's_particip_women', 's_particip_men'])
scores['T.16.7'] = cond_na(['s_coop', 's_particip_women', 's_particip_men'])
scores['T.17.3'] = scores['s_global_resource']
scores['T.17.11'] = cond_na([ 's_export_growth', 's_export_share'])


# SDG weak-strong calculation
scores['sdg1_weak'] = cond_na(['T.1.1', 'T.1.2', 'T.1.4'])
scores['sdg1_strong'] = min_na(['T.1.1', 'T.1.2', 'T.1.4'])

scores['sdg2_weak'] = cond_na(['T.2.1', 'T.2.3'])
scores['sdg2_strong'] = min_na(['T.2.1', 'T.2.3'])

scores['sdg3_weak'] = cond_na(['T.3.3', 'T.3.4'])
scores['sdg3_strong'] = min_na(['T.3.3', 'T.3.4'])

scores['sdg5_weak'] = cond_na(['T.5.5', 'T.5.A'])
scores['sdg5_strong'] = min_na(['T.5.5', 'T.5.A'])

scores['sdg8_weak'] = cond_na(['T.8.2', 'T.8.4', 'T.8.5', 'T.8.7', 'T.8.8', 'T.8.9'])
scores['sdg8_strong'] = min_na(['T.8.2', 'T.8.4', 'T.8.5', 'T.8.7', 'T.8.8', 'T.8.9'])

scores['sdg9_weak'] = scores['T.9.4']
scores['sdg9_strong'] = scores['T.9.4']

scores['sdg10_weak'] = scores['T.10.1']
scores['sdg10_strong'] = scores['T.10.1']

scores['sdg11_weak'] = cond_na(['T.11.1', 'T.11.4'])
scores['sdg11_strong'] = min_na(['T.11.1', 'T.11.4'])

scores['sdg12_weak'] = cond_na(['T.12.2', 'T.12.3', 'T.12.C'])
scores['sdg12_strong'] = min_na(['T.12.2', 'T.12.3', 'T.12.C'])

scores['sdg14_weak'] = cond_na(['T.14.1', 'T.14.2', 'T.14.4', 'T.14.5', 'T.14.6', 'T.14.7', 'T.14.B'])
scores['sdg14_strong'] = min_na(['T.14.1', 'T.14.2', 'T.14.4', 'T.14.5', 'T.14.6', 'T.14.7', 'T.14.B'])
scores['sdg16_weak'] = scores['T.16.7']
scores['sdg16_strong'] = scores['T.16.7']

scores['sdg17_weak'] = cond_na(['T.17.3', 'T.17.11'])
scores['sdg17_strong'] = min_na(['T.17.3', 'T.17.11'])

#Calculate global sustainability index
scores['global_index_weak_sdg'] = cond_na(['sdg1_weak', 'sdg2_weak', 'sdg3_weak', 'sdg5_weak', 'sdg8_weak', 'sdg9_weak', 'sdg11_weak',
                                       'sdg12_weak', 'sdg14_weak', 'sdg16_weak', 'sdg17_weak'])
scores['global_index_strong_sdg'] = cond_na(['sdg1_strong', 'sdg2_strong', 'sdg3_strong','sdg5_strong', 'sdg8_strong', 'sdg9_strong',
                                       'sdg11_strong', 'sdg12_strong', 'sdg14_strong', 'sdg16_strong', 'sdg17_strong'])

# Save to Excel
target_col = scores.filter(regex='T.')
sdg_strong_col = scores.filter(regex='_strong')
sdg_weak_col = scores.filter(regex='_weak')

with pd.ExcelWriter('scores.xlsx') as writer:
    df.to_excel(writer, sheet_name='curated_forms', index=True)
    invalid_form.to_excel(writer, sheet_name='invalid_form_nan_sup8', index=True)
    scores.to_excel(writer, sheet_name='valid_forms', index=True)
    target_col.to_excel(writer, sheet_name='targets', index=True)
    sdg_strong_col.to_excel(writer, sheet_name='strong_SDG', index=True)
    sdg_weak_col.to_excel(writer, sheet_name='weak_SDG', index=True)


