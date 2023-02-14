# OpenMV Driver for Lehigh University AIRLab

This is a suite of Python scripts to bootstrap development for the OpenMV camera system.

It currently consists of 3 files:
- `device.py`: the transmitting component, which should be written to the OpenMV device's storage as `main.py`
- `host.py`: the receiving component, which should be run on a Linux PC alongside the file `rpc.py`
- `rpc.py`: a standard library component shipped with OpenMV, needed by `host.py`

By default, the host script expects access to the OpenMV device via USB at `/dev/ttyACM0`. However, this can be easily changed by passing a serial path as a CLI argument.

So, for example, to run with the default settings:

    python3 host.py

To use another USB port, we can try:

    python3 host.py /dev/ttyACM1

In addition to the OpenMV library file, this requires the following packages (along with their dependencies) installed on the Linux host:
- `numpy`
- `opencv` (preferably NOT headless)
- `pyserial`

A `requirements.yml` file for Anaconda will be included in this repository.