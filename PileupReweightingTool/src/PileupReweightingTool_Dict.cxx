// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME srcdIPileupReweightingTool_Dict

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
#include "include/PileupReweightingTool.h"
#include "include/PUWeight.h"

// Header files passed via #pragma extra_include

namespace {
  void TriggerDictionaryInitialization_PileupReweightingTool_Dict_Impl() {
    static const char* headers[] = {
"include/PileupReweightingTool.h",
"include/PUWeight.h",
0
    };
    static const char* includePaths[] = {
"/mnt/t3nfs01/data01/shome/ineuteli/analysis/SFrameAnalysis_Moriond/SFrame",
"./",
"/cvmfs/cms.cern.ch/slc6_amd64_gcc530/lcg/root/6.06.00-ikhhed4/include",
"/mnt/t3nfs01/data01/shome/ineuteli/analysis/SFrameAnalysis_Moriond/PileupReweightingTool/",
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "PileupReweightingTool_Dict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "PileupReweightingTool_Dict dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "include/PileupReweightingTool.h"
#include "include/PUWeight.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("PileupReweightingTool_Dict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_PileupReweightingTool_Dict_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_PileupReweightingTool_Dict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_PileupReweightingTool_Dict() {
  TriggerDictionaryInitialization_PileupReweightingTool_Dict_Impl();
}
