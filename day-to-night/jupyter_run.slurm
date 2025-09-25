#!/bin/bash
#SBATCH --job-name=jupyter-tensorflow # Job name
#SBATCH --ntasks=1 # Run on a single CPU
#SBATCH --mem=16gb # Job memory request
#SBATCH --time=03:00:00 # Time limit hrs:min:sec
#SBATCH --partition=teaching
#SBATCH --gres=gpu:1
#SBATCH --output=jupyter%j.log # Standard output and error log
# Start Jupyter Notebook port
export PORT=8888
testport() {
nc -z 127.0.0.1 $1
return $?
}


echo "---- Allocated ----"
hostname; date
while testport $PORT
do
echo "Port $PORT in use. Trying next port..."
((PORT=PORT+1))
sleep 0.5
done
echo "-- Forward port from local host --"
echo "ssh -L 8888:localhost:$PORT $HOSTNAME -J cluster1.cecs.anu.edu.au"
echo "-- Starting Notebook --"
singularity exec --nv /opt/apps/containers/tensorflow_21.10-tf2-py3.sif jupyter notebook --port $PORT day-night-image-translations-using-cyclegan.ipynb
echo "---- Completed ----"
