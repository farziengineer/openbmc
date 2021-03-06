# ",/usr/bin/env python,
# ,
# Copyright 2018-present Facebook. All Rights Reserved.,
# ,
# This program file is free software; you can redistribute it and/or modify it,
# under the terms of the GNU General Public License as published by the,
# Free Software Foundation; version 2 of the License.,
# ,
# This program is distributed in the hope that it will be useful, but WITHOUT,
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or,
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License,
# for more details.,
# ,
# You should have received a copy of the GNU General Public License,
# along with this program in a file named COPYING; if not, write to the,
# Free Software Foundation, Inc.,,
# 51 Franklin Street, Fifth Floor,,
# Boston, MA 02110-1301 USA,
# ,

SENSORS = [
    "1V05MIX_VR_CURR",
    "1V05MIX_VR_OUT_POWER",
    "1V05MIX_VR_TEMP",
    "1V05MIX_VR_VOLT",
    "FAN1_FRONT_SPEED",
    "FAN1_REAR_SPEED",
    "FAN2_FRONT_SPEED",
    "FAN2_REAR_SPEED",
    "FAN3_FRONT_SPEED",
    "FAN3_REAR_SPEED",
    "FAN4_FRONT_SPEED",
    "FAN4_REAR_SPEED",
    "FAN5_FRONT_SPEED",
    "FAN5_REAR_SPEED",
    "FAN6_FRONT_SPEED",
    "FAN6_REAR_SPEED",
    "FAN7_FRONT_SPEED",
    "FAN7_REAR_SPEED",
    "FAN8_FRONT_SPEED",
    "FAN8_REAR_SPEED",
    "FCM_B_HSC_CURR",
    "FCM_B_HSC_POWER",
    "FCM_B_HSC_VOLT",
    "FCM_B_TEMP1",
    "FCM_B_TEMP2",
    "FCM_T_HSC_CURR",
    "FCM_T_HSC_POWER",
    "FCM_T_HSC_VOLT",
    "FCM_T_TEMP1",
    "FCM_T_TEMP2",
    "INA230_POWER",
    "INA230_VOLT",
    "MB_INLET_TEMP",
    "MB_OUTLET_TEMP",
    "P12V_MB_VOLT",
    "P1V05_MIX_VOLT",
    "P1V05_PCH_VOLT",
    "P3V3_MB_VOLT",
    "P3V3_STBY_MB_VOLT",
    "P5V_STBY_MB_VOLT",
    "PCH_TEMP",
    "PDB_L_TEMP1",
    "PDB_L_TEMP2",
    "PDB_R_TEMP1",
    "PDB_R_TEMP2",
    "PIM1_HSC_CURR",
    "PIM1_HSC_POWER",
    "PIM1_HSC_VOLT",
    "PIM1_MAX34461_VOLT1",
    "PIM1_MAX34461_VOLT10",
    "PIM1_MAX34461_VOLT11",
    "PIM1_MAX34461_VOLT12",
    "PIM1_MAX34461_VOLT13",
    "PIM1_MAX34461_VOLT14",
    "PIM1_MAX34461_VOLT15",
    "PIM1_MAX34461_VOLT16",
    "PIM1_MAX34461_VOLT2",
    "PIM1_MAX34461_VOLT3",
    "PIM1_MAX34461_VOLT4",
    "PIM1_MAX34461_VOLT5",
    "PIM1_MAX34461_VOLT6",
    "PIM1_MAX34461_VOLT7",
    "PIM1_MAX34461_VOLT8",
    "PIM1_MAX34461_VOLT9",
    "PIM1_QSFP_TEMP",
    "PIM1_TEMP1",
    "PIM1_TEMP2",
    "PIM2_HSC_CURR",
    "PIM2_HSC_POWER",
    "PIM2_HSC_VOLT",
    "PIM2_MAX34461_VOLT1",
    "PIM2_MAX34461_VOLT10",
    "PIM2_MAX34461_VOLT11",
    "PIM2_MAX34461_VOLT12",
    "PIM2_MAX34461_VOLT13",
    "PIM2_MAX34461_VOLT14",
    "PIM2_MAX34461_VOLT15",
    "PIM2_MAX34461_VOLT16",
    "PIM2_MAX34461_VOLT2",
    "PIM2_MAX34461_VOLT3",
    "PIM2_MAX34461_VOLT4",
    "PIM2_MAX34461_VOLT5",
    "PIM2_MAX34461_VOLT6",
    "PIM2_MAX34461_VOLT7",
    "PIM2_MAX34461_VOLT8",
    "PIM2_MAX34461_VOLT9",
    "PIM2_QSFP_TEMP",
    "PIM2_TEMP1",
    "PIM2_TEMP2",
    "PIM3_HSC_CURR",
    "PIM3_HSC_POWER",
    "PIM3_HSC_VOLT",
    "PIM3_MAX34461_VOLT1",
    "PIM3_MAX34461_VOLT10",
    "PIM3_MAX34461_VOLT11",
    "PIM3_MAX34461_VOLT12",
    "PIM3_MAX34461_VOLT13",
    "PIM3_MAX34461_VOLT14",
    "PIM3_MAX34461_VOLT15",
    "PIM3_MAX34461_VOLT16",
    "PIM3_MAX34461_VOLT2",
    "PIM3_MAX34461_VOLT3",
    "PIM3_MAX34461_VOLT4",
    "PIM3_MAX34461_VOLT5",
    "PIM3_MAX34461_VOLT6",
    "PIM3_MAX34461_VOLT7",
    "PIM3_MAX34461_VOLT8",
    "PIM3_MAX34461_VOLT9",
    "PIM3_QSFP_TEMP",
    "PIM3_TEMP1",
    "PIM3_TEMP2",
    "PIM4_HSC_CURR",
    "PIM4_HSC_POWER",
    "PIM4_HSC_VOLT",
    "PIM4_MAX34461_VOLT1",
    "PIM4_MAX34461_VOLT10",
    "PIM4_MAX34461_VOLT11",
    "PIM4_MAX34461_VOLT12",
    "PIM4_MAX34461_VOLT13",
    "PIM4_MAX34461_VOLT14",
    "PIM4_MAX34461_VOLT15",
    "PIM4_MAX34461_VOLT16",
    "PIM4_MAX34461_VOLT2",
    "PIM4_MAX34461_VOLT3",
    "PIM4_MAX34461_VOLT4",
    "PIM4_MAX34461_VOLT5",
    "PIM4_MAX34461_VOLT6",
    "PIM4_MAX34461_VOLT7",
    "PIM4_MAX34461_VOLT8",
    "PIM4_MAX34461_VOLT9",
    "PIM4_QSFP_TEMP",
    "PIM4_TEMP1",
    "PIM4_TEMP2",
    "PIM5_HSC_CURR",
    "PIM5_HSC_POWER",
    "PIM5_HSC_VOLT",
    "PIM5_MAX34461_VOLT1",
    "PIM5_MAX34461_VOLT10",
    "PIM5_MAX34461_VOLT11",
    "PIM5_MAX34461_VOLT12",
    "PIM5_MAX34461_VOLT13",
    "PIM5_MAX34461_VOLT14",
    "PIM5_MAX34461_VOLT15",
    "PIM5_MAX34461_VOLT16",
    "PIM5_MAX34461_VOLT2",
    "PIM5_MAX34461_VOLT3",
    "PIM5_MAX34461_VOLT4",
    "PIM5_MAX34461_VOLT5",
    "PIM5_MAX34461_VOLT6",
    "PIM5_MAX34461_VOLT7",
    "PIM5_MAX34461_VOLT8",
    "PIM5_MAX34461_VOLT9",
    "PIM5_QSFP_TEMP",
    "PIM5_TEMP1",
    "PIM5_TEMP2",
    "PIM6_HSC_CURR",
    "PIM6_HSC_POWER",
    "PIM6_HSC_VOLT",
    "PIM6_MAX34461_VOLT1",
    "PIM6_MAX34461_VOLT10",
    "PIM6_MAX34461_VOLT11",
    "PIM6_MAX34461_VOLT12",
    "PIM6_MAX34461_VOLT13",
    "PIM6_MAX34461_VOLT14",
    "PIM6_MAX34461_VOLT15",
    "PIM6_MAX34461_VOLT16",
    "PIM6_MAX34461_VOLT2",
    "PIM6_MAX34461_VOLT3",
    "PIM6_MAX34461_VOLT4",
    "PIM6_MAX34461_VOLT5",
    "PIM6_MAX34461_VOLT6",
    "PIM6_MAX34461_VOLT7",
    "PIM6_MAX34461_VOLT8",
    "PIM6_MAX34461_VOLT9",
    "PIM6_QSFP_TEMP",
    "PIM6_TEMP1",
    "PIM6_TEMP2",
    "PIM7_HSC_CURR",
    "PIM7_HSC_POWER",
    "PIM7_HSC_VOLT",
    "PIM7_MAX34461_VOLT1",
    "PIM7_MAX34461_VOLT10",
    "PIM7_MAX34461_VOLT11",
    "PIM7_MAX34461_VOLT12",
    "PIM7_MAX34461_VOLT13",
    "PIM7_MAX34461_VOLT14",
    "PIM7_MAX34461_VOLT15",
    "PIM7_MAX34461_VOLT16",
    "PIM7_MAX34461_VOLT2",
    "PIM7_MAX34461_VOLT3",
    "PIM7_MAX34461_VOLT4",
    "PIM7_MAX34461_VOLT5",
    "PIM7_MAX34461_VOLT6",
    "PIM7_MAX34461_VOLT7",
    "PIM7_MAX34461_VOLT8",
    "PIM7_MAX34461_VOLT9",
    "PIM7_QSFP_TEMP",
    "PIM7_TEMP1",
    "PIM7_TEMP2",
    "PIM8_HSC_CURR",
    "PIM8_HSC_POWER",
    "PIM8_HSC_VOLT",
    "PIM8_MAX34461_VOLT1",
    "PIM8_MAX34461_VOLT10",
    "PIM8_MAX34461_VOLT11",
    "PIM8_MAX34461_VOLT12",
    "PIM8_MAX34461_VOLT13",
    "PIM8_MAX34461_VOLT14",
    "PIM8_MAX34461_VOLT15",
    "PIM8_MAX34461_VOLT16",
    "PIM8_MAX34461_VOLT2",
    "PIM8_MAX34461_VOLT3",
    "PIM8_MAX34461_VOLT4",
    "PIM8_MAX34461_VOLT5",
    "PIM8_MAX34461_VOLT6",
    "PIM8_MAX34461_VOLT7",
    "PIM8_MAX34461_VOLT8",
    "PIM8_MAX34461_VOLT9",
    "PIM8_QSFP_TEMP",
    "PIM8_TEMP1",
    "PIM8_TEMP2",
    "POWR1220_VCCA",
    "POWR1220_VCCINP",
    "POWR1220_VMON1",
    "POWR1220_VMON10",
    "POWR1220_VMON11",
    "POWR1220_VMON12",
    "POWR1220_VMON2",
    "POWR1220_VMON3",
    "POWR1220_VMON4",
    "POWR1220_VMON5",
    "POWR1220_VMON6",
    "POWR1220_VMON7",
    "POWR1220_VMON8",
    "POWR1220_VMON9",
    "PSU1_12V_CURR",
    "PSU1_12V_POWER",
    "PSU1_12V_VOLT",
    "PSU1_FAN_SPEED",
    "PSU1_IN_CURR",
    "PSU1_IN_POWER",
    "PSU1_IN_VOLT",
    "PSU1_STBY_CURR",
    "PSU1_STBY_POWER",
    "PSU1_STBY_VOLT",
    "PSU1_TEMP1",
    "PSU1_TEMP2",
    "PSU1_TEMP3",
    "PSU2_12V_CURR",
    "PSU2_12V_POWER",
    "PSU2_12V_VOLT",
    "PSU2_FAN_SPEED",
    "PSU2_IN_CURR",
    "PSU2_IN_POWER",
    "PSU2_IN_VOLT",
    "PSU2_STBY_CURR",
    "PSU2_STBY_POWER",
    "PSU2_STBY_VOLT",
    "PSU2_TEMP1",
    "PSU2_TEMP2",
    "PSU2_TEMP3",
    "PSU3_12V_CURR",
    "PSU3_12V_POWER",
    "PSU3_12V_VOLT",
    "PSU3_FAN_SPEED",
    "PSU3_IN_CURR",
    "PSU3_IN_POWER",
    "PSU3_IN_VOLT",
    "PSU3_STBY_CURR",
    "PSU3_STBY_POWER",
    "PSU3_STBY_VOLT",
    "PSU3_TEMP1",
    "PSU3_TEMP2",
    "PSU3_TEMP3",
    "PSU4_12V_CURR",
    "PSU4_12V_POWER",
    "PSU4_12V_VOLT",
    "PSU4_FAN_SPEED",
    "PSU4_IN_CURR",
    "PSU4_IN_POWER",
    "PSU4_IN_VOLT",
    "PSU4_STBY_CURR",
    "PSU4_STBY_POWER",
    "PSU4_STBY_VOLT",
    "PSU4_TEMP1",
    "PSU4_TEMP2",
    "PSU4_TEMP3",
    "PVDDR_VOLT",
    "PV_BAT_VOLT",
    "SCM_HSC_CURR",
    "SCM_HSC_POWER",
    "SCM_HSC_VOLT",
    "SCM_INLET_LOCAL_TEMP",
    "SCM_INLET_REMOTE_TEMP",
    "SCM_OUTLET_LOCAL_TEMP",
    "SCM_OUTLET_REMOTE_TEMP",
    "SMB_TEMP1",
    "SMB_TEMP2",
    "SMB_TEMP3",
    "SMB_TEMP4",
    "SMB_TEMP5",
    "SOC_DIMMA0_TEMP",
    "SOC_DIMMB0_TEMP",
    "SOC_PACKAGE_POWER",
    "SOC_TEMP",
    "SOC_TJMAX_TEMP",
    "SYSTEM_AIRFLOW",
    "TH3_CORE_CURR",
    "TH3_CORE_TEMP",
    "TH3_CORE_VOLT",
    "TH3_DIE_TEMP1",
    "TH3_DIE_TEMP2",
    "TH3_SERDES_CURR",
    "TH3_SERDES_TEMP",
    "TH3_SERDES_VOLT",
    "VCCIN_VR_CURR",
    "VCCIN_VR_OUT_POWER",
    "VCCIN_VR_TEMP",
    "VCCIN_VR_VOLT",
    "VDDR_VR_CURR",
    "VDDR_VR_OUT_POWER",
    "VDDR_VR_TEMP",
    "VDDR_VR_VOLT",
]

SCM_SENSORS = [
    "SCM_OUTLET_LOCAL_TEMP",
    "SCM_OUTLET_REMOTE_TEMP",
    "SCM_INLET_LOCAL_TEMP",
    "SCM_INLET_REMOTE_TEMP",
    "SCM_HSC_VOLT",
    "SCM_HSC_CURR",
    "SCM_HSC_POWER",
    "MB_OUTLET_TEMP",
    "MB_INLET_TEMP",
    "PCH_TEMP",
    "VCCIN_VR_TEMP",
    "1V05MIX_VR_TEMP",
    "SOC_TEMP",
    #    "SOC_THERM_MARGIN_TEMP",
    "VDDR_VR_TEMP",
    "SOC_DIMMA0_TEMP",
    "SOC_DIMMB0_TEMP",
    "SOC_PACKAGE_POWER",
    "VCCIN_VR_OUT_POWER",
    "VDDR_VR_OUT_POWER",
    "SOC_TJMAX_TEMP",
    "P3V3_MB_VOLT",
    "P12V_MB_VOLT",
    "P1V05_PCH_VOLT",
    "P3V3_STBY_MB_VOLT",
    "P5V_STBY_MB_VOLT",
    "PV_BAT_VOLT",
    "PVDDR_VOLT",
    "P1V05_MIX_VOLT",
    "1V05MIX_VR_CURR",
    "VDDR_VR_CURR",
    "VCCIN_VR_CURR",
    "VCCIN_VR_VOLT",
    "VDDR_VR_VOLT",
    "1V05MIX_VR_VOLT",
    "1V05MIX_VR_OUT_POWER",
    "INA230_POWER",
    "INA230_VOLT",
]

PIM1_SENSORS = [
    "PIM1_TEMP1",
    "PIM1_TEMP2",
    "PIM1_QSFP_TEMP",
    "PIM1_HSC_VOLT",
    "PIM1_HSC_CURR",
    "PIM1_HSC_POWER",
    "PIM1_MAX34461_VOLT1",
    "PIM1_MAX34461_VOLT2",
    "PIM1_MAX34461_VOLT3",
    "PIM1_MAX34461_VOLT4",
    "PIM1_MAX34461_VOLT5",
    "PIM1_MAX34461_VOLT6",
    "PIM1_MAX34461_VOLT7",
    "PIM1_MAX34461_VOLT8",
    "PIM1_MAX34461_VOLT9",
    "PIM1_MAX34461_VOLT10",
    "PIM1_MAX34461_VOLT11",
    "PIM1_MAX34461_VOLT12",
    "PIM1_MAX34461_VOLT13",
    "PIM1_MAX34461_VOLT14",
    "PIM1_MAX34461_VOLT15",
    "PIM1_MAX34461_VOLT16",
]

PIM2_SENSORS = [
    "PIM2_TEMP1",
    "PIM2_TEMP2",
    "PIM2_QSFP_TEMP",
    "PIM2_HSC_VOLT",
    "PIM2_HSC_CURR",
    "PIM2_HSC_POWER",
    "PIM2_MAX34461_VOLT1",
    "PIM2_MAX34461_VOLT2",
    "PIM2_MAX34461_VOLT3",
    "PIM2_MAX34461_VOLT4",
    "PIM2_MAX34461_VOLT5",
    "PIM2_MAX34461_VOLT6",
    "PIM2_MAX34461_VOLT7",
    "PIM2_MAX34461_VOLT8",
    "PIM2_MAX34461_VOLT9",
    "PIM2_MAX34461_VOLT10",
    "PIM2_MAX34461_VOLT11",
    "PIM2_MAX34461_VOLT12",
    "PIM2_MAX34461_VOLT13",
    "PIM2_MAX34461_VOLT14",
    "PIM2_MAX34461_VOLT15",
    "PIM2_MAX34461_VOLT16",
]

PIM3_SENSORS = [
    "PIM3_TEMP1",
    "PIM3_TEMP2",
    "PIM3_QSFP_TEMP",
    "PIM3_HSC_VOLT",
    "PIM3_HSC_CURR",
    "PIM3_HSC_POWER",
    "PIM3_MAX34461_VOLT1",
    "PIM3_MAX34461_VOLT2",
    "PIM3_MAX34461_VOLT3",
    "PIM3_MAX34461_VOLT4",
    "PIM3_MAX34461_VOLT5",
    "PIM3_MAX34461_VOLT6",
    "PIM3_MAX34461_VOLT7",
    "PIM3_MAX34461_VOLT8",
    "PIM3_MAX34461_VOLT9",
    "PIM3_MAX34461_VOLT10",
    "PIM3_MAX34461_VOLT11",
    "PIM3_MAX34461_VOLT12",
    "PIM3_MAX34461_VOLT13",
    "PIM3_MAX34461_VOLT14",
    "PIM3_MAX34461_VOLT15",
    "PIM3_MAX34461_VOLT16",
]

PIM4_SENSORS = [
    "PIM4_TEMP1",
    "PIM4_TEMP2",
    "PIM4_QSFP_TEMP",
    "PIM4_HSC_VOLT",
    "PIM4_HSC_CURR",
    "PIM4_HSC_POWER",
    "PIM4_MAX34461_VOLT1",
    "PIM4_MAX34461_VOLT2",
    "PIM4_MAX34461_VOLT3",
    "PIM4_MAX34461_VOLT4",
    "PIM4_MAX34461_VOLT5",
    "PIM4_MAX34461_VOLT6",
    "PIM4_MAX34461_VOLT7",
    "PIM4_MAX34461_VOLT8",
    "PIM4_MAX34461_VOLT9",
    "PIM4_MAX34461_VOLT10",
    "PIM4_MAX34461_VOLT11",
    "PIM4_MAX34461_VOLT12",
    "PIM4_MAX34461_VOLT13",
    "PIM4_MAX34461_VOLT14",
    "PIM4_MAX34461_VOLT15",
    "PIM4_MAX34461_VOLT16",
]

PIM5_SENSORS = [
    "PIM5_TEMP1",
    "PIM5_TEMP2",
    "PIM5_QSFP_TEMP",
    "PIM5_HSC_VOLT",
    "PIM5_HSC_CURR",
    "PIM5_HSC_POWER",
    "PIM5_MAX34461_VOLT1",
    "PIM5_MAX34461_VOLT2",
    "PIM5_MAX34461_VOLT3",
    "PIM5_MAX34461_VOLT4",
    "PIM5_MAX34461_VOLT5",
    "PIM5_MAX34461_VOLT6",
    "PIM5_MAX34461_VOLT7",
    "PIM5_MAX34461_VOLT8",
    "PIM5_MAX34461_VOLT9",
    "PIM5_MAX34461_VOLT10",
    "PIM5_MAX34461_VOLT11",
    "PIM5_MAX34461_VOLT12",
    "PIM5_MAX34461_VOLT13",
    "PIM5_MAX34461_VOLT14",
    "PIM5_MAX34461_VOLT15",
    "PIM5_MAX34461_VOLT16",
]

PIM6_SENSORS = [
    "PIM6_TEMP1",
    "PIM6_TEMP2",
    "PIM6_QSFP_TEMP",
    "PIM6_HSC_VOLT",
    "PIM6_HSC_CURR",
    "PIM6_HSC_POWER",
    "PIM6_MAX34461_VOLT1",
    "PIM6_MAX34461_VOLT2",
    "PIM6_MAX34461_VOLT3",
    "PIM6_MAX34461_VOLT4",
    "PIM6_MAX34461_VOLT5",
    "PIM6_MAX34461_VOLT6",
    "PIM6_MAX34461_VOLT7",
    "PIM6_MAX34461_VOLT8",
    "PIM6_MAX34461_VOLT9",
    "PIM6_MAX34461_VOLT10",
    "PIM6_MAX34461_VOLT11",
    "PIM6_MAX34461_VOLT12",
    "PIM6_MAX34461_VOLT13",
    "PIM6_MAX34461_VOLT14",
    "PIM6_MAX34461_VOLT15",
    "PIM6_MAX34461_VOLT16",
]

PIM7_SENSORS = [
    "PIM7_TEMP1",
    "PIM7_TEMP2",
    "PIM7_QSFP_TEMP",
    "PIM7_HSC_VOLT",
    "PIM7_HSC_CURR",
    "PIM7_HSC_POWER",
    "PIM7_MAX34461_VOLT1",
    "PIM7_MAX34461_VOLT2",
    "PIM7_MAX34461_VOLT3",
    "PIM7_MAX34461_VOLT4",
    "PIM7_MAX34461_VOLT5",
    "PIM7_MAX34461_VOLT6",
    "PIM7_MAX34461_VOLT7",
    "PIM7_MAX34461_VOLT8",
    "PIM7_MAX34461_VOLT9",
    "PIM7_MAX34461_VOLT10",
    "PIM7_MAX34461_VOLT11",
    "PIM7_MAX34461_VOLT12",
    "PIM7_MAX34461_VOLT13",
    "PIM7_MAX34461_VOLT14",
    "PIM7_MAX34461_VOLT15",
    "PIM7_MAX34461_VOLT16",
]

PIM8_SENSORS = [
    "PIM8_TEMP1",
    "PIM8_TEMP2",
    "PIM8_QSFP_TEMP",
    "PIM8_HSC_VOLT",
    "PIM8_HSC_CURR",
    "PIM8_HSC_POWER",
    "PIM8_MAX34461_VOLT1",
    "PIM8_MAX34461_VOLT2",
    "PIM8_MAX34461_VOLT3",
    "PIM8_MAX34461_VOLT4",
    "PIM8_MAX34461_VOLT5",
    "PIM8_MAX34461_VOLT6",
    "PIM8_MAX34461_VOLT7",
    "PIM8_MAX34461_VOLT8",
    "PIM8_MAX34461_VOLT9",
    "PIM8_MAX34461_VOLT10",
    "PIM8_MAX34461_VOLT11",
    "PIM8_MAX34461_VOLT12",
    "PIM8_MAX34461_VOLT13",
    "PIM8_MAX34461_VOLT14",
    "PIM8_MAX34461_VOLT15",
    "PIM8_MAX34461_VOLT16",
]


PSU1_SENSORS = [
    "PSU1_IN_VOLT",
    "PSU1_12V_VOLT",
    "PSU1_STBY_VOLT",
    "PSU1_IN_CURR",
    "PSU1_12V_CURR",
    "PSU1_STBY_CURR",
    "PSU1_IN_POWER",
    "PSU1_12V_POWER",
    "PSU1_STBY_POWER",
    "PSU1_FAN_SPEED",
    "PSU1_TEMP1",
    "PSU1_TEMP2",
    "PSU1_TEMP3",
]

PSU2_SENSORS = [
    "PSU2_IN_VOLT",
    "PSU2_12V_VOLT",
    "PSU2_STBY_VOLT",
    "PSU2_IN_CURR",
    "PSU2_12V_CURR",
    "PSU2_STBY_CURR",
    "PSU2_IN_POWER",
    "PSU2_12V_POWER",
    "PSU2_STBY_POWER",
    "PSU2_FAN_SPEED",
    "PSU2_TEMP1",
    "PSU2_TEMP2",
    "PSU2_TEMP3",
]

PSU3_SENSORS = [
    "PSU3_IN_VOLT",
    "PSU3_12V_VOLT",
    "PSU3_STBY_VOLT",
    "PSU3_IN_CURR",
    "PSU3_12V_CURR",
    "PSU3_STBY_CURR",
    "PSU3_IN_POWER",
    "PSU3_12V_POWER",
    "PSU3_STBY_POWER",
    "PSU3_FAN_SPEED",
    "PSU3_TEMP1",
    "PSU3_TEMP2",
    "PSU3_TEMP3",
]

PSU4_SENSORS = [
    "PSU4_IN_VOLT",
    "PSU4_12V_VOLT",
    "PSU4_STBY_VOLT",
    "PSU4_IN_CURR",
    "PSU4_12V_CURR",
    "PSU4_STBY_CURR",
    "PSU4_IN_POWER",
    "PSU4_12V_POWER",
    "PSU4_STBY_POWER",
    "PSU4_FAN_SPEED",
    "PSU4_TEMP1",
    "PSU4_TEMP2",
    "PSU4_TEMP3",
]

SMB_SENSORS = [
    "POWR1220_VMON1",
    "POWR1220_VMON2",
    "POWR1220_VMON3",
    "POWR1220_VMON4",
    "POWR1220_VMON5",
    "POWR1220_VMON6",
    "POWR1220_VMON7",
    "POWR1220_VMON8",
    "POWR1220_VMON9",
    "POWR1220_VMON10",
    "POWR1220_VMON11",
    "POWR1220_VMON12",
    "POWR1220_VCCA",
    "POWR1220_VCCINP",
    "TH3_SERDES_VOLT",
    "TH3_SERDES_CURR",
    "TH3_SERDES_TEMP",
    "TH3_CORE_VOLT",
    "TH3_CORE_CURR",
    "TH3_CORE_TEMP",
    "SMB_TEMP1",
    "SMB_TEMP2",
    "SMB_TEMP3",
    "SMB_TEMP4",
    "SMB_TEMP5",
    "TH3_DIE_TEMP1",
    "TH3_DIE_TEMP2",
    "PDB_L_TEMP1",
    "PDB_L_TEMP2",
    "PDB_R_TEMP1",
    "PDB_R_TEMP2",
    "FCM_T_TEMP1",
    "FCM_T_TEMP2",
    "FCM_B_TEMP1",
    "FCM_B_TEMP2",
    "FCM_T_HSC_VOLT",
    "FCM_T_HSC_CURR",
    "FCM_T_HSC_POWER",
    "FCM_B_HSC_VOLT",
    "FCM_B_HSC_CURR",
    "FCM_B_HSC_POWER",
    "FAN1_FRONT_SPEED",
    "FAN1_REAR_SPEED",
    "FAN2_FRONT_SPEED",
    "FAN2_REAR_SPEED",
    "FAN3_FRONT_SPEED",
    "FAN3_REAR_SPEED",
    "FAN4_FRONT_SPEED",
    "FAN4_REAR_SPEED",
    "FAN5_FRONT_SPEED",
    "FAN5_REAR_SPEED",
    "FAN6_FRONT_SPEED",
    "FAN6_REAR_SPEED",
    "FAN7_FRONT_SPEED",
    "FAN7_REAR_SPEED",
    "FAN8_FRONT_SPEED",
    "FAN8_REAR_SPEED",
]
