# AIRIS-TB: Population TB Screening on a Scale of 1M+ CXRs
---
This repository will host the codebase related to the study:

**"Population-scale Cross-sectional Observational Study for AI-powered TB Screening on One Million CXRs"** [(Link to Manuscript)](https://www.nature.com/articles/s41746-025-01832-7)

![AI Enabled Workflow](figs/airis_tb_workflow.png)

---

## Contents

This repository includes:
- Predictions on public datasets
- Performance metric scripts

The predictions on the 4 public datasets, [CheXpert test](https://github.com/rajpurkarlab/cheXpert-test-set-labels), [Chest-IU](https://openi.nlm.nih.gov/faq), [TB-11k](https://arxiv.org/abs/2307.02848) and [PadChest](https://bimcv.cipf.es/bimcv-projects/padchest/) obtained with our AIRIS-TB model can be found inside the folder `preds/`. The labels were binarized to normal/abnormal using the original labels for each dataset. In each CSV, the columns `preds`, `labels` contain th model's predictions and binarized labels respectively. 


To compute the metrics on each dataset:

Ensure you install the required packages:
```
pip install -r requirements.txt
```


The simply run:

```
sh run.sh
```

NOTE: The utils.py script contains all logic for computing performance metrics.

## Results

| Dataset      | AUROC  | FNR |
|--------------|--------|-----|
| Internal Test (~1M CXRs) | 98.51% |0.33%|
| CheXpert     | 85.03% |0.00%| 
| ChestIU      | 65.32% |0.00%| 
| PadChest     | 78.97% |3.03%|
| TB-11k       | 87.97% |0.50%|  

---

## Contact

For any questions feel free to reach out at prateekmunjal31@gmail.com  or pmunjal@m42.ae

---