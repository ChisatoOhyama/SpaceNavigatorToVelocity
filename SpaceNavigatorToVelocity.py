#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file SpaceNavigatorToVelocity.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
spacenavigatortovelocity_spec = ["implementation_id", "SpaceNavigatorToVelocity", 
		 "type_name",         "SpaceNavigatorToVelocity", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "pretty", 
		 "category",          "Convete", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.gainX", "0.01",
		 "conf.default.gainY", "0.01",
		 "conf.default.gainZ", "0.01",
		 "conf.default.xIndex", "0",
		 "conf.default.yIndex", "1",
		 "conf.default.zIndex", "2",
		 "conf.__widget__.gainX", "text",
		 "conf.__widget__.gainY", "text",
		 "conf.__widget__.gainZ", "text",
		 "conf.__widget__.xIndex", "text",
		 "conf.__widget__.yIndex", "text",
		 "conf.__widget__.zIndex", "text",
		 ""]
# </rtc-template>

##
# @class SpaceNavigatorToVelocity
# @brief ModuleDescription
# 
# 
class SpaceNavigatorToVelocity(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_in = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		"""
		"""
		self._inIn = OpenRTM_aist.InPort("in", self._d_in)
		self._d_3DVelocity = RTC.TimedVelocity3D(RTC.Time(0,0), RTC.Velocity3D(0,0,0,0,0,0))
		"""
		"""
		self._3DVelocityOut = OpenRTM_aist.OutPort("3DVelocity", self._d_3DVelocity)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  gainX
		 - DefaultValue: 0.01
		"""
		self._gainX = [0.01]
		"""
		
		 - Name:  gainY
		 - DefaultValue: 0.01
		"""
		self._gainY = [0.01]
		"""
		
		 - Name:  gainZ
		 - DefaultValue: 0.01
		"""
		self._gainZ = [0.01]
		"""
		
		 - Name:  xIndex
		 - DefaultValue: 0
		"""
		self._xIndex = [0]
		"""
		
		 - Name:  yIndex
		 - DefaultValue: 1
		"""
		self._yIndex = [1]
		"""
		
		 - Name:  zIndex
		 - DefaultValue: 2
		"""
		self._zIndex = [2]
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("gainX", self._gainX, "0.01")
		self.bindParameter("gainY", self._gainY, "0.01")
		self.bindParameter("gainZ", self._gainZ, "0.01")
		self.bindParameter("xIndex", self._xIndex, "0")
		self.bindParameter("yIndex", self._yIndex, "1")
		self.bindParameter("zIndex", self._zIndex, "2")
		
		# Set InPort buffers
		self.addInPort("in",self._inIn)
		
		# Set OutPort buffers
		self.addOutPort("3DVelocity",self._3DVelocityOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
                self._d_3DVelocity.data.vx = 0.0
                self._d_3DVelocity.data.vy = 0.0
                self._d_3DVelocity.data.vz = 0.0
                self._d_3DVelocity.data.vr = 0.0
                self._d_3DVelocity.data.vp = 0.0
                self._d_3DVelocity.data.va = 0.0
                
                
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
                if self._inIn.isNew():
                        self._d_in = self._inIn.read()

                        print self._d_in.data
                        #if self._d_in.data.length() <= self._xIndex[0] || self._d_in.data.length() <= self._yIndex[0] || self._d_in.data.length() <= self._zIndex[0] :
                                #print "[RTC::SFMLJoystickToVelocity] Too short Sequence Input." 
                                #return RTC::RTC_ERROR
		
                        #self._d_3DVelocity.data.vx = self._gainX[0] * self._d_in.data[self._xIndex[0]]
                        #self._d_3DVelocity.data.vy = self._gainY[0] * self._d_in.data[self._yIndex[0]]
                        #self._d_3DVelocity.data.vz = self._gainZ[0] * self._d_in.data[self._zIndex[0]]
                
                        self._3DVelocityOut.write()
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def SpaceNavigatorToVelocityInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=spacenavigatortovelocity_spec)
    manager.registerFactory(profile,
                            SpaceNavigatorToVelocity,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SpaceNavigatorToVelocityInit(manager)

    # Create a component
    comp = manager.createComponent("SpaceNavigatorToVelocity")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

