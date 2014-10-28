#include <node.h>
#include <nan.h>
#include <yajl/yajl_version.h>

using v8::FunctionTemplate;
using v8::Handle;
using v8::Object;
using v8::String;
using v8::Number;

NAN_METHOD(getYajlVersion) {
  NanScope();
  NanReturnValue(NanNew<Number>(YAJL_VERSION));
}

void InitAll(Handle<Object> exports) {
  exports->Set(NanNew<String>("getYajlVersion"),
               NanNew<FunctionTemplate>(getYajlVersion)->GetFunction());
}

NODE_MODULE(yajl, InitAll)
