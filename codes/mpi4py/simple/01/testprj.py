from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print(f'Hello, world! I am process {rank} of {size}')
else:
    print(f'Hello! I am process {rank} of {size}')