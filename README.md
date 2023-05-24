# Context

Small-scale fisheries (SSFs) receive increasing international attention for landing around 50% of global marine fisheries 
catches and employing millions of people throughout the globe. Their contribution to food security and poverty alleviation, 
especially in developing countries, makes it relevant to consider them when discussing Sustainable Development Goals (SDGs). 
Achieving sustainable SSFs means understanding them in their broader context, from the health of marine ecosystems to 
employment, public health, equity, and climate change impacts. These relationships are complex and poorly understood, 
thus challenging the identification of policies that could improve the contribution of SSFs to sustainable development. 
Here we developed an expert-based rapid appraisal framework to identify and characterize the relationships between SSFs 
and the SDGs. Based on existing knowledge and expert judgment, the framework serves as a diagnostic tool for identifying 
strengths and gaps in the contribution of SSFs to achieving the SDGs. As a proof of concept, we illustrate the approach 
and its potential contributions through a pilot assessment in Madagascar, highlighting lessons and a global framework application.

These resources allow users to apply to other case studies the method developed in the paper _Bitoun et al., (2023) 
A framework for capturing small-scale fisheries' contribution to the sustainable development goals (SDGs)_.


## The SSF-SDG Framework

A rapid appraisal framework was developed to identify and assess the potential contribution of SSFs to achieving 32 relevant SDG targets.
Here users will find:
- an xls form to import to survey form in Kobo toolbox, a free, open-source form builder developed by the Harvard Humanitarian Initiative. The tool allows for collecting data in the field using mobile devices and can be used offline, facilitating data collection in remote areas.

- a python file to pre-process the data issued with the form.

## How to use these documents

### Import the form in Kobo Toolbox
- Create a Kobo account: https://kf.kobotoolbox.org/accounts/login/
- Create a new project and select "import an XLSForm"
- Import the file aGCYWCGwJLs3bxKnEFseP9.xlsx

Then you can use the form to collect the data. If the country concerned is different than the ones proposed in the list, 
you may edit the form builder to add the appropriate countries. This operation will not compromise the pre-processing code. 
However, any other changes to the structure will make the code obsolete. 

### Generate your results
After completion of the form, you may extract your results from KoboToolbox in an excel sheet and use the python code file 
to process your results.

- Import the python file "SSF-SDG_form_preprocessing.py"
- Provide the adress of the excel file and the name of the sheet

`df = pd.read_excel(r'filedirection.xlsx', sheet_name='sheet name')`

- Run the script

Results will be exported into a new excel sheets as follows:

`with pd.ExcelWriter('scores.xlsx') as writer:`

where **scores.xlsx** is the name of the file.

`df.to_excel(writer, sheet_name='curated_forms', index=True)`

where **curated_forms** is a sheet where unneccesary colums generated with Kobo are dropped.

`invalid_form.to_excel(writer, sheet_name='invalid_form_nan_sup8', index=True)
    scores.to_excel(writer, sheet_name='valid_forms', index=True)` 

where **valid_forms** are those containing enough information to be used (not exceeding a 7 no data/not applicable threshold, see associated paper).

`target_col.to_excel(writer, sheet_name='targets', index=True)` 

where **targets** is a sheet containing scores on each SDG target.

    sdg_strong_col.to_excel(writer, sheet_name='strong_SDG', index=True)
    sdg_weak_col.to_excel(writer, sheet_name='weak_SDG', index=True)

where **strong_SDG** and **weak_SDG** are two sheets containing the lower and upper bound of the performance interval on each SDG.