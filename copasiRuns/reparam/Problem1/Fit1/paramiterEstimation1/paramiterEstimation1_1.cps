<COPASI xmlns="http://www.copasi.org/static/schema" versionMajor="4" versionMinor="27" versionDevel="217" copasiSourcesModified="0">
  <ListOfFunctions>
    <Function key="Function_6" name="Constant flux (irreversible)" type="PreDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_6">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        v
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_49" name="v" order="0" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_13" name="Mass action (irreversible)" type="MassAction" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:CopasiMT="http://www.copasi.org/RDF/MiriamTerms#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_13">
            <CopasiMT:is rdf:resource="urn:miriam:obo.sbo:SBO:0000163"/>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Comment>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <b>Mass action rate law for irreversible reactions</b>
          <p>
Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of one reactant.
</p>
        </body>
      </Comment>
      <Expression>
        k1*PRODUCT&lt;substrate_i&gt;
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_80" name="k1" order="0" role="constant"/>
        <ParameterDescription key="FunctionParameter_81" name="substrate" order="1" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_40" name="Hill Cooperativity_1" type="UserDefined" reversible="unspecified">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_40">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        V*(substrate/Shalve)^h/(1+(substrate/Shalve)^h)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_262" name="substrate" order="0" role="variable"/>
        <ParameterDescription key="FunctionParameter_261" name="Shalve" order="1" role="variable"/>
        <ParameterDescription key="FunctionParameter_250" name="V" order="2" role="variable"/>
        <ParameterDescription key="FunctionParameter_265" name="h" order="3" role="variable"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_41" name="Function for NAD increase by AMPK" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_41">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        AMPK_driven_NAD_source*"Hill Cooperativity_1"(Delay_in_NAD_increase,_NAD_increase_by_AMPK_Shalve,_NAD_increase_by_AMPK_V,_NAD_increase_by_AMPK_h)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_292" name="AMPK_driven_NAD_source" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_293" name="Delay_in_NAD_increase" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_294" name="_NAD_increase_by_AMPK_Shalve" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_295" name="_NAD_increase_by_AMPK_V" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_296" name="_NAD_increase_by_AMPK_h" order="4" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_42" name="Function for NAD decrease by AMPK" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_42">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        AMPK_driven_NegReg_source*"Hill Cooperativity_1"(Delay_in_NAD_increase,_NAD_increase_by_AMPK_Shalve,_NAD_increase_by_AMPK_V,_NAD_increase_by_AMPK_h)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_302" name="AMPK_driven_NegReg_source" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_303" name="Delay_in_NAD_increase" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_304" name="_NAD_increase_by_AMPK_Shalve" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_305" name="_NAD_increase_by_AMPK_V" order="3" role="constant"/>
        <ParameterDescription key="FunctionParameter_306" name="_NAD_increase_by_AMPK_h" order="4" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_43" name="Hill Cooperativity_1_1" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_43">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        _Deacetylation_activity_V*(SIRT1_activity/_Deacetylation_activity_Shalve)^_Deacetylation_activity_h/(1+(SIRT1_activity/_Deacetylation_activity_Shalve)^_Deacetylation_activity_h)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_291" name="SIRT1_activity" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_312" name="_Deacetylation_activity_Shalve" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_313" name="_Deacetylation_activity_V" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_314" name="_Deacetylation_activity_h" order="3" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_44" name="Hill Cooperativity_1_2" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_44">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        _DUMMY_REACTION_Delay_AICAR_stimulus_V*(AICAR_treatment/_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve)^_DUMMY_REACTION_Delay_AICAR_stimulus_h/(1+(AICAR_treatment/_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve)^_DUMMY_REACTION_Delay_AICAR_stimulus_h)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_323" name="AICAR_treatment" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_324" name="_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_325" name="_DUMMY_REACTION_Delay_AICAR_stimulus_V" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_326" name="_DUMMY_REACTION_Delay_AICAR_stimulus_h" order="3" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_45" name="Basal deacetylation function_1" type="UserDefined" reversible="unspecified">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_45">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        _Basal_PGC1a_deacetylation_v+SIRT1_activity*0.75
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_321" name="SIRT1_activity" order="0" role="modifier"/>
        <ParameterDescription key="FunctionParameter_320" name="_Basal_PGC1a_deacetylation_v" order="1" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_46" name="Function for Glucose influx" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_46">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        Glucose_source
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_336" name="Glucose_source" order="0" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_47" name="Hill Cooperativity_1_3" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_47">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        _Glucose_DUMMY_REACTION_delay_V*(Glucose/_Glucose_DUMMY_REACTION_delay_Shalve)^_Glucose_DUMMY_REACTION_delay_h/(1+(Glucose/_Glucose_DUMMY_REACTION_delay_Shalve)^_Glucose_DUMMY_REACTION_delay_h)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_343" name="Glucose" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_344" name="_Glucose_DUMMY_REACTION_delay_Shalve" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_345" name="_Glucose_DUMMY_REACTION_delay_V" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_346" name="_Glucose_DUMMY_REACTION_delay_h" order="3" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_48" name="Hill Cooperativity_1_4" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_48">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        _NR_NMN_supplementation_V*(NR_NMN/_NR_NMN_supplementation_Shalve)^_NR_NMN_supplementation_h/(1+(NR_NMN/_NR_NMN_supplementation_Shalve)^_NR_NMN_supplementation_h)
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_357" name="NR_NMN" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_358" name="_NR_NMN_supplementation_Shalve" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_359" name="_NR_NMN_supplementation_V" order="2" role="constant"/>
        <ParameterDescription key="FunctionParameter_360" name="_NR_NMN_supplementation_h" order="3" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
  </ListOfFunctions>
  <Model key="Model_1" name="Mitonuclear communication model" simulationType="time" timeUnit="h" volumeUnit="ml" areaUnit="m&#178;" lengthUnit="m" quantityUnit="mmol" type="deterministic" avogadroConstant="6.0221417899999999e+23">
    <MiriamAnnotation>
      <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="#Model_1">
          <dcterms:created>
            <rdf:Description>
              <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
            </rdf:Description>
          </dcterms:created>
        </rdf:Description>
      </rdf:RDF>
    </MiriamAnnotation>
    <ListOfCompartments>
      <Compartment key="Compartment_0" name="compartment_" simulationType="fixed" dimensionality="3" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Compartment_0">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Compartment>
    </ListOfCompartments>
    <ListOfMetabolites>
      <Metabolite key="Metabolite_0" name="AMPK" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+21">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_0">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_1" name="AMPK-P" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_1">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_2" name="PGC1a" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+21">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_2">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_3" name="PGC1a-P" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_3">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_4" name="PGC1a_deacet" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_4">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_5" name="SIRT1_activity" simulationType="assignment" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_5">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <Expression>
          &lt;CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[SIRT1],Reference=Concentration&gt;*&lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[quantity to number factor],Reference=Value&gt;*&lt;CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Reference=Volume&gt;*&lt;CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD],Reference=Concentration&gt;*&lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[quantity to number factor],Reference=Value&gt;*&lt;CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Reference=Volume&gt;
        </Expression>
      </Metabolite>
      <Metabolite key="Metabolite_6" name="SIRT1" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_6">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_7" name="NAD" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_7">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_8" name="Delay_in_NAD_increase" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_8">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_9" name="PARP1" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_9">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_10" name="Deacetylation_Delay" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_10">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_11" name="AICAR_Delay" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_11">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_12" name="AICAR" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_12">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_13" name="Glucose" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="1.5055354475000002e+22">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_13">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_14" name="GlucoseDelay" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_14">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_15" name="NAD_NegReg" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_15">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_16" name="NR-NMN" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_16">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_17" name="AMPK_driven_NAD_source" simulationType="fixed" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_17">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_18" name="AMPK_driven_NegReg_source" simulationType="fixed" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+20">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_18">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_19" name="Glucose_source" simulationType="fixed" compartment="Compartment_0" addNoise="false" particle_numbers="1.5055354475000002e+22">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_19">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
    </ListOfMetabolites>
    <ListOfModelValues>
      <ModelValue key="ModelValue_0" name="quantity to number factor" simulationType="fixed" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_0">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_1" name="NAD_fold_increase" simulationType="assignment" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_1">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <Expression>
          &lt;CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD],Reference=Concentration&gt;/&lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[initial_NAD],Reference=Value&gt;
        </Expression>
      </ModelValue>
      <ModelValue key="ModelValue_2" name="initial_NAD" simulationType="fixed" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_2">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <InitialExpression>
          &lt;CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD],Reference=InitialConcentration&gt;
        </InitialExpression>
      </ModelValue>
      <ModelValue key="ModelValue_3" name="_AMPK_phosphorylation_k1" simulationType="fixed" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_3">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_4" name="_AMPK_dephosphorylation_k1" simulationType="fixed" addNoise="false" initial_value="5.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_4">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_5" name="_PGC1a_phosphorylation_k1" simulationType="fixed" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_5">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_6" name="_PGC1a_dephosphorylation_k1" simulationType="fixed" addNoise="false" initial_value="10.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_6">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_7" name="_Induced_PGC1a_deacetylation_k1" simulationType="fixed" addNoise="false" initial_value="1.913">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_7">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_8" name="_PGC1a_acetylation_k1" simulationType="fixed" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_8">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_9" name="_DUMMY_REACTION_Delay_in_NAD_Increase_k1" simulationType="fixed" addNoise="false" initial_value="10.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_9">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_10" name="_DUMMY_REACTION_Delay_in_NAD_Increase_2_k1" simulationType="fixed" addNoise="false" initial_value="10.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_10">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_11" name="_NAD_synthesis_v" simulationType="fixed" addNoise="false" initial_value="0.12">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_11">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_12" name="_NAD_utilisation_k1" simulationType="fixed" addNoise="false" initial_value="0.045">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_12">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_13" name="_NAD_utilisation_by_PARP_k1" simulationType="fixed" addNoise="false" initial_value="0.075">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_13">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_14" name="_NAD_increase_by_AMPK_Shalve" simulationType="fixed" addNoise="false" initial_value="1.45">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_14">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_15" name="_NAD_increase_by_AMPK_V" simulationType="fixed" addNoise="false" initial_value="0.316228">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_15">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_16" name="_NAD_increase_by_AMPK_h" simulationType="fixed" addNoise="false" initial_value="100.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_16">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_17" name="_Deacetylation_activity_Shalve" simulationType="fixed" addNoise="false" initial_value="3.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_17">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_18" name="_Deacetylation_activity_V" simulationType="fixed" addNoise="false" initial_value="0.01">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_18">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_19" name="_Deacetylation_activity_h" simulationType="fixed" addNoise="false" initial_value="30.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_19">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_20" name="_DUMMY_REACTION_AICAR_stimulus_removal_k1" simulationType="fixed" addNoise="false" initial_value="0.293095">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_20">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_21" name="_AMPK_phosphorylation_induced_by_AICAR_k1" simulationType="fixed" addNoise="false" initial_value="3.98586">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_21">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_22" name="_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve" simulationType="fixed" addNoise="false" initial_value="0.6672">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_22">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_23" name="_DUMMY_REACTION_Delay_AICAR_stimulus_V" simulationType="fixed" addNoise="false" initial_value="0.167159">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_23">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_24" name="_DUMMY_REACTION_Delay_AICAR_stimulus_h" simulationType="fixed" addNoise="false" initial_value="9.23537">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_24">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_25" name="_Basal_PGC1a_deacetylation_v" simulationType="fixed" addNoise="false" initial_value="0.25">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_25">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_26" name="_DUMMY_REACTION_PGC1a_Deacetylation_Limiter_k1" simulationType="fixed" addNoise="false" initial_value="0.56472">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_26">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_27" name="_Glucose_induced_AMPK_dephosphorylation_k1" simulationType="fixed" addNoise="false" initial_value="5.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_27">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_28" name="_Glucose_utilisation_k1" simulationType="fixed" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_28">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_29" name="_Glucose_DUMMY_REACTION_delay_Shalve" simulationType="fixed" addNoise="false" initial_value="5.36174">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_29">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_30" name="_Glucose_DUMMY_REACTION_delay_V" simulationType="fixed" addNoise="false" initial_value="0.1013">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_30">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_31" name="_Glucose_DUMMY_REACTION_delay_h" simulationType="fixed" addNoise="false" initial_value="15.04">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_31">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_32" name="_Glucose_DUMMY_REACTION_delay_limiter_k1" simulationType="fixed" addNoise="false" initial_value="0.1">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_32">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_33" name="_NAD_negative_regulation_k1" simulationType="fixed" addNoise="false" initial_value="0.0609264">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_33">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_34" name="_DUMMY_REACTION_NegReg_disappearance_k1" simulationType="fixed" addNoise="false" initial_value="0.1">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_34">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_35" name="_NR_NMN_supplementation_Shalve" simulationType="fixed" addNoise="false" initial_value="100.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_35">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_36" name="_NR_NMN_supplementation_V" simulationType="fixed" addNoise="false" initial_value="0.10829">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_36">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_37" name="_NR_NMN_supplementation_h" simulationType="fixed" addNoise="false" initial_value="1.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_37">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
    </ListOfModelValues>
    <ListOfReactions>
      <Reaction key="Reaction_0" name="AMPK basal phosphorylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_0">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_0" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5385" name="k1" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_0"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_1" name="AMPK basal dephosphorylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_1">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_0" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5384" name="k1" value="5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_4"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_2" name="PGC1a phosphorylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_2">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
          <Substrate metabolite="Metabolite_2" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_3" stoichiometry="1"/>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5383" name="k1" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_5"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_1"/>
              <SourceParameter reference="Metabolite_2"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_3" name="PGC1a dephosphorylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_3">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_2" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5382" name="k1" value="10"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_6"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_4" name="PGC1a induced deacetylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_4">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_3" stoichiometry="1"/>
          <Substrate metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_4" stoichiometry="1"/>
          <Product metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5381" name="k1" value="1.913"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_7"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_3"/>
              <SourceParameter reference="Metabolite_10"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_5" name="PGC1a basal acetylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_5">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_4" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5380" name="k1" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_8"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_4"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_6" name="Delay Reaction NAD increase by AMPK" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_6">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_8" stoichiometry="1"/>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5379" name="k1" value="10"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_9"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_7" name="Dummy Reaction Delay_in_NAD_Increase Removal" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_7">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_5378" name="k1" value="10"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_10"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_8"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_8" name="NAD synthesis" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_8">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfProducts>
          <Product metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5377" name="v" value="0.12"/>
        </ListOfConstants>
        <KineticLaw function="Function_6" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_49">
              <SourceParameter reference="ModelValue_11"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_9" name="NAD utilisation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_9">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_5376" name="k1" value="0.045"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_12"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_7"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_10" name="NAD utilisation by PARP" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_10">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_7" stoichiometry="1"/>
          <Substrate metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5375" name="k1" value="0.075"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_13"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_7"/>
              <SourceParameter reference="Metabolite_9"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_11" name="NAD increase by AMPK" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_11">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_17" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5374" name="_NAD_increase_by_AMPK_Shalve" value="1.45"/>
          <Constant key="Parameter_5373" name="_NAD_increase_by_AMPK_V" value="0.316228"/>
          <Constant key="Parameter_5372" name="_NAD_increase_by_AMPK_h" value="100"/>
        </ListOfConstants>
        <KineticLaw function="Function_41" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_292">
              <SourceParameter reference="Metabolite_17"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_293">
              <SourceParameter reference="Metabolite_8"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_294">
              <SourceParameter reference="ModelValue_14"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_295">
              <SourceParameter reference="ModelValue_15"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_296">
              <SourceParameter reference="ModelValue_16"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_12" name="NAD decrease by AMPK" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_12">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_18" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_15" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5371" name="_NAD_increase_by_AMPK_Shalve" value="1.45"/>
          <Constant key="Parameter_5370" name="_NAD_increase_by_AMPK_V" value="0.316228"/>
          <Constant key="Parameter_5369" name="_NAD_increase_by_AMPK_h" value="100"/>
        </ListOfConstants>
        <KineticLaw function="Function_42" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_302">
              <SourceParameter reference="Metabolite_18"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_303">
              <SourceParameter reference="Metabolite_8"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_304">
              <SourceParameter reference="ModelValue_14"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_305">
              <SourceParameter reference="ModelValue_15"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_306">
              <SourceParameter reference="ModelValue_16"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_13" name="Delay Reaction Induced Deacetylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_13">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_10" stoichiometry="1"/>
          <Product metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5368" name="_Deacetylation_activity_Shalve" value="3"/>
          <Constant key="Parameter_5367" name="_Deacetylation_activity_V" value="0.01"/>
          <Constant key="Parameter_5366" name="_Deacetylation_activity_h" value="30"/>
        </ListOfConstants>
        <KineticLaw function="Function_43" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_291">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_312">
              <SourceParameter reference="ModelValue_17"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_313">
              <SourceParameter reference="ModelValue_18"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_314">
              <SourceParameter reference="ModelValue_19"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_14" name="Dummy Reaction AICAR Stimulus Removal" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_14">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_5365" name="k1" value="0.293095"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_20"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_11"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_15" name="AMPK induced phosphorylation by AICAR" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_15">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_11" stoichiometry="1"/>
          <Substrate metabolite="Metabolite_0" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5364" name="k1" value="3.98586"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_21"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_11"/>
              <SourceParameter reference="Metabolite_0"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_16" name="Delay Reaction AICAR Stimulus" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_16">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
          <Product metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5363" name="_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve" value="0.6672"/>
          <Constant key="Parameter_5362" name="_DUMMY_REACTION_Delay_AICAR_stimulus_V" value="0.167159"/>
          <Constant key="Parameter_5361" name="_DUMMY_REACTION_Delay_AICAR_stimulus_h" value="9.23537"/>
        </ListOfConstants>
        <KineticLaw function="Function_44" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_323">
              <SourceParameter reference="Metabolite_12"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_324">
              <SourceParameter reference="ModelValue_22"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_325">
              <SourceParameter reference="ModelValue_23"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_326">
              <SourceParameter reference="ModelValue_24"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_17" name="PGC1a basal deacetylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_17">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_4" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5360" name="_Basal_PGC1a_deacetylation_v" value="0.25"/>
        </ListOfConstants>
        <KineticLaw function="Function_45" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_321">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_320">
              <SourceParameter reference="ModelValue_25"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_18" name="Dummy Reaction Induced Deacetylation Delay Removal" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_18">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_5359" name="k1" value="0.56472"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_26"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_10"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_19" name="Glucose-induced AMPK dephosphorylation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_19">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_14" stoichiometry="1"/>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_0" stoichiometry="1"/>
          <Product metabolite="Metabolite_14" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5358" name="k1" value="5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_27"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_14"/>
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_20" name="Glucose influx" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_20">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_19" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_13" stoichiometry="1"/>
        </ListOfProducts>
        <KineticLaw function="Function_46" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_336">
              <SourceParameter reference="Metabolite_19"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_21" name="Glucose utilisation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_21">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_13" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_5357" name="k1" value="1"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_28"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_13"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_22" name="Delay Reaction Glucose Stimulus" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_22">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_13" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_14" stoichiometry="1"/>
          <Product metabolite="Metabolite_13" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5356" name="_Glucose_DUMMY_REACTION_delay_Shalve" value="5.36174"/>
          <Constant key="Parameter_5355" name="_Glucose_DUMMY_REACTION_delay_V" value="0.1013"/>
          <Constant key="Parameter_5354" name="_Glucose_DUMMY_REACTION_delay_h" value="15.04"/>
        </ListOfConstants>
        <KineticLaw function="Function_47" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_343">
              <SourceParameter reference="Metabolite_13"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_344">
              <SourceParameter reference="ModelValue_29"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_345">
              <SourceParameter reference="ModelValue_30"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_346">
              <SourceParameter reference="ModelValue_31"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_23" name="Dummy Reaction Glucose Delay Removal" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_23">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_14" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_5353" name="k1" value="0.1"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_32"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_14"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_24" name="NAD negative regulation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_24">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_7" stoichiometry="1"/>
          <Substrate metabolite="Metabolite_15" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_5352" name="k1" value="0.0609264"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_33"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_7"/>
              <SourceParameter reference="Metabolite_15"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_25" name="Dummy Reaction NegReg Removal" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_25">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_15" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfConstants>
          <Constant key="Parameter_5351" name="k1" value="0.1"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_34"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_15"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_26" name="NR/NMN supplementation" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_26">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_16" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5675" name="_NR_NMN_supplementation_Shalve" value="100"/>
          <Constant key="Parameter_5676" name="_NR_NMN_supplementation_V" value="0.10829"/>
          <Constant key="Parameter_5674" name="_NR_NMN_supplementation_h" value="1.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_48" unitType="Default" scalingCompartment="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_357">
              <SourceParameter reference="Metabolite_16"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_358">
              <SourceParameter reference="ModelValue_35"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_359">
              <SourceParameter reference="ModelValue_36"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_360">
              <SourceParameter reference="ModelValue_37"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
    </ListOfReactions>
    <ListOfModelParameterSets activeSet="ModelParameterSet_1">
      <ModelParameterSet key="ModelParameterSet_1" name="Initial State">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelParameterSet_1">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ModelParameterGroup cn="String=Initial Time" type="Group">
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model" value="0" type="Model" simulationType="time"/>
        </ModelParameterGroup>
        <ModelParameterGroup cn="String=Initial Compartment Sizes" type="Group">
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_]" value="1" type="Compartment" simulationType="fixed"/>
        </ModelParameterGroup>
        <ModelParameterGroup cn="String=Initial Species Values" type="Group">
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AMPK]" value="6.0221417900000003e+21" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AMPK-P]" value="6.0221417900000005e+20" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[PGC1a]" value="6.0221417900000003e+21" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[PGC1a-P]" value="6.0221417900000005e+20" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[PGC1a_deacet]" value="6.0221417900000005e+20" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[SIRT1_activity]" value="6.0221417900000005e+20" type="Species" simulationType="assignment"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[SIRT1]" value="6.0221417900000005e+20" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD]" value="6.0221417900000005e+20" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Delay_in_NAD_increase]" value="6.0221417900000005e+20" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[PARP1]" value="6.0221417900000005e+20" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Deacetylation_Delay]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AICAR_Delay]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AICAR]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Glucose]" value="1.5055354475000002e+22" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[GlucoseDelay]" value="6.0221417900000005e+20" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD_NegReg]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NR-NMN]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AMPK_driven_NAD_source]" value="6.0221417900000005e+20" type="Species" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AMPK_driven_NegReg_source]" value="6.0221417900000005e+20" type="Species" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Glucose_source]" value="1.5055354475000002e+22" type="Species" simulationType="fixed"/>
        </ModelParameterGroup>
        <ModelParameterGroup cn="String=Initial Global Quantities" type="Group">
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[quantity to number factor]" value="1" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[NAD_fold_increase]" value="1" type="ModelValue" simulationType="assignment"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[initial_NAD]" value="1" type="ModelValue" simulationType="fixed">
            <InitialExpression>
              &lt;CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD],Reference=InitialConcentration&gt;
            </InitialExpression>
          </ModelParameter>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_phosphorylation_k1]" value="1" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_dephosphorylation_k1]" value="5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_phosphorylation_k1]" value="1" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_dephosphorylation_k1]" value="10" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Induced_PGC1a_deacetylation_k1]" value="1.913" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_acetylation_k1]" value="1" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_in_NAD_Increase_k1]" value="10" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_in_NAD_Increase_2_k1]" value="10" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_synthesis_v]" value="0.12" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_utilisation_k1]" value="0.044999999999999998" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_utilisation_by_PARP_k1]" value="0.074999999999999997" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_Shalve]" value="1.45" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_V]" value="0.31622800000000001" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_h]" value="100" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_Shalve]" value="3" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_V]" value="0.01" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_h]" value="30" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_AICAR_stimulus_removal_k1]" value="0.29309499999999999" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_phosphorylation_induced_by_AICAR_k1]" value="3.9858600000000002" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve]" value="0.66720000000000002" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_V]" value="0.167159" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_h]" value="9.2353699999999996" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Basal_PGC1a_deacetylation_v]" value="0.25" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_PGC1a_Deacetylation_Limiter_k1]" value="0.56472" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_induced_AMPK_dephosphorylation_k1]" value="5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_utilisation_k1]" value="1" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_Shalve]" value="5.3617400000000002" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_V]" value="0.1013" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_h]" value="15.039999999999999" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_limiter_k1]" value="0.10000000000000001" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_negative_regulation_k1]" value="0.060926399999999999" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_NegReg_disappearance_k1]" value="0.10000000000000001" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_Shalve]" value="100" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_V]" value="0.10829" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_h]" value="1.5" type="ModelValue" simulationType="fixed"/>
        </ModelParameterGroup>
        <ModelParameterGroup cn="String=Kinetic Parameters" type="Group">
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[AMPK basal phosphorylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[AMPK basal phosphorylation],ParameterGroup=Parameters,Parameter=k1" value="1" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_phosphorylation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[AMPK basal dephosphorylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[AMPK basal dephosphorylation],ParameterGroup=Parameters,Parameter=k1" value="5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_dephosphorylation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a phosphorylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a phosphorylation],ParameterGroup=Parameters,Parameter=k1" value="1" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_phosphorylation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a dephosphorylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a dephosphorylation],ParameterGroup=Parameters,Parameter=k1" value="10" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_dephosphorylation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a induced deacetylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a induced deacetylation],ParameterGroup=Parameters,Parameter=k1" value="1.913" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Induced_PGC1a_deacetylation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a basal acetylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a basal acetylation],ParameterGroup=Parameters,Parameter=k1" value="1" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_acetylation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction NAD increase by AMPK]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction NAD increase by AMPK],ParameterGroup=Parameters,Parameter=k1" value="10" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_in_NAD_Increase_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction Delay_in_NAD_Increase Removal]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction Delay_in_NAD_Increase Removal],ParameterGroup=Parameters,Parameter=k1" value="10" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_in_NAD_Increase_2_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD synthesis]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD synthesis],ParameterGroup=Parameters,Parameter=v" value="0.12" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_synthesis_v],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD utilisation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD utilisation],ParameterGroup=Parameters,Parameter=k1" value="0.044999999999999998" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_utilisation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD utilisation by PARP]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD utilisation by PARP],ParameterGroup=Parameters,Parameter=k1" value="0.074999999999999997" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_utilisation_by_PARP_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD increase by AMPK]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD increase by AMPK],ParameterGroup=Parameters,Parameter=_NAD_increase_by_AMPK_Shalve" value="1.45" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_Shalve],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD increase by AMPK],ParameterGroup=Parameters,Parameter=_NAD_increase_by_AMPK_V" value="0.31622800000000001" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_V],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD increase by AMPK],ParameterGroup=Parameters,Parameter=_NAD_increase_by_AMPK_h" value="100" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_h],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD decrease by AMPK]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD decrease by AMPK],ParameterGroup=Parameters,Parameter=_NAD_increase_by_AMPK_Shalve" value="1.45" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_Shalve],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD decrease by AMPK],ParameterGroup=Parameters,Parameter=_NAD_increase_by_AMPK_V" value="0.31622800000000001" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_V],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD decrease by AMPK],ParameterGroup=Parameters,Parameter=_NAD_increase_by_AMPK_h" value="100" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_h],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction Induced Deacetylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction Induced Deacetylation],ParameterGroup=Parameters,Parameter=_Deacetylation_activity_Shalve" value="3" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_Shalve],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction Induced Deacetylation],ParameterGroup=Parameters,Parameter=_Deacetylation_activity_V" value="0.01" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_V],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction Induced Deacetylation],ParameterGroup=Parameters,Parameter=_Deacetylation_activity_h" value="30" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_h],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction AICAR Stimulus Removal]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction AICAR Stimulus Removal],ParameterGroup=Parameters,Parameter=k1" value="0.29309499999999999" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_AICAR_stimulus_removal_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[AMPK induced phosphorylation by AICAR]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[AMPK induced phosphorylation by AICAR],ParameterGroup=Parameters,Parameter=k1" value="3.9858600000000002" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_phosphorylation_induced_by_AICAR_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction AICAR Stimulus]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction AICAR Stimulus],ParameterGroup=Parameters,Parameter=_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve" value="0.66720000000000002" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction AICAR Stimulus],ParameterGroup=Parameters,Parameter=_DUMMY_REACTION_Delay_AICAR_stimulus_V" value="0.167159" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_V],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction AICAR Stimulus],ParameterGroup=Parameters,Parameter=_DUMMY_REACTION_Delay_AICAR_stimulus_h" value="9.2353699999999996" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_h],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a basal deacetylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[PGC1a basal deacetylation],ParameterGroup=Parameters,Parameter=_Basal_PGC1a_deacetylation_v" value="0.25" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Basal_PGC1a_deacetylation_v],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction Induced Deacetylation Delay Removal]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction Induced Deacetylation Delay Removal],ParameterGroup=Parameters,Parameter=k1" value="0.56472" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_PGC1a_Deacetylation_Limiter_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Glucose-induced AMPK dephosphorylation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Glucose-induced AMPK dephosphorylation],ParameterGroup=Parameters,Parameter=k1" value="5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_induced_AMPK_dephosphorylation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Glucose influx]" type="Reaction">
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Glucose utilisation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Glucose utilisation],ParameterGroup=Parameters,Parameter=k1" value="1" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_utilisation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction Glucose Stimulus]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction Glucose Stimulus],ParameterGroup=Parameters,Parameter=_Glucose_DUMMY_REACTION_delay_Shalve" value="5.3617400000000002" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_Shalve],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction Glucose Stimulus],ParameterGroup=Parameters,Parameter=_Glucose_DUMMY_REACTION_delay_V" value="0.1013" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_V],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Delay Reaction Glucose Stimulus],ParameterGroup=Parameters,Parameter=_Glucose_DUMMY_REACTION_delay_h" value="15.039999999999999" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_h],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction Glucose Delay Removal]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction Glucose Delay Removal],ParameterGroup=Parameters,Parameter=k1" value="0.10000000000000001" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_limiter_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD negative regulation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NAD negative regulation],ParameterGroup=Parameters,Parameter=k1" value="0.060926399999999999" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_negative_regulation_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction NegReg Removal]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[Dummy Reaction NegReg Removal],ParameterGroup=Parameters,Parameter=k1" value="0.10000000000000001" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_NegReg_disappearance_k1],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NR/NMN supplementation]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NR/NMN supplementation],ParameterGroup=Parameters,Parameter=_NR_NMN_supplementation_Shalve" value="100" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_Shalve],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NR/NMN supplementation],ParameterGroup=Parameters,Parameter=_NR_NMN_supplementation_V" value="0.10829" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_V],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=Mitonuclear communication model,Vector=Reactions[NR/NMN supplementation],ParameterGroup=Parameters,Parameter=_NR_NMN_supplementation_h" value="1.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_h],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
        </ModelParameterGroup>
      </ModelParameterSet>
    </ListOfModelParameterSets>
    <StateTemplate>
      <StateTemplateVariable objectReference="Model_1"/>
      <StateTemplateVariable objectReference="Metabolite_7"/>
      <StateTemplateVariable objectReference="Metabolite_3"/>
      <StateTemplateVariable objectReference="Metabolite_1"/>
      <StateTemplateVariable objectReference="Metabolite_15"/>
      <StateTemplateVariable objectReference="Metabolite_8"/>
      <StateTemplateVariable objectReference="Metabolite_10"/>
      <StateTemplateVariable objectReference="Metabolite_11"/>
      <StateTemplateVariable objectReference="Metabolite_13"/>
      <StateTemplateVariable objectReference="Metabolite_14"/>
      <StateTemplateVariable objectReference="Metabolite_2"/>
      <StateTemplateVariable objectReference="Metabolite_16"/>
      <StateTemplateVariable objectReference="Metabolite_4"/>
      <StateTemplateVariable objectReference="Metabolite_0"/>
      <StateTemplateVariable objectReference="Metabolite_5"/>
      <StateTemplateVariable objectReference="ModelValue_1"/>
      <StateTemplateVariable objectReference="Metabolite_17"/>
      <StateTemplateVariable objectReference="Metabolite_18"/>
      <StateTemplateVariable objectReference="Metabolite_19"/>
      <StateTemplateVariable objectReference="Metabolite_6"/>
      <StateTemplateVariable objectReference="Metabolite_9"/>
      <StateTemplateVariable objectReference="Metabolite_12"/>
      <StateTemplateVariable objectReference="Compartment_0"/>
      <StateTemplateVariable objectReference="ModelValue_0"/>
      <StateTemplateVariable objectReference="ModelValue_2"/>
      <StateTemplateVariable objectReference="ModelValue_3"/>
      <StateTemplateVariable objectReference="ModelValue_4"/>
      <StateTemplateVariable objectReference="ModelValue_5"/>
      <StateTemplateVariable objectReference="ModelValue_6"/>
      <StateTemplateVariable objectReference="ModelValue_7"/>
      <StateTemplateVariable objectReference="ModelValue_8"/>
      <StateTemplateVariable objectReference="ModelValue_9"/>
      <StateTemplateVariable objectReference="ModelValue_10"/>
      <StateTemplateVariable objectReference="ModelValue_11"/>
      <StateTemplateVariable objectReference="ModelValue_12"/>
      <StateTemplateVariable objectReference="ModelValue_13"/>
      <StateTemplateVariable objectReference="ModelValue_14"/>
      <StateTemplateVariable objectReference="ModelValue_15"/>
      <StateTemplateVariable objectReference="ModelValue_16"/>
      <StateTemplateVariable objectReference="ModelValue_17"/>
      <StateTemplateVariable objectReference="ModelValue_18"/>
      <StateTemplateVariable objectReference="ModelValue_19"/>
      <StateTemplateVariable objectReference="ModelValue_20"/>
      <StateTemplateVariable objectReference="ModelValue_21"/>
      <StateTemplateVariable objectReference="ModelValue_22"/>
      <StateTemplateVariable objectReference="ModelValue_23"/>
      <StateTemplateVariable objectReference="ModelValue_24"/>
      <StateTemplateVariable objectReference="ModelValue_25"/>
      <StateTemplateVariable objectReference="ModelValue_26"/>
      <StateTemplateVariable objectReference="ModelValue_27"/>
      <StateTemplateVariable objectReference="ModelValue_28"/>
      <StateTemplateVariable objectReference="ModelValue_29"/>
      <StateTemplateVariable objectReference="ModelValue_30"/>
      <StateTemplateVariable objectReference="ModelValue_31"/>
      <StateTemplateVariable objectReference="ModelValue_32"/>
      <StateTemplateVariable objectReference="ModelValue_33"/>
      <StateTemplateVariable objectReference="ModelValue_34"/>
      <StateTemplateVariable objectReference="ModelValue_35"/>
      <StateTemplateVariable objectReference="ModelValue_36"/>
      <StateTemplateVariable objectReference="ModelValue_37"/>
    </StateTemplate>
    <InitialState type="initialState">
      0 6.0221417900000005e+20 6.0221417900000005e+20 6.0221417900000005e+20 0 6.0221417900000005e+20 0 0 1.5055354475000002e+22 6.0221417900000005e+20 6.0221417900000003e+21 0 6.0221417900000005e+20 6.0221417900000003e+21 6.0221417900000005e+20 1 6.0221417900000005e+20 6.0221417900000005e+20 1.5055354475000002e+22 6.0221417900000005e+20 6.0221417900000005e+20 0 1 1 1 1 5 1 10 1.913 1 10 10 0.12 0.044999999999999998 0.074999999999999997 1.45 0.31622800000000001 100 3 0.01 30 0.29309499999999999 3.9858600000000002 0.66720000000000002 0.167159 9.2353699999999996 0.25 0.56472 5 1 5.3617400000000002 0.1013 15.039999999999999 0.10000000000000001 0.060926399999999999 0.10000000000000001 100 0.10829 1.5 
    </InitialState>
  </Model>
  <ListOfTasks>
    <Task key="Task_14" name="Steady-State" type="steadyState" scheduled="false" updateModel="false">
      <Report reference="Report_10" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="JacobianRequested" type="bool" value="1"/>
        <Parameter name="StabilityAnalysisRequested" type="bool" value="1"/>
      </Problem>
      <Method name="Enhanced Newton" type="EnhancedNewton">
        <Parameter name="Resolution" type="unsignedFloat" value="1.0000000000000001e-09"/>
        <Parameter name="Derivation Factor" type="unsignedFloat" value="0.001"/>
        <Parameter name="Use Newton" type="bool" value="1"/>
        <Parameter name="Use Integration" type="bool" value="1"/>
        <Parameter name="Use Back Integration" type="bool" value="0"/>
        <Parameter name="Accept Negative Concentrations" type="bool" value="0"/>
        <Parameter name="Iteration Limit" type="unsignedInteger" value="50"/>
        <Parameter name="Maximum duration for forward integration" type="unsignedFloat" value="1000000000"/>
        <Parameter name="Maximum duration for backward integration" type="unsignedFloat" value="1000000"/>
      </Method>
    </Task>
    <Task key="Task_15" name="Time-Course" type="timeCourse" scheduled="false" updateModel="false">
      <Problem>
        <Parameter name="AutomaticStepSize" type="bool" value="0"/>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
        <Parameter name="Output Event" type="bool" value="0"/>
        <Parameter name="Start in Steady State" type="bool" value="0"/>
        <Parameter name="Use Values" type="bool" value="0"/>
        <Parameter name="Values" type="string" value=""/>
      </Problem>
      <Method name="Deterministic (LSODA)" type="Deterministic(LSODA)">
        <Parameter name="Integrate Reduced Model" type="bool" value="0"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="9.9999999999999995e-07"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="9.9999999999999998e-13"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="100000"/>
        <Parameter name="Max Internal Step Size" type="unsignedFloat" value="0"/>
      </Method>
    </Task>
    <Task key="Task_16" name="Scan" type="scan" scheduled="true" updateModel="0">
      <Report append="0" target="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/Problem1/Fit1/paramiterEstimation1/ParameterEstimationData/PEData1.txt" reference="Report_35" confirmOverwrite="0"/>
      <Problem>
        <Parameter name="Subtask" type="unsignedInteger" value="5"/>
        <ParameterGroup name="ScanItems">
        <ParameterGroup name="ScanItem"><Parameter type="unsignedInteger" name="Number of steps" value="1"/><Parameter type="unsignedInteger" name="Type" value="0"/><Parameter type="cn" name="Object" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AMPK],Reference=InitialConcentration"/></ParameterGroup></ParameterGroup>
        <Parameter name="Output in subtask" type="bool" value="0"/>
        <Parameter name="Adjust initial conditions" type="bool" value="0"/>
        <Parameter name="Continue on Error" type="bool" value="0"/>
      </Problem>
      <Method name="Scan Framework" type="ScanFramework">
      </Method>
    </Task>
    <Task key="Task_17" name="Elementary Flux Modes" type="fluxMode" scheduled="false" updateModel="false">
      <Report reference="Report_11" target="" append="1" confirmOverwrite="1"/>
      <Problem>
      </Problem>
      <Method name="EFM Algorithm" type="EFMAlgorithm">
      </Method>
    </Task>
    <Task key="Task_18" name="Optimization" type="optimization" scheduled="false" updateModel="false">
      <Report reference="Report_12" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Subtask" type="cn" value="CN=Root,Vector=TaskList[Steady-State]"/>
        <ParameterText name="ObjectiveExpression" type="expression">
          
        </ParameterText>
        <Parameter name="Maximize" type="bool" value="0"/>
        <Parameter name="Randomize Start Values" type="bool" value="0"/>
        <Parameter name="Calculate Statistics" type="bool" value="1"/>
        <ParameterGroup name="OptimizationItemList">
        </ParameterGroup>
        <ParameterGroup name="OptimizationConstraintList">
        </ParameterGroup>
      </Problem>
      <Method name="Random Search" type="RandomSearch">
        <Parameter name="Log Verbosity" type="unsignedInteger" value="0"/>
        <Parameter name="Number of Iterations" type="unsignedInteger" value="100000"/>
        <Parameter name="Random Number Generator" type="unsignedInteger" value="1"/>
        <Parameter name="Seed" type="unsignedInteger" value="0"/>
      </Method>
    </Task>
    <Task key="Task_19" name="Parameter Estimation" type="parameterFitting" scheduled="false" updateModel="0">
      <Report reference="Report_32" target="PEData.txt" append="False" confirmOverwrite="False"/>
      <Problem>
        <Parameter name="Maximize" type="bool" value="0"/>
        <Parameter name="Randomize Start Values" type="bool" value="1"/>
        <Parameter name="Calculate Statistics" type="bool" value="0"/>
        <ParameterGroup name="OptimizationItemList">
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_dephosphorylation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_phosphorylation_induced_by_AICAR_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_AMPK_phosphorylation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Basal_PGC1a_deacetylation_v],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_AICAR_stimulus_removal_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_V],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_AICAR_stimulus_h],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_in_NAD_Increase_2_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_Delay_in_NAD_Increase_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_NegReg_disappearance_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_DUMMY_REACTION_PGC1a_Deacetylation_Limiter_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_Shalve],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_V],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Deacetylation_activity_h],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_Shalve],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_V],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_h],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_DUMMY_REACTION_delay_limiter_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_induced_AMPK_dephosphorylation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Glucose_utilisation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_Induced_PGC1a_deacetylation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_Shalve],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_V],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_increase_by_AMPK_h],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_negative_regulation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_synthesis_v],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_utilisation_by_PARP_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NAD_utilisation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_Shalve],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_V],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_NR_NMN_supplementation_h],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_acetylation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_dephosphorylation_k1],Reference=InitialValue"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter type="cn" name="LowerBound" value="1e-06"/>
            <Parameter type="cn" name="UpperBound" value="1000"/>
            <Parameter type="float" name="StartValue" value="0.1"/>
            <Parameter type="cn" name="ObjectCN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[_PGC1a_phosphorylation_k1],Reference=InitialValue"/>
          </ParameterGroup>
        </ParameterGroup>
        <ParameterGroup name="OptimizationConstraintList">
        </ParameterGroup>
        <Parameter name="Steady-State" type="cn" value="CN=Root,Vector=TaskList[Steady-State]"/>
        <Parameter name="Time-Course" type="cn" value="CN=Root,Vector=TaskList[Time-Course]"/>
        <Parameter name="Create Parameter Sets" type="bool" value="0"/>
        <ParameterGroup name="Experiment Set">
          <ParameterGroup name="NR_effects1000">
            <Parameter type="key" name="Key" value="Experiment_NR_effects1000"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/NR_effects1000.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="3"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="4"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[NAD_fold_increase],Reference=Value"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NR-NMN],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="NR_effects500">
            <Parameter type="key" name="Key" value="Experiment_NR_effects500"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/NR_effects500.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="3"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="4"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[NAD_fold_increase],Reference=Value"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NR-NMN],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="NR_effects200">
            <Parameter type="key" name="Key" value="Experiment_NR_effects200"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/NR_effects200.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="3"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="4"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[NAD_fold_increase],Reference=Value"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NR-NMN],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="NR_effects100">
            <Parameter type="key" name="Key" value="Experiment_NR_effects100"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/NR_effects100.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="3"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="4"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[NAD_fold_increase],Reference=Value"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NR-NMN],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="NR_effects50">
            <Parameter type="key" name="Key" value="Experiment_NR_effects50"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/NR_effects50.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="3"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="4"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[NAD_fold_increase],Reference=Value"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NR-NMN],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="NR_effects0">
            <Parameter type="key" name="Key" value="Experiment_NR_effects0"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/NR_effects0.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="3"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="4"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Values[NAD_fold_increase],Reference=Value"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NR-NMN],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="PE_PARP_Inhib_PJ34_NAD">
            <Parameter type="key" name="Key" value="Experiment_PE_PARP_Inhib_PJ34_NAD"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/PE_PARP_Inhib_PJ34_NAD.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="6"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="6"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD],Reference=Concentration"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[PARP1],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="4">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AMPK_driven_NAD_source],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="5">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AMPK_driven_NegReg_source],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="PE_5mM_GlucRestric_NAD">
            <Parameter type="key" name="Key" value="Experiment_PE_5mM_GlucRestric_NAD"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/PE_5mM_GlucRestric_NAD.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="9"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="4"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD],Reference=Concentration"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Glucose_source],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="PE_0.5mM_AICAR_NAD_and_PGC1aDeacet">
            <Parameter type="key" name="Key" value="Experiment_PE_0.5mM_AICAR_NAD_and_PGC1aDeacet"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/PE_0.5mM_AICAR_NAD_and_PGC1aDeacet.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="6"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="8"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[NAD],Reference=Concentration"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[PGC1a_deacet],Reference=Concentration"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="4">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AICAR],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="5">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Glucose_source],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="6">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Glucose],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="7">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[GlucoseDelay],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="PE_0.5mM_AICAR_AMPK-P">
            <Parameter type="key" name="Key" value="Experiment_PE_0.5mM_AICAR_AMPK-P"/>
            <Parameter type="file" name="File Name" value="/Users/peter/Documents/GitHub/NAD-SIRT1-alvero-model/copasiRuns/reparam/PE_0.5mM_AICAR_AMPK-P.csv"/>
            <Parameter type="bool" name="Data is Row Oriented" value="1"/>
            <Parameter type="unsignedInteger" name="First Row" value="1"/>
            <Parameter type="unsignedInteger" name="Last Row" value="6"/>
            <Parameter type="unsignedInteger" name="Experiment Type" value="1"/>
            <Parameter type="bool" name="Normalize Weights per Experiment" value="1"/>
            <Parameter type="string" name="Separator" value=","/>
            <Parameter type="unsignedInteger" name="Weight Method" value="1"/>
            <Parameter type="unsignedInteger" name="Row containing Names" value="1"/>
            <Parameter type="unsignedInteger" name="Number of Columns" value="7"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0"/>
              <ParameterGroup name="1">
                <Parameter type="unsignedInteger" name="Role" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="2">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AMPK-P],Reference=Concentration"/>
                <Parameter type="unsignedInteger" name="Role" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[AICAR],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="4">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Glucose_source],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="5">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[Glucose],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="6">
                <Parameter type="cn" name="Object CN" value="CN=Root,Model=Mitonuclear communication model,Vector=Compartments[compartment_],Vector=Metabolites[GlucoseDelay],Reference=InitialConcentration"/>
                <Parameter type="unsignedInteger" name="Role" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
        </ParameterGroup>
        <ParameterGroup name="Validation Set">
          <Parameter name="Weight" type="unsignedFloat" value="1"/>
          <Parameter name="Threshold" type="unsignedInteger" value="5"/>
        </ParameterGroup>
      </Problem>
      <Method name="Particle Swarm" type="ParticleSwarm">
        <Parameter type="unsignedInteger" name="Iteration Limit" value="4000"/>
        <Parameter type="unsignedInteger" name="Swarm Size" value="100"/>
        <Parameter type="unsignedFloat" name="Std. Deviation" value="1e-06"/>
        <Parameter type="unsignedInteger" name="Random Number Generator" value="1"/>
        <Parameter type="unsignedInteger" name="Seed" value="0"/>
      </Method>
    </Task>
    <Task key="Task_20" name="Metabolic Control Analysis" type="metabolicControlAnalysis" scheduled="false" updateModel="false">
      <Report reference="Report_14" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Steady-State" type="key" value="Task_14"/>
      </Problem>
      <Method name="MCA Method (Reder)" type="MCAMethod(Reder)">
        <Parameter name="Modulation Factor" type="unsignedFloat" value="1.0000000000000001e-09"/>
        <Parameter name="Use Reder" type="bool" value="1"/>
        <Parameter name="Use Smallbone" type="bool" value="1"/>
      </Method>
    </Task>
    <Task key="Task_21" name="Lyapunov Exponents" type="lyapunovExponents" scheduled="false" updateModel="false">
      <Report reference="Report_15" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="ExponentNumber" type="unsignedInteger" value="3"/>
        <Parameter name="DivergenceRequested" type="bool" value="1"/>
        <Parameter name="TransientTime" type="float" value="0"/>
      </Problem>
      <Method name="Wolf Method" type="WolfMethod">
        <Parameter name="Orthonormalization Interval" type="unsignedFloat" value="1"/>
        <Parameter name="Overall time" type="unsignedFloat" value="1000"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="9.9999999999999995e-07"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="9.9999999999999998e-13"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
      </Method>
    </Task>
    <Task key="Task_22" name="Time Scale Separation Analysis" type="timeScaleSeparationAnalysis" scheduled="false" updateModel="false">
      <Report reference="Report_16" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
      </Problem>
      <Method name="ILDM (LSODA,Deuflhard)" type="TimeScaleSeparation(ILDM,Deuflhard)">
        <Parameter name="Deuflhard Tolerance" type="unsignedFloat" value="0.0001"/>
      </Method>
    </Task>
    <Task key="Task_23" name="Sensitivities" type="sensitivities" scheduled="false" updateModel="false">
      <Report reference="Report_17" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="SubtaskType" type="unsignedInteger" value="1"/>
        <ParameterGroup name="TargetFunctions">
          <Parameter name="SingleObject" type="cn" value=""/>
          <Parameter name="ObjectListType" type="unsignedInteger" value="7"/>
        </ParameterGroup>
        <ParameterGroup name="ListOfVariables">
          <ParameterGroup name="Variables">
            <Parameter name="SingleObject" type="cn" value=""/>
            <Parameter name="ObjectListType" type="unsignedInteger" value="41"/>
          </ParameterGroup>
          <ParameterGroup name="Variables">
            <Parameter name="SingleObject" type="cn" value=""/>
            <Parameter name="ObjectListType" type="unsignedInteger" value="0"/>
          </ParameterGroup>
        </ParameterGroup>
      </Problem>
      <Method name="Sensitivities Method" type="SensitivitiesMethod">
        <Parameter name="Delta factor" type="unsignedFloat" value="0.001"/>
        <Parameter name="Delta minimum" type="unsignedFloat" value="9.9999999999999998e-13"/>
      </Method>
    </Task>
    <Task key="Task_24" name="Moieties" type="moieties" scheduled="false" updateModel="false">
      <Report reference="Report_18" target="" append="1" confirmOverwrite="1"/>
      <Problem>
      </Problem>
      <Method name="Householder Reduction" type="Householder">
      </Method>
    </Task>
    <Task key="Task_25" name="Cross Section" type="crosssection" scheduled="false" updateModel="false">
      <Problem>
        <Parameter name="AutomaticStepSize" type="bool" value="0"/>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
        <Parameter name="Output Event" type="bool" value="0"/>
        <Parameter name="Start in Steady State" type="bool" value="0"/>
        <Parameter name="Use Values" type="bool" value="0"/>
        <Parameter name="Values" type="string" value=""/>
        <Parameter name="LimitCrossings" type="bool" value="0"/>
        <Parameter name="NumCrossingsLimit" type="unsignedInteger" value="0"/>
        <Parameter name="LimitOutTime" type="bool" value="0"/>
        <Parameter name="LimitOutCrossings" type="bool" value="0"/>
        <Parameter name="PositiveDirection" type="bool" value="1"/>
        <Parameter name="NumOutCrossingsLimit" type="unsignedInteger" value="0"/>
        <Parameter name="LimitUntilConvergence" type="bool" value="0"/>
        <Parameter name="ConvergenceTolerance" type="float" value="9.9999999999999995e-07"/>
        <Parameter name="Threshold" type="float" value="0"/>
        <Parameter name="DelayOutputUntilConvergence" type="bool" value="0"/>
        <Parameter name="OutputConvergenceTolerance" type="float" value="9.9999999999999995e-07"/>
        <ParameterText name="TriggerExpression" type="expression">
          
        </ParameterText>
        <Parameter name="SingleVariable" type="cn" value=""/>
      </Problem>
      <Method name="Deterministic (LSODA)" type="Deterministic(LSODA)">
        <Parameter name="Integrate Reduced Model" type="bool" value="0"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="9.9999999999999995e-07"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="9.9999999999999998e-13"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="100000"/>
        <Parameter name="Max Internal Step Size" type="unsignedFloat" value="0"/>
      </Method>
    </Task>
    <Task key="Task_26" name="Linear Noise Approximation" type="linearNoiseApproximation" scheduled="false" updateModel="false">
      <Report reference="Report_19" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Steady-State" type="key" value="Task_14"/>
      </Problem>
      <Method name="Linear Noise Approximation" type="LinearNoiseApproximation">
      </Method>
    </Task>
    <Task key="Task_27" name="Time-Course Sensitivities" type="timeSensitivities" scheduled="false" updateModel="false">
      <Problem>
        <Parameter name="AutomaticStepSize" type="bool" value="0"/>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
        <Parameter name="Output Event" type="bool" value="0"/>
        <Parameter name="Start in Steady State" type="bool" value="0"/>
        <Parameter name="Use Values" type="bool" value="0"/>
        <Parameter name="Values" type="string" value=""/>
        <ParameterGroup name="ListOfParameters">
        </ParameterGroup>
        <ParameterGroup name="ListOfTargets">
        </ParameterGroup>
      </Problem>
      <Method name="LSODA Sensitivities" type="Sensitivities(LSODA)">
        <Parameter name="Integrate Reduced Model" type="bool" value="0"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="9.9999999999999995e-07"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="9.9999999999999998e-13"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
        <Parameter name="Max Internal Step Size" type="unsignedFloat" value="0"/>
      </Method>
    </Task>
  </ListOfTasks>
  <ListOfReports>
    <Report key="Report_10" name="Steady-State" taskType="steadyState" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Steady-State]"/>
      </Footer>
    </Report>
    <Report key="Report_11" name="Elementary Flux Modes" taskType="fluxMode" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Elementary Flux Modes],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_12" name="Optimization" taskType="optimization" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Object=Description"/>
        <Object cn="String=\[Function Evaluations\]"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="String=\[Best Value\]"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="String=\[Best Parameters\]"/>
      </Header>
      <Body>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Function Evaluations"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Best Value"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Best Parameters"/>
      </Body>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_13" name="Parameter Estimation" taskType="parameterFitting" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Object=Description"/>
        <Object cn="String=\[Function Evaluations\]"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="String=\[Best Value\]"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="String=\[Best Parameters\]"/>
      </Header>
      <Body>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Function Evaluations"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Value"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Parameters"/>
      </Body>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_14" name="Metabolic Control Analysis" taskType="metabolicControlAnalysis" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Metabolic Control Analysis],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Metabolic Control Analysis],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_15" name="Lyapunov Exponents" taskType="lyapunovExponents" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Lyapunov Exponents],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Lyapunov Exponents],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_16" name="Time Scale Separation Analysis" taskType="timeScaleSeparationAnalysis" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Time Scale Separation Analysis],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Time Scale Separation Analysis],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_17" name="Sensitivities" taskType="sensitivities" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Sensitivities],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Sensitivities],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_18" name="Moieties" taskType="moieties" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Moieties],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Moieties],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_19" name="Linear Noise Approximation" taskType="linearNoiseApproximation" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Linear Noise Approximation],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Linear Noise Approximation],Object=Result"/>
      </Footer>
    </Report>
    <Report precision="6" separator="&#9;" name="multi_parameter_estimation" key="Report_35" taskType="parameterFitting">
      <Comment/>
      <Table printTitle="1">
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Parameters"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Value"/>
      </Table>
    </Report>
  </ListOfReports>
  <SBMLReference file="paramiterEstimation1.sbml">
    <SBMLMap SBMLid="AICAR_Delay" COPASIkey="Metabolite_11"/>
    <SBMLMap SBMLid="AICAR_treatment" COPASIkey="Metabolite_12"/>
    <SBMLMap SBMLid="AMPK" COPASIkey="Metabolite_0"/>
    <SBMLMap SBMLid="AMPK_P" COPASIkey="Metabolite_1"/>
    <SBMLMap SBMLid="AMPK_dephosphorylation" COPASIkey="Reaction_1"/>
    <SBMLMap SBMLid="AMPK_driven_NAD_source" COPASIkey="Metabolite_17"/>
    <SBMLMap SBMLid="AMPK_driven_NegReg_source" COPASIkey="Metabolite_18"/>
    <SBMLMap SBMLid="AMPK_phosphorylation" COPASIkey="Reaction_0"/>
    <SBMLMap SBMLid="AMPK_phosphorylation_induced_by_AICAR" COPASIkey="Reaction_15"/>
    <SBMLMap SBMLid="Basal_PGC1a_deacetylation" COPASIkey="Reaction_17"/>
    <SBMLMap SBMLid="DUMMY_REACTION_AICAR_stimulus_removal" COPASIkey="Reaction_14"/>
    <SBMLMap SBMLid="DUMMY_REACTION_Delay_AICAR_stimulus" COPASIkey="Reaction_16"/>
    <SBMLMap SBMLid="DUMMY_REACTION_Delay_in_NAD_Increase" COPASIkey="Reaction_6"/>
    <SBMLMap SBMLid="DUMMY_REACTION_Delay_in_NAD_Increase_2" COPASIkey="Reaction_7"/>
    <SBMLMap SBMLid="DUMMY_REACTION_NegReg_disappearance" COPASIkey="Reaction_25"/>
    <SBMLMap SBMLid="DUMMY_REACTION_PGC1a_Deacetylation_Limiter" COPASIkey="Reaction_18"/>
    <SBMLMap SBMLid="Deacetylation_activity" COPASIkey="Reaction_13"/>
    <SBMLMap SBMLid="Delay_in_NAD_increase" COPASIkey="Metabolite_8"/>
    <SBMLMap SBMLid="Glucose" COPASIkey="Metabolite_13"/>
    <SBMLMap SBMLid="GlucoseDelay" COPASIkey="Metabolite_14"/>
    <SBMLMap SBMLid="Glucose_DUMMY_REACTION_delay" COPASIkey="Reaction_22"/>
    <SBMLMap SBMLid="Glucose_DUMMY_REACTION_delay_limiter" COPASIkey="Reaction_23"/>
    <SBMLMap SBMLid="Glucose_induced_AMPK_dephosphorylation" COPASIkey="Reaction_19"/>
    <SBMLMap SBMLid="Glucose_input" COPASIkey="Reaction_20"/>
    <SBMLMap SBMLid="Glucose_source" COPASIkey="Metabolite_19"/>
    <SBMLMap SBMLid="Glucose_utilisation" COPASIkey="Reaction_21"/>
    <SBMLMap SBMLid="Hill_Cooperativity" COPASIkey="Function_40"/>
    <SBMLMap SBMLid="Induced_PGC1a_deacetylation" COPASIkey="Reaction_4"/>
    <SBMLMap SBMLid="NAD" COPASIkey="Metabolite_7"/>
    <SBMLMap SBMLid="NAD_NegReg" COPASIkey="Metabolite_15"/>
    <SBMLMap SBMLid="NAD_decrease_by_AMPK" COPASIkey="Reaction_12"/>
    <SBMLMap SBMLid="NAD_fold_increase" COPASIkey="ModelValue_1"/>
    <SBMLMap SBMLid="NAD_increase_by_AMPK" COPASIkey="Reaction_11"/>
    <SBMLMap SBMLid="NAD_negative_regulation" COPASIkey="Reaction_24"/>
    <SBMLMap SBMLid="NAD_synthesis" COPASIkey="Reaction_8"/>
    <SBMLMap SBMLid="NAD_utilisation" COPASIkey="Reaction_9"/>
    <SBMLMap SBMLid="NAD_utilisation_by_PARP" COPASIkey="Reaction_10"/>
    <SBMLMap SBMLid="NR_NMN" COPASIkey="Metabolite_16"/>
    <SBMLMap SBMLid="NR_NMN_supplementation" COPASIkey="Reaction_26"/>
    <SBMLMap SBMLid="PARP" COPASIkey="Metabolite_9"/>
    <SBMLMap SBMLid="PGC1a" COPASIkey="Metabolite_2"/>
    <SBMLMap SBMLid="PGC1a_Deacetylation_Activity" COPASIkey="Metabolite_10"/>
    <SBMLMap SBMLid="PGC1a_P" COPASIkey="Metabolite_3"/>
    <SBMLMap SBMLid="PGC1a_acetylation" COPASIkey="Reaction_5"/>
    <SBMLMap SBMLid="PGC1a_deacet" COPASIkey="Metabolite_4"/>
    <SBMLMap SBMLid="PGC1a_dephosphorylation" COPASIkey="Reaction_3"/>
    <SBMLMap SBMLid="PGC1a_phosphorylation" COPASIkey="Reaction_2"/>
    <SBMLMap SBMLid="SIRT1" COPASIkey="Metabolite_6"/>
    <SBMLMap SBMLid="SIRT1_activity" COPASIkey="Metabolite_5"/>
    <SBMLMap SBMLid="_AMPK_dephosphorylation_k1" COPASIkey="ModelValue_4"/>
    <SBMLMap SBMLid="_AMPK_phosphorylation_induced_by_AICAR_k1" COPASIkey="ModelValue_21"/>
    <SBMLMap SBMLid="_AMPK_phosphorylation_k1" COPASIkey="ModelValue_3"/>
    <SBMLMap SBMLid="_Basal_PGC1a_deacetylation_v" COPASIkey="ModelValue_25"/>
    <SBMLMap SBMLid="_DUMMY_REACTION_AICAR_stimulus_removal_k1" COPASIkey="ModelValue_20"/>
    <SBMLMap SBMLid="_DUMMY_REACTION_Delay_AICAR_stimulus_Shalve" COPASIkey="ModelValue_22"/>
    <SBMLMap SBMLid="_DUMMY_REACTION_Delay_AICAR_stimulus_V" COPASIkey="ModelValue_23"/>
    <SBMLMap SBMLid="_DUMMY_REACTION_Delay_AICAR_stimulus_h" COPASIkey="ModelValue_24"/>
    <SBMLMap SBMLid="_DUMMY_REACTION_Delay_in_NAD_Increase_2_k1" COPASIkey="ModelValue_10"/>
    <SBMLMap SBMLid="_DUMMY_REACTION_Delay_in_NAD_Increase_k1" COPASIkey="ModelValue_9"/>
    <SBMLMap SBMLid="_DUMMY_REACTION_NegReg_disappearance_k1" COPASIkey="ModelValue_34"/>
    <SBMLMap SBMLid="_DUMMY_REACTION_PGC1a_Deacetylation_Limiter_k1" COPASIkey="ModelValue_26"/>
    <SBMLMap SBMLid="_Deacetylation_activity_Shalve" COPASIkey="ModelValue_17"/>
    <SBMLMap SBMLid="_Deacetylation_activity_V" COPASIkey="ModelValue_18"/>
    <SBMLMap SBMLid="_Deacetylation_activity_h" COPASIkey="ModelValue_19"/>
    <SBMLMap SBMLid="_Glucose_DUMMY_REACTION_delay_Shalve" COPASIkey="ModelValue_29"/>
    <SBMLMap SBMLid="_Glucose_DUMMY_REACTION_delay_V" COPASIkey="ModelValue_30"/>
    <SBMLMap SBMLid="_Glucose_DUMMY_REACTION_delay_h" COPASIkey="ModelValue_31"/>
    <SBMLMap SBMLid="_Glucose_DUMMY_REACTION_delay_limiter_k1" COPASIkey="ModelValue_32"/>
    <SBMLMap SBMLid="_Glucose_induced_AMPK_dephosphorylation_k1" COPASIkey="ModelValue_27"/>
    <SBMLMap SBMLid="_Glucose_utilisation_k1" COPASIkey="ModelValue_28"/>
    <SBMLMap SBMLid="_Induced_PGC1a_deacetylation_k1" COPASIkey="ModelValue_7"/>
    <SBMLMap SBMLid="_NAD_increase_by_AMPK_Shalve" COPASIkey="ModelValue_14"/>
    <SBMLMap SBMLid="_NAD_increase_by_AMPK_V" COPASIkey="ModelValue_15"/>
    <SBMLMap SBMLid="_NAD_increase_by_AMPK_h" COPASIkey="ModelValue_16"/>
    <SBMLMap SBMLid="_NAD_negative_regulation_k1" COPASIkey="ModelValue_33"/>
    <SBMLMap SBMLid="_NAD_synthesis_v" COPASIkey="ModelValue_11"/>
    <SBMLMap SBMLid="_NAD_utilisation_by_PARP_k1" COPASIkey="ModelValue_13"/>
    <SBMLMap SBMLid="_NAD_utilisation_k1" COPASIkey="ModelValue_12"/>
    <SBMLMap SBMLid="_NR_NMN_supplementation_Shalve" COPASIkey="ModelValue_35"/>
    <SBMLMap SBMLid="_NR_NMN_supplementation_V" COPASIkey="ModelValue_36"/>
    <SBMLMap SBMLid="_NR_NMN_supplementation_h" COPASIkey="ModelValue_37"/>
    <SBMLMap SBMLid="_PGC1a_acetylation_k1" COPASIkey="ModelValue_8"/>
    <SBMLMap SBMLid="_PGC1a_dephosphorylation_k1" COPASIkey="ModelValue_6"/>
    <SBMLMap SBMLid="_PGC1a_phosphorylation_k1" COPASIkey="ModelValue_5"/>
    <SBMLMap SBMLid="compartment_" COPASIkey="Compartment_0"/>
    <SBMLMap SBMLid="initial_NAD" COPASIkey="ModelValue_2"/>
    <SBMLMap SBMLid="quantity_to_number_factor" COPASIkey="ModelValue_0"/>
  </SBMLReference>
  <ListOfUnitDefinitions>
    <UnitDefinition key="Unit_1" name="meter" symbol="m">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_0">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        m
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_5" name="second" symbol="s">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_4">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        s
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_13" name="Avogadro" symbol="Avogadro">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_12">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        Avogadro
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_17" name="item" symbol="#">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_16">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        #
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_35" name="liter" symbol="l">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_34">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        0.001*m^3
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_41" name="mole" symbol="mol">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_40">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        Avogadro*#
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_67" name="hour" symbol="h">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_66">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2020-01-13T15:19:03Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        3600*s
      </Expression>
    </UnitDefinition>
  </ListOfUnitDefinitions>
</COPASI>
