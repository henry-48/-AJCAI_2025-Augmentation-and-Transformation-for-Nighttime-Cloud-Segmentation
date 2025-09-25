#!/bin/bash
#SBATCH --job-name=Unet # Job name
#SBATCH --mail-type=END,FAIL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=u6596617@anu.edu.au # Where to send mail
#SBATCH --ntasks=1 # Run on a single CPU
#SBATCH --mem=24G # Job memory request
#SBATCH --time=08:00:00 # Time limit hrs:min:sec
#SBATCH --partition=teaching
#SBATCH --gres=gpu:1
#SBATCH --constraint="nvidia535"
#SBATCH --output=Unet_%j.log # Standard output and error log


export WANDB_API_KEY="98a5f4a48b5ad8f4cb89bc86e6cc3c105fe05677"

pwd; hostname; date
echo "--- training ---"
wandb login --relogin
singularity exec --nv /opt/apps/containers/tensorflow_21.10-tf2-py3.sif python train.py --amp -l 0.0001 --bilinear --batch-size 16 -e 10 -c 1
echo "--- done ---"
date
