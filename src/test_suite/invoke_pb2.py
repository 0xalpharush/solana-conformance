import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

_sym_db = _symbol_database.Default()
from . import context_pb2 as context__pb2
from . import txn_pb2 as txn__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="invoke.proto",
    package="org.solana.sealevel.v1",
    syntax="proto3",
    serialized_pb=_b(
        '\n\x0cinvoke.proto\x12\x16org.solana.sealevel.v1\x1a\rcontext.proto\x1a\ttxn.proto"B\n\tInstrAcct\x12\r\n\x05index\x18\x01 \x01(\r\x12\x13\n\x0bis_writable\x18\x02 \x01(\x08\x12\x11\n\tis_signer\x18\x03 \x01(\x08"ã\x02\n\x0cInstrContext\x12\x12\n\nprogram_id\x18\x01 \x01(\x0c\x123\n\x08accounts\x18\x03 \x03(\x0b2!.org.solana.sealevel.v1.AcctState\x129\n\x0einstr_accounts\x18\x04 \x03(\x0b2!.org.solana.sealevel.v1.InstrAcct\x12\x0c\n\x04data\x18\x05 \x01(\x0c\x12\x10\n\x08cu_avail\x18\x06 \x01(\x04\x127\n\x0btxn_context\x18\x07 \x01(\x0b2".org.solana.sealevel.v1.TxnContext\x129\n\x0cslot_context\x18\x08 \x01(\x0b2#.org.solana.sealevel.v1.SlotContext\x12;\n\repoch_context\x18\t \x01(\x0b2$.org.solana.sealevel.v1.EpochContext"\x97\x01\n\x0cInstrEffects\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x12\n\ncustom_err\x18\x02 \x01(\r\x12<\n\x11modified_accounts\x18\x03 \x03(\x0b2!.org.solana.sealevel.v1.AcctState\x12\x10\n\x08cu_avail\x18\x04 \x01(\x04\x12\x13\n\x0breturn_data\x18\x05 \x01(\x0c"y\n\x0cInstrFixture\x123\n\x05input\x18\x01 \x01(\x0b2$.org.solana.sealevel.v1.InstrContext\x124\n\x06output\x18\x02 \x01(\x0b2$.org.solana.sealevel.v1.InstrEffectsb\x06proto3'
    ),
    dependencies=[context__pb2.DESCRIPTOR, txn__pb2.DESCRIPTOR],
)
_INSTRACCT = _descriptor.Descriptor(
    name="InstrAcct",
    full_name="org.solana.sealevel.v1.InstrAcct",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="index",
            full_name="org.solana.sealevel.v1.InstrAcct.index",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="is_writable",
            full_name="org.solana.sealevel.v1.InstrAcct.is_writable",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="is_signer",
            full_name="org.solana.sealevel.v1.InstrAcct.is_signer",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=66,
    serialized_end=132,
)
_INSTRCONTEXT = _descriptor.Descriptor(
    name="InstrContext",
    full_name="org.solana.sealevel.v1.InstrContext",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="program_id",
            full_name="org.solana.sealevel.v1.InstrContext.program_id",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="accounts",
            full_name="org.solana.sealevel.v1.InstrContext.accounts",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="instr_accounts",
            full_name="org.solana.sealevel.v1.InstrContext.instr_accounts",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="org.solana.sealevel.v1.InstrContext.data",
            index=3,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="cu_avail",
            full_name="org.solana.sealevel.v1.InstrContext.cu_avail",
            index=4,
            number=6,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="txn_context",
            full_name="org.solana.sealevel.v1.InstrContext.txn_context",
            index=5,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="slot_context",
            full_name="org.solana.sealevel.v1.InstrContext.slot_context",
            index=6,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="epoch_context",
            full_name="org.solana.sealevel.v1.InstrContext.epoch_context",
            index=7,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=135,
    serialized_end=490,
)
_INSTREFFECTS = _descriptor.Descriptor(
    name="InstrEffects",
    full_name="org.solana.sealevel.v1.InstrEffects",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="result",
            full_name="org.solana.sealevel.v1.InstrEffects.result",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="custom_err",
            full_name="org.solana.sealevel.v1.InstrEffects.custom_err",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="modified_accounts",
            full_name="org.solana.sealevel.v1.InstrEffects.modified_accounts",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="cu_avail",
            full_name="org.solana.sealevel.v1.InstrEffects.cu_avail",
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="return_data",
            full_name="org.solana.sealevel.v1.InstrEffects.return_data",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=493,
    serialized_end=644,
)
_INSTRFIXTURE = _descriptor.Descriptor(
    name="InstrFixture",
    full_name="org.solana.sealevel.v1.InstrFixture",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="input",
            full_name="org.solana.sealevel.v1.InstrFixture.input",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="output",
            full_name="org.solana.sealevel.v1.InstrFixture.output",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=646,
    serialized_end=767,
)
_INSTRCONTEXT.fields_by_name["accounts"].message_type = context__pb2._ACCTSTATE
_INSTRCONTEXT.fields_by_name["instr_accounts"].message_type = _INSTRACCT
_INSTRCONTEXT.fields_by_name["txn_context"].message_type = txn__pb2._TXNCONTEXT
_INSTRCONTEXT.fields_by_name["slot_context"].message_type = context__pb2._SLOTCONTEXT
_INSTRCONTEXT.fields_by_name["epoch_context"].message_type = context__pb2._EPOCHCONTEXT
_INSTREFFECTS.fields_by_name["modified_accounts"].message_type = context__pb2._ACCTSTATE
_INSTRFIXTURE.fields_by_name["input"].message_type = _INSTRCONTEXT
_INSTRFIXTURE.fields_by_name["output"].message_type = _INSTREFFECTS
DESCRIPTOR.message_types_by_name["InstrAcct"] = _INSTRACCT
DESCRIPTOR.message_types_by_name["InstrContext"] = _INSTRCONTEXT
DESCRIPTOR.message_types_by_name["InstrEffects"] = _INSTREFFECTS
DESCRIPTOR.message_types_by_name["InstrFixture"] = _INSTRFIXTURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
InstrAcct = _reflection.GeneratedProtocolMessageType(
    "InstrAcct",
    (_message.Message,),
    dict(DESCRIPTOR=_INSTRACCT, __module__="invoke_pb2"),
)
_sym_db.RegisterMessage(InstrAcct)
InstrContext = _reflection.GeneratedProtocolMessageType(
    "InstrContext",
    (_message.Message,),
    dict(DESCRIPTOR=_INSTRCONTEXT, __module__="invoke_pb2"),
)
_sym_db.RegisterMessage(InstrContext)
InstrEffects = _reflection.GeneratedProtocolMessageType(
    "InstrEffects",
    (_message.Message,),
    dict(DESCRIPTOR=_INSTREFFECTS, __module__="invoke_pb2"),
)
_sym_db.RegisterMessage(InstrEffects)
InstrFixture = _reflection.GeneratedProtocolMessageType(
    "InstrFixture",
    (_message.Message,),
    dict(DESCRIPTOR=_INSTRFIXTURE, __module__="invoke_pb2"),
)
_sym_db.RegisterMessage(InstrFixture)
