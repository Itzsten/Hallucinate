from win32con import *

import ctypes
import ctypes.wintypes as wintypes

if ctypes.sizeof(ctypes.c_longlong) == ctypes.sizeof(ctypes.c_void_p): # added support for 32-bit systems
    UINT_PTR = ctypes.c_ulonglong
    LONG_PTR = ctypes.c_longlong
    ULONG_PTR = ctypes.c_ulonglong
else:
    UINT_PTR = ctypes.c_ulong
    LONG_PTR = ctypes.c_long
    ULONG_PTR = ctypes.c_ulong
LPARAM = LONG_PTR
WPARAM = UINT_PTR

LONG = ctypes.c_long
DWORD = ctypes.c_ulong
WORD = USHORT = ctypes.c_ushort
HANDLE = ctypes.c_void_p

UINT64 = ctypes.c_uint64
UINT8  = ctypes.c_uint8

PDWORD = ctypes.POINTER(DWORD)
CHAR = ctypes.c_char
WCHAR = ctypes.c_wchar
UINT = ctypes.c_uint
INT = ctypes.c_int
LPCOLESTR = LPOLESTR = OLESTR = ctypes.c_wchar_p
LPCWSTR = LPWSTR = ctypes.c_wchar_p
LPCSTR = LPSTR = ctypes.c_char_p
LPCVOID = LPVOID = PVOID = ctypes.c_void_p
LPUINT = PUINT = ctypes.POINTER(UINT)
PWSTR = ctypes.POINTER(WCHAR)

STATUS_SUCCESS = 0x0
NonPagedPoolNx = 512

def BSOD():
    m = ctypes.windll.ntdll
    ErrorResponse = ctypes.c_ulong(0)
    m.NtRaiseHardError(0xDEADDEAD, 0, 0, None, 6, ctypes.byref(ErrorResponse))
class NtPrivilege:
    SeCreateTokenPrivilege = 1
    SeAssignPrimaryTokenPrivilege = 2
    SeLockMemoryPrivilege = 3
    SeIncreaseQuotaPrivilege = 4
    SeUnsolicitedInputPrivilege = 5
    SeMachineAccountPrivilege = 6
    SeTcbPrivilege = 7
    SeSecurityPrivilege = 8
    SeTakeOwnershipPrivilege = 9
    SeLoadDriverPrivilege = 10
    SeSystemProfilePrivilege = 11
    SeSystemtimePrivilege = 12
    SeProfileSingleProcessPrivilege = 13
    SeIncreaseBasePriorityPrivilege = 14
    SeCreatePagefilePrivilege = 15
    SeCreatePermanentPrivilege = 16
    SeBackupPrivilege = 17
    SeRestorePrivilege = 18
    SeShutdownPrivilege = 19
    SeDebugPrivilege = 20
    SeAuditPrivilege = 21
    SeSystemEnvironmentPrivilege = 22
    SeChangeNotifyPrivilege = 23
    SeRemoteShutdownPrivilege = 24
    SeUndockPrivilege = 25
    SeSyncAgentPrivilege = 26
    SeEnableDelegationPrivilege = 27
    SeManageVolumePrivilege = 28
    SeImpersonatePrivilege = 29
    SeCreateGlobalPrivilege = 30
    SeTrustedCredManAccessPrivilege = 31
    SeRelabelPrivilege = 32
    SeIncreaseWorkingSetPrivilege = 33
    SeTimeZonePrivilege = 34
    SeCreateSymbolicLinkPrivilege = 35
class NtProcessClass:
    SeCriticalProcess = 0x1d
class SYSTEM_POWER_STATE:
    PowerSystemUnspecified = 0
    PowerSystemWorking = 1
    PowerSystemSleeping1 = 2
    PowerSystemSleeping2 = 3
    PowerSystemSleeping3 = 4
    PowerSystemHibernate = 5
    PowerSystemShutdown = 6
    PowerSystemMaximum = 7
class DEVICE_POWER_STATE:
    PowerDeviceUnspecified = -1
    PowerDeviceD0 = 0 # Full On: full power, full functionality
    PowerDeviceD1 = 1 #Low Power On: fully functional at low power/performance
    PowerDeviceD2 = 2 # Standby: partially powered with automatic wake
    PowerDeviceD3 = 3 # Sleep: partially powered with device initiated wake
    PowerDeviceD4 = 4 # Off: unpowered
    PowerDeviceMaximum = 5 # System shall only use it
class _POWER_STATE(ctypes.Union):
    _fields_ = [
        ("SystemState", INT),
        ("DeviceState", INT)
    ]
POWER_STATE = _POWER_STATE
PPOWER_STATE = ctypes.POINTER(_POWER_STATE)
CloseHandleC = ctypes.windll.Kernel32.CloseHandle

def RtlAdjustPrivilege(Privilege, Enable, CurrentThread, Enabled=True):
    PrivilegeState = ctypes.c_bool(int(Enabled))
    res = ctypes.windll.ntdll.RtlAdjustPrivilege(Privilege, Enable, CurrentThread, ctypes.pointer(PrivilegeState))
    return res

def NtSetInformationProcess(ProcessHandle, ProcessInformationClass, ProcessInformation):
    ProcessHandle = wintypes.HANDLE(ProcessHandle)
    NtSe = ctypes.windll.ntdll.NtSetInformationProcess
    ProcessInformation = ctypes.c_ulong(ProcessInformation) 
    ProcessInformationLength = ctypes.sizeof(ctypes.c_ulong)
    NtSe.argtypes = (
        wintypes.HANDLE,
        ctypes.c_int,
        PVOID,
        ctypes.c_ulong
    )
    r = NtSe(ProcessHandle, ProcessInformationClass, ctypes.byref(ProcessInformation), ProcessInformationLength)
    CloseHandleC(ProcessHandle)
    return r
def RtlCopyMemory(Destination, Source, Length):
    return ctypes.windll.ntdll.RtlCopyMemory(Destination, Source, Length)
class _UNICODE_STRING(ctypes.Structure):
    _fields_ = [
        ("Length", USHORT),
        ("MaximumLength", USHORT),
        ("Buffer", PWSTR)
    ]
UNICODE_STRING = _UNICODE_STRING
PUNICODE_STRING = _UNICODE_STRING

def RGB(red, green, blue):
    return blue + (green << 8) + (red << 16)

sizeof = ctypes.sizeof
u0 = UINT64(0)

PowerActionShutdownOff = 6
PowerSystemShutdown = 6
SHTDN_REASON_MAJOR_HARDWARE = 0x00010000
SHTDN_REASON_MINOR_POWER_SUPPLY = 0x0000000a

def NtSetSystemPowerState(SystemPowerState, NoResumeAlarm, ForcePowerDown):
    return ctypes.windll.ntdll.NtSetSystemPowerState(SystemPowerState, NoResumeAlarm, ForcePowerDown)
