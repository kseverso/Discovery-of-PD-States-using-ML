# Discovery-of-PD-States-using-ML
Code to supplement the analysis presented in 'Discovery of Parkinson's disease states using a machine learning approach'. If you are would like to use the exact model or cohort presented in the paper, please reach out to us directly.

## Data availability
The code in this repositiory leverages data made available via PPMI. For information about the dataset and to gain access, visit [ppmi-info.org](http://www.ppmi-info.org).

## Organization of the code
The analysis is organized as follows

### Data pre-processing
Several notebooks are used to pre-process the raw data from ppmi. `Motor_Data_Processing.ipynb`, `Non_Motor_Data_Processing.ipynb`, `Demographics_Data_Processing.ipynb` process those measures respectively. `Full_Data_Processing.ipynb` merges those sources and addresses date entry errors. `LEDD_Data_Processing.ipynb` processes the medication information using functionality provided in `calc_ledd.py`. `Train_Test_Split.ipynb` creates the train/test split used in analysis.

### Contrastive latent variable model
The processed data is used as input to a contrastive latent variable model as demonstrated in `Learn_and_Apply_cLVM.ipynb`. The code for the model can be found [here](https://github.com/kseverso/contrastive-LVM).

### Personalized input-output hidden Markov model
The latent representation is used as input to the personalized input-output hidden Markov model in `Learn_and_Apply_PIOHMM.ipynb`. The code for the model can be found [here](https://github.com/kseverso/DiseaseProgressionModeling-HMM) The latent representation data from the cLVM must first be processed into a format the progression model can use as demonstrated in `LD_Data_Processing.ipynb`

### Analysis of results
`Manuscript_Figures.ipynb` presents code the generates the primary figures of the manuscript.
