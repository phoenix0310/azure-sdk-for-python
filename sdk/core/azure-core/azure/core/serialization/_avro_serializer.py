# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from typing import BinaryIO, Optional, Any, Union, Type

from ._object_serializer import ObjectSerializer


class AvroObjectSerializer(ObjectSerializer):

    def __init__(self, codec=None):
        """A Avro serializer using avro lib from Apache.

        :param str codec: The writer codec. If None, let the avro library decides.
        """
        try:
            import avro  # pylint: disable=unused-import
        except ImportError:
            raise ImportError("In order to create a AvroObjectSerializer you need to install the 'avro' library")

        self._writer_codec = codec

    def serialize(
        self,
        stream,  # type: BinaryIO
        value,  # type: ObjectType
        schema=None,  # type: Optional[Any]
    ):
        # type: (...) -> None
        """Convert the provided value to it's binary representation and write it to the stream.

        Schema must be a Avro RecordSchema:
        https://avro.apache.org/docs/1.10.0/gettingstartedpython.html#Defining+a+schema

        :param stream: A stream of bytes or bytes directly
        :type stream: BinaryIO
        :param value: An object to serialize
        :param schema: A Avro RecordSchema
        """
        if not schema:
            raise ValueError("Schema is required in Avro serializer.")

        from avro.datafile import DataFileWriter
        from avro.io import DatumWriter

        kwargs = {}
        if self._writer_codec:
            kwargs['codec'] = self._writer_codec

        writer = DataFileWriter(
            stream,
            DatumWriter(),
            schema,
            **kwargs
        )
        writer.append(value)
        writer.flush()

    def deserialize(
        self,
        data,  # type: Union[bytes, BinaryIO]
        return_type=None,  # type: Optional[Type[ObjectType]]
    ):
        # type: (...) -> ObjectType
        """Read the binary representation into a specific type.

        Return type will be ignored, since the schema is deduced from the provided bytes.

        :param data: A stream of bytes or bytes directly
        :type data: BinaryIO or bytes
        :param return_type: Return type is not supported in the Avro serializer.
        :returns: An instanciated object
        :rtype: ObjectType
        """
        if not hasattr(data, 'read'):
            from io import BytesIO
            data = BytesIO(data)

        from avro.datafile import DataFileReader
        from avro.io import DatumReader

        reader = DataFileReader(
            data,
            DatumReader()
        )
        obj = next(reader)
        try:
            next(reader)
            raise ValueError("This avro stream is multiple object stream")
        except StopIteration:
            pass
        reader.close()
        return obj