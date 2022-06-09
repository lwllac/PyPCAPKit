# -*- coding: utf-8 -*-
# pylint: disable=unused-import
""":class:`~pcapkit.protocols.internet.hip.HIP` Constant Enumerations
========================================================================

.. module:: pcapkit.const.hip

This module contains all constant enumerations of
:class:`~pcapkit.protocols.internet.hip.HIP` enumerations include:

.. list-table::
   :widths: auto

   * - :class:`HIP_Certificate <pcapkit.const.hip.certificate.Certificate>`
     - HIP Certificate Types [*]_
   * - :class:`HIP_Cipher <pcapkit.const.hip.cipher.Cipher>`
     - HIP Cipher IDs [*]_
   * - :class:`HIP_DITypes <pcapkit.const.hip.di.DITypes>`
     - DI-Types [*]_
   * - :class:`HIP_ECDSACurve <pcapkit.const.hip.ecdsa_curve.ECDSACurve>`
     - ECDSA Curve Label [*]_
   * - :class:`HIP_ECDSALowCurve <pcapkit.const.hip.ecdsa_low_curve.ECDSALowCurve>`
     - ECDSA_LOW Curve Label [*]_
   * - :class:`HIP_ESPTransformSuite <pcapkit.const.hip.esp_transform_suite.ESPTransformSuite>`
     - ESP Transform Suite IDs [*]_
   * - :class:`HIP_Group <pcapkit.const.hip.group.Group>`
     - Group IDs [*]_
   * - :class:`HIP_HIAlgorithm <pcapkit.const.hip.hi_algorithm.HIAlgorithm>`
     - HI Algorithm [*]_
   * - :class:`HIP_HITSuite <pcapkit.const.hip.hit_suite.HITSuite>`
     - HIT Suite IDs [*]_
   * - :class:`HIP_NATTraversal <pcapkit.const.hip.nat_traversal.NATTraversal>`
     - HIP NAT Traversal Modes [*]_
   * - :class:`HIP_NotifyMessage <pcapkit.const.hip.notify_message.NotifyMessage>`
     - Notify Message Types [*]_
   * - :class:`HIP_Packet <pcapkit.const.hip.packet.Packet>`
     - Packet Types [*]_
   * - :class:`HIP_Parameter <pcapkit.const.hip.parameter.Parameter>`
     - Parameter Types [*]_
   * - :class:`HIP_Registration <pcapkit.const.hip.registration.Registration>`
     - Registration Types [*]_
   * - :class:`HIP_RegistrationFailure <pcapkit.const.hip.registration_failure.RegistrationFailure>`
     - Registration Failure Types [*]_
   * - :class:`HIP_Suite <pcapkit.const.hip.suite.Suite>`
     - Suite IDs [*]_
   * - :class:`HIP_Transport <pcapkit.const.hip.transport.Transport>`
     - HIP Transport Modes [*]_

.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#certificate-types
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-cipher-id
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-parameters-7
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#ecdsa-curve-label
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#ecdsa-low-curve-label
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#esp-transform-suite-ids
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-parameters-5
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hi-algorithm
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hit-suite-id
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#nat-traversal
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-parameters-9
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-parameters-1
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-parameters-4
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-parameters-11
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-parameters-13
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#hip-parameters-6
.. [*] https://www.iana.org/assignments/hip-parameters/hip-parameters.xhtml#transport-modes

"""

from pcapkit.const.hip.certificate import Certificate as HIP_Certificate
from pcapkit.const.hip.cipher import Cipher as HIP_Cipher
from pcapkit.const.hip.di import DITypes as HIP_DITypes
from pcapkit.const.hip.ecdsa_curve import ECDSACurve as HIP_ECDSACurve
from pcapkit.const.hip.ecdsa_low_curve import ECDSALowCurve as HIP_ECDSALowCurve
from pcapkit.const.hip.esp_transform_suite import ESPTransformSuite as HIP_ESPTransformSuite
from pcapkit.const.hip.group import Group as HIP_Group
from pcapkit.const.hip.hi_algorithm import HIAlgorithm as HIP_HIAlgorithm
from pcapkit.const.hip.hit_suite import HITSuite as HIP_HITSuite
from pcapkit.const.hip.nat_traversal import NATTraversal as HIP_NATTraversal
from pcapkit.const.hip.notify_message import NotifyMessage as HIP_NotifyMessage
from pcapkit.const.hip.packet import Packet as HIP_Packet
from pcapkit.const.hip.parameter import Parameter as HIP_Parameter
from pcapkit.const.hip.registration import Registration as HIP_Registration
from pcapkit.const.hip.registration_failure import RegistrationFailure as HIP_RegistrationFailure
from pcapkit.const.hip.suite import Suite as HIP_Suite
from pcapkit.const.hip.transport import Transport as HIP_Transport

__all__ = ['HIP_Certificate', 'HIP_Cipher', 'HIP_DITypes', 'HIP_ECDSACurve', 'HIP_ECDSALowCurve',
           'HIP_ESPTransformSuite', 'HIP_Group', 'HIP_HIAlgorithm', 'HIP_HITSuite', 'HIP_NATTraversal',
           'HIP_NotifyMessage', 'HIP_Packet', 'HIP_Parameter', 'HIP_Registration', 'HIP_RegistrationFailure',
           'HIP_Suite', 'HIP_Transport']
