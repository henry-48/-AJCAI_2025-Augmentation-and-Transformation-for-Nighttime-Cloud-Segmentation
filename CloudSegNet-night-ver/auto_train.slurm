#!/bin/bash
#SBATCH --job-name=CloudSegNet # Job name
#SBATCH --mail-type=END,FAIL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=u6596617@anu.edu.au # Where to send mail
#SBATCH --ntasks=1 # Run on a single CPU
#SBATCH --mem=16G # Job memory request
#SBATCH --time=08:00:00 # Time limit hrs:min:sec
#SBATCH --partition=teaching
#SBATCH --gres=gpu:1
#SBATCH --output=CloudSegNet_%j.log # Standard output and error log


pwd; hostname; date
echo "--- training ---"

singularity exec --nv /opt/apps/containers/tensorflow_21.10-tf2-py3.sif python train_model.py
singularity exec --nv /opt/apps/containers/tensorflow_21.10-tf2-py3.sif python train_model_balanced.py
echo "--- done ---"
date
