#include <nan.h>
#include <yajl/yajl_version.h>

using namespace v8;

NAN_METHOD(Method) {
  NanScope();
  NanReturnValue(NanNew(YAJL_VERSION));
}

void Init(Handle<Object> exports) {
  exports->Set(NanNew("getYajlVersion"), NanNew<FunctionTemplate>(Method)->GetFunction());
}

NODE_MODULE(getYajlVersion, Init)