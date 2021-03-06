liesl API
----------

The main API can be accessed directly from liesl using e.g.

.. code-block:: python

   import liesl
   stream = liesl.print_available_streams()

Stream Handling
***************

Detect and print information about available streams.

.. automodule:: liesl.streams.finder
   :members: open_stream, open_streaminfo, print_available_streams, get_streams_matching, get_streaminfos_matching

.. automodule:: liesl.streams.convert
   :members: inlet_to_dict, get_channel_map

.. automodule:: liesl.streams
   :members: localhostname, localhost, localip


Buffers
*******

.. automodule:: liesl.buffers.ringbuffer
   :members: RingBuffer

.. automodule:: liesl.buffers.blockbuffer
   :members: SimpleBlockBuffer

.. automodule:: liesl.buffers.response
   :members: Response, MockResponse


Recording
*********

.. automodule:: liesl.files.run
   :members: Run

.. automodule:: liesl.files.session
   :members: Session, Recorder

Loading
*******

.. automodule:: liesl.files.xdf.load
   :members: XDFFile, XDFStream
   
.. automodule:: liesl.files.xdf.inspect_xdf
   :members: peek


