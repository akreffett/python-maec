#MAEC Action Reference List Class

#Copyright (c) 2013, The MITRE Corporation
#All rights reserved.

#Compatible with MAEC v4.0
#Last updated 06/26/2013

import maec
import maec.bindings.maec_bundle as bundle_binding
from cybox.core.action_reference import ActionReference

class ActionReferenceList(maec.EntityList):
    _contained_type = ActionReference
    _binding_class = bundle_binding.ActionReferenceListType
    _binding_var = "Action_Reference"