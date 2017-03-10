// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME srcdISFramePlugIns_Dict

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
#include "include/SH1.h"
#include "include/SInputVariables.h"
#include "include/SParticle.h"
#include "include/FPCompare.h"
#include "include/SToolBase.h"
#include "include/SOutputVariables.h"
#include "include/SSummedVar.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static void *new_SParticle(void *p = 0);
   static void *newArray_SParticle(Long_t size, void *p);
   static void delete_SParticle(void *p);
   static void deleteArray_SParticle(void *p);
   static void destruct_SParticle(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SParticle*)
   {
      ::SParticle *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SParticle >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SParticle", ::SParticle::Class_Version(), "include/SParticle.h", 51,
                  typeid(::SParticle), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SParticle::Dictionary, isa_proxy, 4,
                  sizeof(::SParticle) );
      instance.SetNew(&new_SParticle);
      instance.SetNewArray(&newArray_SParticle);
      instance.SetDelete(&delete_SParticle);
      instance.SetDeleteArray(&deleteArray_SParticle);
      instance.SetDestructor(&destruct_SParticle);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SParticle*)
   {
      return GenerateInitInstanceLocal((::SParticle*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SParticle*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEshortgR_Dictionary();
   static void ProofSummedVarlEshortgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEshortgR(void *p = 0);
   static void *newArray_ProofSummedVarlEshortgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEshortgR(void *p);
   static void deleteArray_ProofSummedVarlEshortgR(void *p);
   static void destruct_ProofSummedVarlEshortgR(void *p);
   static Long64_t merge_ProofSummedVarlEshortgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<short>*)
   {
      ::ProofSummedVar<short> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<short> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<short>", ::ProofSummedVar<short>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<short>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEshortgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<short>) );
      instance.SetNew(&new_ProofSummedVarlEshortgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEshortgR);
      instance.SetDelete(&delete_ProofSummedVarlEshortgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEshortgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEshortgR);
      instance.SetMerge(&merge_ProofSummedVarlEshortgR);

      ::ROOT::AddClassAlternate("ProofSummedVar<short>","ProofSummedVar<Short_t>");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<short>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<short>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<short>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEshortgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<short>*)0x0)->GetClass();
      ProofSummedVarlEshortgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEshortgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEunsignedsPshortgR_Dictionary();
   static void ProofSummedVarlEunsignedsPshortgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEunsignedsPshortgR(void *p = 0);
   static void *newArray_ProofSummedVarlEunsignedsPshortgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEunsignedsPshortgR(void *p);
   static void deleteArray_ProofSummedVarlEunsignedsPshortgR(void *p);
   static void destruct_ProofSummedVarlEunsignedsPshortgR(void *p);
   static Long64_t merge_ProofSummedVarlEunsignedsPshortgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<unsigned short>*)
   {
      ::ProofSummedVar<unsigned short> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<unsigned short> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<unsigned short>", ::ProofSummedVar<unsigned short>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<unsigned short>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEunsignedsPshortgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<unsigned short>) );
      instance.SetNew(&new_ProofSummedVarlEunsignedsPshortgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEunsignedsPshortgR);
      instance.SetDelete(&delete_ProofSummedVarlEunsignedsPshortgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEunsignedsPshortgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEunsignedsPshortgR);
      instance.SetMerge(&merge_ProofSummedVarlEunsignedsPshortgR);

      ::ROOT::AddClassAlternate("ProofSummedVar<unsigned short>","ProofSummedVar<UShort_t>");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<unsigned short>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<unsigned short>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned short>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEunsignedsPshortgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned short>*)0x0)->GetClass();
      ProofSummedVarlEunsignedsPshortgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEunsignedsPshortgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEintgR_Dictionary();
   static void ProofSummedVarlEintgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEintgR(void *p = 0);
   static void *newArray_ProofSummedVarlEintgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEintgR(void *p);
   static void deleteArray_ProofSummedVarlEintgR(void *p);
   static void destruct_ProofSummedVarlEintgR(void *p);
   static Long64_t merge_ProofSummedVarlEintgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<int>*)
   {
      ::ProofSummedVar<int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<int> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<int>", ::ProofSummedVar<int>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEintgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<int>) );
      instance.SetNew(&new_ProofSummedVarlEintgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEintgR);
      instance.SetDelete(&delete_ProofSummedVarlEintgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEintgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEintgR);
      instance.SetMerge(&merge_ProofSummedVarlEintgR);

      ::ROOT::AddClassAlternate("ProofSummedVar<int>","ProofSummedVar<Int_t>");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<int>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<int>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<int>*)0x0)->GetClass();
      ProofSummedVarlEintgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEunsignedsPintgR_Dictionary();
   static void ProofSummedVarlEunsignedsPintgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEunsignedsPintgR(void *p = 0);
   static void *newArray_ProofSummedVarlEunsignedsPintgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEunsignedsPintgR(void *p);
   static void deleteArray_ProofSummedVarlEunsignedsPintgR(void *p);
   static void destruct_ProofSummedVarlEunsignedsPintgR(void *p);
   static Long64_t merge_ProofSummedVarlEunsignedsPintgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<unsigned int>*)
   {
      ::ProofSummedVar<unsigned int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<unsigned int> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<unsigned int>", ::ProofSummedVar<unsigned int>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<unsigned int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEunsignedsPintgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<unsigned int>) );
      instance.SetNew(&new_ProofSummedVarlEunsignedsPintgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEunsignedsPintgR);
      instance.SetDelete(&delete_ProofSummedVarlEunsignedsPintgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEunsignedsPintgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEunsignedsPintgR);
      instance.SetMerge(&merge_ProofSummedVarlEunsignedsPintgR);

      ::ROOT::AddClassAlternate("ProofSummedVar<unsigned int>","ProofSummedVar<UInt_t>");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<unsigned int>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<unsigned int>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEunsignedsPintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned int>*)0x0)->GetClass();
      ProofSummedVarlEunsignedsPintgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEunsignedsPintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlElonggR_Dictionary();
   static void ProofSummedVarlElonggR_TClassManip(TClass*);
   static void *new_ProofSummedVarlElonggR(void *p = 0);
   static void *newArray_ProofSummedVarlElonggR(Long_t size, void *p);
   static void delete_ProofSummedVarlElonggR(void *p);
   static void deleteArray_ProofSummedVarlElonggR(void *p);
   static void destruct_ProofSummedVarlElonggR(void *p);
   static Long64_t merge_ProofSummedVarlElonggR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<long>*)
   {
      ::ProofSummedVar<long> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<long> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<long>", ::ProofSummedVar<long>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<long>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlElonggR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<long>) );
      instance.SetNew(&new_ProofSummedVarlElonggR);
      instance.SetNewArray(&newArray_ProofSummedVarlElonggR);
      instance.SetDelete(&delete_ProofSummedVarlElonggR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlElonggR);
      instance.SetDestructor(&destruct_ProofSummedVarlElonggR);
      instance.SetMerge(&merge_ProofSummedVarlElonggR);

      ::ROOT::AddClassAlternate("ProofSummedVar<long>","ProofSummedVar<Long_t>");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<long>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<long>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<long>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlElonggR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<long>*)0x0)->GetClass();
      ProofSummedVarlElonggR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlElonggR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEunsignedsPlonggR_Dictionary();
   static void ProofSummedVarlEunsignedsPlonggR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEunsignedsPlonggR(void *p = 0);
   static void *newArray_ProofSummedVarlEunsignedsPlonggR(Long_t size, void *p);
   static void delete_ProofSummedVarlEunsignedsPlonggR(void *p);
   static void deleteArray_ProofSummedVarlEunsignedsPlonggR(void *p);
   static void destruct_ProofSummedVarlEunsignedsPlonggR(void *p);
   static Long64_t merge_ProofSummedVarlEunsignedsPlonggR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<unsigned long>*)
   {
      ::ProofSummedVar<unsigned long> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<unsigned long> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<unsigned long>", ::ProofSummedVar<unsigned long>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<unsigned long>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEunsignedsPlonggR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<unsigned long>) );
      instance.SetNew(&new_ProofSummedVarlEunsignedsPlonggR);
      instance.SetNewArray(&newArray_ProofSummedVarlEunsignedsPlonggR);
      instance.SetDelete(&delete_ProofSummedVarlEunsignedsPlonggR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEunsignedsPlonggR);
      instance.SetDestructor(&destruct_ProofSummedVarlEunsignedsPlonggR);
      instance.SetMerge(&merge_ProofSummedVarlEunsignedsPlonggR);

      ::ROOT::AddClassAlternate("ProofSummedVar<unsigned long>","ProofSummedVar<ULong_t>");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<unsigned long>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<unsigned long>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned long>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEunsignedsPlonggR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned long>*)0x0)->GetClass();
      ProofSummedVarlEunsignedsPlonggR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEunsignedsPlonggR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlELong64_tgR_Dictionary();
   static void ProofSummedVarlELong64_tgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlELong64_tgR(void *p = 0);
   static void *newArray_ProofSummedVarlELong64_tgR(Long_t size, void *p);
   static void delete_ProofSummedVarlELong64_tgR(void *p);
   static void deleteArray_ProofSummedVarlELong64_tgR(void *p);
   static void destruct_ProofSummedVarlELong64_tgR(void *p);
   static Long64_t merge_ProofSummedVarlELong64_tgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<Long64_t>*)
   {
      ::ProofSummedVar<Long64_t> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<Long64_t> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<Long64_t>", ::ProofSummedVar<Long64_t>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<Long64_t>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlELong64_tgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<Long64_t>) );
      instance.SetNew(&new_ProofSummedVarlELong64_tgR);
      instance.SetNewArray(&newArray_ProofSummedVarlELong64_tgR);
      instance.SetDelete(&delete_ProofSummedVarlELong64_tgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlELong64_tgR);
      instance.SetDestructor(&destruct_ProofSummedVarlELong64_tgR);
      instance.SetMerge(&merge_ProofSummedVarlELong64_tgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<Long64_t>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<Long64_t>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<Long64_t>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlELong64_tgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<Long64_t>*)0x0)->GetClass();
      ProofSummedVarlELong64_tgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlELong64_tgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEULong64_tgR_Dictionary();
   static void ProofSummedVarlEULong64_tgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEULong64_tgR(void *p = 0);
   static void *newArray_ProofSummedVarlEULong64_tgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEULong64_tgR(void *p);
   static void deleteArray_ProofSummedVarlEULong64_tgR(void *p);
   static void destruct_ProofSummedVarlEULong64_tgR(void *p);
   static Long64_t merge_ProofSummedVarlEULong64_tgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<ULong64_t>*)
   {
      ::ProofSummedVar<ULong64_t> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<ULong64_t> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<ULong64_t>", ::ProofSummedVar<ULong64_t>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<ULong64_t>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEULong64_tgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<ULong64_t>) );
      instance.SetNew(&new_ProofSummedVarlEULong64_tgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEULong64_tgR);
      instance.SetDelete(&delete_ProofSummedVarlEULong64_tgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEULong64_tgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEULong64_tgR);
      instance.SetMerge(&merge_ProofSummedVarlEULong64_tgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<ULong64_t>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<ULong64_t>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<ULong64_t>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEULong64_tgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<ULong64_t>*)0x0)->GetClass();
      ProofSummedVarlEULong64_tgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEULong64_tgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEfloatgR_Dictionary();
   static void ProofSummedVarlEfloatgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEfloatgR(void *p = 0);
   static void *newArray_ProofSummedVarlEfloatgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEfloatgR(void *p);
   static void deleteArray_ProofSummedVarlEfloatgR(void *p);
   static void destruct_ProofSummedVarlEfloatgR(void *p);
   static Long64_t merge_ProofSummedVarlEfloatgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<float>*)
   {
      ::ProofSummedVar<float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<float> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<float>", ::ProofSummedVar<float>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<float>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEfloatgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<float>) );
      instance.SetNew(&new_ProofSummedVarlEfloatgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEfloatgR);
      instance.SetDelete(&delete_ProofSummedVarlEfloatgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEfloatgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEfloatgR);
      instance.SetMerge(&merge_ProofSummedVarlEfloatgR);

      ::ROOT::AddClassAlternate("ProofSummedVar<float>","ProofSummedVar<Float_t>");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<float>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<float>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<float>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<float>*)0x0)->GetClass();
      ProofSummedVarlEfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEdoublegR_Dictionary();
   static void ProofSummedVarlEdoublegR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEdoublegR(void *p = 0);
   static void *newArray_ProofSummedVarlEdoublegR(Long_t size, void *p);
   static void delete_ProofSummedVarlEdoublegR(void *p);
   static void deleteArray_ProofSummedVarlEdoublegR(void *p);
   static void destruct_ProofSummedVarlEdoublegR(void *p);
   static Long64_t merge_ProofSummedVarlEdoublegR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<double>*)
   {
      ::ProofSummedVar<double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<double>", ::ProofSummedVar<double>::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<double>) );
      instance.SetNew(&new_ProofSummedVarlEdoublegR);
      instance.SetNewArray(&newArray_ProofSummedVarlEdoublegR);
      instance.SetDelete(&delete_ProofSummedVarlEdoublegR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEdoublegR);
      instance.SetDestructor(&destruct_ProofSummedVarlEdoublegR);
      instance.SetMerge(&merge_ProofSummedVarlEdoublegR);

      ::ROOT::AddClassAlternate("ProofSummedVar<double>","ProofSummedVar<Double_t>");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<double>*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<double>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<double>*)0x0)->GetClass();
      ProofSummedVarlEdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlEshortgRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlEshortgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlEshortgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlEshortgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlEshortgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlEshortgRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlEshortgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlEshortgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<short> >*)
   {
      ::ProofSummedVar<vector<short> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<short> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<short> >", ::ProofSummedVar<vector<short> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<short> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlEshortgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<short> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlEshortgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlEshortgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlEshortgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlEshortgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlEshortgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlEshortgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<short> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<short> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<short> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlEshortgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<short> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlEshortgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlEshortgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlEunsignedsPshortgRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlEunsignedsPshortgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<unsigned short> >*)
   {
      ::ProofSummedVar<vector<unsigned short> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<unsigned short> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<unsigned short> >", ::ProofSummedVar<vector<unsigned short> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<unsigned short> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlEunsignedsPshortgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<unsigned short> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<unsigned short> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<unsigned short> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned short> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlEunsignedsPshortgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned short> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlEunsignedsPshortgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlEunsignedsPshortgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlEintgRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlEintgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlEintgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlEintgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlEintgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlEintgRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlEintgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlEintgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<int> >*)
   {
      ::ProofSummedVar<vector<int> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<int> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<int> >", ::ProofSummedVar<vector<int> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<int> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlEintgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<int> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlEintgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlEintgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlEintgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlEintgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlEintgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlEintgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<int> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<int> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<int> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlEintgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<int> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlEintgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlEintgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlEunsignedsPintgRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlEunsignedsPintgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<unsigned int> >*)
   {
      ::ProofSummedVar<vector<unsigned int> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<unsigned int> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<unsigned int> >", ::ProofSummedVar<vector<unsigned int> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<unsigned int> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlEunsignedsPintgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<unsigned int> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlEunsignedsPintgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlEunsignedsPintgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlEunsignedsPintgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlEunsignedsPintgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlEunsignedsPintgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlEunsignedsPintgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<unsigned int> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<unsigned int> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned int> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlEunsignedsPintgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned int> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlEunsignedsPintgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlEunsignedsPintgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlElonggRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlElonggRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlElonggRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlElonggRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlElonggRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlElonggRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlElonggRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlElonggRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<long> >*)
   {
      ::ProofSummedVar<vector<long> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<long> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<long> >", ::ProofSummedVar<vector<long> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<long> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlElonggRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<long> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlElonggRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlElonggRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlElonggRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlElonggRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlElonggRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlElonggRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<long> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<long> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<long> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlElonggRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<long> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlElonggRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlElonggRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlEunsignedsPlonggRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlEunsignedsPlonggRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<unsigned long> >*)
   {
      ::ProofSummedVar<vector<unsigned long> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<unsigned long> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<unsigned long> >", ::ProofSummedVar<vector<unsigned long> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<unsigned long> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlEunsignedsPlonggRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<unsigned long> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<unsigned long> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<unsigned long> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned long> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlEunsignedsPlonggRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned long> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlEunsignedsPlonggRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlEunsignedsPlonggRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlELong64_tgRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlELong64_tgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlELong64_tgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlELong64_tgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlELong64_tgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlELong64_tgRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlELong64_tgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlELong64_tgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<Long64_t> >*)
   {
      ::ProofSummedVar<vector<Long64_t> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<Long64_t> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<Long64_t> >", ::ProofSummedVar<vector<Long64_t> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<Long64_t> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlELong64_tgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<Long64_t> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlELong64_tgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlELong64_tgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlELong64_tgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlELong64_tgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlELong64_tgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlELong64_tgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<Long64_t> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<Long64_t> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<Long64_t> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlELong64_tgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<Long64_t> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlELong64_tgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlELong64_tgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlEULong64_tgRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlEULong64_tgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlEULong64_tgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<ULong64_t> >*)
   {
      ::ProofSummedVar<vector<ULong64_t> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<ULong64_t> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<ULong64_t> >", ::ProofSummedVar<vector<ULong64_t> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<ULong64_t> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlEULong64_tgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<ULong64_t> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlEULong64_tgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlEULong64_tgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlEULong64_tgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlEULong64_tgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlEULong64_tgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlEULong64_tgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<ULong64_t> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<ULong64_t> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<ULong64_t> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlEULong64_tgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<ULong64_t> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlEULong64_tgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlEULong64_tgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlEfloatgRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlEfloatgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlEfloatgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlEfloatgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlEfloatgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlEfloatgRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlEfloatgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlEfloatgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<float> >*)
   {
      ::ProofSummedVar<vector<float> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<float> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<float> >", ::ProofSummedVar<vector<float> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<float> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlEfloatgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<float> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlEfloatgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlEfloatgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlEfloatgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlEfloatgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlEfloatgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlEfloatgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<float> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<float> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<float> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlEfloatgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<float> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlEfloatgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlEfloatgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEvectorlEdoublegRsPgR_Dictionary();
   static void ProofSummedVarlEvectorlEdoublegRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEvectorlEdoublegRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEvectorlEdoublegRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEvectorlEdoublegRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEvectorlEdoublegRsPgR(void *p);
   static void destruct_ProofSummedVarlEvectorlEdoublegRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEvectorlEdoublegRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<vector<double> >*)
   {
      ::ProofSummedVar<vector<double> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<vector<double> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<vector<double> >", ::ProofSummedVar<vector<double> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<vector<double> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEvectorlEdoublegRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<vector<double> >) );
      instance.SetNew(&new_ProofSummedVarlEvectorlEdoublegRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEvectorlEdoublegRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEvectorlEdoublegRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEvectorlEdoublegRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEvectorlEdoublegRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEvectorlEdoublegRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<vector<double> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<vector<double> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<vector<double> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEvectorlEdoublegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<double> >*)0x0)->GetClass();
      ProofSummedVarlEvectorlEdoublegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEvectorlEdoublegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *pairlEstringcOunsignedsPintgR_Dictionary();
   static void pairlEstringcOunsignedsPintgR_TClassManip(TClass*);
   static void *new_pairlEstringcOunsignedsPintgR(void *p = 0);
   static void *newArray_pairlEstringcOunsignedsPintgR(Long_t size, void *p);
   static void delete_pairlEstringcOunsignedsPintgR(void *p);
   static void deleteArray_pairlEstringcOunsignedsPintgR(void *p);
   static void destruct_pairlEstringcOunsignedsPintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const pair<string,unsigned int>*)
   {
      pair<string,unsigned int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(pair<string,unsigned int>));
      static ::ROOT::TGenericClassInfo 
         instance("pair<string,unsigned int>", "string", 96,
                  typeid(pair<string,unsigned int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &pairlEstringcOunsignedsPintgR_Dictionary, isa_proxy, 4,
                  sizeof(pair<string,unsigned int>) );
      instance.SetNew(&new_pairlEstringcOunsignedsPintgR);
      instance.SetNewArray(&newArray_pairlEstringcOunsignedsPintgR);
      instance.SetDelete(&delete_pairlEstringcOunsignedsPintgR);
      instance.SetDeleteArray(&deleteArray_pairlEstringcOunsignedsPintgR);
      instance.SetDestructor(&destruct_pairlEstringcOunsignedsPintgR);
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const pair<string,unsigned int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *pairlEstringcOunsignedsPintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const pair<string,unsigned int>*)0x0)->GetClass();
      pairlEstringcOunsignedsPintgR_TClassManip(theClass);
   return theClass;
   }

   static void pairlEstringcOunsignedsPintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEmaplEstringcOintgRsPgR_Dictionary();
   static void ProofSummedVarlEmaplEstringcOintgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEmaplEstringcOintgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEmaplEstringcOintgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEmaplEstringcOintgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEmaplEstringcOintgRsPgR(void *p);
   static void destruct_ProofSummedVarlEmaplEstringcOintgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEmaplEstringcOintgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<map<string,int> >*)
   {
      ::ProofSummedVar<map<string,int> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<map<string,int> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<map<string,int> >", ::ProofSummedVar<map<string,int> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<map<string,int> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEmaplEstringcOintgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<map<string,int> >) );
      instance.SetNew(&new_ProofSummedVarlEmaplEstringcOintgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEmaplEstringcOintgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEmaplEstringcOintgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEmaplEstringcOintgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEmaplEstringcOintgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEmaplEstringcOintgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<map<string,int> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<map<string,int> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,int> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEmaplEstringcOintgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,int> >*)0x0)->GetClass();
      ProofSummedVarlEmaplEstringcOintgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEmaplEstringcOintgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR_Dictionary();
   static void ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *p);
   static void destruct_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<map<string,unsigned int> >*)
   {
      ::ProofSummedVar<map<string,unsigned int> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<map<string,unsigned int> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<map<string,unsigned int> >", ::ProofSummedVar<map<string,unsigned int> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<map<string,unsigned int> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<map<string,unsigned int> >) );
      instance.SetNew(&new_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<map<string,unsigned int> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<map<string,unsigned int> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,unsigned int> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,unsigned int> >*)0x0)->GetClass();
      ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEmaplEstringcOfloatgRsPgR_Dictionary();
   static void ProofSummedVarlEmaplEstringcOfloatgRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEmaplEstringcOfloatgRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *p);
   static void destruct_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<map<string,float> >*)
   {
      ::ProofSummedVar<map<string,float> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<map<string,float> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<map<string,float> >", ::ProofSummedVar<map<string,float> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<map<string,float> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEmaplEstringcOfloatgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<map<string,float> >) );
      instance.SetNew(&new_ProofSummedVarlEmaplEstringcOfloatgRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEmaplEstringcOfloatgRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEmaplEstringcOfloatgRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEmaplEstringcOfloatgRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEmaplEstringcOfloatgRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEmaplEstringcOfloatgRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<map<string,float> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<map<string,float> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,float> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEmaplEstringcOfloatgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,float> >*)0x0)->GetClass();
      ProofSummedVarlEmaplEstringcOfloatgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEmaplEstringcOfloatgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ProofSummedVarlEmaplEstringcOdoublegRsPgR_Dictionary();
   static void ProofSummedVarlEmaplEstringcOdoublegRsPgR_TClassManip(TClass*);
   static void *new_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *p = 0);
   static void *newArray_ProofSummedVarlEmaplEstringcOdoublegRsPgR(Long_t size, void *p);
   static void delete_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *p);
   static void deleteArray_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *p);
   static void destruct_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *p);
   static Long64_t merge_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ProofSummedVar<map<string,double> >*)
   {
      ::ProofSummedVar<map<string,double> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ProofSummedVar<map<string,double> > >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ProofSummedVar<map<string,double> >", ::ProofSummedVar<map<string,double> >::Class_Version(), "include/SSummedVar.h", 44,
                  typeid(::ProofSummedVar<map<string,double> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ProofSummedVarlEmaplEstringcOdoublegRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(::ProofSummedVar<map<string,double> >) );
      instance.SetNew(&new_ProofSummedVarlEmaplEstringcOdoublegRsPgR);
      instance.SetNewArray(&newArray_ProofSummedVarlEmaplEstringcOdoublegRsPgR);
      instance.SetDelete(&delete_ProofSummedVarlEmaplEstringcOdoublegRsPgR);
      instance.SetDeleteArray(&deleteArray_ProofSummedVarlEmaplEstringcOdoublegRsPgR);
      instance.SetDestructor(&destruct_ProofSummedVarlEmaplEstringcOdoublegRsPgR);
      instance.SetMerge(&merge_ProofSummedVarlEmaplEstringcOdoublegRsPgR);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ProofSummedVar<map<string,double> >*)
   {
      return GenerateInitInstanceLocal((::ProofSummedVar<map<string,double> >*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,double> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ProofSummedVarlEmaplEstringcOdoublegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,double> >*)0x0)->GetClass();
      ProofSummedVarlEmaplEstringcOdoublegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ProofSummedVarlEmaplEstringcOdoublegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *SH1lEfloatgR_Dictionary();
   static void SH1lEfloatgR_TClassManip(TClass*);
   static void *new_SH1lEfloatgR(void *p = 0);
   static void *newArray_SH1lEfloatgR(Long_t size, void *p);
   static void delete_SH1lEfloatgR(void *p);
   static void deleteArray_SH1lEfloatgR(void *p);
   static void destruct_SH1lEfloatgR(void *p);
   static Long64_t merge_SH1lEfloatgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SH1<float>*)
   {
      ::SH1<float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SH1<float> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SH1<float>", ::SH1<float>::Class_Version(), "include/SH1.h", 52,
                  typeid(::SH1<float>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &SH1lEfloatgR_Dictionary, isa_proxy, 4,
                  sizeof(::SH1<float>) );
      instance.SetNew(&new_SH1lEfloatgR);
      instance.SetNewArray(&newArray_SH1lEfloatgR);
      instance.SetDelete(&delete_SH1lEfloatgR);
      instance.SetDeleteArray(&deleteArray_SH1lEfloatgR);
      instance.SetDestructor(&destruct_SH1lEfloatgR);
      instance.SetMerge(&merge_SH1lEfloatgR);

      ::ROOT::AddClassAlternate("SH1<float>","SH1F");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SH1<float>*)
   {
      return GenerateInitInstanceLocal((::SH1<float>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SH1<float>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *SH1lEfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::SH1<float>*)0x0)->GetClass();
      SH1lEfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void SH1lEfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *SH1lEdoublegR_Dictionary();
   static void SH1lEdoublegR_TClassManip(TClass*);
   static void *new_SH1lEdoublegR(void *p = 0);
   static void *newArray_SH1lEdoublegR(Long_t size, void *p);
   static void delete_SH1lEdoublegR(void *p);
   static void deleteArray_SH1lEdoublegR(void *p);
   static void destruct_SH1lEdoublegR(void *p);
   static Long64_t merge_SH1lEdoublegR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SH1<double>*)
   {
      ::SH1<double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SH1<double> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SH1<double>", ::SH1<double>::Class_Version(), "include/SH1.h", 52,
                  typeid(::SH1<double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &SH1lEdoublegR_Dictionary, isa_proxy, 4,
                  sizeof(::SH1<double>) );
      instance.SetNew(&new_SH1lEdoublegR);
      instance.SetNewArray(&newArray_SH1lEdoublegR);
      instance.SetDelete(&delete_SH1lEdoublegR);
      instance.SetDeleteArray(&deleteArray_SH1lEdoublegR);
      instance.SetDestructor(&destruct_SH1lEdoublegR);
      instance.SetMerge(&merge_SH1lEdoublegR);

      ::ROOT::AddClassAlternate("SH1<double>","SH1D");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SH1<double>*)
   {
      return GenerateInitInstanceLocal((::SH1<double>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SH1<double>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *SH1lEdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::SH1<double>*)0x0)->GetClass();
      SH1lEdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void SH1lEdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *SH1lEintgR_Dictionary();
   static void SH1lEintgR_TClassManip(TClass*);
   static void *new_SH1lEintgR(void *p = 0);
   static void *newArray_SH1lEintgR(Long_t size, void *p);
   static void delete_SH1lEintgR(void *p);
   static void deleteArray_SH1lEintgR(void *p);
   static void destruct_SH1lEintgR(void *p);
   static Long64_t merge_SH1lEintgR(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SH1<int>*)
   {
      ::SH1<int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SH1<int> >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SH1<int>", ::SH1<int>::Class_Version(), "include/SH1.h", 52,
                  typeid(::SH1<int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &SH1lEintgR_Dictionary, isa_proxy, 4,
                  sizeof(::SH1<int>) );
      instance.SetNew(&new_SH1lEintgR);
      instance.SetNewArray(&newArray_SH1lEintgR);
      instance.SetDelete(&delete_SH1lEintgR);
      instance.SetDeleteArray(&deleteArray_SH1lEintgR);
      instance.SetDestructor(&destruct_SH1lEintgR);
      instance.SetMerge(&merge_SH1lEintgR);

      ::ROOT::AddClassAlternate("SH1<int>","SH1I");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SH1<int>*)
   {
      return GenerateInitInstanceLocal((::SH1<int>*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SH1<int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *SH1lEintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::SH1<int>*)0x0)->GetClass();
      SH1lEintgR_TClassManip(theClass);
   return theClass;
   }

   static void SH1lEintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

//______________________________________________________________________________
atomic_TClass_ptr SParticle::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SParticle::Class_Name()
{
   return "SParticle";
}

//______________________________________________________________________________
const char *SParticle::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SParticle*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SParticle::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SParticle*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SParticle::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SParticle*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SParticle::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SParticle*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<short>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<short>::Class_Name()
{
   return "ProofSummedVar<short>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<short>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<short>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<short>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<short>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<short>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<short>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<short>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<short>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<unsigned short>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<unsigned short>::Class_Name()
{
   return "ProofSummedVar<unsigned short>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<unsigned short>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned short>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<unsigned short>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned short>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<unsigned short>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned short>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<unsigned short>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned short>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<int>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<int>::Class_Name()
{
   return "ProofSummedVar<int>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<int>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<int>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<int>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<int>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<int>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<int>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<int>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<int>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<unsigned int>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<unsigned int>::Class_Name()
{
   return "ProofSummedVar<unsigned int>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<unsigned int>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned int>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<unsigned int>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned int>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<unsigned int>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned int>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<unsigned int>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned int>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<long>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<long>::Class_Name()
{
   return "ProofSummedVar<long>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<long>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<long>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<long>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<long>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<long>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<long>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<long>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<long>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<unsigned long>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<unsigned long>::Class_Name()
{
   return "ProofSummedVar<unsigned long>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<unsigned long>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned long>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<unsigned long>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned long>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<unsigned long>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned long>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<unsigned long>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<unsigned long>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<Long64_t>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<Long64_t>::Class_Name()
{
   return "ProofSummedVar<Long64_t>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<Long64_t>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<Long64_t>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<Long64_t>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<Long64_t>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<Long64_t>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<Long64_t>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<Long64_t>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<Long64_t>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<ULong64_t>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<ULong64_t>::Class_Name()
{
   return "ProofSummedVar<ULong64_t>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<ULong64_t>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<ULong64_t>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<ULong64_t>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<ULong64_t>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<ULong64_t>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<ULong64_t>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<ULong64_t>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<ULong64_t>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<float>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<float>::Class_Name()
{
   return "ProofSummedVar<float>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<float>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<float>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<float>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<float>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<float>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<float>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<float>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<float>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<double>::Class_Name()
{
   return "ProofSummedVar<double>";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<short> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<short> >::Class_Name()
{
   return "ProofSummedVar<vector<short> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<short> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<short> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<short> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<short> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<short> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<short> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<short> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<short> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<unsigned short> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<unsigned short> >::Class_Name()
{
   return "ProofSummedVar<vector<unsigned short> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<unsigned short> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned short> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<unsigned short> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned short> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<unsigned short> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned short> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<unsigned short> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned short> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<int> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<int> >::Class_Name()
{
   return "ProofSummedVar<vector<int> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<int> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<int> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<int> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<int> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<int> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<int> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<int> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<int> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<unsigned int> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<unsigned int> >::Class_Name()
{
   return "ProofSummedVar<vector<unsigned int> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<unsigned int> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned int> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<unsigned int> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned int> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<unsigned int> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned int> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<unsigned int> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned int> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<long> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<long> >::Class_Name()
{
   return "ProofSummedVar<vector<long> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<long> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<long> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<long> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<long> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<long> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<long> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<long> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<long> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<unsigned long> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<unsigned long> >::Class_Name()
{
   return "ProofSummedVar<vector<unsigned long> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<unsigned long> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned long> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<unsigned long> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned long> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<unsigned long> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned long> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<unsigned long> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<unsigned long> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<Long64_t> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<Long64_t> >::Class_Name()
{
   return "ProofSummedVar<vector<Long64_t> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<Long64_t> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<Long64_t> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<Long64_t> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<Long64_t> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<Long64_t> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<Long64_t> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<Long64_t> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<Long64_t> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<ULong64_t> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<ULong64_t> >::Class_Name()
{
   return "ProofSummedVar<vector<ULong64_t> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<ULong64_t> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<ULong64_t> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<ULong64_t> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<ULong64_t> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<ULong64_t> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<ULong64_t> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<ULong64_t> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<ULong64_t> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<float> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<float> >::Class_Name()
{
   return "ProofSummedVar<vector<float> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<float> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<float> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<float> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<float> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<float> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<float> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<float> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<float> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<vector<double> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<double> >::Class_Name()
{
   return "ProofSummedVar<vector<double> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<vector<double> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<double> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<vector<double> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<double> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<double> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<double> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<vector<double> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<vector<double> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<map<string,int> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<map<string,int> >::Class_Name()
{
   return "ProofSummedVar<map<string,int> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<map<string,int> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,int> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<map<string,int> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,int> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<map<string,int> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,int> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<map<string,int> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,int> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<map<string,unsigned int> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<map<string,unsigned int> >::Class_Name()
{
   return "ProofSummedVar<map<string,unsigned int> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<map<string,unsigned int> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,unsigned int> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<map<string,unsigned int> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,unsigned int> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<map<string,unsigned int> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,unsigned int> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<map<string,unsigned int> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,unsigned int> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<map<string,float> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<map<string,float> >::Class_Name()
{
   return "ProofSummedVar<map<string,float> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<map<string,float> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,float> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<map<string,float> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,float> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<map<string,float> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,float> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<map<string,float> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,float> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr ProofSummedVar<map<string,double> >::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *ProofSummedVar<map<string,double> >::Class_Name()
{
   return "ProofSummedVar<map<string,double> >";
}

//______________________________________________________________________________
template <> const char *ProofSummedVar<map<string,double> >::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,double> >*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int ProofSummedVar<map<string,double> >::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,double> >*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<map<string,double> >::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,double> >*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *ProofSummedVar<map<string,double> >::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ProofSummedVar<map<string,double> >*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr SH1<float>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *SH1<float>::Class_Name()
{
   return "SH1<float>";
}

//______________________________________________________________________________
template <> const char *SH1<float>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SH1<float>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int SH1<float>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SH1<float>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *SH1<float>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SH1<float>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *SH1<float>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SH1<float>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr SH1<double>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *SH1<double>::Class_Name()
{
   return "SH1<double>";
}

//______________________________________________________________________________
template <> const char *SH1<double>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SH1<double>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int SH1<double>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SH1<double>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *SH1<double>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SH1<double>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *SH1<double>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SH1<double>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
template <> atomic_TClass_ptr SH1<int>::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
template <> const char *SH1<int>::Class_Name()
{
   return "SH1<int>";
}

//______________________________________________________________________________
template <> const char *SH1<int>::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SH1<int>*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
template <> int SH1<int>::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SH1<int>*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
template <> TClass *SH1<int>::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SH1<int>*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
template <> TClass *SH1<int>::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SH1<int>*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
void SParticle::Streamer(TBuffer &R__b)
{
   // Stream an object of class SParticle.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SParticle::Class(),this);
   } else {
      R__b.WriteClassBuffer(SParticle::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SParticle(void *p) {
      return  p ? new(p) ::SParticle : new ::SParticle;
   }
   static void *newArray_SParticle(Long_t nElements, void *p) {
      return p ? new(p) ::SParticle[nElements] : new ::SParticle[nElements];
   }
   // Wrapper around operator delete
   static void delete_SParticle(void *p) {
      delete ((::SParticle*)p);
   }
   static void deleteArray_SParticle(void *p) {
      delete [] ((::SParticle*)p);
   }
   static void destruct_SParticle(void *p) {
      typedef ::SParticle current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SParticle

//______________________________________________________________________________
template <> void ProofSummedVar<short>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<short>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<short>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<short>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEshortgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<short> : new ::ProofSummedVar<short>;
   }
   static void *newArray_ProofSummedVarlEshortgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<short>[nElements] : new ::ProofSummedVar<short>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEshortgR(void *p) {
      delete ((::ProofSummedVar<short>*)p);
   }
   static void deleteArray_ProofSummedVarlEshortgR(void *p) {
      delete [] ((::ProofSummedVar<short>*)p);
   }
   static void destruct_ProofSummedVarlEshortgR(void *p) {
      typedef ::ProofSummedVar<short> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEshortgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<short>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<short>

//______________________________________________________________________________
template <> void ProofSummedVar<unsigned short>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<unsigned short>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<unsigned short>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<unsigned short>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEunsignedsPshortgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<unsigned short> : new ::ProofSummedVar<unsigned short>;
   }
   static void *newArray_ProofSummedVarlEunsignedsPshortgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<unsigned short>[nElements] : new ::ProofSummedVar<unsigned short>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEunsignedsPshortgR(void *p) {
      delete ((::ProofSummedVar<unsigned short>*)p);
   }
   static void deleteArray_ProofSummedVarlEunsignedsPshortgR(void *p) {
      delete [] ((::ProofSummedVar<unsigned short>*)p);
   }
   static void destruct_ProofSummedVarlEunsignedsPshortgR(void *p) {
      typedef ::ProofSummedVar<unsigned short> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEunsignedsPshortgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<unsigned short>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<unsigned short>

//______________________________________________________________________________
template <> void ProofSummedVar<int>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<int>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<int>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<int>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEintgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<int> : new ::ProofSummedVar<int>;
   }
   static void *newArray_ProofSummedVarlEintgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<int>[nElements] : new ::ProofSummedVar<int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEintgR(void *p) {
      delete ((::ProofSummedVar<int>*)p);
   }
   static void deleteArray_ProofSummedVarlEintgR(void *p) {
      delete [] ((::ProofSummedVar<int>*)p);
   }
   static void destruct_ProofSummedVarlEintgR(void *p) {
      typedef ::ProofSummedVar<int> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEintgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<int>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<int>

//______________________________________________________________________________
template <> void ProofSummedVar<unsigned int>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<unsigned int>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<unsigned int>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<unsigned int>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEunsignedsPintgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<unsigned int> : new ::ProofSummedVar<unsigned int>;
   }
   static void *newArray_ProofSummedVarlEunsignedsPintgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<unsigned int>[nElements] : new ::ProofSummedVar<unsigned int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEunsignedsPintgR(void *p) {
      delete ((::ProofSummedVar<unsigned int>*)p);
   }
   static void deleteArray_ProofSummedVarlEunsignedsPintgR(void *p) {
      delete [] ((::ProofSummedVar<unsigned int>*)p);
   }
   static void destruct_ProofSummedVarlEunsignedsPintgR(void *p) {
      typedef ::ProofSummedVar<unsigned int> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEunsignedsPintgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<unsigned int>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<unsigned int>

//______________________________________________________________________________
template <> void ProofSummedVar<long>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<long>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<long>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<long>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlElonggR(void *p) {
      return  p ? new(p) ::ProofSummedVar<long> : new ::ProofSummedVar<long>;
   }
   static void *newArray_ProofSummedVarlElonggR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<long>[nElements] : new ::ProofSummedVar<long>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlElonggR(void *p) {
      delete ((::ProofSummedVar<long>*)p);
   }
   static void deleteArray_ProofSummedVarlElonggR(void *p) {
      delete [] ((::ProofSummedVar<long>*)p);
   }
   static void destruct_ProofSummedVarlElonggR(void *p) {
      typedef ::ProofSummedVar<long> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlElonggR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<long>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<long>

//______________________________________________________________________________
template <> void ProofSummedVar<unsigned long>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<unsigned long>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<unsigned long>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<unsigned long>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEunsignedsPlonggR(void *p) {
      return  p ? new(p) ::ProofSummedVar<unsigned long> : new ::ProofSummedVar<unsigned long>;
   }
   static void *newArray_ProofSummedVarlEunsignedsPlonggR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<unsigned long>[nElements] : new ::ProofSummedVar<unsigned long>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEunsignedsPlonggR(void *p) {
      delete ((::ProofSummedVar<unsigned long>*)p);
   }
   static void deleteArray_ProofSummedVarlEunsignedsPlonggR(void *p) {
      delete [] ((::ProofSummedVar<unsigned long>*)p);
   }
   static void destruct_ProofSummedVarlEunsignedsPlonggR(void *p) {
      typedef ::ProofSummedVar<unsigned long> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEunsignedsPlonggR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<unsigned long>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<unsigned long>

//______________________________________________________________________________
template <> void ProofSummedVar<Long64_t>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<Long64_t>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<Long64_t>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<Long64_t>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlELong64_tgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<Long64_t> : new ::ProofSummedVar<Long64_t>;
   }
   static void *newArray_ProofSummedVarlELong64_tgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<Long64_t>[nElements] : new ::ProofSummedVar<Long64_t>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlELong64_tgR(void *p) {
      delete ((::ProofSummedVar<Long64_t>*)p);
   }
   static void deleteArray_ProofSummedVarlELong64_tgR(void *p) {
      delete [] ((::ProofSummedVar<Long64_t>*)p);
   }
   static void destruct_ProofSummedVarlELong64_tgR(void *p) {
      typedef ::ProofSummedVar<Long64_t> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlELong64_tgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<Long64_t>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<Long64_t>

//______________________________________________________________________________
template <> void ProofSummedVar<ULong64_t>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<ULong64_t>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<ULong64_t>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<ULong64_t>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEULong64_tgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<ULong64_t> : new ::ProofSummedVar<ULong64_t>;
   }
   static void *newArray_ProofSummedVarlEULong64_tgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<ULong64_t>[nElements] : new ::ProofSummedVar<ULong64_t>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEULong64_tgR(void *p) {
      delete ((::ProofSummedVar<ULong64_t>*)p);
   }
   static void deleteArray_ProofSummedVarlEULong64_tgR(void *p) {
      delete [] ((::ProofSummedVar<ULong64_t>*)p);
   }
   static void destruct_ProofSummedVarlEULong64_tgR(void *p) {
      typedef ::ProofSummedVar<ULong64_t> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEULong64_tgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<ULong64_t>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<ULong64_t>

//______________________________________________________________________________
template <> void ProofSummedVar<float>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<float>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<float>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<float>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEfloatgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<float> : new ::ProofSummedVar<float>;
   }
   static void *newArray_ProofSummedVarlEfloatgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<float>[nElements] : new ::ProofSummedVar<float>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEfloatgR(void *p) {
      delete ((::ProofSummedVar<float>*)p);
   }
   static void deleteArray_ProofSummedVarlEfloatgR(void *p) {
      delete [] ((::ProofSummedVar<float>*)p);
   }
   static void destruct_ProofSummedVarlEfloatgR(void *p) {
      typedef ::ProofSummedVar<float> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEfloatgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<float>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<float>

//______________________________________________________________________________
template <> void ProofSummedVar<double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<double>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEdoublegR(void *p) {
      return  p ? new(p) ::ProofSummedVar<double> : new ::ProofSummedVar<double>;
   }
   static void *newArray_ProofSummedVarlEdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<double>[nElements] : new ::ProofSummedVar<double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEdoublegR(void *p) {
      delete ((::ProofSummedVar<double>*)p);
   }
   static void deleteArray_ProofSummedVarlEdoublegR(void *p) {
      delete [] ((::ProofSummedVar<double>*)p);
   }
   static void destruct_ProofSummedVarlEdoublegR(void *p) {
      typedef ::ProofSummedVar<double> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEdoublegR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<double>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<double>

//______________________________________________________________________________
template <> void ProofSummedVar<vector<short> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<short> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<short> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<short> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlEshortgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<short> > : new ::ProofSummedVar<vector<short> >;
   }
   static void *newArray_ProofSummedVarlEvectorlEshortgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<short> >[nElements] : new ::ProofSummedVar<vector<short> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlEshortgRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<short> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlEshortgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<short> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlEshortgRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<short> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlEshortgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<short> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<short> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<unsigned short> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<unsigned short> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<unsigned short> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<unsigned short> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<unsigned short> > : new ::ProofSummedVar<vector<unsigned short> >;
   }
   static void *newArray_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<unsigned short> >[nElements] : new ::ProofSummedVar<vector<unsigned short> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<unsigned short> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<unsigned short> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<unsigned short> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlEunsignedsPshortgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<unsigned short> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<unsigned short> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<int> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<int> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<int> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<int> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlEintgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<int> > : new ::ProofSummedVar<vector<int> >;
   }
   static void *newArray_ProofSummedVarlEvectorlEintgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<int> >[nElements] : new ::ProofSummedVar<vector<int> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlEintgRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<int> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlEintgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<int> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlEintgRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<int> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlEintgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<int> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<int> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<unsigned int> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<unsigned int> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<unsigned int> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<unsigned int> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<unsigned int> > : new ::ProofSummedVar<vector<unsigned int> >;
   }
   static void *newArray_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<unsigned int> >[nElements] : new ::ProofSummedVar<vector<unsigned int> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<unsigned int> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<unsigned int> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<unsigned int> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlEunsignedsPintgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<unsigned int> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<unsigned int> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<long> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<long> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<long> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<long> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlElonggRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<long> > : new ::ProofSummedVar<vector<long> >;
   }
   static void *newArray_ProofSummedVarlEvectorlElonggRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<long> >[nElements] : new ::ProofSummedVar<vector<long> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlElonggRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<long> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlElonggRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<long> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlElonggRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<long> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlElonggRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<long> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<long> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<unsigned long> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<unsigned long> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<unsigned long> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<unsigned long> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<unsigned long> > : new ::ProofSummedVar<vector<unsigned long> >;
   }
   static void *newArray_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<unsigned long> >[nElements] : new ::ProofSummedVar<vector<unsigned long> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<unsigned long> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<unsigned long> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<unsigned long> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlEunsignedsPlonggRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<unsigned long> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<unsigned long> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<Long64_t> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<Long64_t> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<Long64_t> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<Long64_t> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlELong64_tgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<Long64_t> > : new ::ProofSummedVar<vector<Long64_t> >;
   }
   static void *newArray_ProofSummedVarlEvectorlELong64_tgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<Long64_t> >[nElements] : new ::ProofSummedVar<vector<Long64_t> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlELong64_tgRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<Long64_t> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlELong64_tgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<Long64_t> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlELong64_tgRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<Long64_t> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlELong64_tgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<Long64_t> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<Long64_t> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<ULong64_t> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<ULong64_t> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<ULong64_t> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<ULong64_t> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<ULong64_t> > : new ::ProofSummedVar<vector<ULong64_t> >;
   }
   static void *newArray_ProofSummedVarlEvectorlEULong64_tgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<ULong64_t> >[nElements] : new ::ProofSummedVar<vector<ULong64_t> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<ULong64_t> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<ULong64_t> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<ULong64_t> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlEULong64_tgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<ULong64_t> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<ULong64_t> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<float> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<float> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<float> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<float> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlEfloatgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<float> > : new ::ProofSummedVar<vector<float> >;
   }
   static void *newArray_ProofSummedVarlEvectorlEfloatgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<float> >[nElements] : new ::ProofSummedVar<vector<float> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlEfloatgRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<float> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlEfloatgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<float> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlEfloatgRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<float> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlEfloatgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<float> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<float> >

//______________________________________________________________________________
template <> void ProofSummedVar<vector<double> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<vector<double> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<vector<double> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<vector<double> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEvectorlEdoublegRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<vector<double> > : new ::ProofSummedVar<vector<double> >;
   }
   static void *newArray_ProofSummedVarlEvectorlEdoublegRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<vector<double> >[nElements] : new ::ProofSummedVar<vector<double> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEvectorlEdoublegRsPgR(void *p) {
      delete ((::ProofSummedVar<vector<double> >*)p);
   }
   static void deleteArray_ProofSummedVarlEvectorlEdoublegRsPgR(void *p) {
      delete [] ((::ProofSummedVar<vector<double> >*)p);
   }
   static void destruct_ProofSummedVarlEvectorlEdoublegRsPgR(void *p) {
      typedef ::ProofSummedVar<vector<double> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEvectorlEdoublegRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<vector<double> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<vector<double> >

namespace ROOT {
   // Wrappers around operator new
   static void *new_pairlEstringcOunsignedsPintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) pair<string,unsigned int> : new pair<string,unsigned int>;
   }
   static void *newArray_pairlEstringcOunsignedsPintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) pair<string,unsigned int>[nElements] : new pair<string,unsigned int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_pairlEstringcOunsignedsPintgR(void *p) {
      delete ((pair<string,unsigned int>*)p);
   }
   static void deleteArray_pairlEstringcOunsignedsPintgR(void *p) {
      delete [] ((pair<string,unsigned int>*)p);
   }
   static void destruct_pairlEstringcOunsignedsPintgR(void *p) {
      typedef pair<string,unsigned int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class pair<string,unsigned int>

//______________________________________________________________________________
template <> void ProofSummedVar<map<string,int> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<map<string,int> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<map<string,int> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<map<string,int> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEmaplEstringcOintgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<map<string,int> > : new ::ProofSummedVar<map<string,int> >;
   }
   static void *newArray_ProofSummedVarlEmaplEstringcOintgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<map<string,int> >[nElements] : new ::ProofSummedVar<map<string,int> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEmaplEstringcOintgRsPgR(void *p) {
      delete ((::ProofSummedVar<map<string,int> >*)p);
   }
   static void deleteArray_ProofSummedVarlEmaplEstringcOintgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<map<string,int> >*)p);
   }
   static void destruct_ProofSummedVarlEmaplEstringcOintgRsPgR(void *p) {
      typedef ::ProofSummedVar<map<string,int> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEmaplEstringcOintgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<map<string,int> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<map<string,int> >

//______________________________________________________________________________
template <> void ProofSummedVar<map<string,unsigned int> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<map<string,unsigned int> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<map<string,unsigned int> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<map<string,unsigned int> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<map<string,unsigned int> > : new ::ProofSummedVar<map<string,unsigned int> >;
   }
   static void *newArray_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<map<string,unsigned int> >[nElements] : new ::ProofSummedVar<map<string,unsigned int> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *p) {
      delete ((::ProofSummedVar<map<string,unsigned int> >*)p);
   }
   static void deleteArray_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<map<string,unsigned int> >*)p);
   }
   static void destruct_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *p) {
      typedef ::ProofSummedVar<map<string,unsigned int> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEmaplEstringcOunsignedsPintgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<map<string,unsigned int> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<map<string,unsigned int> >

//______________________________________________________________________________
template <> void ProofSummedVar<map<string,float> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<map<string,float> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<map<string,float> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<map<string,float> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<map<string,float> > : new ::ProofSummedVar<map<string,float> >;
   }
   static void *newArray_ProofSummedVarlEmaplEstringcOfloatgRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<map<string,float> >[nElements] : new ::ProofSummedVar<map<string,float> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *p) {
      delete ((::ProofSummedVar<map<string,float> >*)p);
   }
   static void deleteArray_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *p) {
      delete [] ((::ProofSummedVar<map<string,float> >*)p);
   }
   static void destruct_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *p) {
      typedef ::ProofSummedVar<map<string,float> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEmaplEstringcOfloatgRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<map<string,float> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<map<string,float> >

//______________________________________________________________________________
template <> void ProofSummedVar<map<string,double> >::Streamer(TBuffer &R__b)
{
   // Stream an object of class ProofSummedVar<map<string,double> >.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ProofSummedVar<map<string,double> >::Class(),this);
   } else {
      R__b.WriteClassBuffer(ProofSummedVar<map<string,double> >::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *p) {
      return  p ? new(p) ::ProofSummedVar<map<string,double> > : new ::ProofSummedVar<map<string,double> >;
   }
   static void *newArray_ProofSummedVarlEmaplEstringcOdoublegRsPgR(Long_t nElements, void *p) {
      return p ? new(p) ::ProofSummedVar<map<string,double> >[nElements] : new ::ProofSummedVar<map<string,double> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *p) {
      delete ((::ProofSummedVar<map<string,double> >*)p);
   }
   static void deleteArray_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *p) {
      delete [] ((::ProofSummedVar<map<string,double> >*)p);
   }
   static void destruct_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *p) {
      typedef ::ProofSummedVar<map<string,double> > current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_ProofSummedVarlEmaplEstringcOdoublegRsPgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::ProofSummedVar<map<string,double> >*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::ProofSummedVar<map<string,double> >

//______________________________________________________________________________
template <> void SH1<float>::Streamer(TBuffer &R__b)
{
   // Stream an object of class SH1<float>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SH1<float>::Class(),this);
   } else {
      R__b.WriteClassBuffer(SH1<float>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SH1lEfloatgR(void *p) {
      return  p ? new(p) ::SH1<float> : new ::SH1<float>;
   }
   static void *newArray_SH1lEfloatgR(Long_t nElements, void *p) {
      return p ? new(p) ::SH1<float>[nElements] : new ::SH1<float>[nElements];
   }
   // Wrapper around operator delete
   static void delete_SH1lEfloatgR(void *p) {
      delete ((::SH1<float>*)p);
   }
   static void deleteArray_SH1lEfloatgR(void *p) {
      delete [] ((::SH1<float>*)p);
   }
   static void destruct_SH1lEfloatgR(void *p) {
      typedef ::SH1<float> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_SH1lEfloatgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::SH1<float>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::SH1<float>

//______________________________________________________________________________
template <> void SH1<double>::Streamer(TBuffer &R__b)
{
   // Stream an object of class SH1<double>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SH1<double>::Class(),this);
   } else {
      R__b.WriteClassBuffer(SH1<double>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SH1lEdoublegR(void *p) {
      return  p ? new(p) ::SH1<double> : new ::SH1<double>;
   }
   static void *newArray_SH1lEdoublegR(Long_t nElements, void *p) {
      return p ? new(p) ::SH1<double>[nElements] : new ::SH1<double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_SH1lEdoublegR(void *p) {
      delete ((::SH1<double>*)p);
   }
   static void deleteArray_SH1lEdoublegR(void *p) {
      delete [] ((::SH1<double>*)p);
   }
   static void destruct_SH1lEdoublegR(void *p) {
      typedef ::SH1<double> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_SH1lEdoublegR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::SH1<double>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::SH1<double>

//______________________________________________________________________________
template <> void SH1<int>::Streamer(TBuffer &R__b)
{
   // Stream an object of class SH1<int>.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SH1<int>::Class(),this);
   } else {
      R__b.WriteClassBuffer(SH1<int>::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SH1lEintgR(void *p) {
      return  p ? new(p) ::SH1<int> : new ::SH1<int>;
   }
   static void *newArray_SH1lEintgR(Long_t nElements, void *p) {
      return p ? new(p) ::SH1<int>[nElements] : new ::SH1<int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_SH1lEintgR(void *p) {
      delete ((::SH1<int>*)p);
   }
   static void deleteArray_SH1lEintgR(void *p) {
      delete [] ((::SH1<int>*)p);
   }
   static void destruct_SH1lEintgR(void *p) {
      typedef ::SH1<int> current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_SH1lEintgR(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::SH1<int>*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::SH1<int>

namespace ROOT {
   static TClass *vectorlEunsignedsPshortgR_Dictionary();
   static void vectorlEunsignedsPshortgR_TClassManip(TClass*);
   static void *new_vectorlEunsignedsPshortgR(void *p = 0);
   static void *newArray_vectorlEunsignedsPshortgR(Long_t size, void *p);
   static void delete_vectorlEunsignedsPshortgR(void *p);
   static void deleteArray_vectorlEunsignedsPshortgR(void *p);
   static void destruct_vectorlEunsignedsPshortgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<unsigned short>*)
   {
      vector<unsigned short> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<unsigned short>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<unsigned short>", -2, "vector", 214,
                  typeid(vector<unsigned short>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEunsignedsPshortgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<unsigned short>) );
      instance.SetNew(&new_vectorlEunsignedsPshortgR);
      instance.SetNewArray(&newArray_vectorlEunsignedsPshortgR);
      instance.SetDelete(&delete_vectorlEunsignedsPshortgR);
      instance.SetDeleteArray(&deleteArray_vectorlEunsignedsPshortgR);
      instance.SetDestructor(&destruct_vectorlEunsignedsPshortgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<unsigned short> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<unsigned short>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEunsignedsPshortgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<unsigned short>*)0x0)->GetClass();
      vectorlEunsignedsPshortgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEunsignedsPshortgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEunsignedsPshortgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<unsigned short> : new vector<unsigned short>;
   }
   static void *newArray_vectorlEunsignedsPshortgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<unsigned short>[nElements] : new vector<unsigned short>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEunsignedsPshortgR(void *p) {
      delete ((vector<unsigned short>*)p);
   }
   static void deleteArray_vectorlEunsignedsPshortgR(void *p) {
      delete [] ((vector<unsigned short>*)p);
   }
   static void destruct_vectorlEunsignedsPshortgR(void *p) {
      typedef vector<unsigned short> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<unsigned short>

namespace ROOT {
   static TClass *vectorlEunsignedsPlonggR_Dictionary();
   static void vectorlEunsignedsPlonggR_TClassManip(TClass*);
   static void *new_vectorlEunsignedsPlonggR(void *p = 0);
   static void *newArray_vectorlEunsignedsPlonggR(Long_t size, void *p);
   static void delete_vectorlEunsignedsPlonggR(void *p);
   static void deleteArray_vectorlEunsignedsPlonggR(void *p);
   static void destruct_vectorlEunsignedsPlonggR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<unsigned long>*)
   {
      vector<unsigned long> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<unsigned long>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<unsigned long>", -2, "vector", 214,
                  typeid(vector<unsigned long>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEunsignedsPlonggR_Dictionary, isa_proxy, 0,
                  sizeof(vector<unsigned long>) );
      instance.SetNew(&new_vectorlEunsignedsPlonggR);
      instance.SetNewArray(&newArray_vectorlEunsignedsPlonggR);
      instance.SetDelete(&delete_vectorlEunsignedsPlonggR);
      instance.SetDeleteArray(&deleteArray_vectorlEunsignedsPlonggR);
      instance.SetDestructor(&destruct_vectorlEunsignedsPlonggR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<unsigned long> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<unsigned long>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEunsignedsPlonggR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<unsigned long>*)0x0)->GetClass();
      vectorlEunsignedsPlonggR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEunsignedsPlonggR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEunsignedsPlonggR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<unsigned long> : new vector<unsigned long>;
   }
   static void *newArray_vectorlEunsignedsPlonggR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<unsigned long>[nElements] : new vector<unsigned long>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEunsignedsPlonggR(void *p) {
      delete ((vector<unsigned long>*)p);
   }
   static void deleteArray_vectorlEunsignedsPlonggR(void *p) {
      delete [] ((vector<unsigned long>*)p);
   }
   static void destruct_vectorlEunsignedsPlonggR(void *p) {
      typedef vector<unsigned long> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<unsigned long>

namespace ROOT {
   static TClass *vectorlEunsignedsPintgR_Dictionary();
   static void vectorlEunsignedsPintgR_TClassManip(TClass*);
   static void *new_vectorlEunsignedsPintgR(void *p = 0);
   static void *newArray_vectorlEunsignedsPintgR(Long_t size, void *p);
   static void delete_vectorlEunsignedsPintgR(void *p);
   static void deleteArray_vectorlEunsignedsPintgR(void *p);
   static void destruct_vectorlEunsignedsPintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<unsigned int>*)
   {
      vector<unsigned int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<unsigned int>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<unsigned int>", -2, "vector", 214,
                  typeid(vector<unsigned int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEunsignedsPintgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<unsigned int>) );
      instance.SetNew(&new_vectorlEunsignedsPintgR);
      instance.SetNewArray(&newArray_vectorlEunsignedsPintgR);
      instance.SetDelete(&delete_vectorlEunsignedsPintgR);
      instance.SetDeleteArray(&deleteArray_vectorlEunsignedsPintgR);
      instance.SetDestructor(&destruct_vectorlEunsignedsPintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<unsigned int> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<unsigned int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEunsignedsPintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<unsigned int>*)0x0)->GetClass();
      vectorlEunsignedsPintgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEunsignedsPintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEunsignedsPintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<unsigned int> : new vector<unsigned int>;
   }
   static void *newArray_vectorlEunsignedsPintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<unsigned int>[nElements] : new vector<unsigned int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEunsignedsPintgR(void *p) {
      delete ((vector<unsigned int>*)p);
   }
   static void deleteArray_vectorlEunsignedsPintgR(void *p) {
      delete [] ((vector<unsigned int>*)p);
   }
   static void destruct_vectorlEunsignedsPintgR(void *p) {
      typedef vector<unsigned int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<unsigned int>

namespace ROOT {
   static TClass *vectorlEshortgR_Dictionary();
   static void vectorlEshortgR_TClassManip(TClass*);
   static void *new_vectorlEshortgR(void *p = 0);
   static void *newArray_vectorlEshortgR(Long_t size, void *p);
   static void delete_vectorlEshortgR(void *p);
   static void deleteArray_vectorlEshortgR(void *p);
   static void destruct_vectorlEshortgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<short>*)
   {
      vector<short> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<short>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<short>", -2, "vector", 214,
                  typeid(vector<short>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEshortgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<short>) );
      instance.SetNew(&new_vectorlEshortgR);
      instance.SetNewArray(&newArray_vectorlEshortgR);
      instance.SetDelete(&delete_vectorlEshortgR);
      instance.SetDeleteArray(&deleteArray_vectorlEshortgR);
      instance.SetDestructor(&destruct_vectorlEshortgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<short> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<short>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEshortgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<short>*)0x0)->GetClass();
      vectorlEshortgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEshortgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEshortgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<short> : new vector<short>;
   }
   static void *newArray_vectorlEshortgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<short>[nElements] : new vector<short>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEshortgR(void *p) {
      delete ((vector<short>*)p);
   }
   static void deleteArray_vectorlEshortgR(void *p) {
      delete [] ((vector<short>*)p);
   }
   static void destruct_vectorlEshortgR(void *p) {
      typedef vector<short> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<short>

namespace ROOT {
   static TClass *vectorlElonggR_Dictionary();
   static void vectorlElonggR_TClassManip(TClass*);
   static void *new_vectorlElonggR(void *p = 0);
   static void *newArray_vectorlElonggR(Long_t size, void *p);
   static void delete_vectorlElonggR(void *p);
   static void deleteArray_vectorlElonggR(void *p);
   static void destruct_vectorlElonggR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<long>*)
   {
      vector<long> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<long>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<long>", -2, "vector", 214,
                  typeid(vector<long>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlElonggR_Dictionary, isa_proxy, 0,
                  sizeof(vector<long>) );
      instance.SetNew(&new_vectorlElonggR);
      instance.SetNewArray(&newArray_vectorlElonggR);
      instance.SetDelete(&delete_vectorlElonggR);
      instance.SetDeleteArray(&deleteArray_vectorlElonggR);
      instance.SetDestructor(&destruct_vectorlElonggR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<long> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<long>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlElonggR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<long>*)0x0)->GetClass();
      vectorlElonggR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlElonggR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlElonggR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<long> : new vector<long>;
   }
   static void *newArray_vectorlElonggR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<long>[nElements] : new vector<long>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlElonggR(void *p) {
      delete ((vector<long>*)p);
   }
   static void deleteArray_vectorlElonggR(void *p) {
      delete [] ((vector<long>*)p);
   }
   static void destruct_vectorlElonggR(void *p) {
      typedef vector<long> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<long>

namespace ROOT {
   static TClass *vectorlEintgR_Dictionary();
   static void vectorlEintgR_TClassManip(TClass*);
   static void *new_vectorlEintgR(void *p = 0);
   static void *newArray_vectorlEintgR(Long_t size, void *p);
   static void delete_vectorlEintgR(void *p);
   static void deleteArray_vectorlEintgR(void *p);
   static void destruct_vectorlEintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<int>*)
   {
      vector<int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<int>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<int>", -2, "vector", 214,
                  typeid(vector<int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEintgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<int>) );
      instance.SetNew(&new_vectorlEintgR);
      instance.SetNewArray(&newArray_vectorlEintgR);
      instance.SetDelete(&delete_vectorlEintgR);
      instance.SetDeleteArray(&deleteArray_vectorlEintgR);
      instance.SetDestructor(&destruct_vectorlEintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<int> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<int>*)0x0)->GetClass();
      vectorlEintgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<int> : new vector<int>;
   }
   static void *newArray_vectorlEintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<int>[nElements] : new vector<int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEintgR(void *p) {
      delete ((vector<int>*)p);
   }
   static void deleteArray_vectorlEintgR(void *p) {
      delete [] ((vector<int>*)p);
   }
   static void destruct_vectorlEintgR(void *p) {
      typedef vector<int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<int>

namespace ROOT {
   static TClass *vectorlEfloatgR_Dictionary();
   static void vectorlEfloatgR_TClassManip(TClass*);
   static void *new_vectorlEfloatgR(void *p = 0);
   static void *newArray_vectorlEfloatgR(Long_t size, void *p);
   static void delete_vectorlEfloatgR(void *p);
   static void deleteArray_vectorlEfloatgR(void *p);
   static void destruct_vectorlEfloatgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<float>*)
   {
      vector<float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<float>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<float>", -2, "vector", 214,
                  typeid(vector<float>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEfloatgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<float>) );
      instance.SetNew(&new_vectorlEfloatgR);
      instance.SetNewArray(&newArray_vectorlEfloatgR);
      instance.SetDelete(&delete_vectorlEfloatgR);
      instance.SetDeleteArray(&deleteArray_vectorlEfloatgR);
      instance.SetDestructor(&destruct_vectorlEfloatgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<float> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<float>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<float>*)0x0)->GetClass();
      vectorlEfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEfloatgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<float> : new vector<float>;
   }
   static void *newArray_vectorlEfloatgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<float>[nElements] : new vector<float>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEfloatgR(void *p) {
      delete ((vector<float>*)p);
   }
   static void deleteArray_vectorlEfloatgR(void *p) {
      delete [] ((vector<float>*)p);
   }
   static void destruct_vectorlEfloatgR(void *p) {
      typedef vector<float> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<float>

namespace ROOT {
   static TClass *vectorlEdoublegR_Dictionary();
   static void vectorlEdoublegR_TClassManip(TClass*);
   static void *new_vectorlEdoublegR(void *p = 0);
   static void *newArray_vectorlEdoublegR(Long_t size, void *p);
   static void delete_vectorlEdoublegR(void *p);
   static void deleteArray_vectorlEdoublegR(void *p);
   static void destruct_vectorlEdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<double>*)
   {
      vector<double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<double>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<double>", -2, "vector", 214,
                  typeid(vector<double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEdoublegR_Dictionary, isa_proxy, 0,
                  sizeof(vector<double>) );
      instance.SetNew(&new_vectorlEdoublegR);
      instance.SetNewArray(&newArray_vectorlEdoublegR);
      instance.SetDelete(&delete_vectorlEdoublegR);
      instance.SetDeleteArray(&deleteArray_vectorlEdoublegR);
      instance.SetDestructor(&destruct_vectorlEdoublegR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<double> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<double>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<double>*)0x0)->GetClass();
      vectorlEdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEdoublegR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<double> : new vector<double>;
   }
   static void *newArray_vectorlEdoublegR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<double>[nElements] : new vector<double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEdoublegR(void *p) {
      delete ((vector<double>*)p);
   }
   static void deleteArray_vectorlEdoublegR(void *p) {
      delete [] ((vector<double>*)p);
   }
   static void destruct_vectorlEdoublegR(void *p) {
      typedef vector<double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<double>

namespace ROOT {
   static TClass *vectorlEULong64_tgR_Dictionary();
   static void vectorlEULong64_tgR_TClassManip(TClass*);
   static void *new_vectorlEULong64_tgR(void *p = 0);
   static void *newArray_vectorlEULong64_tgR(Long_t size, void *p);
   static void delete_vectorlEULong64_tgR(void *p);
   static void deleteArray_vectorlEULong64_tgR(void *p);
   static void destruct_vectorlEULong64_tgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<ULong64_t>*)
   {
      vector<ULong64_t> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<ULong64_t>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<ULong64_t>", -2, "vector", 214,
                  typeid(vector<ULong64_t>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEULong64_tgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<ULong64_t>) );
      instance.SetNew(&new_vectorlEULong64_tgR);
      instance.SetNewArray(&newArray_vectorlEULong64_tgR);
      instance.SetDelete(&delete_vectorlEULong64_tgR);
      instance.SetDeleteArray(&deleteArray_vectorlEULong64_tgR);
      instance.SetDestructor(&destruct_vectorlEULong64_tgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<ULong64_t> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<ULong64_t>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEULong64_tgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<ULong64_t>*)0x0)->GetClass();
      vectorlEULong64_tgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEULong64_tgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEULong64_tgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<ULong64_t> : new vector<ULong64_t>;
   }
   static void *newArray_vectorlEULong64_tgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<ULong64_t>[nElements] : new vector<ULong64_t>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEULong64_tgR(void *p) {
      delete ((vector<ULong64_t>*)p);
   }
   static void deleteArray_vectorlEULong64_tgR(void *p) {
      delete [] ((vector<ULong64_t>*)p);
   }
   static void destruct_vectorlEULong64_tgR(void *p) {
      typedef vector<ULong64_t> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<ULong64_t>

namespace ROOT {
   static TClass *vectorlESParticlegR_Dictionary();
   static void vectorlESParticlegR_TClassManip(TClass*);
   static void *new_vectorlESParticlegR(void *p = 0);
   static void *newArray_vectorlESParticlegR(Long_t size, void *p);
   static void delete_vectorlESParticlegR(void *p);
   static void deleteArray_vectorlESParticlegR(void *p);
   static void destruct_vectorlESParticlegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<SParticle>*)
   {
      vector<SParticle> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<SParticle>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<SParticle>", -2, "vector", 214,
                  typeid(vector<SParticle>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlESParticlegR_Dictionary, isa_proxy, 4,
                  sizeof(vector<SParticle>) );
      instance.SetNew(&new_vectorlESParticlegR);
      instance.SetNewArray(&newArray_vectorlESParticlegR);
      instance.SetDelete(&delete_vectorlESParticlegR);
      instance.SetDeleteArray(&deleteArray_vectorlESParticlegR);
      instance.SetDestructor(&destruct_vectorlESParticlegR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<SParticle> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<SParticle>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlESParticlegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<SParticle>*)0x0)->GetClass();
      vectorlESParticlegR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlESParticlegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlESParticlegR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SParticle> : new vector<SParticle>;
   }
   static void *newArray_vectorlESParticlegR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SParticle>[nElements] : new vector<SParticle>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlESParticlegR(void *p) {
      delete ((vector<SParticle>*)p);
   }
   static void deleteArray_vectorlESParticlegR(void *p) {
      delete [] ((vector<SParticle>*)p);
   }
   static void destruct_vectorlESParticlegR(void *p) {
      typedef vector<SParticle> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<SParticle>

namespace ROOT {
   static TClass *vectorlELong64_tgR_Dictionary();
   static void vectorlELong64_tgR_TClassManip(TClass*);
   static void *new_vectorlELong64_tgR(void *p = 0);
   static void *newArray_vectorlELong64_tgR(Long_t size, void *p);
   static void delete_vectorlELong64_tgR(void *p);
   static void deleteArray_vectorlELong64_tgR(void *p);
   static void destruct_vectorlELong64_tgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<Long64_t>*)
   {
      vector<Long64_t> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<Long64_t>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<Long64_t>", -2, "vector", 214,
                  typeid(vector<Long64_t>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlELong64_tgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<Long64_t>) );
      instance.SetNew(&new_vectorlELong64_tgR);
      instance.SetNewArray(&newArray_vectorlELong64_tgR);
      instance.SetDelete(&delete_vectorlELong64_tgR);
      instance.SetDeleteArray(&deleteArray_vectorlELong64_tgR);
      instance.SetDestructor(&destruct_vectorlELong64_tgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<Long64_t> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<Long64_t>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlELong64_tgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<Long64_t>*)0x0)->GetClass();
      vectorlELong64_tgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlELong64_tgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlELong64_tgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<Long64_t> : new vector<Long64_t>;
   }
   static void *newArray_vectorlELong64_tgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<Long64_t>[nElements] : new vector<Long64_t>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlELong64_tgR(void *p) {
      delete ((vector<Long64_t>*)p);
   }
   static void deleteArray_vectorlELong64_tgR(void *p) {
      delete [] ((vector<Long64_t>*)p);
   }
   static void destruct_vectorlELong64_tgR(void *p) {
      typedef vector<Long64_t> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<Long64_t>

namespace ROOT {
   static TClass *maplEstringcOunsignedsPintgR_Dictionary();
   static void maplEstringcOunsignedsPintgR_TClassManip(TClass*);
   static void *new_maplEstringcOunsignedsPintgR(void *p = 0);
   static void *newArray_maplEstringcOunsignedsPintgR(Long_t size, void *p);
   static void delete_maplEstringcOunsignedsPintgR(void *p);
   static void deleteArray_maplEstringcOunsignedsPintgR(void *p);
   static void destruct_maplEstringcOunsignedsPintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<string,unsigned int>*)
   {
      map<string,unsigned int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<string,unsigned int>));
      static ::ROOT::TGenericClassInfo 
         instance("map<string,unsigned int>", -2, "map", 96,
                  typeid(map<string,unsigned int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEstringcOunsignedsPintgR_Dictionary, isa_proxy, 4,
                  sizeof(map<string,unsigned int>) );
      instance.SetNew(&new_maplEstringcOunsignedsPintgR);
      instance.SetNewArray(&newArray_maplEstringcOunsignedsPintgR);
      instance.SetDelete(&delete_maplEstringcOunsignedsPintgR);
      instance.SetDeleteArray(&deleteArray_maplEstringcOunsignedsPintgR);
      instance.SetDestructor(&destruct_maplEstringcOunsignedsPintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<string,unsigned int> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const map<string,unsigned int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEstringcOunsignedsPintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<string,unsigned int>*)0x0)->GetClass();
      maplEstringcOunsignedsPintgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEstringcOunsignedsPintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEstringcOunsignedsPintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<string,unsigned int> : new map<string,unsigned int>;
   }
   static void *newArray_maplEstringcOunsignedsPintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<string,unsigned int>[nElements] : new map<string,unsigned int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEstringcOunsignedsPintgR(void *p) {
      delete ((map<string,unsigned int>*)p);
   }
   static void deleteArray_maplEstringcOunsignedsPintgR(void *p) {
      delete [] ((map<string,unsigned int>*)p);
   }
   static void destruct_maplEstringcOunsignedsPintgR(void *p) {
      typedef map<string,unsigned int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<string,unsigned int>

namespace ROOT {
   static TClass *maplEstringcOintgR_Dictionary();
   static void maplEstringcOintgR_TClassManip(TClass*);
   static void *new_maplEstringcOintgR(void *p = 0);
   static void *newArray_maplEstringcOintgR(Long_t size, void *p);
   static void delete_maplEstringcOintgR(void *p);
   static void deleteArray_maplEstringcOintgR(void *p);
   static void destruct_maplEstringcOintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<string,int>*)
   {
      map<string,int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<string,int>));
      static ::ROOT::TGenericClassInfo 
         instance("map<string,int>", -2, "map", 96,
                  typeid(map<string,int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEstringcOintgR_Dictionary, isa_proxy, 0,
                  sizeof(map<string,int>) );
      instance.SetNew(&new_maplEstringcOintgR);
      instance.SetNewArray(&newArray_maplEstringcOintgR);
      instance.SetDelete(&delete_maplEstringcOintgR);
      instance.SetDeleteArray(&deleteArray_maplEstringcOintgR);
      instance.SetDestructor(&destruct_maplEstringcOintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<string,int> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const map<string,int>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEstringcOintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<string,int>*)0x0)->GetClass();
      maplEstringcOintgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEstringcOintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEstringcOintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<string,int> : new map<string,int>;
   }
   static void *newArray_maplEstringcOintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<string,int>[nElements] : new map<string,int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEstringcOintgR(void *p) {
      delete ((map<string,int>*)p);
   }
   static void deleteArray_maplEstringcOintgR(void *p) {
      delete [] ((map<string,int>*)p);
   }
   static void destruct_maplEstringcOintgR(void *p) {
      typedef map<string,int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<string,int>

namespace ROOT {
   static TClass *maplEstringcOfloatgR_Dictionary();
   static void maplEstringcOfloatgR_TClassManip(TClass*);
   static void *new_maplEstringcOfloatgR(void *p = 0);
   static void *newArray_maplEstringcOfloatgR(Long_t size, void *p);
   static void delete_maplEstringcOfloatgR(void *p);
   static void deleteArray_maplEstringcOfloatgR(void *p);
   static void destruct_maplEstringcOfloatgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<string,float>*)
   {
      map<string,float> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<string,float>));
      static ::ROOT::TGenericClassInfo 
         instance("map<string,float>", -2, "map", 96,
                  typeid(map<string,float>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEstringcOfloatgR_Dictionary, isa_proxy, 0,
                  sizeof(map<string,float>) );
      instance.SetNew(&new_maplEstringcOfloatgR);
      instance.SetNewArray(&newArray_maplEstringcOfloatgR);
      instance.SetDelete(&delete_maplEstringcOfloatgR);
      instance.SetDeleteArray(&deleteArray_maplEstringcOfloatgR);
      instance.SetDestructor(&destruct_maplEstringcOfloatgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<string,float> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const map<string,float>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEstringcOfloatgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<string,float>*)0x0)->GetClass();
      maplEstringcOfloatgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEstringcOfloatgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEstringcOfloatgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<string,float> : new map<string,float>;
   }
   static void *newArray_maplEstringcOfloatgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<string,float>[nElements] : new map<string,float>[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEstringcOfloatgR(void *p) {
      delete ((map<string,float>*)p);
   }
   static void deleteArray_maplEstringcOfloatgR(void *p) {
      delete [] ((map<string,float>*)p);
   }
   static void destruct_maplEstringcOfloatgR(void *p) {
      typedef map<string,float> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<string,float>

namespace ROOT {
   static TClass *maplEstringcOdoublegR_Dictionary();
   static void maplEstringcOdoublegR_TClassManip(TClass*);
   static void *new_maplEstringcOdoublegR(void *p = 0);
   static void *newArray_maplEstringcOdoublegR(Long_t size, void *p);
   static void delete_maplEstringcOdoublegR(void *p);
   static void deleteArray_maplEstringcOdoublegR(void *p);
   static void destruct_maplEstringcOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<string,double>*)
   {
      map<string,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<string,double>));
      static ::ROOT::TGenericClassInfo 
         instance("map<string,double>", -2, "map", 96,
                  typeid(map<string,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEstringcOdoublegR_Dictionary, isa_proxy, 0,
                  sizeof(map<string,double>) );
      instance.SetNew(&new_maplEstringcOdoublegR);
      instance.SetNewArray(&newArray_maplEstringcOdoublegR);
      instance.SetDelete(&delete_maplEstringcOdoublegR);
      instance.SetDeleteArray(&deleteArray_maplEstringcOdoublegR);
      instance.SetDestructor(&destruct_maplEstringcOdoublegR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<string,double> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const map<string,double>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEstringcOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<string,double>*)0x0)->GetClass();
      maplEstringcOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void maplEstringcOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEstringcOdoublegR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<string,double> : new map<string,double>;
   }
   static void *newArray_maplEstringcOdoublegR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<string,double>[nElements] : new map<string,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEstringcOdoublegR(void *p) {
      delete ((map<string,double>*)p);
   }
   static void deleteArray_maplEstringcOdoublegR(void *p) {
      delete [] ((map<string,double>*)p);
   }
   static void destruct_maplEstringcOdoublegR(void *p) {
      typedef map<string,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<string,double>

namespace {
  void TriggerDictionaryInitialization_SFramePlugIns_Dict_Impl() {
    static const char* headers[] = {
"include/SH1.h",
"include/SInputVariables.h",
"include/SParticle.h",
"include/FPCompare.h",
"include/SToolBase.h",
"include/SOutputVariables.h",
"include/SSummedVar.h",
0
    };
    static const char* includePaths[] = {
"/mnt/t3nfs01/data01/shome/ineuteli/analysis/SFrameAnalysis_Moriond/SFrame",
"./",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/lcg/root/6.06.00-ikhhed4/include",
"/mnt/t3nfs01/data01/shome/ineuteli/analysis/SFrameAnalysis_Moriond/SFrame/plug-ins/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "SFramePlugIns_Dict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
class __attribute__((annotate("$clingAutoload$include/SParticle.h")))  SParticle;
namespace std{template <typename _Tp> class __attribute__((annotate("$clingAutoload$string")))  allocator;
}
template <class Type> class __attribute__((annotate("$clingAutoload$include/SSummedVar.h")))  ProofSummedVar;

namespace std{template <class _CharT> struct __attribute__((annotate("$clingAutoload$string")))  char_traits;
}
template <typename Type> class __attribute__((annotate("$clingAutoload$include/SH1.h")))  SH1;

typedef float Float_t __attribute__((annotate("$clingAutoload$RtypesCore.h"))) ;
typedef SH1<Float_t> SH1F __attribute__((annotate("$clingAutoload$include/SH1.h"))) ;
typedef double Double_t __attribute__((annotate("$clingAutoload$RtypesCore.h"))) ;
typedef SH1<Double_t> SH1D __attribute__((annotate("$clingAutoload$include/SH1.h"))) ;
typedef int Int_t __attribute__((annotate("$clingAutoload$RtypesCore.h"))) ;
typedef SH1<Int_t> SH1I __attribute__((annotate("$clingAutoload$include/SH1.h"))) ;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "SFramePlugIns_Dict dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "include/SH1.h"
#include "include/SInputVariables.h"
#include "include/SParticle.h"
#include "include/FPCompare.h"
#include "include/SToolBase.h"
#include "include/SOutputVariables.h"
#include "include/SSummedVar.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"ProofSummedVar<Double_t>", payloadCode, "@",
"ProofSummedVar<Float_t>", payloadCode, "@",
"ProofSummedVar<Int_t>", payloadCode, "@",
"ProofSummedVar<Long64_t>", payloadCode, "@",
"ProofSummedVar<Long_t>", payloadCode, "@",
"ProofSummedVar<Short_t>", payloadCode, "@",
"ProofSummedVar<UInt_t>", payloadCode, "@",
"ProofSummedVar<ULong64_t>", payloadCode, "@",
"ProofSummedVar<ULong_t>", payloadCode, "@",
"ProofSummedVar<UShort_t>", payloadCode, "@",
"ProofSummedVar<double>", payloadCode, "@",
"ProofSummedVar<float>", payloadCode, "@",
"ProofSummedVar<int>", payloadCode, "@",
"ProofSummedVar<long>", payloadCode, "@",
"ProofSummedVar<map<string,double> >", payloadCode, "@",
"ProofSummedVar<map<string,float> >", payloadCode, "@",
"ProofSummedVar<map<string,int> >", payloadCode, "@",
"ProofSummedVar<map<string,unsigned int> >", payloadCode, "@",
"ProofSummedVar<short>", payloadCode, "@",
"ProofSummedVar<unsigned int>", payloadCode, "@",
"ProofSummedVar<unsigned long>", payloadCode, "@",
"ProofSummedVar<unsigned short>", payloadCode, "@",
"ProofSummedVar<vector<Long64_t> >", payloadCode, "@",
"ProofSummedVar<vector<ULong64_t> >", payloadCode, "@",
"ProofSummedVar<vector<double> >", payloadCode, "@",
"ProofSummedVar<vector<float> >", payloadCode, "@",
"ProofSummedVar<vector<int> >", payloadCode, "@",
"ProofSummedVar<vector<long> >", payloadCode, "@",
"ProofSummedVar<vector<short> >", payloadCode, "@",
"ProofSummedVar<vector<unsigned int> >", payloadCode, "@",
"ProofSummedVar<vector<unsigned long> >", payloadCode, "@",
"ProofSummedVar<vector<unsigned short> >", payloadCode, "@",
"SH1<double>", payloadCode, "@",
"SH1<float>", payloadCode, "@",
"SH1<int>", payloadCode, "@",
"SH1D", payloadCode, "@",
"SH1F", payloadCode, "@",
"SH1I", payloadCode, "@",
"SParticle", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("SFramePlugIns_Dict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_SFramePlugIns_Dict_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_SFramePlugIns_Dict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_SFramePlugIns_Dict() {
  TriggerDictionaryInitialization_SFramePlugIns_Dict_Impl();
}
