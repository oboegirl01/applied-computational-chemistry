"""B3LYP/6-31G(d) gas-phase thermochemistry of water at 298.15 K and 1 atm."""

from maestro import DFT, Maestro, OrcaEngine, SystemQM, ThermoTask
from maestro.engines.jobspec import EnvInfo, Resources

mae = Maestro(mode="slurm", workdir=".", runinfo_path="h2o_orca_runinfo.toml")

system = SystemQM(geometry="h2o.xyz", charge=0, spin=0)
theory = DFT(functional="B3LYP", basis="6-31G(d)")
qm_engine = OrcaEngine(
    env=EnvInfo(kind="module", modules=["orca/v6.0.1"]),
    resources=Resources(cores=1),
)
task = ThermoTask(system=system, theory=theory, temperature=298.15, pressure=1.0)

result = mae.run(rundir="h2o_thermo_work", task=task, engines=qm_engine)

print("Gibbs free energy in", result.unit("gibbs_free_energy"), ":")
print(result.load("gibbs_free_energy"))
