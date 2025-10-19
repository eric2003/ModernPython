import re

text = """VTK::DICOM;
VTK::zlib;VTK::MomentInvariants;VTK::eigen;VTK::kissfft;VTK::WrappingTools;
VTK::ViewsContext2D;VTK::loguru;VTK::TestingRendering;VTK::TestingCore;
VTK::vtksys;VTK::ViewsInfovis;VTK::CommonColor;VTK::RenderingVolumeOpenGL2;
VTK::glew;VTK::opengl;VTK::RenderingLabel;VTK::octree;VTK::RenderingLOD;
VTK::RenderingLICOpenGL2;VTK::RenderingImage;VTK::RenderingContextOpenGL2;
VTK::RenderingCellGrid;VTK::IOVeraOut;VTK::hdf5;VTK::IOTecplotTable;
VTK::utf8;
VTK::IOSegY;VTK::IOParallelXML;VTK::IOParallel;VTK::jsoncpp;VTK::IOPLY;
VTK::IOOggTheora;VTK::theora;VTK::ogg;VTK::IONetCDF;VTK::netcdf;
VTK::libproj;
VTK::IOMotionFX;VTK::pegtl;VTK::IOMINC;VTK::IOLSDyna;VTK::IOInfovis;
VTK::libxml2;VTK::IOImport;VTK::IOIOSS;VTK::fmt;VTK::ioss;VTK::cgns;
VTK::exodusII;VTK::IOFLUENTCFF;VTK::IOVideo;VTK::IOMovie;
VTK::IOExportPDF;VTK::libharu;VTK::IOExportGL2PS;VTK::RenderingGL2PSOpenGL2;
VTK::gl2ps;VTK::png;VTK::IOExport;VTK::RenderingVtkJS;VTK::nlohmannjson;
VTK::RenderingSceneGraph;VTK::IOExodus;VTK::IOEnSight;VTK::IOCityGML;
VTK::pugixml;
VTK::IOChemistry;VTK::IOCesium3DTiles;VTK::IOGeometry;VTK::IOCellGrid;
VTK::IOCONVERGECFD;VTK::IOHDF;VTK::IOCGNSReader;VTK::IOAsynchronous;
VTK::IOAMR;VTK::InteractionImage;VTK::ImagingStencil;VTK::ImagingStatistics;
VTK::ImagingMorphological;VTK::ImagingMath;VTK::ImagingFourier;
VTK::IOSQL;VTK::sqlite;VTK::GeovisCore;VTK::InfovisLayout;VTK::ViewsCore;
VTK::InteractionWidgets;VTK::RenderingVolume;VTK::RenderingAnnotation;
VTK::ImagingHybrid;VTK::ImagingColor;VTK::InteractionStyle;
VTK::FiltersTopology;
VTK::FiltersTensor;VTK::FiltersSelection;VTK::FiltersSMP;
VTK::FiltersReduction;
VTK::FiltersProgrammable;VTK::FiltersPoints;VTK::FiltersParallelImaging;
VTK::FiltersImaging;VTK::ImagingGeneral;VTK::FiltersGeometryPreview;
VTK::FiltersGeneric;VTK::FiltersFlowPaths;VTK::FiltersCellGrid;
VTK::FiltersAMR;
VTK::FiltersParallel;VTK::FiltersTexture;VTK::FiltersModeling;
VTK::DomainsChemistryOpenGL2;VTK::RenderingOpenGL2;
VTK::RenderingHyperTreeGrid;
VTK::RenderingUI;VTK::FiltersHybrid;VTK::DomainsChemistry;VTK::ChartsCore;
VTK::InfovisCore;VTK::FiltersExtraction;VTK::ParallelDIY;VTK::diy2;
VTK::IOXML;VTK::IOXMLParser;VTK::expat;VTK::ParallelCore;VTK::IOLegacy;
VTK::IOCore;VTK::doubleconversion;VTK::lz4;VTK::lzma;VTK::fast_float;
VTK::FiltersStatistics;VTK::FiltersHyperTree;VTK::ImagingSources;
VTK::IOImage;VTK::DICOMParser;VTK::jpeg;VTK::metaio;VTK::tiff;
VTK::RenderingContext2D;VTK::RenderingFreeType;VTK::freetype;VTK::kwiml;
VTK::RenderingCore;VTK::FiltersSources;VTK::ImagingCore;VTK::FiltersGeneral;
VTK::FiltersVerdict;VTK::verdict;VTK::FiltersGeometry;
VTK::CommonComputationalGeometry;
VTK::FiltersCore;VTK::CommonExecutionModel;
VTK::CommonDataModel;VTK::CommonSystem;
VTK::CommonMisc;VTK::exprtk;VTK::CommonTransforms;
VTK::CommonMath;VTK::CommonCore"""
words = re.split(';|,| |\n|VTK::', text)
new_list = [item for item in words if item]
#print(words)
print(new_list)