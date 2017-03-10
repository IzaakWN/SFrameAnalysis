// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME srcdISFrameUser_Dict

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Since CINT ignores the std namespace, we need to do so in this file.
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "include/SecondCycle.h"
#include "include/FirstCycle.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static void *new_FirstCycle(void *p = 0);
   static void *newArray_FirstCycle(Long_t size, void *p);
   static void delete_FirstCycle(void *p);
   static void deleteArray_FirstCycle(void *p);
   static void destruct_FirstCycle(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::FirstCycle*)
   {
      ::FirstCycle *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::FirstCycle >(0);
      static ::ROOT::TGenericClassInfo 
         instance("FirstCycle", ::FirstCycle::Class_Version(), "include/FirstCycle.h", 30,
                  typeid(::FirstCycle), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::FirstCycle::Dictionary, isa_proxy, 4,
                  sizeof(::FirstCycle) );
      instance.SetNew(&new_FirstCycle);
      instance.SetNewArray(&newArray_FirstCycle);
      instance.SetDelete(&delete_FirstCycle);
      instance.SetDeleteArray(&deleteArray_FirstCycle);
      instance.SetDestructor(&destruct_FirstCycle);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::FirstCycle*)
   {
      return GenerateInitInstanceLocal((::FirstCycle*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::FirstCycle*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SecondCycle(void *p = 0);
   static void *newArray_SecondCycle(Long_t size, void *p);
   static void delete_SecondCycle(void *p);
   static void deleteArray_SecondCycle(void *p);
   static void destruct_SecondCycle(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SecondCycle*)
   {
      ::SecondCycle *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SecondCycle >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SecondCycle", ::SecondCycle::Class_Version(), "include/SecondCycle.h", 29,
                  typeid(::SecondCycle), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SecondCycle::Dictionary, isa_proxy, 4,
                  sizeof(::SecondCycle) );
      instance.SetNew(&new_SecondCycle);
      instance.SetNewArray(&newArray_SecondCycle);
      instance.SetDelete(&delete_SecondCycle);
      instance.SetDeleteArray(&deleteArray_SecondCycle);
      instance.SetDestructor(&destruct_SecondCycle);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SecondCycle*)
   {
      return GenerateInitInstanceLocal((::SecondCycle*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SecondCycle*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

//______________________________________________________________________________
atomic_TClass_ptr FirstCycle::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *FirstCycle::Class_Name()
{
   return "FirstCycle";
}

//______________________________________________________________________________
const char *FirstCycle::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FirstCycle*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int FirstCycle::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::FirstCycle*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *FirstCycle::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FirstCycle*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *FirstCycle::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::FirstCycle*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SecondCycle::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SecondCycle::Class_Name()
{
   return "SecondCycle";
}

//______________________________________________________________________________
const char *SecondCycle::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SecondCycle*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SecondCycle::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SecondCycle*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SecondCycle::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SecondCycle*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SecondCycle::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SecondCycle*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
void FirstCycle::Streamer(TBuffer &R__b)
{
   // Stream an object of class FirstCycle.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(FirstCycle::Class(),this);
   } else {
      R__b.WriteClassBuffer(FirstCycle::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_FirstCycle(void *p) {
      return  p ? new(p) ::FirstCycle : new ::FirstCycle;
   }
   static void *newArray_FirstCycle(Long_t nElements, void *p) {
      return p ? new(p) ::FirstCycle[nElements] : new ::FirstCycle[nElements];
   }
   // Wrapper around operator delete
   static void delete_FirstCycle(void *p) {
      delete ((::FirstCycle*)p);
   }
   static void deleteArray_FirstCycle(void *p) {
      delete [] ((::FirstCycle*)p);
   }
   static void destruct_FirstCycle(void *p) {
      typedef ::FirstCycle current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::FirstCycle

//______________________________________________________________________________
void SecondCycle::Streamer(TBuffer &R__b)
{
   // Stream an object of class SecondCycle.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SecondCycle::Class(),this);
   } else {
      R__b.WriteClassBuffer(SecondCycle::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SecondCycle(void *p) {
      return  p ? new(p) ::SecondCycle : new ::SecondCycle;
   }
   static void *newArray_SecondCycle(Long_t nElements, void *p) {
      return p ? new(p) ::SecondCycle[nElements] : new ::SecondCycle[nElements];
   }
   // Wrapper around operator delete
   static void delete_SecondCycle(void *p) {
      delete ((::SecondCycle*)p);
   }
   static void deleteArray_SecondCycle(void *p) {
      delete [] ((::SecondCycle*)p);
   }
   static void destruct_SecondCycle(void *p) {
      typedef ::SecondCycle current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SecondCycle

namespace {
  void TriggerDictionaryInitialization_SFrameUser_Dict_Impl() {
    static const char* headers[] = {
"include/SecondCycle.h",
"include/FirstCycle.h",
0
    };
    static const char* includePaths[] = {
"/mnt/t3nfs01/data01/shome/ineuteli/analysis/SFrameAnalysis_Moriond/SFrame",
"./",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/lcg/root/6.06.00-ikhhed4/include",
"/mnt/t3nfs01/data01/shome/ineuteli/analysis/SFrameAnalysis_Moriond/SFrame/user/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "SFrameUser_Dict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
class __attribute__((annotate("$clingAutoload$include/FirstCycle.h")))  FirstCycle;
class __attribute__((annotate("$clingAutoload$include/SecondCycle.h")))  SecondCycle;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "SFrameUser_Dict dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "include/SecondCycle.h"
#include "include/FirstCycle.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"FirstCycle", payloadCode, "@",
"SecondCycle", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("SFrameUser_Dict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_SFrameUser_Dict_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_SFrameUser_Dict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_SFrameUser_Dict() {
  TriggerDictionaryInitialization_SFrameUser_Dict_Impl();
}
