from pymol import cmd

@cmd.extend
def pharm_view(pharm_name, mols_name, s_scale = 0.35, s_transparency = 0.5):
	"""
	Makes specified changes to pharmacophore and molecule representations
	
	:param pharm_name: name of pharmacophore object
	:param mols_name: name of molecule object
	:param s_scale: size of spheres representing pharmacophore features (default = 0.35)
	:param s_transparency: transparency of spheres representing pharmacophore features (default = 0.5)
	"""
	
	cmd.show("spheres", pharm_name)
	cmd.show("sticks", mols_name)
	cmd.set('sphere_scale', value=s_scale, selection=pharm_name, state=0)
	cmd.set('sphere_transparency', value=s_transparency, selection=pharm_name, state=0)
	cmd.label(pharm_name, 'name')
	cmd.set('label_position', value=(2,1,2))
	cmd.spectrum(expression="name", palette="rainbow", selection=pharm_name)


@cmd.extend
def pharm_view2(pharm_name, s_scale = 0.35, s_transparency = 0.5, show_id=0):
	"""
	Makes specified changes to pharmacophore and molecule representations
	
	:param pharm_name: name of pharmacophore object
	:param s_scale: size of spheres representing pharmacophore features (default = 0.35)
	:param s_transparency: transparency of spheres representing pharmacophore features (default = 0.5)
	:param show_id: 0 - show feature names, 1 - show feature IDs
	"""
	
	cmd.alter(pharm_name + ' and name A+D+H', 'vdw=0.85')
	cmd.alter(pharm_name + ' and name ar+P+N', 'vdw=1.15')
	cmd.show_as("spheres", pharm_name)
	#cmd.set('sphere_scale', value=s_scale, selection=pharm_name, state=0)
	cmd.set('sphere_transparency', value=s_transparency, selection=pharm_name, state=0)
	if show_id:
		cmd.label(pharm_name, 'ID')
	else:
		cmd.label(pharm_name, 'name')
	cmd.set('label_position', value=(2,1,2))
	cmd.color('blue', pharm_name + ' and name ar')
	cmd.color('orange', pharm_name + ' and name H')
	cmd.color('red', pharm_name + ' and name A')
	cmd.color('forest', pharm_name + ' and name D')
	cmd.color('yellow', pharm_name + ' and name N')
	cmd.color('violet', pharm_name + ' and name P')
	#cmd.spectrum(expression="name", palette="rainbow", selection=pharm_name)
