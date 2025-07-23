
from sklearn.metrics import (
    roc_curve,
    auc,
    confusion_matrix,
)

def compute_auroc(preds: list, targets: list) -> float:
    fpr, tpr, _ = roc_curve(targets, preds)
    return auc(fpr, tpr)   

def compute_fnr(preds:list, targets:list, threshold:float):
    cfm = confusion_matrix(targets, (preds >= threshold).astype('uint8') )
    tn, fp, fn, tp = cfm.ravel()
    fnr = fn / (fn + tp)    
    return fnr 

def compute_wlr(preds:list, targets:list, threshold: float, eps=1e-8):
    cfm = confusion_matrix(targets, (preds >= threshold).astype('uint8') )
    tn, fp, fn, tp = cfm.ravel()
    return (1 - ((tp + fp) / (tn + fp + fn + tp + eps))) * 100