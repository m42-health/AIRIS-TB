import argparse
import pandas as pd
from utils import *



def compute_metrics(preds, targets, threshold,verbose=True):
    auroc = compute_auroc(preds, targets)
    fnr = compute_fnr(preds, targets, threshold)
    if verbose:
        print(f"AUROC: {auroc*100:.2f}%")
        print(f"FNR: {fnr*100:.2f}%")
    return auroc, fnr

def main(args):
    THRESHOLD = args.threshold

    print(" ---- Computing metrics for CheXpert -----")
    df = pd.read_csv("preds/chexpert_preds.csv")
    chexpert_preds = df['preds']
    chexpert_targets = df['labels']
    _ = compute_metrics(chexpert_preds, chexpert_targets, THRESHOLD)

    print("\n ---- Computing metrics for PadChest -----")
    df = pd.read_csv("preds/padchest_preds.csv")
    padchest_preds = df['preds']
    padchest_targets = df['labels']
    _ = compute_metrics(padchest_preds, padchest_targets, THRESHOLD)
    
    print("\n---- Computing metrics for ChestIU-CXR -----")
    df = pd.read_csv("preds/chest-iu_preds.csv")
    chestiu_preds = df['preds']
    chestiu_targets = df['labels']
    _ = compute_metrics(chestiu_preds, chestiu_targets, THRESHOLD)

    print("\n---- Computing metrics for TB-11k -----")
    df = pd.read_csv("preds/tb11k_val_preds.csv")
    chestiu_preds = df['preds']
    chestiu_targets = df['labels']
    _ = compute_metrics(chestiu_preds, chestiu_targets, THRESHOLD)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Description of your script.")
    
    parser.add_argument(
        '-t', '--threshold',
        type=float,
        default=0.0202,
        help='Classification threshold'
    )
    args = parser.parse_args()    
    main(args)
