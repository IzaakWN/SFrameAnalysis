// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME srcdISFrameCore_Dict

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
#include "include/SCycleBaseConfig.h"
#include "include/SParLocator.h"
#include "include/SLogWriter.h"
#include "include/SInputData.h"
#include "include/ISCycleBaseNTuple.h"
#include "include/SErrorHandler.h"
#include "include/SError.h"
#include "include/SLogger.h"
#include "include/SCycleStatistics.h"
#include "include/SFileMerger.h"
#include "include/ISCycleBaseHist.h"
#include "include/SCycleBaseBase.h"
#include "include/ISCycleBase.h"
#include "include/SOutputFile.h"
#include "include/SCycleBaseHist.h"
#include "include/SCycleOutput.h"
#include "include/SMsgType.h"
#include "include/STreeType.h"
#include "include/SCycleBase.h"
#include "include/SCycleController.h"
#include "include/SPointer.h"
#include "include/SProofManager.h"
#include "include/ISCycleBaseConfig.h"
#include "include/SCycleBaseNTuple.h"
#include "include/SCycleConfig.h"
#include "include/SCycleBaseExec.h"
#include "include/STreeTypeDecoder.h"
#include "include/SGeneratorCut.h"
#include "include/SConstants.h"

// Header files passed via #pragma extra_include

namespace ROOT {
   static void *new_SGeneratorCut(void *p = 0);
   static void *newArray_SGeneratorCut(Long_t size, void *p);
   static void delete_SGeneratorCut(void *p);
   static void deleteArray_SGeneratorCut(void *p);
   static void destruct_SGeneratorCut(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SGeneratorCut*)
   {
      ::SGeneratorCut *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SGeneratorCut >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SGeneratorCut", ::SGeneratorCut::Class_Version(), "include/SGeneratorCut.h", 30,
                  typeid(::SGeneratorCut), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SGeneratorCut::Dictionary, isa_proxy, 4,
                  sizeof(::SGeneratorCut) );
      instance.SetNew(&new_SGeneratorCut);
      instance.SetNewArray(&newArray_SGeneratorCut);
      instance.SetDelete(&delete_SGeneratorCut);
      instance.SetDeleteArray(&deleteArray_SGeneratorCut);
      instance.SetDestructor(&destruct_SGeneratorCut);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SGeneratorCut*)
   {
      return GenerateInitInstanceLocal((::SGeneratorCut*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SGeneratorCut*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SDataSet(void *p = 0);
   static void *newArray_SDataSet(Long_t size, void *p);
   static void delete_SDataSet(void *p);
   static void deleteArray_SDataSet(void *p);
   static void destruct_SDataSet(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SDataSet*)
   {
      ::SDataSet *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SDataSet >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SDataSet", ::SDataSet::Class_Version(), "include/SInputData.h", 45,
                  typeid(::SDataSet), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SDataSet::Dictionary, isa_proxy, 4,
                  sizeof(::SDataSet) );
      instance.SetNew(&new_SDataSet);
      instance.SetNewArray(&newArray_SDataSet);
      instance.SetDelete(&delete_SDataSet);
      instance.SetDeleteArray(&deleteArray_SDataSet);
      instance.SetDestructor(&destruct_SDataSet);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SDataSet*)
   {
      return GenerateInitInstanceLocal((::SDataSet*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SDataSet*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SFile(void *p = 0);
   static void *newArray_SFile(Long_t size, void *p);
   static void delete_SFile(void *p);
   static void deleteArray_SFile(void *p);
   static void destruct_SFile(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SFile*)
   {
      ::SFile *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SFile >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SFile", ::SFile::Class_Version(), "include/SInputData.h", 94,
                  typeid(::SFile), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SFile::Dictionary, isa_proxy, 4,
                  sizeof(::SFile) );
      instance.SetNew(&new_SFile);
      instance.SetNewArray(&newArray_SFile);
      instance.SetDelete(&delete_SFile);
      instance.SetDeleteArray(&deleteArray_SFile);
      instance.SetDestructor(&destruct_SFile);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SFile*)
   {
      return GenerateInitInstanceLocal((::SFile*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SFile*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_STree(void *p = 0);
   static void *newArray_STree(Long_t size, void *p);
   static void delete_STree(void *p);
   static void deleteArray_STree(void *p);
   static void destruct_STree(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::STree*)
   {
      ::STree *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::STree >(0);
      static ::ROOT::TGenericClassInfo 
         instance("STree", ::STree::Class_Version(), "include/SInputData.h", 151,
                  typeid(::STree), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::STree::Dictionary, isa_proxy, 4,
                  sizeof(::STree) );
      instance.SetNew(&new_STree);
      instance.SetNewArray(&newArray_STree);
      instance.SetDelete(&delete_STree);
      instance.SetDeleteArray(&deleteArray_STree);
      instance.SetDestructor(&destruct_STree);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::STree*)
   {
      return GenerateInitInstanceLocal((::STree*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::STree*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *pairlEintcOvectorlESTreegRsPgR_Dictionary();
   static void pairlEintcOvectorlESTreegRsPgR_TClassManip(TClass*);
   static void *new_pairlEintcOvectorlESTreegRsPgR(void *p = 0);
   static void *newArray_pairlEintcOvectorlESTreegRsPgR(Long_t size, void *p);
   static void delete_pairlEintcOvectorlESTreegRsPgR(void *p);
   static void deleteArray_pairlEintcOvectorlESTreegRsPgR(void *p);
   static void destruct_pairlEintcOvectorlESTreegRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const pair<int,vector<STree> >*)
   {
      pair<int,vector<STree> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(pair<int,vector<STree> >));
      static ::ROOT::TGenericClassInfo 
         instance("pair<int,vector<STree> >", "string", 96,
                  typeid(pair<int,vector<STree> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &pairlEintcOvectorlESTreegRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(pair<int,vector<STree> >) );
      instance.SetNew(&new_pairlEintcOvectorlESTreegRsPgR);
      instance.SetNewArray(&newArray_pairlEintcOvectorlESTreegRsPgR);
      instance.SetDelete(&delete_pairlEintcOvectorlESTreegRsPgR);
      instance.SetDeleteArray(&deleteArray_pairlEintcOvectorlESTreegRsPgR);
      instance.SetDestructor(&destruct_pairlEintcOvectorlESTreegRsPgR);
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const pair<int,vector<STree> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *pairlEintcOvectorlESTreegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const pair<int,vector<STree> >*)0x0)->GetClass();
      pairlEintcOvectorlESTreegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void pairlEintcOvectorlESTreegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_SInputData(void *p = 0);
   static void *newArray_SInputData(Long_t size, void *p);
   static void delete_SInputData(void *p);
   static void deleteArray_SInputData(void *p);
   static void destruct_SInputData(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SInputData*)
   {
      ::SInputData *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SInputData >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SInputData", ::SInputData::Class_Version(), "include/SInputData.h", 202,
                  typeid(::SInputData), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SInputData::Dictionary, isa_proxy, 4,
                  sizeof(::SInputData) );
      instance.SetNew(&new_SInputData);
      instance.SetNewArray(&newArray_SInputData);
      instance.SetDelete(&delete_SInputData);
      instance.SetDeleteArray(&deleteArray_SInputData);
      instance.SetDestructor(&destruct_SInputData);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SInputData*)
   {
      return GenerateInitInstanceLocal((::SInputData*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SInputData*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *pairlEstringcOstringgR_Dictionary();
   static void pairlEstringcOstringgR_TClassManip(TClass*);
   static void *new_pairlEstringcOstringgR(void *p = 0);
   static void *newArray_pairlEstringcOstringgR(Long_t size, void *p);
   static void delete_pairlEstringcOstringgR(void *p);
   static void deleteArray_pairlEstringcOstringgR(void *p);
   static void destruct_pairlEstringcOstringgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const pair<string,string>*)
   {
      pair<string,string> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(pair<string,string>));
      static ::ROOT::TGenericClassInfo 
         instance("pair<string,string>", "string", 96,
                  typeid(pair<string,string>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &pairlEstringcOstringgR_Dictionary, isa_proxy, 4,
                  sizeof(pair<string,string>) );
      instance.SetNew(&new_pairlEstringcOstringgR);
      instance.SetNewArray(&newArray_pairlEstringcOstringgR);
      instance.SetDelete(&delete_pairlEstringcOstringgR);
      instance.SetDeleteArray(&deleteArray_pairlEstringcOstringgR);
      instance.SetDestructor(&destruct_pairlEstringcOstringgR);

      ::ROOT::AddClassAlternate("pair<string,string>","pair<std::string,std::string>");
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const pair<string,string>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *pairlEstringcOstringgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const pair<string,string>*)0x0)->GetClass();
      pairlEstringcOstringgR_TClassManip(theClass);
   return theClass;
   }

   static void pairlEstringcOstringgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_SCycleConfig(void *p = 0);
   static void *newArray_SCycleConfig(Long_t size, void *p);
   static void delete_SCycleConfig(void *p);
   static void deleteArray_SCycleConfig(void *p);
   static void destruct_SCycleConfig(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleConfig*)
   {
      ::SCycleConfig *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleConfig >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleConfig", ::SCycleConfig::Class_Version(), "include/SCycleConfig.h", 42,
                  typeid(::SCycleConfig), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleConfig::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleConfig) );
      instance.SetNew(&new_SCycleConfig);
      instance.SetNewArray(&newArray_SCycleConfig);
      instance.SetDelete(&delete_SCycleConfig);
      instance.SetDeleteArray(&deleteArray_SCycleConfig);
      instance.SetDestructor(&destruct_SCycleConfig);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleConfig*)
   {
      return GenerateInitInstanceLocal((::SCycleConfig*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleConfig*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SCycleOutput(void *p = 0);
   static void *newArray_SCycleOutput(Long_t size, void *p);
   static void delete_SCycleOutput(void *p);
   static void deleteArray_SCycleOutput(void *p);
   static void destruct_SCycleOutput(void *p);
   static Long64_t merge_SCycleOutput(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleOutput*)
   {
      ::SCycleOutput *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleOutput >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleOutput", ::SCycleOutput::Class_Version(), "include/SCycleOutput.h", 43,
                  typeid(::SCycleOutput), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleOutput::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleOutput) );
      instance.SetNew(&new_SCycleOutput);
      instance.SetNewArray(&newArray_SCycleOutput);
      instance.SetDelete(&delete_SCycleOutput);
      instance.SetDeleteArray(&deleteArray_SCycleOutput);
      instance.SetDestructor(&destruct_SCycleOutput);
      instance.SetMerge(&merge_SCycleOutput);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleOutput*)
   {
      return GenerateInitInstanceLocal((::SCycleOutput*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleOutput*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SCycleStatistics(void *p = 0);
   static void *newArray_SCycleStatistics(Long_t size, void *p);
   static void delete_SCycleStatistics(void *p);
   static void deleteArray_SCycleStatistics(void *p);
   static void destruct_SCycleStatistics(void *p);
   static Long64_t merge_SCycleStatistics(void *obj, TCollection *coll,TFileMergeInfo *info);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleStatistics*)
   {
      ::SCycleStatistics *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleStatistics >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleStatistics", ::SCycleStatistics::Class_Version(), "include/SCycleStatistics.h", 39,
                  typeid(::SCycleStatistics), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleStatistics::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleStatistics) );
      instance.SetNew(&new_SCycleStatistics);
      instance.SetNewArray(&newArray_SCycleStatistics);
      instance.SetDelete(&delete_SCycleStatistics);
      instance.SetDeleteArray(&deleteArray_SCycleStatistics);
      instance.SetDestructor(&destruct_SCycleStatistics);
      instance.SetMerge(&merge_SCycleStatistics);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleStatistics*)
   {
      return GenerateInitInstanceLocal((::SCycleStatistics*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleStatistics*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_SOutputFile(void *p);
   static void deleteArray_SOutputFile(void *p);
   static void destruct_SOutputFile(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SOutputFile*)
   {
      ::SOutputFile *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SOutputFile >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SOutputFile", ::SOutputFile::Class_Version(), "include/SOutputFile.h", 32,
                  typeid(::SOutputFile), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SOutputFile::Dictionary, isa_proxy, 4,
                  sizeof(::SOutputFile) );
      instance.SetDelete(&delete_SOutputFile);
      instance.SetDeleteArray(&deleteArray_SOutputFile);
      instance.SetDestructor(&destruct_SOutputFile);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SOutputFile*)
   {
      return GenerateInitInstanceLocal((::SOutputFile*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SOutputFile*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static TClass *ISCycleBaseConfig_Dictionary();
   static void ISCycleBaseConfig_TClassManip(TClass*);
   static void delete_ISCycleBaseConfig(void *p);
   static void deleteArray_ISCycleBaseConfig(void *p);
   static void destruct_ISCycleBaseConfig(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ISCycleBaseConfig*)
   {
      ::ISCycleBaseConfig *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ISCycleBaseConfig));
      static ::ROOT::TGenericClassInfo 
         instance("ISCycleBaseConfig", "include/ISCycleBaseConfig.h", 37,
                  typeid(::ISCycleBaseConfig), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ISCycleBaseConfig_Dictionary, isa_proxy, 4,
                  sizeof(::ISCycleBaseConfig) );
      instance.SetDelete(&delete_ISCycleBaseConfig);
      instance.SetDeleteArray(&deleteArray_ISCycleBaseConfig);
      instance.SetDestructor(&destruct_ISCycleBaseConfig);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ISCycleBaseConfig*)
   {
      return GenerateInitInstanceLocal((::ISCycleBaseConfig*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ISCycleBaseConfig*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ISCycleBaseConfig_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ISCycleBaseConfig*)0x0)->GetClass();
      ISCycleBaseConfig_TClassManip(theClass);
   return theClass;
   }

   static void ISCycleBaseConfig_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ISCycleBaseHist_Dictionary();
   static void ISCycleBaseHist_TClassManip(TClass*);
   static void delete_ISCycleBaseHist(void *p);
   static void deleteArray_ISCycleBaseHist(void *p);
   static void destruct_ISCycleBaseHist(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ISCycleBaseHist*)
   {
      ::ISCycleBaseHist *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ISCycleBaseHist));
      static ::ROOT::TGenericClassInfo 
         instance("ISCycleBaseHist", "include/ISCycleBaseHist.h", 33,
                  typeid(::ISCycleBaseHist), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ISCycleBaseHist_Dictionary, isa_proxy, 4,
                  sizeof(::ISCycleBaseHist) );
      instance.SetDelete(&delete_ISCycleBaseHist);
      instance.SetDeleteArray(&deleteArray_ISCycleBaseHist);
      instance.SetDestructor(&destruct_ISCycleBaseHist);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ISCycleBaseHist*)
   {
      return GenerateInitInstanceLocal((::ISCycleBaseHist*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ISCycleBaseHist*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ISCycleBaseHist_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ISCycleBaseHist*)0x0)->GetClass();
      ISCycleBaseHist_TClassManip(theClass);
   return theClass;
   }

   static void ISCycleBaseHist_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static TClass *ISCycleBaseNTuple_Dictionary();
   static void ISCycleBaseNTuple_TClassManip(TClass*);
   static void delete_ISCycleBaseNTuple(void *p);
   static void deleteArray_ISCycleBaseNTuple(void *p);
   static void destruct_ISCycleBaseNTuple(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ISCycleBaseNTuple*)
   {
      ::ISCycleBaseNTuple *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(::ISCycleBaseNTuple));
      static ::ROOT::TGenericClassInfo 
         instance("ISCycleBaseNTuple", "include/ISCycleBaseNTuple.h", 45,
                  typeid(::ISCycleBaseNTuple), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ISCycleBaseNTuple_Dictionary, isa_proxy, 4,
                  sizeof(::ISCycleBaseNTuple) );
      instance.SetDelete(&delete_ISCycleBaseNTuple);
      instance.SetDeleteArray(&deleteArray_ISCycleBaseNTuple);
      instance.SetDestructor(&destruct_ISCycleBaseNTuple);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ISCycleBaseNTuple*)
   {
      return GenerateInitInstanceLocal((::ISCycleBaseNTuple*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ISCycleBaseNTuple*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ISCycleBaseNTuple_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ::ISCycleBaseNTuple*)0x0)->GetClass();
      ISCycleBaseNTuple_TClassManip(theClass);
   return theClass;
   }

   static void ISCycleBaseNTuple_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   static void *new_SCycleBaseBase(void *p = 0);
   static void *newArray_SCycleBaseBase(Long_t size, void *p);
   static void delete_SCycleBaseBase(void *p);
   static void deleteArray_SCycleBaseBase(void *p);
   static void destruct_SCycleBaseBase(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleBaseBase*)
   {
      ::SCycleBaseBase *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleBaseBase >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleBaseBase", ::SCycleBaseBase::Class_Version(), "include/SCycleBaseBase.h", 32,
                  typeid(::SCycleBaseBase), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleBaseBase::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleBaseBase) );
      instance.SetNew(&new_SCycleBaseBase);
      instance.SetNewArray(&newArray_SCycleBaseBase);
      instance.SetDelete(&delete_SCycleBaseBase);
      instance.SetDeleteArray(&deleteArray_SCycleBaseBase);
      instance.SetDestructor(&destruct_SCycleBaseBase);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleBaseBase*)
   {
      return GenerateInitInstanceLocal((::SCycleBaseBase*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleBaseBase*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_SCycleBaseConfig(void *p = 0);
   static void *newArray_SCycleBaseConfig(Long_t size, void *p);
   static void delete_SCycleBaseConfig(void *p);
   static void deleteArray_SCycleBaseConfig(void *p);
   static void destruct_SCycleBaseConfig(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleBaseConfig*)
   {
      ::SCycleBaseConfig *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleBaseConfig >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleBaseConfig", ::SCycleBaseConfig::Class_Version(), "include/SCycleBaseConfig.h", 47,
                  typeid(::SCycleBaseConfig), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleBaseConfig::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleBaseConfig) );
      instance.SetNew(&new_SCycleBaseConfig);
      instance.SetNewArray(&newArray_SCycleBaseConfig);
      instance.SetDelete(&delete_SCycleBaseConfig);
      instance.SetDeleteArray(&deleteArray_SCycleBaseConfig);
      instance.SetDestructor(&destruct_SCycleBaseConfig);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleBaseConfig*)
   {
      return GenerateInitInstanceLocal((::SCycleBaseConfig*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleBaseConfig*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_SCycleBaseHist(void *p);
   static void deleteArray_SCycleBaseHist(void *p);
   static void destruct_SCycleBaseHist(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleBaseHist*)
   {
      ::SCycleBaseHist *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleBaseHist >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleBaseHist", ::SCycleBaseHist::Class_Version(), "include/SCycleBaseHist.h", 49,
                  typeid(::SCycleBaseHist), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleBaseHist::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleBaseHist) );
      instance.SetDelete(&delete_SCycleBaseHist);
      instance.SetDeleteArray(&deleteArray_SCycleBaseHist);
      instance.SetDestructor(&destruct_SCycleBaseHist);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleBaseHist*)
   {
      return GenerateInitInstanceLocal((::SCycleBaseHist*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleBaseHist*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_SCycleBaseNTuple(void *p);
   static void deleteArray_SCycleBaseNTuple(void *p);
   static void destruct_SCycleBaseNTuple(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleBaseNTuple*)
   {
      ::SCycleBaseNTuple *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleBaseNTuple >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleBaseNTuple", ::SCycleBaseNTuple::Class_Version(), "include/SCycleBaseNTuple.h", 47,
                  typeid(::SCycleBaseNTuple), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleBaseNTuple::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleBaseNTuple) );
      instance.SetDelete(&delete_SCycleBaseNTuple);
      instance.SetDeleteArray(&deleteArray_SCycleBaseNTuple);
      instance.SetDestructor(&destruct_SCycleBaseNTuple);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleBaseNTuple*)
   {
      return GenerateInitInstanceLocal((::SCycleBaseNTuple*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleBaseNTuple*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_SCycleBaseExec(void *p);
   static void deleteArray_SCycleBaseExec(void *p);
   static void destruct_SCycleBaseExec(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleBaseExec*)
   {
      ::SCycleBaseExec *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleBaseExec >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleBaseExec", ::SCycleBaseExec::Class_Version(), "include/SCycleBaseExec.h", 46,
                  typeid(::SCycleBaseExec), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleBaseExec::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleBaseExec) );
      instance.SetDelete(&delete_SCycleBaseExec);
      instance.SetDeleteArray(&deleteArray_SCycleBaseExec);
      instance.SetDestructor(&destruct_SCycleBaseExec);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleBaseExec*)
   {
      return GenerateInitInstanceLocal((::SCycleBaseExec*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleBaseExec*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_ISCycleBase(void *p);
   static void deleteArray_ISCycleBase(void *p);
   static void destruct_ISCycleBase(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::ISCycleBase*)
   {
      ::ISCycleBase *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::ISCycleBase >(0);
      static ::ROOT::TGenericClassInfo 
         instance("ISCycleBase", ::ISCycleBase::Class_Version(), "include/ISCycleBase.h", 37,
                  typeid(::ISCycleBase), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::ISCycleBase::Dictionary, isa_proxy, 4,
                  sizeof(::ISCycleBase) );
      instance.SetDelete(&delete_ISCycleBase);
      instance.SetDeleteArray(&deleteArray_ISCycleBase);
      instance.SetDestructor(&destruct_ISCycleBase);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::ISCycleBase*)
   {
      return GenerateInitInstanceLocal((::ISCycleBase*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::ISCycleBase*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_SCycleBase(void *p);
   static void deleteArray_SCycleBase(void *p);
   static void destruct_SCycleBase(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::SCycleBase*)
   {
      ::SCycleBase *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::SCycleBase >(0);
      static ::ROOT::TGenericClassInfo 
         instance("SCycleBase", ::SCycleBase::Class_Version(), "include/SCycleBase.h", 48,
                  typeid(::SCycleBase), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::SCycleBase::Dictionary, isa_proxy, 4,
                  sizeof(::SCycleBase) );
      instance.SetDelete(&delete_SCycleBase);
      instance.SetDeleteArray(&deleteArray_SCycleBase);
      instance.SetDestructor(&destruct_SCycleBase);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::SCycleBase*)
   {
      return GenerateInitInstanceLocal((::SCycleBase*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const ::SCycleBase*)0x0); R__UseDummy(_R__UNIQUE_(Init));
} // end of namespace ROOT

//______________________________________________________________________________
atomic_TClass_ptr SGeneratorCut::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SGeneratorCut::Class_Name()
{
   return "SGeneratorCut";
}

//______________________________________________________________________________
const char *SGeneratorCut::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SGeneratorCut*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SGeneratorCut::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SGeneratorCut*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SGeneratorCut::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SGeneratorCut*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SGeneratorCut::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SGeneratorCut*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SDataSet::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SDataSet::Class_Name()
{
   return "SDataSet";
}

//______________________________________________________________________________
const char *SDataSet::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SDataSet*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SDataSet::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SDataSet*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SDataSet::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SDataSet*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SDataSet::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SDataSet*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SFile::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SFile::Class_Name()
{
   return "SFile";
}

//______________________________________________________________________________
const char *SFile::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SFile*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SFile::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SFile*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SFile::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SFile*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SFile::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SFile*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr STree::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *STree::Class_Name()
{
   return "STree";
}

//______________________________________________________________________________
const char *STree::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::STree*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int STree::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::STree*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *STree::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::STree*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *STree::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::STree*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SInputData::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SInputData::Class_Name()
{
   return "SInputData";
}

//______________________________________________________________________________
const char *SInputData::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SInputData*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SInputData::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SInputData*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SInputData::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SInputData*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SInputData::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SInputData*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleConfig::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleConfig::Class_Name()
{
   return "SCycleConfig";
}

//______________________________________________________________________________
const char *SCycleConfig::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleConfig*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleConfig::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleConfig*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleConfig::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleConfig*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleConfig::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleConfig*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleOutput::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleOutput::Class_Name()
{
   return "SCycleOutput";
}

//______________________________________________________________________________
const char *SCycleOutput::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleOutput*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleOutput::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleOutput*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleOutput::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleOutput*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleOutput::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleOutput*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleStatistics::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleStatistics::Class_Name()
{
   return "SCycleStatistics";
}

//______________________________________________________________________________
const char *SCycleStatistics::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleStatistics*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleStatistics::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleStatistics*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleStatistics::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleStatistics*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleStatistics::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleStatistics*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SOutputFile::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SOutputFile::Class_Name()
{
   return "SOutputFile";
}

//______________________________________________________________________________
const char *SOutputFile::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SOutputFile*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SOutputFile::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SOutputFile*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SOutputFile::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SOutputFile*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SOutputFile::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SOutputFile*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleBaseBase::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleBaseBase::Class_Name()
{
   return "SCycleBaseBase";
}

//______________________________________________________________________________
const char *SCycleBaseBase::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseBase*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleBaseBase::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseBase*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleBaseBase::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseBase*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleBaseBase::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseBase*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleBaseConfig::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleBaseConfig::Class_Name()
{
   return "SCycleBaseConfig";
}

//______________________________________________________________________________
const char *SCycleBaseConfig::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseConfig*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleBaseConfig::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseConfig*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleBaseConfig::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseConfig*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleBaseConfig::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseConfig*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleBaseHist::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleBaseHist::Class_Name()
{
   return "SCycleBaseHist";
}

//______________________________________________________________________________
const char *SCycleBaseHist::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseHist*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleBaseHist::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseHist*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleBaseHist::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseHist*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleBaseHist::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseHist*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleBaseNTuple::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleBaseNTuple::Class_Name()
{
   return "SCycleBaseNTuple";
}

//______________________________________________________________________________
const char *SCycleBaseNTuple::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseNTuple*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleBaseNTuple::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseNTuple*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleBaseNTuple::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseNTuple*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleBaseNTuple::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseNTuple*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleBaseExec::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleBaseExec::Class_Name()
{
   return "SCycleBaseExec";
}

//______________________________________________________________________________
const char *SCycleBaseExec::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseExec*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleBaseExec::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseExec*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleBaseExec::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseExec*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleBaseExec::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBaseExec*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr ISCycleBase::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *ISCycleBase::Class_Name()
{
   return "ISCycleBase";
}

//______________________________________________________________________________
const char *ISCycleBase::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ISCycleBase*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int ISCycleBase::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::ISCycleBase*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *ISCycleBase::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ISCycleBase*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *ISCycleBase::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::ISCycleBase*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr SCycleBase::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *SCycleBase::Class_Name()
{
   return "SCycleBase";
}

//______________________________________________________________________________
const char *SCycleBase::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBase*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int SCycleBase::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::SCycleBase*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *SCycleBase::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBase*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *SCycleBase::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::SCycleBase*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
void SGeneratorCut::Streamer(TBuffer &R__b)
{
   // Stream an object of class SGeneratorCut.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SGeneratorCut::Class(),this);
   } else {
      R__b.WriteClassBuffer(SGeneratorCut::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SGeneratorCut(void *p) {
      return  p ? new(p) ::SGeneratorCut : new ::SGeneratorCut;
   }
   static void *newArray_SGeneratorCut(Long_t nElements, void *p) {
      return p ? new(p) ::SGeneratorCut[nElements] : new ::SGeneratorCut[nElements];
   }
   // Wrapper around operator delete
   static void delete_SGeneratorCut(void *p) {
      delete ((::SGeneratorCut*)p);
   }
   static void deleteArray_SGeneratorCut(void *p) {
      delete [] ((::SGeneratorCut*)p);
   }
   static void destruct_SGeneratorCut(void *p) {
      typedef ::SGeneratorCut current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SGeneratorCut

//______________________________________________________________________________
void SDataSet::Streamer(TBuffer &R__b)
{
   // Stream an object of class SDataSet.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SDataSet::Class(),this);
   } else {
      R__b.WriteClassBuffer(SDataSet::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SDataSet(void *p) {
      return  p ? new(p) ::SDataSet : new ::SDataSet;
   }
   static void *newArray_SDataSet(Long_t nElements, void *p) {
      return p ? new(p) ::SDataSet[nElements] : new ::SDataSet[nElements];
   }
   // Wrapper around operator delete
   static void delete_SDataSet(void *p) {
      delete ((::SDataSet*)p);
   }
   static void deleteArray_SDataSet(void *p) {
      delete [] ((::SDataSet*)p);
   }
   static void destruct_SDataSet(void *p) {
      typedef ::SDataSet current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SDataSet

//______________________________________________________________________________
void SFile::Streamer(TBuffer &R__b)
{
   // Stream an object of class SFile.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SFile::Class(),this);
   } else {
      R__b.WriteClassBuffer(SFile::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SFile(void *p) {
      return  p ? new(p) ::SFile : new ::SFile;
   }
   static void *newArray_SFile(Long_t nElements, void *p) {
      return p ? new(p) ::SFile[nElements] : new ::SFile[nElements];
   }
   // Wrapper around operator delete
   static void delete_SFile(void *p) {
      delete ((::SFile*)p);
   }
   static void deleteArray_SFile(void *p) {
      delete [] ((::SFile*)p);
   }
   static void destruct_SFile(void *p) {
      typedef ::SFile current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SFile

//______________________________________________________________________________
void STree::Streamer(TBuffer &R__b)
{
   // Stream an object of class STree.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(STree::Class(),this);
   } else {
      R__b.WriteClassBuffer(STree::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_STree(void *p) {
      return  p ? new(p) ::STree : new ::STree;
   }
   static void *newArray_STree(Long_t nElements, void *p) {
      return p ? new(p) ::STree[nElements] : new ::STree[nElements];
   }
   // Wrapper around operator delete
   static void delete_STree(void *p) {
      delete ((::STree*)p);
   }
   static void deleteArray_STree(void *p) {
      delete [] ((::STree*)p);
   }
   static void destruct_STree(void *p) {
      typedef ::STree current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::STree

namespace ROOT {
   // Wrappers around operator new
   static void *new_pairlEintcOvectorlESTreegRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) pair<int,vector<STree> > : new pair<int,vector<STree> >;
   }
   static void *newArray_pairlEintcOvectorlESTreegRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) pair<int,vector<STree> >[nElements] : new pair<int,vector<STree> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_pairlEintcOvectorlESTreegRsPgR(void *p) {
      delete ((pair<int,vector<STree> >*)p);
   }
   static void deleteArray_pairlEintcOvectorlESTreegRsPgR(void *p) {
      delete [] ((pair<int,vector<STree> >*)p);
   }
   static void destruct_pairlEintcOvectorlESTreegRsPgR(void *p) {
      typedef pair<int,vector<STree> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class pair<int,vector<STree> >

//______________________________________________________________________________
void SInputData::Streamer(TBuffer &R__b)
{
   // Stream an object of class SInputData.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SInputData::Class(),this);
   } else {
      R__b.WriteClassBuffer(SInputData::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SInputData(void *p) {
      return  p ? new(p) ::SInputData : new ::SInputData;
   }
   static void *newArray_SInputData(Long_t nElements, void *p) {
      return p ? new(p) ::SInputData[nElements] : new ::SInputData[nElements];
   }
   // Wrapper around operator delete
   static void delete_SInputData(void *p) {
      delete ((::SInputData*)p);
   }
   static void deleteArray_SInputData(void *p) {
      delete [] ((::SInputData*)p);
   }
   static void destruct_SInputData(void *p) {
      typedef ::SInputData current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SInputData

namespace ROOT {
   // Wrappers around operator new
   static void *new_pairlEstringcOstringgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) pair<string,string> : new pair<string,string>;
   }
   static void *newArray_pairlEstringcOstringgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) pair<string,string>[nElements] : new pair<string,string>[nElements];
   }
   // Wrapper around operator delete
   static void delete_pairlEstringcOstringgR(void *p) {
      delete ((pair<string,string>*)p);
   }
   static void deleteArray_pairlEstringcOstringgR(void *p) {
      delete [] ((pair<string,string>*)p);
   }
   static void destruct_pairlEstringcOstringgR(void *p) {
      typedef pair<string,string> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class pair<string,string>

//______________________________________________________________________________
void SCycleConfig::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleConfig.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleConfig::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleConfig::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SCycleConfig(void *p) {
      return  p ? new(p) ::SCycleConfig : new ::SCycleConfig;
   }
   static void *newArray_SCycleConfig(Long_t nElements, void *p) {
      return p ? new(p) ::SCycleConfig[nElements] : new ::SCycleConfig[nElements];
   }
   // Wrapper around operator delete
   static void delete_SCycleConfig(void *p) {
      delete ((::SCycleConfig*)p);
   }
   static void deleteArray_SCycleConfig(void *p) {
      delete [] ((::SCycleConfig*)p);
   }
   static void destruct_SCycleConfig(void *p) {
      typedef ::SCycleConfig current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SCycleConfig

//______________________________________________________________________________
void SCycleOutput::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleOutput.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleOutput::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleOutput::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SCycleOutput(void *p) {
      return  p ? new(p) ::SCycleOutput : new ::SCycleOutput;
   }
   static void *newArray_SCycleOutput(Long_t nElements, void *p) {
      return p ? new(p) ::SCycleOutput[nElements] : new ::SCycleOutput[nElements];
   }
   // Wrapper around operator delete
   static void delete_SCycleOutput(void *p) {
      delete ((::SCycleOutput*)p);
   }
   static void deleteArray_SCycleOutput(void *p) {
      delete [] ((::SCycleOutput*)p);
   }
   static void destruct_SCycleOutput(void *p) {
      typedef ::SCycleOutput current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_SCycleOutput(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::SCycleOutput*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::SCycleOutput

//______________________________________________________________________________
void SCycleStatistics::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleStatistics.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleStatistics::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleStatistics::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SCycleStatistics(void *p) {
      return  p ? new(p) ::SCycleStatistics : new ::SCycleStatistics;
   }
   static void *newArray_SCycleStatistics(Long_t nElements, void *p) {
      return p ? new(p) ::SCycleStatistics[nElements] : new ::SCycleStatistics[nElements];
   }
   // Wrapper around operator delete
   static void delete_SCycleStatistics(void *p) {
      delete ((::SCycleStatistics*)p);
   }
   static void deleteArray_SCycleStatistics(void *p) {
      delete [] ((::SCycleStatistics*)p);
   }
   static void destruct_SCycleStatistics(void *p) {
      typedef ::SCycleStatistics current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around the merge function.
   static Long64_t  merge_SCycleStatistics(void *obj,TCollection *coll,TFileMergeInfo *) {
      return ((::SCycleStatistics*)obj)->Merge(coll);
   }
} // end of namespace ROOT for class ::SCycleStatistics

//______________________________________________________________________________
void SOutputFile::Streamer(TBuffer &R__b)
{
   // Stream an object of class SOutputFile.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SOutputFile::Class(),this);
   } else {
      R__b.WriteClassBuffer(SOutputFile::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_SOutputFile(void *p) {
      delete ((::SOutputFile*)p);
   }
   static void deleteArray_SOutputFile(void *p) {
      delete [] ((::SOutputFile*)p);
   }
   static void destruct_SOutputFile(void *p) {
      typedef ::SOutputFile current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SOutputFile

namespace ROOT {
   // Wrapper around operator delete
   static void delete_ISCycleBaseConfig(void *p) {
      delete ((::ISCycleBaseConfig*)p);
   }
   static void deleteArray_ISCycleBaseConfig(void *p) {
      delete [] ((::ISCycleBaseConfig*)p);
   }
   static void destruct_ISCycleBaseConfig(void *p) {
      typedef ::ISCycleBaseConfig current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ISCycleBaseConfig

namespace ROOT {
   // Wrapper around operator delete
   static void delete_ISCycleBaseHist(void *p) {
      delete ((::ISCycleBaseHist*)p);
   }
   static void deleteArray_ISCycleBaseHist(void *p) {
      delete [] ((::ISCycleBaseHist*)p);
   }
   static void destruct_ISCycleBaseHist(void *p) {
      typedef ::ISCycleBaseHist current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ISCycleBaseHist

namespace ROOT {
   // Wrapper around operator delete
   static void delete_ISCycleBaseNTuple(void *p) {
      delete ((::ISCycleBaseNTuple*)p);
   }
   static void deleteArray_ISCycleBaseNTuple(void *p) {
      delete [] ((::ISCycleBaseNTuple*)p);
   }
   static void destruct_ISCycleBaseNTuple(void *p) {
      typedef ::ISCycleBaseNTuple current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ISCycleBaseNTuple

//______________________________________________________________________________
void SCycleBaseBase::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleBaseBase.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleBaseBase::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleBaseBase::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SCycleBaseBase(void *p) {
      return  p ? new(p) ::SCycleBaseBase : new ::SCycleBaseBase;
   }
   static void *newArray_SCycleBaseBase(Long_t nElements, void *p) {
      return p ? new(p) ::SCycleBaseBase[nElements] : new ::SCycleBaseBase[nElements];
   }
   // Wrapper around operator delete
   static void delete_SCycleBaseBase(void *p) {
      delete ((::SCycleBaseBase*)p);
   }
   static void deleteArray_SCycleBaseBase(void *p) {
      delete [] ((::SCycleBaseBase*)p);
   }
   static void destruct_SCycleBaseBase(void *p) {
      typedef ::SCycleBaseBase current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SCycleBaseBase

//______________________________________________________________________________
void SCycleBaseConfig::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleBaseConfig.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleBaseConfig::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleBaseConfig::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_SCycleBaseConfig(void *p) {
      return  p ? new(p) ::SCycleBaseConfig : new ::SCycleBaseConfig;
   }
   static void *newArray_SCycleBaseConfig(Long_t nElements, void *p) {
      return p ? new(p) ::SCycleBaseConfig[nElements] : new ::SCycleBaseConfig[nElements];
   }
   // Wrapper around operator delete
   static void delete_SCycleBaseConfig(void *p) {
      delete ((::SCycleBaseConfig*)p);
   }
   static void deleteArray_SCycleBaseConfig(void *p) {
      delete [] ((::SCycleBaseConfig*)p);
   }
   static void destruct_SCycleBaseConfig(void *p) {
      typedef ::SCycleBaseConfig current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SCycleBaseConfig

//______________________________________________________________________________
void SCycleBaseHist::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleBaseHist.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleBaseHist::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleBaseHist::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_SCycleBaseHist(void *p) {
      delete ((::SCycleBaseHist*)p);
   }
   static void deleteArray_SCycleBaseHist(void *p) {
      delete [] ((::SCycleBaseHist*)p);
   }
   static void destruct_SCycleBaseHist(void *p) {
      typedef ::SCycleBaseHist current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SCycleBaseHist

//______________________________________________________________________________
void SCycleBaseNTuple::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleBaseNTuple.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleBaseNTuple::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleBaseNTuple::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_SCycleBaseNTuple(void *p) {
      delete ((::SCycleBaseNTuple*)p);
   }
   static void deleteArray_SCycleBaseNTuple(void *p) {
      delete [] ((::SCycleBaseNTuple*)p);
   }
   static void destruct_SCycleBaseNTuple(void *p) {
      typedef ::SCycleBaseNTuple current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SCycleBaseNTuple

//______________________________________________________________________________
void SCycleBaseExec::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleBaseExec.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleBaseExec::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleBaseExec::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_SCycleBaseExec(void *p) {
      delete ((::SCycleBaseExec*)p);
   }
   static void deleteArray_SCycleBaseExec(void *p) {
      delete [] ((::SCycleBaseExec*)p);
   }
   static void destruct_SCycleBaseExec(void *p) {
      typedef ::SCycleBaseExec current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SCycleBaseExec

//______________________________________________________________________________
void ISCycleBase::Streamer(TBuffer &R__b)
{
   // Stream an object of class ISCycleBase.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(ISCycleBase::Class(),this);
   } else {
      R__b.WriteClassBuffer(ISCycleBase::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_ISCycleBase(void *p) {
      delete ((::ISCycleBase*)p);
   }
   static void deleteArray_ISCycleBase(void *p) {
      delete [] ((::ISCycleBase*)p);
   }
   static void destruct_ISCycleBase(void *p) {
      typedef ::ISCycleBase current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::ISCycleBase

//______________________________________________________________________________
void SCycleBase::Streamer(TBuffer &R__b)
{
   // Stream an object of class SCycleBase.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(SCycleBase::Class(),this);
   } else {
      R__b.WriteClassBuffer(SCycleBase::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_SCycleBase(void *p) {
      delete ((::SCycleBase*)p);
   }
   static void deleteArray_SCycleBase(void *p) {
      delete [] ((::SCycleBase*)p);
   }
   static void destruct_SCycleBase(void *p) {
      typedef ::SCycleBase current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::SCycleBase

namespace ROOT {
   static TClass *vectorlEpairlEstringcOstringgRsPgR_Dictionary();
   static void vectorlEpairlEstringcOstringgRsPgR_TClassManip(TClass*);
   static void *new_vectorlEpairlEstringcOstringgRsPgR(void *p = 0);
   static void *newArray_vectorlEpairlEstringcOstringgRsPgR(Long_t size, void *p);
   static void delete_vectorlEpairlEstringcOstringgRsPgR(void *p);
   static void deleteArray_vectorlEpairlEstringcOstringgRsPgR(void *p);
   static void destruct_vectorlEpairlEstringcOstringgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<pair<string,string> >*)
   {
      vector<pair<string,string> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<pair<string,string> >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<pair<string,string> >", -2, "vector", 214,
                  typeid(vector<pair<string,string> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEpairlEstringcOstringgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<pair<string,string> >) );
      instance.SetNew(&new_vectorlEpairlEstringcOstringgRsPgR);
      instance.SetNewArray(&newArray_vectorlEpairlEstringcOstringgRsPgR);
      instance.SetDelete(&delete_vectorlEpairlEstringcOstringgRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEpairlEstringcOstringgRsPgR);
      instance.SetDestructor(&destruct_vectorlEpairlEstringcOstringgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<pair<string,string> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<pair<string,string> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEpairlEstringcOstringgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<pair<string,string> >*)0x0)->GetClass();
      vectorlEpairlEstringcOstringgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEpairlEstringcOstringgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEpairlEstringcOstringgRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<pair<string,string> > : new vector<pair<string,string> >;
   }
   static void *newArray_vectorlEpairlEstringcOstringgRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<pair<string,string> >[nElements] : new vector<pair<string,string> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEpairlEstringcOstringgRsPgR(void *p) {
      delete ((vector<pair<string,string> >*)p);
   }
   static void deleteArray_vectorlEpairlEstringcOstringgRsPgR(void *p) {
      delete [] ((vector<pair<string,string> >*)p);
   }
   static void destruct_vectorlEpairlEstringcOstringgRsPgR(void *p) {
      typedef vector<pair<string,string> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<pair<string,string> >

namespace ROOT {
   static TClass *vectorlESTreegR_Dictionary();
   static void vectorlESTreegR_TClassManip(TClass*);
   static void *new_vectorlESTreegR(void *p = 0);
   static void *newArray_vectorlESTreegR(Long_t size, void *p);
   static void delete_vectorlESTreegR(void *p);
   static void deleteArray_vectorlESTreegR(void *p);
   static void destruct_vectorlESTreegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<STree>*)
   {
      vector<STree> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<STree>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<STree>", -2, "vector", 214,
                  typeid(vector<STree>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlESTreegR_Dictionary, isa_proxy, 4,
                  sizeof(vector<STree>) );
      instance.SetNew(&new_vectorlESTreegR);
      instance.SetNewArray(&newArray_vectorlESTreegR);
      instance.SetDelete(&delete_vectorlESTreegR);
      instance.SetDeleteArray(&deleteArray_vectorlESTreegR);
      instance.SetDestructor(&destruct_vectorlESTreegR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<STree> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<STree>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlESTreegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<STree>*)0x0)->GetClass();
      vectorlESTreegR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlESTreegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlESTreegR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<STree> : new vector<STree>;
   }
   static void *newArray_vectorlESTreegR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<STree>[nElements] : new vector<STree>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlESTreegR(void *p) {
      delete ((vector<STree>*)p);
   }
   static void deleteArray_vectorlESTreegR(void *p) {
      delete [] ((vector<STree>*)p);
   }
   static void destruct_vectorlESTreegR(void *p) {
      typedef vector<STree> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<STree>

namespace ROOT {
   static TClass *vectorlESInputDatagR_Dictionary();
   static void vectorlESInputDatagR_TClassManip(TClass*);
   static void *new_vectorlESInputDatagR(void *p = 0);
   static void *newArray_vectorlESInputDatagR(Long_t size, void *p);
   static void delete_vectorlESInputDatagR(void *p);
   static void deleteArray_vectorlESInputDatagR(void *p);
   static void destruct_vectorlESInputDatagR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<SInputData>*)
   {
      vector<SInputData> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<SInputData>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<SInputData>", -2, "vector", 214,
                  typeid(vector<SInputData>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlESInputDatagR_Dictionary, isa_proxy, 4,
                  sizeof(vector<SInputData>) );
      instance.SetNew(&new_vectorlESInputDatagR);
      instance.SetNewArray(&newArray_vectorlESInputDatagR);
      instance.SetDelete(&delete_vectorlESInputDatagR);
      instance.SetDeleteArray(&deleteArray_vectorlESInputDatagR);
      instance.SetDestructor(&destruct_vectorlESInputDatagR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<SInputData> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<SInputData>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlESInputDatagR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<SInputData>*)0x0)->GetClass();
      vectorlESInputDatagR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlESInputDatagR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlESInputDatagR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SInputData> : new vector<SInputData>;
   }
   static void *newArray_vectorlESInputDatagR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SInputData>[nElements] : new vector<SInputData>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlESInputDatagR(void *p) {
      delete ((vector<SInputData>*)p);
   }
   static void deleteArray_vectorlESInputDatagR(void *p) {
      delete [] ((vector<SInputData>*)p);
   }
   static void destruct_vectorlESInputDatagR(void *p) {
      typedef vector<SInputData> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<SInputData>

namespace ROOT {
   static TClass *vectorlESGeneratorCutgR_Dictionary();
   static void vectorlESGeneratorCutgR_TClassManip(TClass*);
   static void *new_vectorlESGeneratorCutgR(void *p = 0);
   static void *newArray_vectorlESGeneratorCutgR(Long_t size, void *p);
   static void delete_vectorlESGeneratorCutgR(void *p);
   static void deleteArray_vectorlESGeneratorCutgR(void *p);
   static void destruct_vectorlESGeneratorCutgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<SGeneratorCut>*)
   {
      vector<SGeneratorCut> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<SGeneratorCut>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<SGeneratorCut>", -2, "vector", 214,
                  typeid(vector<SGeneratorCut>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlESGeneratorCutgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<SGeneratorCut>) );
      instance.SetNew(&new_vectorlESGeneratorCutgR);
      instance.SetNewArray(&newArray_vectorlESGeneratorCutgR);
      instance.SetDelete(&delete_vectorlESGeneratorCutgR);
      instance.SetDeleteArray(&deleteArray_vectorlESGeneratorCutgR);
      instance.SetDestructor(&destruct_vectorlESGeneratorCutgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<SGeneratorCut> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<SGeneratorCut>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlESGeneratorCutgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<SGeneratorCut>*)0x0)->GetClass();
      vectorlESGeneratorCutgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlESGeneratorCutgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlESGeneratorCutgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SGeneratorCut> : new vector<SGeneratorCut>;
   }
   static void *newArray_vectorlESGeneratorCutgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SGeneratorCut>[nElements] : new vector<SGeneratorCut>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlESGeneratorCutgR(void *p) {
      delete ((vector<SGeneratorCut>*)p);
   }
   static void deleteArray_vectorlESGeneratorCutgR(void *p) {
      delete [] ((vector<SGeneratorCut>*)p);
   }
   static void destruct_vectorlESGeneratorCutgR(void *p) {
      typedef vector<SGeneratorCut> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<SGeneratorCut>

namespace ROOT {
   static TClass *vectorlESFilegR_Dictionary();
   static void vectorlESFilegR_TClassManip(TClass*);
   static void *new_vectorlESFilegR(void *p = 0);
   static void *newArray_vectorlESFilegR(Long_t size, void *p);
   static void delete_vectorlESFilegR(void *p);
   static void deleteArray_vectorlESFilegR(void *p);
   static void destruct_vectorlESFilegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<SFile>*)
   {
      vector<SFile> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<SFile>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<SFile>", -2, "vector", 214,
                  typeid(vector<SFile>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlESFilegR_Dictionary, isa_proxy, 4,
                  sizeof(vector<SFile>) );
      instance.SetNew(&new_vectorlESFilegR);
      instance.SetNewArray(&newArray_vectorlESFilegR);
      instance.SetDelete(&delete_vectorlESFilegR);
      instance.SetDeleteArray(&deleteArray_vectorlESFilegR);
      instance.SetDestructor(&destruct_vectorlESFilegR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<SFile> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<SFile>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlESFilegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<SFile>*)0x0)->GetClass();
      vectorlESFilegR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlESFilegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlESFilegR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SFile> : new vector<SFile>;
   }
   static void *newArray_vectorlESFilegR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SFile>[nElements] : new vector<SFile>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlESFilegR(void *p) {
      delete ((vector<SFile>*)p);
   }
   static void deleteArray_vectorlESFilegR(void *p) {
      delete [] ((vector<SFile>*)p);
   }
   static void destruct_vectorlESFilegR(void *p) {
      typedef vector<SFile> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<SFile>

namespace ROOT {
   static TClass *vectorlESDataSetgR_Dictionary();
   static void vectorlESDataSetgR_TClassManip(TClass*);
   static void *new_vectorlESDataSetgR(void *p = 0);
   static void *newArray_vectorlESDataSetgR(Long_t size, void *p);
   static void delete_vectorlESDataSetgR(void *p);
   static void deleteArray_vectorlESDataSetgR(void *p);
   static void destruct_vectorlESDataSetgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<SDataSet>*)
   {
      vector<SDataSet> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<SDataSet>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<SDataSet>", -2, "vector", 214,
                  typeid(vector<SDataSet>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlESDataSetgR_Dictionary, isa_proxy, 4,
                  sizeof(vector<SDataSet>) );
      instance.SetNew(&new_vectorlESDataSetgR);
      instance.SetNewArray(&newArray_vectorlESDataSetgR);
      instance.SetDelete(&delete_vectorlESDataSetgR);
      instance.SetDeleteArray(&deleteArray_vectorlESDataSetgR);
      instance.SetDestructor(&destruct_vectorlESDataSetgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<SDataSet> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const vector<SDataSet>*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlESDataSetgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<SDataSet>*)0x0)->GetClass();
      vectorlESDataSetgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlESDataSetgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlESDataSetgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SDataSet> : new vector<SDataSet>;
   }
   static void *newArray_vectorlESDataSetgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<SDataSet>[nElements] : new vector<SDataSet>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlESDataSetgR(void *p) {
      delete ((vector<SDataSet>*)p);
   }
   static void deleteArray_vectorlESDataSetgR(void *p) {
      delete [] ((vector<SDataSet>*)p);
   }
   static void destruct_vectorlESDataSetgR(void *p) {
      typedef vector<SDataSet> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<SDataSet>

namespace ROOT {
   static TClass *maplEintcOvectorlESTreegRsPgR_Dictionary();
   static void maplEintcOvectorlESTreegRsPgR_TClassManip(TClass*);
   static void *new_maplEintcOvectorlESTreegRsPgR(void *p = 0);
   static void *newArray_maplEintcOvectorlESTreegRsPgR(Long_t size, void *p);
   static void delete_maplEintcOvectorlESTreegRsPgR(void *p);
   static void deleteArray_maplEintcOvectorlESTreegRsPgR(void *p);
   static void destruct_maplEintcOvectorlESTreegRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<int,vector<STree> >*)
   {
      map<int,vector<STree> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<int,vector<STree> >));
      static ::ROOT::TGenericClassInfo 
         instance("map<int,vector<STree> >", -2, "map", 96,
                  typeid(map<int,vector<STree> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEintcOvectorlESTreegRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(map<int,vector<STree> >) );
      instance.SetNew(&new_maplEintcOvectorlESTreegRsPgR);
      instance.SetNewArray(&newArray_maplEintcOvectorlESTreegRsPgR);
      instance.SetDelete(&delete_maplEintcOvectorlESTreegRsPgR);
      instance.SetDeleteArray(&deleteArray_maplEintcOvectorlESTreegRsPgR);
      instance.SetDestructor(&destruct_maplEintcOvectorlESTreegRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<int,vector<STree> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_(Init) = GenerateInitInstanceLocal((const map<int,vector<STree> >*)0x0); R__UseDummy(_R__UNIQUE_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEintcOvectorlESTreegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<int,vector<STree> >*)0x0)->GetClass();
      maplEintcOvectorlESTreegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEintcOvectorlESTreegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEintcOvectorlESTreegRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,vector<STree> > : new map<int,vector<STree> >;
   }
   static void *newArray_maplEintcOvectorlESTreegRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,vector<STree> >[nElements] : new map<int,vector<STree> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEintcOvectorlESTreegRsPgR(void *p) {
      delete ((map<int,vector<STree> >*)p);
   }
   static void deleteArray_maplEintcOvectorlESTreegRsPgR(void *p) {
      delete [] ((map<int,vector<STree> >*)p);
   }
   static void destruct_maplEintcOvectorlESTreegRsPgR(void *p) {
      typedef map<int,vector<STree> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<int,vector<STree> >

namespace {
  void TriggerDictionaryInitialization_SFrameCore_Dict_Impl() {
    static const char* headers[] = {
"include/SCycleBaseConfig.h",
"include/SParLocator.h",
"include/SLogWriter.h",
"include/SInputData.h",
"include/ISCycleBaseNTuple.h",
"include/SErrorHandler.h",
"include/SError.h",
"include/SLogger.h",
"include/SCycleStatistics.h",
"include/SFileMerger.h",
"include/ISCycleBaseHist.h",
"include/SCycleBaseBase.h",
"include/ISCycleBase.h",
"include/SOutputFile.h",
"include/SCycleBaseHist.h",
"include/SCycleOutput.h",
"include/SMsgType.h",
"include/STreeType.h",
"include/SCycleBase.h",
"include/SCycleController.h",
"include/SPointer.h",
"include/SProofManager.h",
"include/ISCycleBaseConfig.h",
"include/SCycleBaseNTuple.h",
"include/SCycleConfig.h",
"include/SCycleBaseExec.h",
"include/STreeTypeDecoder.h",
"include/SGeneratorCut.h",
"include/SConstants.h",
0
    };
    static const char* includePaths[] = {
"/mnt/t3nfs01/data01/shome/ineuteli/analysis/SFrameAnalysis_Moriond/SFrame",
"./",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/lcg/root/6.06.00-ikhhed4/include",
"/mnt/t3nfs01/data01/shome/ineuteli/analysis/SFrameAnalysis_Moriond/SFrame/core/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "SFrameCore_Dict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  SGeneratorCut;
namespace std{template <typename _Tp> class __attribute__((annotate("$clingAutoload$string")))  allocator;
}
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  SDataSet;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  SFile;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  STree;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  SInputData;
namespace std{template <class _CharT> struct __attribute__((annotate("$clingAutoload$string")))  char_traits;
}
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  SCycleConfig;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseHist.h")))  SCycleOutput;
class __attribute__((annotate("$clingAutoload$include/SCycleStatistics.h")))  SCycleStatistics;
class __attribute__((annotate("$clingAutoload$include/SOutputFile.h")))  SOutputFile;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  ISCycleBaseConfig;
class __attribute__((annotate("$clingAutoload$include/ISCycleBaseHist.h")))  ISCycleBaseHist;
class __attribute__((annotate("$clingAutoload$include/ISCycleBaseNTuple.h")))  ISCycleBaseNTuple;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  SCycleBaseBase;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseConfig.h")))  SCycleBaseConfig;
class __attribute__((annotate("$clingAutoload$include/SCycleBaseHist.h")))  SCycleBaseHist;
class __attribute__((annotate("$clingAutoload$include/SCycleBase.h")))  SCycleBaseNTuple;
class __attribute__((annotate("$clingAutoload$include/ISCycleBase.h")))  SCycleBaseExec;
class __attribute__((annotate("$clingAutoload$include/ISCycleBase.h")))  ISCycleBase;
class __attribute__((annotate("$clingAutoload$include/SCycleBase.h")))  SCycleBase;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "SFrameCore_Dict dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "include/SCycleBaseConfig.h"
#include "include/SParLocator.h"
#include "include/SLogWriter.h"
#include "include/SInputData.h"
#include "include/ISCycleBaseNTuple.h"
#include "include/SErrorHandler.h"
#include "include/SError.h"
#include "include/SLogger.h"
#include "include/SCycleStatistics.h"
#include "include/SFileMerger.h"
#include "include/ISCycleBaseHist.h"
#include "include/SCycleBaseBase.h"
#include "include/ISCycleBase.h"
#include "include/SOutputFile.h"
#include "include/SCycleBaseHist.h"
#include "include/SCycleOutput.h"
#include "include/SMsgType.h"
#include "include/STreeType.h"
#include "include/SCycleBase.h"
#include "include/SCycleController.h"
#include "include/SPointer.h"
#include "include/SProofManager.h"
#include "include/ISCycleBaseConfig.h"
#include "include/SCycleBaseNTuple.h"
#include "include/SCycleConfig.h"
#include "include/SCycleBaseExec.h"
#include "include/STreeTypeDecoder.h"
#include "include/SGeneratorCut.h"
#include "include/SConstants.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"ISCycleBase", payloadCode, "@",
"ISCycleBaseConfig", payloadCode, "@",
"ISCycleBaseHist", payloadCode, "@",
"ISCycleBaseNTuple", payloadCode, "@",
"SCycleBase", payloadCode, "@",
"SCycleBaseBase", payloadCode, "@",
"SCycleBaseConfig", payloadCode, "@",
"SCycleBaseExec", payloadCode, "@",
"SCycleBaseHist", payloadCode, "@",
"SCycleBaseNTuple", payloadCode, "@",
"SCycleConfig", payloadCode, "@",
"SCycleOutput", payloadCode, "@",
"SCycleStatistics", payloadCode, "@",
"SDataSet", payloadCode, "@",
"SFile", payloadCode, "@",
"SGeneratorCut", payloadCode, "@",
"SInputData", payloadCode, "@",
"SOutputFile", payloadCode, "@",
"STree", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("SFrameCore_Dict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_SFrameCore_Dict_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_SFrameCore_Dict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_SFrameCore_Dict() {
  TriggerDictionaryInitialization_SFrameCore_Dict_Impl();
}
